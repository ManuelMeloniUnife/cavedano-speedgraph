from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FuncFormatter

def create_plot(d1, d2=None):
    x_1 = list(d1.keys())
    y_1 = list(d1.values())

    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    ax.plot(x_1, y_1,linewidth=2.0, marker='o', linestyle='-', markersize=0, color='#7047eb')
    
    if d2 is not None:
        x_2 = list(d2.keys())
        y_2 = list(d2.values())
        ax.plot(x_2, y_2, marker='o', linestyle='-', markersize=0, color='orange')
    
    ax.set_xlabel('DISTANCE [m]')
    ax.set_ylabel('SPEED [km/h]')
    

    #configurazione dello stylesheet del grafico:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    #plt.fill_between(x_1, y_1, step="mid", alpha=0.1)

    # Configurazione della griglia principale e secondaria
    ax.grid(True, which='both')
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    # Impostazioni della griglia principale
    ax.grid(which='major', linestyle='-', linewidth='0.6', color='#818185')

    # Impostazioni della griglia secondaria
    ax.grid(which='minor', linestyle='-', linewidth='0.4', color='#d2d1d6')

    # Formattatori per i tick principali e secondari senza decimali
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{int(y)}'))
    ax.xaxis.set_minor_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))
    ax.yaxis.set_minor_formatter(FuncFormatter(lambda y, _: f'{int(y)}'))

    # Aggiunta delle etichette secondarie
    for label in ax.xaxis.get_minorticklabels():
        label.set_fontsize(9)  # Imposta la dimensione del font delle etichette secondarie
        label.set_color('gray')  # Imposta il colore delle etichette secondarie
    
    for label in ax.yaxis.get_minorticklabels():
        label.set_fontsize(7)
        label.set_color('gray')
    plt.show()
    return fig, ax
