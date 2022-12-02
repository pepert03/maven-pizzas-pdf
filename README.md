Reporte ejecutivo en pdf
=================

## Introducción
Instalar librerías de Python necesarias:
```
pip install -r requirements.txt
```
Todos los archivos necesarios se encuentran en la carpeta `data`. Entre ellos se encuentra ```predicción.csv``` obtenido en 
[maven-pizzas-xml](https://github.com/pepert03/maven-pizzas-xml).

## Reporte pdf
El archivo ```pizzas_to_pdf.py``` contiene 3 funciones:
* ```get_data()```: Obtiene los datos de ```predicción.csv``` y devuelve:
    * ```ganancias_mensuales.json```: Diccionario con las ganancias mensuales.
    * ```pizzas_totales.json```: Diccionario con las pizzas compradas cada dia.
* ```get_graphs()```: Genera los graficos ```ingredientes.png```, ```ganancias_mensuales.png``` y ```pizzas_totales.png```.
* ```get_pdf()```: Genera el pdf con el reporte ejecutivo.
