Requisitos Previos

-Tener Python 3.6+ instalado

-Descargar ambos archivos en la misma carpeta:

-servidor.py

-cliente.py

1. Iniciar el Servidor

-Abrir una terminal/consola
-Navegar hasta la carpeta de los archivos
-Ejecutar:
    python servidor.py

2. Iniciar el Cliente
-Abrir otra terminal nueva (dejar el servidor corriendo)
-En la misma carpeta, ejecutar:
    python cliente.py

Prueba 1: Mensaje Normal
-En el cliente, ingresar:
   cleinte envia: Hola server
    
-Verificar:
    Servidor muestra:
    Respuesta responde: HOLA CLIENTE

Prueba 2: Desconexión Controlada
-En el cliente, ingresar:
    cliente envia: DESCONEXION
-Verificar:
    Servidor responde: Servidor cierra conexion con el cliente.

Detener servidor con Ctrl+C en su terminal