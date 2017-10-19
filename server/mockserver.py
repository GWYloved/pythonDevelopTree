import socket

class Request(object):
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.body = ''

def run(host='', port= 3000):
    with socket.socket() as s:
        while True:
            s.listen(3)
            connection, address = s.accept()
            r = connection.recv(1024)
            r = r.decode('utf-8')
            print('r = ',r)
            if len(r.split()) <2:
                continue
            request.method = r.split()[0]
            request.body = r.split('\r\n\r\n')[1]
            path = r.split()[1]
            response = response_for_path(path)
