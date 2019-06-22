import matplotlib.pyplot as plt
import random
import os
def save(name='', fmt='png'):
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
#Создаем график с максимумом и минимумом
def create_maxmin():
    plt.clf()
    series1 = []
    series2 = []
    series3 = []
    xs = range(50)
    for i in xs:
        series1.append(random.randint(0,30))
    x = max(series1)
    for i in xs:
        series2.append(x)
    y = min(series1)
    for i in xs:
        series3.append(y)
    plt.plot(xs, series1, linestyle='-')
    plt.plot(xs, series2, linestyle='-')
    plt.plot(xs, series3, linestyle='-')
    save(name='maxmin', fmt='png')
#Создаем график со средней линией
def create_middle():
    plt.clf()
    series1 = []
    series2 = []
    xs = range(50)
    x = 0
    for i in xs:
        series1.append(random.randint(0,30))
    for i in series1:
        x += i
    x = x/len(series1)
    for i in xs:
        series2.append(x)
    plt.plot(xs, series1, linestyle='-')
    plt.plot(xs, series2, linestyle='-')
    save(name='middle', fmt='png')
create_maxmin()
create_middle()
