import re


def read_speeds_from_file(path):
    speeds = []
    reading = False

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()

            if re.match(r'^\d+,\d+$', line):
                if line not in ["0,00", "00,00", "00,0", "0,0"]:
                    reading = True
                if reading:
                    speeds.append(float(line.replace(',', '.')))

    speeds.insert(0, 0.0)

    incremento = 1.52
    chiave_iniziale = 0.00
    dizionario = {}

    for value in speeds:
        dizionario[round(chiave_iniziale, 2)] = value
        chiave_iniziale += incremento

    return dizionario


def populate_table(table, dict):
    for item in table.get_children():
        table.delete(item)
    for (dist, speed) in enumerate(dict):
        speed_f = f"{speed:.2f}"
        dist_f = f"{dist:.2f}"
        table.insert('', 'end', values=(dist_f, speed_f))
