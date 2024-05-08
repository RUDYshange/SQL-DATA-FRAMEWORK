# Server
import socket
import mysql.connector
class Server:
    def __init__(self, port,

                 listen=5,

                 timeout=10,

                 buf=4096,

                 queueSize=10):

        self.port = port

        self.listen = listen

        self.soc = socket.socket(socket.AF_INET,

                                 socket.SOCK_STREAM)

        self.timeout = timeout

        self.bufsize = buf

        self.queueSize = queueSize

    def send(self, conn, string):

        conn.send(bytes(string, encoding='ascii'))

    def recv(self, conn):

        return str(conn.recv(self.bufSize), encoding='ascii')

    def run(self):

        print("Server has started ...\nport:", self.port,

              "\nlisten number:", self.listen)

        print()

        try:

            self.soc.bind(('', self.port))

            while (True):

                self.soc.listen(self.listen)

                connection, address = self.soc.accept()

                choice = self.recv(connection)

                conn = mysql.connector.connect(user='root',

                                               password='Password11.',

                                               host='127.0.0.1',

                                               database='video_store')

                if (choice == '1'):

                    cur = conn.cursor()

                    phone = self.recv(connection)

                    query = "SELECT * FROM customers_table "

                    query += "WHERE phone = '%s'" % (phone)

                    try:

                        cur.execute(query)

                        result_set = cur.fetchall()

                        if (len(result_set) == 0):

                            r = "Yes"

                            self.send(connection, r)

                            fname = self.recv(connection)

                            sname = self.recv(connection)

                            address = self.recv(connection)

                            query = "INSERT INTO customers_table(fname,sname,address,phone)"

                            query += "VALUES ('" + str(fname) + "',"

                            query += "'" + str(sname) + "',"

                            query += "'" + str(address) + "',"

                            query += "'" + str(phone) + "');"

                            try:

                                cur.execute(query)

                                client_back = "Customer Added"

                            except:

                                client_back = "Error occured when trying to addd customer"

                            self.send(connection, client_back)

                        if (len(result_set) > 0):
                            r = "No"

                            self.send(connection, r)

                            client_back = "Customer is Already Exists"

                            self.send(connection, client_back)

                    except:

                        print("Error unable to fetch data")

                        client_back = ("Not found")

                        self.send(connection, client_back)

                if (choice) == 'x':
                    connection.close()

                cur.close()

                conn.commit()

                conn.close()



        except:

            print("Port in use")


if __name__ == "__main__":
    s = Server(8081, listen=1000)

    s.run()



