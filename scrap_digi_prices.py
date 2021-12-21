from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#genero lista de cantidad de páginas
#pongo un número exagerado para que dure por mucho tiempo el scrap sin modificarlo, actualmente son 20 pág
paginas = list(range(10000))
#lista para nombres
nombres = []
#lista para precios
precios = []
#for loop para ir scrapeando por cada página
for pagina in paginas:
    try:
        r = requests.get("https://www.trollandtoad.com/final-fantasy-more-ccgs/all-digimon-singles/17909?Keywords=&min-price=&max-price=&items-pp=60&item-condition=&selected-cat=17909&sort-order=&page-no="+str(pagina)+"&view=grid&subproduct=0")
        soup = BeautifulSoup(r.text, "html.parser")
        #selecciono el contenedor que tiene nombre y precio de la carta
        total = soup.findAll("div", {"class":"product-info card-body col pl-0 pl-sm-3"})
        #agrego esta linea para que salte IndexError si el número de página no contiene info y corte el loop
        total[0].text
        #por cada carta en cada pagina
        for carta in total :
            #selecciono nombre
            nombre = carta.text.split("\n")[1]

            try:
                #precio de la carta si esta en stock
                precio_stock = carta.text.split("\n")[6].split("$")[1]
            except IndexError:
                try:
                    #precio de la carta si no esta en stock, xq esta en un lugar distinto
                    precio_stock = carta.text.split("\n")[2].split("$")[1]
                except IndexError:
                    #en caso de que no haya ninguno (no deberia) le pone NAN
                    precio_stock = np.NaN

            nombres.append(nombre)
            precios.append(precio_stock)
    except IndexError:
        break

#junto todo en el dataframe
df = pd.DataFrame(list(zip(nombres, precios)),
               columns =['Carta', 'Precio_Usd'])

#pasar precio a número
df.Precio_Usd = pd.to_numeric(df.Precio_Usd)

#scrap precio dolar blue o setear dolar a gusto!
re = requests.get("https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB")
sopa = BeautifulSoup(re.text, "html.parser")
dolar_vendedor = sopa.findAll("div", {"class":"sell-value"},{"class":"currency"})
dolar = pd.to_numeric(dolar_vendedor[0].text.strip("$").replace(",","."))

#convertir a pesos
df["Precio_Pesos"] = df.Precio_Usd * dolar

#dejo nombres únicos
df.drop_duplicates(["Carta"],inplace=True)
#ordeno de la A - Z
df = df.sort_values(by=["Carta"],ascending=True)

#grabo el excel
df.to_excel("Precios_Digimon.xlsx")