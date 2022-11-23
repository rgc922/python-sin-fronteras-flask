Curso UDEMY
Python sin fronteras: HTML, CSS, Flask y MySQL


https://www.udemy.com/course/python-sin-fronteras-html-css-mysql/
Created by: Nicolas Schurmann

Aplicación de ToDo (tareas pendientes) elaborada con interfaz en HTLM, Python haciendo uso de Flask y SQL para almacenar los usuarios y las tareas generadas en la página.

Particularmente, la práctica de Flask fue bastante difícil de seguir. Muchos conceptos nuevos se introducen muy rápido en esta practica. 

Dentro de los formularios de preguntas y respuestas, encontré que yo no era el único con problemas para seguir la práctica y ejecutar el programa tal como lo mostraban en el curso.

Errores sencillos pero complicados de encontrar, como por ejemplo, un espacio dentro de una instrucción de SQL que cambia de renglón y por tanto se debe dejar un espacio o arriba al final o abajo al comienzo hicieron que tomara bastante tiempo reproducir el programa completo.

Por esta razón, publico este repositorio para que puedan ver mi código que después de bastantes horas funcionó tal como lo mencionan en el código.

NO incluyo en el repositorio la carpeta venv porque esta debe generarse con las comandos mencionados en el curso. 

A continuación, un corto resumen de los comandos para ejecutarlo en MAC

1. Instalar ambiente virtual con python3 -m venv venv (en Windows es py -3 -m venv venv)
2. A continuación se activa el entorno virtual con: . venv/bin/activate (tener cuidado con el espacio)
3. Instalar werkzeug con: pip3 install werkzeug
4. Instalar conector de base de datos con flask: pip3 install mysql-connector-python
5. Instalar flask con: pip3 install Flask


Asegurarse de que el usuario en MySql Workbench tenga los permisos adecuados para el usuario que va a manipular las tablas en Python. Mi usuario es user y el password de pruebas es 123456. La base de datos se llama prueba.

También se deben declarar las variables de entorno para acceder a la base de datos:

export FLASK_DATABASE_HOST=’localhost’
export FLASK_DATABASE_PASSWORD=’USER’
export FLASK_DATABASE_USER=’123456’
export FLASK_DATABASE=’prueba’

finalmente, se ejecuta: flask run