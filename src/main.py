from utils import read_speeds_from_file, populate_table
from graph import create_plot

import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


# inizializzo dizionari
dict1 = {}
dict2 = {}
# colori utilizzati
col1 = "#1c1d1f"
col2 = "#29292a"
col3 = "#303030"
col4 = "#454649"
col5 = "#f3f3f3"
col6 = "#c5f04d"


# Funzione per aggiornare dict1 e table1 dal primo file inserito
# def update_data_1(file_path):
#    global dict1
#    dict1 = read_speeds_from_file(file_path)
#    populate_table(table1, dict1)
#    update_plot()
#
# def update_data_2(file_path):
#


def file_from_start():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path and ('normal' == start_window.state()):
        open_main_window(file_path)


def file_from_root():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path and ('normal' == root.state()):
        #        update_data_1(file_path)
        print(file_path)


def file2_from_root():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path and ('normal' == root.state()):
        #        update_data_2(file_path)
        print(file_path)


def open_main_window(path):
    if 'normal' == start_window.state():
        start_window.destroy()  # Chiude la finestra di avvio
    main_window(path)  # Apre la finestra principale


def main_window(path):
    global root, canvas, table1, table2, fig, ax, table_frame_1, table_frame_2
    root = tk.Tk()
    root.title("Team Cavedano - speedchart")
    root.minsize(1200, 700)
    root.configure(bg=col1)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Cambia file", command=file_from_root)
    file_menu.add_command(label="Sovrapponi file", command=file2_from_root)
    clear_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Cancella", menu=clear_menu)
    clear_menu.add_command(label="Pulisci grafico", command=file2_from_root)

    root.mainloop()


def main():
    global start_window
    start_window = tk.Tk()
    start_window.title("Team Cavedano - speedchart")
    start_window.minsize(1000, 700)
    start_window.maxsize(1000, 700)
    start_window.configure(bg=col1)

    logo = Image.open("../sourceFiles/logo.png")
    # Ridimensiona l'immagine se necessario
    logo = logo.resize((700, 300))
    logo_image = ImageTk.PhotoImage(logo)
    # Mostra l'immagine
    logo_label = tk.Label(start_window, image=logo_image, bg=col1)
    logo_label.pack(pady=20)
    # bottone per passare al grafico
    start_button = tk.Button(start_window,
                             text="Apri file",
                             background=col6,
                             foreground=col1,
                             activebackground=col4,
                             activeforeground=col5,
                             highlightbackground=col3,
                             width=15,
                             height=1,
                             border=0,
                             cursor='hand2',
                             font=('Sans-serif', 14),
                             borderwidth=0,
                             command=file_from_start)
    start_button.pack(pady=20)

    start_window.mainloop()


if __name__ == "__main__":
    main()
