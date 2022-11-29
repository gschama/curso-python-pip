import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png') # guarda el grafico en una imagen, ya que no lo puede mostrar por el entorno grafico (solucion temporal).
    plt.close()
    #plt.show()
    
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig("pie.png")
    plt.close()
    
if __name__ == "__main__":
    labels = ['a', 'b', 'c']
    values = [100, 400, 800]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)