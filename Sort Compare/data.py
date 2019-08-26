import pandas
import matplotlib.pyplot as plt
import numpy


def log(data: dict):
    print(f'''
    Data:
        Algoritmo: {data['algorithm']}
        Tipo: {data['type']}
        Quantidade: {data['size']}
        Média de trocas: {data['md_exchange']}
        Desvio padrão de trocas: {data['sd_exchange']}
        Média de comparações: {data['md_compare']}
        Desvio padrão de comparações: {data['sd_compare']}
        Média de tempo: {data['md_time']}
        Desvio padrão de tempo: {data['sd_time']}
        ''')


def show_analysis(data: list):
    # Panda Data Frame
    pandas.set_option('display.max_columns', None)

    cols = ['algorithm', 'type', 'size', 'md_exchange', 'md_compare', 'md_time']

    df = pandas.DataFrame(data)
    df = df[cols]
    df.groupby('size')
    df.to_csv('test_size_%d.csv' % data[0]['size'])

    values_time = []
    values_time_sd = []
    values_exchange = []
    values_exchange_sd = []
    values_compare = []
    values_compare_sd = []

    for i in range(0, len(data)):
        values_time.append(data[i]['md_time'] * 1000)
        values_time_sd.append(data[i]['sd_time'] * 1000)
        values_exchange.append(data[i]['md_exchange'])
        values_exchange_sd.append(data[i]['sd_exchange'])
        values_compare.append(data[i]['md_compare'])
        values_compare_sd.append(data[i]['sd_compare'])

    show_graphics(data, 'Algorithm: Time average', 'Time (ms)', values_time, values_time_sd)
    show_graphics(data, 'Algorithm: Exchanges average', 'Number of Exchanges', values_exchange, values_exchange_sd)
    show_graphics(data, 'Algorithm: Compares average', 'Number of Compares', values_compare, values_compare_sd)


def show_graphics(data: list, title: str, label: str, values: list, dps: list):
    # Plot
    names = []
    size = data[0]['size']

    for i in range(0, len(data)):
        names.append(data[i]['algorithm'])

    fig, ax = plt.subplots()
    y_pos = numpy.arange(len(data))

    ax.barh(y_pos, values, xerr=dps, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel(label)
    ax.set_title(title + ', size: %d' % size)

    plt.show()