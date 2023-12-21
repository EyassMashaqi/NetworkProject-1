import socket
import time

HOST = "192.168.1.108"
PORT = 9955


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print("Server is running...")

    data, address = server.recvfrom(1024)#packet size
    connectionName = data.decode()
    print ("received message from ", connectionName)
    if(connectionName == "1200640"or connectionName=="1193102"or connectionName=="1200085"):

        server.sendto(b"The screen will lock in 10 seconds", address)
        time.sleep(10)
        print("The screen is locked")
    else:
        server.sendto(b"Invalid connection name", address)


main()