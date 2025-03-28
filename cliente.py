import socket

def StartCliente():
    host = 'localhost'
    port = 5000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Conectado al servidor en {host}:{port}")
        
        while True:
            message = input("Cliente envia: ")
            client_socket.sendall(message.encode())
            
            if message == "DESCONEXION":
                break
            
            else:
                response = client_socket.recv(1024).decode()
                print(f"Servidor responde: {response}")
            
        print("Servidor cierra conexion con el cliente.")

if __name__ == "__main__":
    StartCliente()