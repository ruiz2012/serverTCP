import socket

def StartServer():
	host = 'localhost'
	port = 5000

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
		server_socket.bind((host, port))
		server_socket.listen()
		print(f"Servidor iniciado en {host}:{port}. Esperando conexiones...")

		while True:
			connex, addr = server_socket.accept()
			print(f"Conexion exitosa con {addr}")

			with connex:
				while True:
					data = connex.recv(1024).decode()
					if not data:
						break

					if data == "DESCONEXION":
						print(f"Cerrando conexion con {addr}")
						break

					else:
						message = data.upper()
						if "SERVER" in message:
							message = message.replace("SERVER", "CLIENTE") 
						connex.sendall(message.encode())

				print("Conexion cerrada. Disponible para conexiones nuevas")

if __name__ == "__main__":
	StartServer()