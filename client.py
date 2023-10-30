from socket import create_connection
from ssl import SSLContext, PROTOCOL_TLS_CLIENT
from pathlib import Path
from os import environ

host = environ.get("HOST", "server")
hostname = environ["HOSTNAME"]
port = int(environ.get("PORT", "8443"))

path_to_cert = Path(__file__).parent.joinpath(environ["CERT"])

context = SSLContext(PROTOCOL_TLS_CLIENT)
context.load_verify_locations(path_to_cert)

with create_connection((host, port)) as client:
    with context.wrap_socket(client, server_hostname=hostname) as tls:
        print(f"Using {tls.version()}\n")
        tls.sendall(b"Hello, world")
        data = tls.recv(1024)
        print(f"Server says: {data}")
