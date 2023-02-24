#Module for charts

#Matplotlib must be installed in the terminal before it can be used in the program
# pip install matplotlib

import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    #ax is the coordenate where the chart will be
    fig, ax= plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax= plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__=="__main__":
    labels = ['a', 'b', 'c']
    values = [115, 300, 80]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
