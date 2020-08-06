import socket
import threading

class HttpProxy:
    logger = None
    def __init__(self, host, port, user_data):
        self.host = host
        self.port = port
        self.user_data = user_data
        HttpProxy.logger = open('log.txt', 'w')

    def run(self):

        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket.bind((self.host, self.port))
        serverSocket.listen(10)
        while True:
            # print('proxy server is ready...')
            (clientSocket, clientAddress) = serverSocket.accept()
            t = threading.Thread(target=self.http_proxy, args=(clientSocket, clientAddress,))
            t.setDaemon(True)
            t.start()


    def http_proxy(self, clientSocket, clientAddress):
        try:
            request = clientSocket.recv(1024)
            first_line = request.split(b'\n')[0]
            first_line_str = str(first_line, 'utf-8')
            HttpProxy.logger.write('Info : first line = ' + first_line_str + '\n')
            if first_line_str.strip() != '':
                url = first_line.split(b' ')[1]
                url_string = str(url, 'utf-8')
                HttpProxy.logger.write('Info : url = ' + url_string + '\n')
                if True:
                    http_pos = url.find(b"://")
                    temp = None
                    if (http_pos == -1):
                        temp = url
                    else:
                        temp = url[(http_pos + 3):]
                    port_pos = temp.find(b":")
                    webserver_pos = temp.find(b"/")
                    if webserver_pos == -1:
                        webserver_pos = len(temp)
                    webserver = ""
                    port = -1
                    if (port_pos == -1 or webserver_pos < port_pos):
                        port = 80
                        webserver = temp[:webserver_pos]

                    else:
                        port = int((temp[(port_pos + 1):])[:webserver_pos - port_pos - 1])
                        webserver = temp[:port_pos]
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(30)
                    sock.connect((webserver, port))
                    sock.sendall(request)
                    category_index = -1
                    website_index = -1
                    for i in range(len(self.user_data)):
                        for j in range(len(self.user_data[i][1])):
                            if self.user_data[i][1][j][0] in url_string:
                                category_index = i
                                website_index = j
                                break
                    while 1:
                        data = sock.recv(1024)
                        if (len(data) > 0):
                            clientSocket.send(data)
                            if category_index != -1:
                                self.user_data[category_index][2] += 1
                                self.user_data[category_index][1][website_index][1] += 1
                        else:
                            break
        except IndexError:
            # print('Index Error')
            HttpProxy.logger.write('Exception : Index Error\n')
        except ConnectionResetError:
            # print('Connection reset error')
            HttpProxy.logger.write('Exception : Connection reset error\n')
        except socket.timeout:
            # print('Socket timeout Error')
            HttpProxy.logger.write('Exception : Socket timeout Error\n')
        except TimeoutError:
            HttpProxy.logger.write('Exception : Timeout Error\n')
        except ConnectionRefusedError:
            HttpProxy.logger.write('Exception : Connection Refused Error\n')
