import socket


class Server():

    def start(self):
        #Per Protocollo UDP utilizzare - socket.SOCK_DGRAM
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Il server è in ascolto sulla porta 8080
        self.server_socket.bind(("", 8080))
        self.server_socket.listen(5)

        self.client_socket, address = self.server_socket.accept()

        while True:
             #Riceviamo i dati inviati dal client.
             data = self.client_socket.recv(512)
             data = data.decode('UTF-8')
             print("Ricevuto:" , data)

             #Controlliamo che il client non abbia inviato un comando di chiusura.
             if ( data == 'q' or data == 'Q'):
                 self.client_socket.close()
                 break;


             #Se non è un comando di chiusura facciamo qualcosa con i dati ricevuti.
             else:
                 #FARE QUALCOSA CON I DATI.
                 #Inviare i dati processati dal server.
                 #self.client_socket.send (bytes(data, 'UTF-8'))
                self.sendImage()


    def sendImage(self):
        img = open("icon_cancel.png", 'rb')
        #byteImage = img.read()

        while True:
            strng = img.readline(512)
            print(strng)
            if not strng:
                break
            self.client_socket.sendall(strng)

        img.close()
        #self.client_socket.sendall(byteImage)
        print("Data sent successfully")
        exit()

s = Server()
s.start()