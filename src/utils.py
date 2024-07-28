def read_speeds_from_file(path):
    speeds = []
    start_reading = False
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if (line == "0,00") or (line == "00,00") or (line == "00,0") or (line == '0,0'):
                start_reading = True
                continue
            if start_reading:
                speeds.append(float(line.replace(',', '.')))
    speeds.insert(0,00.0)
    incremento = 1.52
    chiave_iniziale= 0.00
    dizionario={}
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
        table.insert('','end',values=(dist_f,speed_f))
    print(table)


