import socket
import time
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9001)

tim = 60030
lat = 1099010
lon = 7482000

m = '>REV0519101' + str(tim) + '+' + str(lat) + '-0' + str(lon) + '00000012;ID=ENOMOTO<\r\n'
try:
    sent = sock.sendto(bytes(m, 'UTF-8'), server_address)

finally:
    print('Done')

sock.close()