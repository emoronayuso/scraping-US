Informe para el cumplimiento del Esquema Nacional de Interoperabilidad (ENI) en la US
=====================================================================================

Esta aplicación genera un informe en formato html de los tipos de enlaces a documentos generados en cada uno de los dominios de la Universidad de Sevilla.


PASOS PARA LA INSTALACIÓN Y LA EJECUCIÓN DEL SCRIPT

1) INSTALAR  el framework scrapy usando pip, y las librerias matplotlib:

    $ sudo pip install Scrapy
     - Dependencias: python2.7, setuptools, lxml, pyOpenSSL

    $ sudo apt-get install matplotlib

    - Más información sobre scrapy en la web oficial: http://scrapy.org/

2) DESCARGAMOS EL PROYECTO:

    $ git clone https://github.com/emoronayuso/scraping-US.git

3) EJECUTAMOS EL SCRIPT:$ cd ./scraping-US/scraper/
  
    $ scrapy crawl documents_spider -o documents.json

4) GENERAMOS LAS IMAGENES DE LAS GRÁFICAS, que se guardarán en la la carpeta "./graphs/img":

    $ cd ../graphs/
    $ python general.py

 5) GENERAMOS EL HTML ESTÁTICO CON EL INFORME, que se guardará en la carpeta "./hmlt/files/":

    $ cd ../html/
    $ python gererante_html.py

