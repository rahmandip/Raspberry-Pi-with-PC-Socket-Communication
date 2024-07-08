import socket

serverIP = '192.168.xx.xx' # Manually input the IP Address of PI
serverPort = int(input("Enter the server port number: "))  # Manually input the port number
bufferSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    cmd = input("Enter command (TEMP/HUM): ").upper()
    if cmd in ['TEMP', 'HUM']:
        cmd = cmd.encode('utf-8')
        UDPClientSocket.sendto(cmd, (serverIP, serverPort))
        data, address = UDPClientSocket.recvfrom(bufferSize)
        data = data.decode('utf-8')
        print("Data from Server:", data)
        print("Server's Address:", address[0])
        print("Server's Port:", address[1])
    else:
        print("Invalid command, please enter TEMP or HUM.")


if __name__ == '__main__':
    print("Client is running")

