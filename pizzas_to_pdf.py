from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd
import json


class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 20)
        self.cell(0, 10, 'Reporte de ventas', 20, 0, 'C')
        self.ln(30)
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, 'Pagina ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def get_graphs():
    # ingredientes mas vendidos
    prediccion = pd.read_csv('./data/prediccion.csv', sep=';', encoding='latin-1')

    ingredientes = {}
    for columna in prediccion.columns:
        a = prediccion[columna].sum()//53
        b = columna.replace('Cheese', 'chs.')
    
        ingredientes[b] = a
    plt.figure(figsize=(10,15))
    plt.barh(list(ingredientes.keys()), list(ingredientes.values()))
    plt.title('Predicciones', fontdict={'fontname': 'DejaVu Sans', 'fontweight': 'bold', 'fontsize': 20})
    # ajustar margen de la izquierda
    plt.subplots_adjust(left=0.2)
    plt.savefig('./data/ingredientes.png')

    # Ganancias mensuales
    with open('./data/ganancias_mensuales.json', 'r') as f:
        ganancias_mensuales = json.load(f)

    x = list(ganancias_mensuales.keys())
    y = list(ganancias_mensuales.values())
    plt.figure(figsize=(16, 9))
    plt.plot(x, y)
    plt.title('Ganancias mensuales', fontdict={'fontname': 'DejaVu Sans', 'fontweight': 'bold', 'fontsize': 20})
    plt.yticks(range(50000, 75000, 1000))
    plt.savefig('./data/ganancias_mensuales.png')

    # pizzas totales
    with open('./data/pizzas_totales.json', 'r') as f:
        pizzas_totales = json.load(f)
    x = list(pizzas_totales.keys())
    y = list(pizzas_totales.values())
    plt.figure(figsize=(16, 9))
    plt.subplots_adjust(bottom=0.2)
    plt.bar(x, y)   
    plt.title('Pizzas totales', fontdict={'fontname': 'DejaVu Sans', 'fontweight': 'bold', 'fontsize': 20})
    plt.xticks(rotation=90, fontsize=8)
    plt.savefig('./data/pizzas_totales.png')


def get_data():
    pizzas_dias = pd.read_csv('./data/dias_pizzas.csv', sep=';', encoding='latin-1')
    pizzas_precios = pd.read_csv('./data/pizzas.csv', sep=',', encoding='latin-1')
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    ganancias_mensuales = {}
    pizzas_totales = {}
    for i,row in pizzas_dias.iterrows():
        mes = meses[i//30]
        lista = eval(row['pizzas'])
        for pizza in lista:
            if pizza in pizzas_totales:
                pizzas_totales[pizza] += 1
            else:
                pizzas_totales[pizza] = 1
            for j,row2 in pizzas_precios.iterrows():
                if pizza == row2['pizza_id']:
                    if mes in ganancias_mensuales:
                        ganancias_mensuales[mes] += row2['price']
                    else:
                        ganancias_mensuales[mes] = row2['price']

    with open('./data/ganancias_mensuales.json', 'w') as f:
        json.dump(ganancias_mensuales, f)
    with open('./data/pizzas_totales.json', 'w') as f:
        json.dump(pizzas_totales, f)


def get_pdf():
    pdf = PDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.image('./data/ganancias_mensuales.png', 10, 50, 190, 100)
    pdf.image('./data/pizzas_totales.png', 10, 160, 190, 100)
    pdf.add_page()
    pdf.image('./data/ingredientes.png', x=15, y=30, w=170)
    pdf.output('reporte.pdf', 'F')


if __name__ == '__main__':
    # get_data()
    get_graphs()
    get_pdf()