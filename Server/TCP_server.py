import socket


class LocalServer(object):
    def __init__(self, socket, ip_port, nomefile):
        self.socket = socket
        self.ip_port = ip_port
        self.nomefile = nomefile
        self.socket.bind(self.ip_port)
        self.socket.listen(5)
        print ('Server Attivo ... , Indirizzo %s porta %s' % self.ip_port)
        self.start_connection()
        

    def start_connection(self):
        while True:
            # aspettando la connessione del client
            print ('Attesa connessione del client >>>:')
            [client_connection, self.ip_port] = self.socket.accept()

            try:
                print ('Questo Client e Connesso (', self.ip_port, ')\n')
                
                with open(self.nomefile, "rb") as file:

                    print ('Invio dati in corso...\n')
                    while True:
                        dati = file.read()
                        if dati:
                            client_connection.sendall(dati)
                        else:
                            break
                    print("Invio Dati Completato!\n")
                    file.close()
            
            finally:
                # Ad invio finito Connessione chiusa
                client_connection.close()


#Metodo connessione TCP/IP
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
indirizzo_server = (("192.168.0.105", 8080))
nomefile = "capture.jpg"
server = LocalServer(socket, indirizzo_server, nomefile)


