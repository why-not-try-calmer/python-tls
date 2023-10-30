from pathlib import Path
from socket import socket, AF_INET, SOCK_STREAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER
from os import environ

host = environ.get("HOST", "0.0.0.0")
port = int(environ.get("PORT", "8443"))

path_to_cert = Path(__file__).parent.joinpath(environ["CERT"])
path_to_key = Path(__file__).parent.joinpath(environ["CERT_KEY"])

context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain(path_to_cert, path_to_key)

with socket(AF_INET, SOCK_STREAM) as server:
    server.bind((host, port))
    server.listen(1)
    with context.wrap_socket(server, server_side=True) as tls:
        connection, address = tls.accept()
        print(f"Connected by {address}\n")

        data = connection.recv(1024)
        print(f"Client Says: {data}")

        connection.sendall(b"You're welcome")
