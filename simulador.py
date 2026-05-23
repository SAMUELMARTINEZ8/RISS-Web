import time
import random
import requests

# La dirección de tu API local
URL = "http://127.0.0.1:8000/api/lecturas/"

print("Iniciando simulador de placa K2E/H (Proyecto RISS)...")
print("Presiona Ctrl+C en esta terminal para detener el envío de datos.")
print("-" * 50)

while True:
    # 1. Simular la lectura del sensor PT-1000 (temperatura entre 70.0 y 90.0 grados)
    temperatura_actual = round(random.uniform(70.0, 90.0), 1)
    
    try:
        # 2. Enviar el dato a nuestra API mediante una petición POST
        # Nota: FastAPI espera el dato en la URL como parámetro de consulta (?temperatura=X)
        respuesta = requests.post(f"{URL}?temperatura={temperatura_actual}")
        
        if respuesta.status_code == 200:
            print(f"[+] Éxito: Temperatura de {temperatura_actual}°C enviada al servidor.")
        else:
            print(f"[-] Error del servidor: código {respuesta.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("[-] Error: No se pudo conectar al servidor. Asegúrate de que uvicorn esté corriendo.")
    
    # 3. Esperar 2 segundos antes de la siguiente lectura
    time.sleep(2)