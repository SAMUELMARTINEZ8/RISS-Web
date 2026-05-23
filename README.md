# Remote Internet-Based Supervision System (RISS) - V1.0

## Descripción del Proyecto
RISS es un sistema integral de monitoreo e IoT diseñado para la supervisión remota de variables críticas en calderas y entornos industriales/hoteleros. El objetivo principal es optimizar la eficiencia energética y reducir costos operativos mediante la automatización, eliminando la necesidad de costosas pantallas físicas en el sitio.

## Pila Tecnológica (Tech Stack)
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla), Chart.js (Métricas en tiempo real).
- **Backend:** Python, FastAPI (Arquitectura de API robusta y rápida).
- **Base de Datos:** PostgreSQL / SQLModel (Persistencia e histórico de telemetría).
- **Infraestructura:** Despliegue en la nube mediante plataformas de servicios web y bases de datos gestionadas.

## Arquitectura del Sistema
1. **Dispositivos Edge / Hardware:** Módulos de control que leen sensores térmicos (PT-1000) y transmiten datos a través de conectividad estándar.
2. **Servidor Central:** API REST encargada de recibir las lecturas, procesar alertas de ciberseguridad e ingestar la información en la base de datos.
3. **Panel Web de Usuario:** Interfaz responsiva B2B accesible desde cualquier navegador para la consulta de métricas y estados en tiempo real.

## Instrucciones de Instalación (Entorno Local)
1. Clonar el repositorio: `git clone <url_del_repositorio>`
2. Instalar las dependencias de Python: `pip install -r requirements.txt`
3. Ejecutar el servidor de la API: `uvicorn main:app --reload`
4. Abrir `index.html` en el navegador.

## Licencia
Este proyecto es de código abierto bajo la licencia MIT.

---
*Developed by Martinez Reyes Samuel*