import socket
import os
import time

HOST = "192.168.1.108"
PORT = 9955
def main():
      client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      connectionName = ("1200640")
      client.sendto(bytes(connectionName, "utf-8"), (HOST, PORT))
      response, server_address = client.recvfrom(1024)
      print(response.decode())
      time.sleep(10)
      os.system("rundll32.exe user32.dll,LockWorkStation")


while True:
    
    main()