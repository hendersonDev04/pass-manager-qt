# 🐍 PCAP Python Password-Manager App  

Este proyecto fue desarrollado como parte de mi proceso de certificación **PCAP – Certified Associate in Python Programming**.  
Su objetivo es demostrar habilidades obtenidas en el curso de Python Fundamentals 1 y 2 de CISCO, las cuales incluyen **fundamentos de programacion**,
**Variables**, **Condicionales y Bucles**, **Manejo de errores**, **programación orientada a objetos** y **buenas prácticas** de desarrollo. 
Lo que me permitio rendir el examen existosamente y ser certificado por la Python Institute.

---

## 🚀 Características principales
- CRUD de [Entidades, por ejemplo: *Registro de Passwords*, *Mostrar Passwords*, etc.].
- Arquitectura basada en **tres capas**: Vista, Controllers y Models.
- Persistencia de datos con **SQLite3**.
- Código estructurado siguiendo las recomendaciones **PEP 8**.

---

## 🗂 Estructura del proyecto
pass-manager-qt/
├── app/
│ ├── Views/ # Parte con la que interacciona el usuario.
│ ├── controllers/ # Manejo de la lógica de entrada/salida
│ ├── models/ # Recuperacion de datos.
│ ├── Dto/ # Clases encargadas de transportar y validar los datos entre capas.
│ ├── connection/ # Conexión a la base de datos
│ ├── assets/ # Iconos.
│ └── app_manager.py # Administra logica entre login y la App.
│ └── main.py # Punto de entrada
├── requirements.txt # Dependencias
└── README.md

## ⚙️ Instalación y ejecución

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/hendersonDev04/password-manager-qt.git

2. **Entra al directorio del proyecto**:
   ```bash
   cd password-manager-qt  
3. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
4. **Activa el entorno virtual**:
   En Window :
     venv\Scripts\activate
   En Mac :
     source venv/bin/activate
5. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
6. **Ejecuta la aplicación**:
   ```bash
   python app/main.py

## Nota:
- Las views fueron creadas con el programa Qt Designer