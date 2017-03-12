import socket

class Client():

    def start(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("192.168.0.100", 8080))

        while True:
            data = input("Invia( Digita q or Q per chiudere):")
            if (data != 'Q' and data != 'q'):
                client_socket.send(bytes(data, 'UTF-8'))
                # data = client_socket.recv(512)
                # print ("Ricevuto:" , data.decode('UTF-8'))

                fp = open("img.png", 'wb')
                while True:
                    strng = client_socket.recv(512)
                    if not strng:
                        break
                    fp.write(strng)
                #byteImage = client_socket.recv(12024)
                #fp.write(byteImage)
                fp.close()
                print("Data Received successfully")
                exit()
            else:
                client_socket.send(bytes(data, 'UTF-8'))
                client_socket.close()
                break;


c = Client()
c.start()