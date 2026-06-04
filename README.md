# Django Architecture Boilerplate & Core Setup

Este repositorio contiene una plantilla base (*boilerplate*) para el despliegue e inicialización de aplicaciones web robustas utilizando **Django** y **Python**. El objetivo principal de este proyecto es establecer una estructura monolítica limpia, configurar de forma segura el entorno de desarrollo y validar el ciclo de vida inicial del servidor siguiendo las mejores prácticas de la industria.

## 🚀 Capacidades Técnicas y Componentes

* **Inicialización de la Arquitectura:** Configuración del esqueleto base del proyecto mediante el CLI de Django (`django-admin`).
* **Aislamiento de Entornos:** Configuración y uso de entornos virtuales para la gestión controlada de dependencias, evitando conflictos globales en el sistema.
* **Ciclo de Vida del Servidor:** Configuración de los archivos nucleares (`settings.py`, `urls.py`, `wsgi.py`) para el correcto enrutamiento y levantamiento del servidor local.
* **Estructura de Archivos Extensible:** Organización modular de carpetas preparada para la inyección progresiva de aplicaciones internas, modelos y vistas.

## 🛠️ Stack Tecnológico

* **Lenguaje de Programación:** Python 3.x
* **Framework Principal:** Django 4.x / 5.x
* **Entorno Virtual:** `venv` / `virtualenv`
* **Servidor de Desarrollo:** WSGI integrado de Django

## ⚙️ Configuración del Núcleo y Solución de Problemas

El desarrollo se enfocó en resolver la configuración inicial que garantiza la escalabilidad de cualquier software web:

1. **Gestión de Dependencias:** Creación del archivo `requirements.txt` para asegurar que el proyecto sea perfectamente replicable en cualquier entorno de desarrollo o servidores de Integración Continua (CI).
2. **Estrategia de Debugging Inicial:** Configuración y control del entorno `DEBUG=True` en `settings.py` para la captura y resolución de errores HTTP iniciales durante la fase de desarrollo.
3. **Control de Puertos y Host:** Validación del servidor web local contra direcciones seguras loops (`127.0.0.1` / `localhost`).

## 🔧 Guía de Despliegue Local

Sigue estos pasos detallados para inicializar y correr esta base de proyecto en tu máquina:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/longaresf/django-architecture-boilerplate.git](https://github.com/longaresf/django-architecture-boilerplate.git)
   ```
2. Ingresar al directorio:
   Bash
   cd django-architecture-boilerplate

3. Crear y activar el entorno virtual:
   Bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate

4. Instalar el framework y dependencias:
   Bash
   pip install -r requirements.txt

5. Ejecutar el servidor de desarrollo:
   Bash
   python manage.py runserver

   Una vez ejecutado, abre tu navegador e ingresa a http://127.0.0.1:8000/ para comprobar el renderizado de la pantalla de bienvenida de Django.

✒️ Créditos y Contexto Académico

    Francisco Longares - Desarrollador Backend Python - longaresf

    Este proyecto representa el hito práctico de inicialización y control de entornos del programa Full Stack Python de Desafío Latam.
   
