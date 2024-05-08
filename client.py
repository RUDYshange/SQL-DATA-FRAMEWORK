#client
import socket
import os
import time


class Client:
    def __init__(self,
                 host,
                 port,
                 bufSize=1024,
                 timeout=10):
        self.client = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.bufSize = bufSize
        self.timeout = timeout

    def connect(self):
        self.client.connect((self.host, self.port))

    def close(self):
        self.client.close()

    def send(self, string):
        self.client.send(bytes(string, 'ascii'))

    def recv(self):
        return str(self.client.recv(self.bufSize), encoding='ascii')


if __name__ == "__main__":

    while True:
        c = Client('localhost', 8081)
        c.connect()

        os.system("cls")
        print("\t==============================================")
        print("\t|                VIDEO STORE                 |")
        print("\t==============================================")
        print("\t| 1. Register Customer                       |")
        print("\t| 2. Register Movie                          |")
        print("\t==============================================")
        print("\t| 3. Hire Out Movie                          |")
        print("\t| 4. Return Movie                            | ")
        print("\t==============================================")
        print("\t| x. Exit                                    | ")
        print("\t==============================================")

        choice = input("\tChoice: ")
        c.send(choice)
        if choice == '1':
            os.system("cls")
            phone = input("Please enter phone number client: ")
            c.send(phone)

            r = c.recv()
            if r == " yes":
                os.system("cls")
                print("\t===============================================")
                print("\t===============================================")
                print("\t                  ADD CUSTOMER")
                print("\t===============================================")
                fname = input("Please enter the first name of client: ")
                c.send(fname)
                sname = input("Please enter client's surname: ")
                c.send(sname)
                address = input("Please enter the client's address: ")
                c.send(address)
            server_reply = c.recv()
            print(server_reply)

        if choice =='2':
            os.system("cls")
            print("\t===============================================")
            print("\t===============================================")
            print("\t                  ADD MOVIE")
            print("\t===============================================")
            vname = input("Please enter movie name: ")
            c.send(vname)
            type = input("Please enter the movies type: ")
            if type == 'R':
                print("New Movie")
            if type != 'B':
                continue
            print('Old MOVIE')
        c.send(type)
        server_reply = c.recv()
        print(server_reply)

        if choice =='3':
            os.system("cls")
            print("\t===============================================")
            print("\t===============================================")
            print("\t                  Hire MOVIE")
            print("\t===============================================")
            phone = input("Please enter customers numbers: ")
            c.send(phone)
            videoID = input("Please enter the videoID: ")
            print('Hired out')
        c.send(type)
        server_reply = c.recv()
        print(server_reply)

        if choice =='4':
            os.system("cls")
            print("\t===============================================")
            print("\t===============================================")
            print("\t                  Return Movie")
            print("\t===============================================")
            videoID = input("Please enter videoID: ")
            c.send(videoID)
            print('Movie Returned')
        c.send(type)
        server_reply = c.recv()
        print(server_reply)

        if choice == 'x':
            c.close()

        wait = input("please press enter to return to the main menu...")
        c.close()