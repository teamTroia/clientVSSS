import socket

class CommandSender:
    def __init__(self, ip, port):
        self._addr = (ip, port)
        self._sock = self._create_socket()
    
    def _create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(self._addr)
        except socket.error as e:
            str(e)
        return sock
    
    def send_command(self, command):
        cmd = command.encode()
        self._sock.sendall(cmd)
    
    def receive_command(self, buffer_size):
        command = self._sock.recv(buffer_size)
        return command