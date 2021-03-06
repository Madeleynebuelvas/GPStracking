import socket
import sqlite3
import time
import datetime

method = 'tcp'  # Reemplaza por tcp si lo requieres

if method == 'udp':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
else:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9001
sock.bind(("", port))

print('Esperando conexión')

# Crear base de datos y habilitarla
conn = sqlite3.connect('log.db')
cc = conn.cursor()
cc.execute('''CREATE TABLE IF NOT EXISTS log
            (IP TEXT, puerto TEXT, mensaje TEXT, tiempo TEXT)''')
conn.commit()

# Escuchar el puerto por un tiempo indefinido
while 1:
    data, (r_ip, r_port) = sock.recvfrom(1024)

    # Crear set de datos
    t = datetime.datetime.fromtimestamp(time.time()).strftime('''
        %Y-%m-%d %H:%M:%S''')
    sent_data = (r_ip, r_port, data, t)

    # Hacer que se escriban los datos en una base de datos SQLite
    cc.execute('''INSERT INTO log VALUES
        (?,?,?,?)''', sent_data)
    conn.commit()

    # La siguiente línea es para que puedas ver lo que hay en la base de datos
    # actualmente, para la versión final se omite
    for row in cc.execute('SELECT * FROM log ORDER BY tiempo'):
        print(row)
