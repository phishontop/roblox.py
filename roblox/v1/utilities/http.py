import socket
import ssl
import json

blocksize = 1024 ** 2
ssl_context = ssl.create_default_context()


class ProxyError(Exception):
    """Raises an error when client proxy has not worked"""
    pass


class HttpClient:

    def __init__(self, host, proxy=None, timeout=20):
        self.host = host
        self.timeout = timeout

        if proxy is None:
            self.connection = self.create()
        else:
            self.proxy = proxy.split(":")
            self.connection = self.createProxy()

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        if value is None:
            raise ProxyError("Proxy has failed to connect")
        else:
            self._connection = value

    def sslWrap(self, sock):
        sock = ssl_context.wrap_socket(
            sock,
            server_side=False,
            do_handshake_on_connect=False,
            suppress_ragged_eofs=False,
            server_hostname=self.host)
        sock.do_handshake()
        return sock

    def createProxy(self):
        try:
            sock = socket.socket()
            sock.settimeout(self.timeout)
            sock.connect(
                (self.proxy[0], int(self.proxy[1]))
            )
            request = f"""CONNECT {self.host}:443 HTTP/1.1\r\n\r\n""".encode()
            sock.send(request)

            connect_resp = sock.recv(4096)
            if connect_resp.startswith(b"HTTP/1.1 200"):
                return self.sslWrap(sock)
        except:
            return None

    def create(self, proxy=None):
        sock = socket.socket()
        sock.settimeout(self.timeout)
        sock.connect(
            (self.host, 443)
        )
        sock = self.sslWrap(sock)

        return sock

    def lowerByte(self, byte):
        byteString = byte.decode()
        byteLower = byteString.lower().encode()
        return byteLower

    def send(self, sock, data):
        sock.sendall(data)
        response, body = sock.recv(blocksize).split(b"\r\n\r\n", 1)
        lowerResponse = self.lowerByte(response)
        content_length = int(lowerResponse.split(b"content-length: ", 1)[1].split(b"\r\n", 1)[0])
        while content_length > len(body):
            body += sock.recv(blocksize)

        return body, response

    def parseHeaders(self, headers):
        if headers is None:
            return ""
        headersRequest = ""
        for headerType, headerValue in headers.items():
            headersRequest += f"{headerType}: {headerValue}\r\n"
        return headersRequest

    def get(self, resource, headers=None):
        headers = self.parseHeaders(headers)
        request = f"""GET {resource} HTTP/1.1\r\nHost: {self.host}\r\n{headers}\r\n\r\n""".encode()

        return self.send(self.connection, request)

    def post(self, resource, data, headers=None):
        headers = self.parseHeaders(headers)
        contentLength = len(json.dumps(data))
        request = f"POST {resource} HTTP/1.1\r\nHost: {self.host}\r\n{headers}Content-Length: {contentLength}\r\nContent-Type: application/json\r\n\r\n{data}".encode()
        return self.send(self.connection, request)