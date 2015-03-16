#!/usr/bin/python
# -*- coding: utf-8 -*-

import markup
import os
import json
import re

def generate_html():
    page = markup.page()
    page.init(title="Informe de tipos de archivos en la US",
              charset="utf-8",
              lang="es")

    page.img(src="http://solfa.us.es/solfa/themes/danland/danblog/logo.png")
    page.h1("Informe de tipos de archivos en la US")

    page.a("Esquema Nacional de Interoperabilidad (ENI)", href="http://administracionelectronica.gob.es/ctt/resources/Soluciones/145/Area%20descargas/RD_4/2010-Esquema-Nacional-de-Interoperabilidad--ENI-.pdf?idIniciativa=145&idElemento=68")
    page.a("Catalogo de estandares", href="http://www.boe.es/boe/dias/2012/10/31/pdfs/BOE-A-2012-13501.pdf")

    domains = extract_json_links()
    
    page.ul()
    for domain in domains:
        page.li()
        page.a("Documentos en: " + domain, href=domain+'.html')
        page.li.close()
    page.ul.close()

    list_dir = os.listdir("../graphs/img")
    for dir_ in list_dir:
        page.img(src="../graphs/img/"+dir_)

    with open("informe_extensiones.html", 'w') as new_file:
        new_file.write(str(page))

    for domain in domains:
        page = markup.page()
        page.init(title=domain, charset="utf-8", lang="es")

        links = domains[domain]

        count = 0
        page.table(summary="Services, or Links box template", style=" border: 1px none black;")
        #page.style("border-width=1px")
        for link in links:
            if count % 2 == 0:
                page.tr(style=" background-color: #FFFFFF;")
            else:
                page.tr(style=" background-color: #D8D8D8;")
            
            page.td()
            page.a(link[0], href=link[0])
            page.td.close()
            page.td()
            page.a('fuente', href=link[1])
            page.td.close()
            page.tr.close()
            
            count += 1
        page.table.close()

        with open(domain+'.html', 'w') as new_file:
            new_file.write(str(page))

def extract_json_links():
    with open("../scraper/documents.json") as data_file:
        data = json.load(data_file)

    domains = {}

    for element in data:
        if not domains.has_key(element["domain"]):
            domains[element["domain"]] = []

        domains[element["domain"]].append((element["link"],
            element["location"]))

    return domains

if __name__ == "__main__":
    generate_html()
    # extract_json_links()
