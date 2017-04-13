import socket, threading


class Server_Deamon(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ip = "192.168.0.107"
        self.port = 8080
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip,self.port))
        self.socket.listen(5)
        print("Socket Creato\n")

    def run(self):
        while True:
            # aspettando la connessione del client
            print('Server Attivo, Connessione aperta su >>>:',self.ip , self.port)
            (client_connection, (self.ip, self.port)) = self.socket.accept()

            try:
                print('Questo Client e Connesso (', self.ip, self.port, ')\n')
                with open("capture.jpg", "rb") as imageFile:
                    while True:
                        self.dati = imageFile.read()
                        client_connection.sendall(self.dati)
                        break
                    imageFile.close()
                print('Invio Dati completato\n')

            finally:
                # Ad invio finito Connessione chiusa
                client_connection.close()