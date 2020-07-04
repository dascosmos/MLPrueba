# MLPrueba

Desarrollo de la prueba Stellar System en Python 3.7

## Prerequisitos y librerias necesarias

- Python 3.7
- pip
- virtualenv
- numpy
- point2d
- flask

## Correr el proyecto
### Configurar venv
#### Desde linea de comandos
* teniendo python y pip instalados en el equipo y seteadas las variables de entorno para python, 
abrir un comand prompt en la carpeta del proyecto.
* ejecutar el comando pip install virtualenv
* crear el entorno virtual:
    * virtualenv env
* iniciar el entorno virtual:
    * .\env\Scripts\activate
* Instalar los paquetes con el pip del entorno virtual:
    * pip install -r requeriments.txt
* cambiar a la carpeta app:
    * cd ..\app
* Ejecutar python:
    * python webService.py

#### Desde Pycharm

* Descargar e instalar [Pycharm community edition](https://github.com/dascosmos/MLPrueba)
* Clonar el proye4cto
* Abrir proyecto desde Pycharm
* Ir a File/settings/Project:MLPrueba/Project interpreter
* Hacer clic en el icono de la herramienta ubicado en la superor derecha y luego en add
* Seleccionar new envirenment (por defecto es env) y seleccionar el interprete de python
* Click en ok
* Hacer click en el icono '+' que se muestra a la derecha, escribir el nombre del paquete a instalar, seleccionar el paquete y hacer click en install package
* Hacer esta operacion para cada uno de los paquetes:
    * numpy
    * point2d
    * flask
* Pulsar ok y ya se habrá instaldo el venv con los paquetes necesarios.

##### Correr desde pycharm:
* Click en edit configurations ubicado en la parte superior derecha de la pantalla
* Click en el icono '+' que se muestra en la parte superior izquierda de la ventana que acaba de aparecer
* Seleccionar python
* En el cuadro de dialogo de "Script path" seleccionar el icono de la carpata ubicado al extremo derecho
* Seleccionar el archivo webService.py y pulsar ok
* Hacer click en el icono play en la parte superior derecha.
* Acceder desde el navegador a [http://localhost:5000/](http://localhost:5000/)

### URLs de acceso
* [http://localhost:5000/](http://localhost:5000/) para la pagina principal
* [http://localhost:5000/forecast/weather](http://localhost:5000/forecast/weather) para los datos de todos los dias (a 10 años)
* [http://localhost:5000/forecast/byDay?day={dia}](http://localhost:5000/forecast/byDay?day={dia}) para obtener la informacion del clima del dia especificado
 



