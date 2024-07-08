import socket

serverAddress = ('192.168.31.27', 2222)
bufferSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == '__main__':
    print("Client is running")

while True:
    cmd = input("Enter command (TEMP/HUM): ").upper()
    if cmd in ['TEMP', 'HUM']:
        cmd = cmd.encode('utf-8')
        UDPClientSocket.sendto(cmd, serverAddress)
        data, address = UDPClientSocket.recvfrom(bufferSize)
        data = data.decode('utf-8')
        print("Data from Server:", data)
        print("Server's Address:", address[0])
        print("Server's Port:", address[1])
    else:
        print("Invalid command, please enter TEMP or HUM.")
