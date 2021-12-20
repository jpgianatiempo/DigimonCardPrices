# DigimonCardPrices

Un amigo necesitaba tener los precios actualizados de todas las cartas (singles) de Digimon. El punto es que el hacia todo el proceso a mano y las iba cargando en su respectiva página. Pero encontramos que podía cargar un csv/xlsx con el precio y eso aumentaría notablemente su eficiencia.

Además, como su página es de Argentina y los precios de las cartas de Troll and Toad están en íngles había que conseguir un tipo de cambio paralelo que le garantice la reposición de sus productos.

Por este motivo le cree un código que recorre el listado de cartas publicadas en Troll and Toad y obtiene de cada una el precio y su nombre. Hubo que prestar atención porque cuando una carta no tenía stock, el precio estaba alojado en otro lugar de la página. No obstante, existía un contenedor que tenía todos los datos necesarios.

Una vez que se resolvió eso, solo restaba conseguir un tipo de cambio que sea representativo del valor de mercado (no el tipo de cambio oficial). Entonces encontré una página que publica el precio del dólar paralelo (blue) y lo scrapea para obtener los precios de las cartas en pesos.