Informe para el cumplimiento del Esquema Nacional de Interoperabilidad (ENI) en la US
=====================================================================================

Esta aplicación genera un informe en formato html de los tipos de enlaces a documentos generados en cada uno de los dominios de la Universidad de Sevilla.

- Enlace de descarga del ENI: http://administracionelectronica.gob.es/ctt/resources/Soluciones/145/Area%20descargas/RD_4/2010-Esquema-Nacional-de-Interoperabilidad--ENI-.pdf?idIniciativa=145&idElemento=68

- Enlace al catálogo de estándares (BOE): http://www.boe.es/boe/dias/2012/10/31/pdfs/BOE-A-2012-13501.pdf


PASOS PARA LA INSTALACIÓN Y LA EJECUCIÓN DEL SCRIPT

1) INSTALAR  el framework scrapy usando pip, las librerias matplotlib para generar las gŕaficas y python-crontab para las tareas programadas:

    $ sudo pip install Scrapy
     - Dependencias: python2.7, setuptools, lxml, pyOpenSSL

    $ sudo pip install python-crontab

    - Más información en: https://pypi.python.org/pypi/python-crontab

    $ sudo apt-get install matplotlib

    - Más información sobre scrapy en la web oficial: http://scrapy.org/

2) DESCARGAMOS EL PROYECTO:

    $ git clone https://github.com/emoronayuso/scraping-US.git

3) ANTES DE EJECUTAR LOS SCRIPTS DEBEMOS MODIFICAR LA RUTA ABSOLUTA DE CADA UNO, esto evitará problemas en la ejecución de la tarea programada:

    - Modificamos la línea 'root_directory' en los ficheros:
          ./html/generate_html.py
          ./graphs/general.py
          ./cron_job/script_crontab.py

      Indicando la ruta ABSOLUTA de la aplicación.

4) EJECUTAMOS EL SCRIPT:$ cd ./scraping-US/scraper/

    $ scrapy crawl documents_spider -o <DIRECTORIO_RAIZ>/scraper/documents.json

5) GENERAMOS LAS IMAGENES DE LAS GRÁFICAS, que se guardarán en la la carpeta ".html/files/graphs/":

    $ cd ../graphs/
    $ python general.py

6) GENERAMOS EL HTML ESTÁTICO CON EL INFORME, que se guardará en la carpeta "./hmlt/files/":

    $ cd ../html/
    $ python gererante_html.py


7) [OPCIONAL] Los PASOS 4,5 y 6 se pueden automatizar generando una tarea programada que se ejecutará cada 7 días a la 1 de la madrugada (por defecto), generando un html stático junto con las gŕaficas en el directorio "./html/files/", para ello:

    $ cd ./cron_job/
    $ sudo python script_crontab.py


