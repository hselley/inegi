# INEGIpy

Este repositorio intenta mostrar los pasos a seguir para la instalación, configuración y uso de la API de la INEGI.

La [documentación del proyecto](https://github.com/andreslomeliv/DatosMex/tree/master/INEGIpy) se encuentra alojada en Github.

De acuerdo con las dependencias descritas por los desarrolladores en su documentación,
se deben instalar varios paquetes necesarios para el funcionamiento de la API.

* pandas
* numpy
* requests
* shapely
* geopandas

Para este ejercicio se utilizará ArchLinux y el comando para instalar todos los paquetes es el siguiente:

```bash 
sudo pacman -S python-pandas python-numpy python-requests python-shapely python-geopandas
```

Ahora se debe crear un _sandbox_ para la instalación del paquete externo via `pip`.

```bash
python -m venv inegi_python
source ~/inegi_python/bin/activate
cd ~/inegi_python
pip install INEGIpy
```
