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
    page.body(style="background-color: #F5FBEF;")

    page.div(style="text-align:center;")
    page.img(src="http://solfa.us.es/solfa/themes/danland/danblog/logo.png")
    page.div.close()
    page.h2("Listado de enlaces a documentos de los distintos dominios de la US")

    page.div(style="float: right;")
    page.h3("Enlaces de inter&eacute;s", style="text-align: center;")
    page.ul()
    page.li()
    page.a("Esquema Nacional de Interoperabilidad (ENI)", href="http://administracionelectronica.gob.es/ctt/resources/Soluciones/145/Area%20descargas/RD_4/2010-Esquema-Nacional-de-Interoperabilidad--ENI-.pdf?idIniciativa=145&idElemento=68")
    page.li.close()
    page.li()
    page.a("Cat&aacute;logo de est&aacute;ndares", href="http://www.boe.es/boe/dias/2012/10/31/pdfs/BOE-A-2012-13501.pdf")
    page.li.close()
    page.ul.close()
    page.div.close()

    domains = extract_json_links()

    page.div()
    page.ul()
    for domain in domains:
        page.li()
        page.a("Documentos en: " + domain, href=domain+'.html')
        page.li.close()
    page.ul.close()
    page.div.close()

    page.div()
    page.h3("Tipos de archivos")
    page.ul()
    page.li("Estandar")
    page.li.close()
    page.ul.close()
    page.div.close()


    list_dir = os.listdir("../graphs/img")
    for dir_ in list_dir:
        page.img(src="../../graphs/img/"+dir_, style="float: left; display: block;")
        page.a.close()

    with open("./files/informe_extensiones.html", 'w') as new_file:
        new_file.write(str(page))

    for domain in domains:
        page = markup.page()
        page.init(title=domain, charset="utf-8", lang="es")

        links = domains[domain]


        count = 0
        page.table(summary="Services, or Links box template", style=" border: 1px none black;")
        #page.style("border-width=1px")
        for link in links:

            color_line = map_color_type_link(link[0])
            page.tr(style="background-color: "+color_line+";")

            page.td()
            page.a(link[0], href=link[0])
            page.td.close()
            page.td()
            page.a('fuente', href=link[1])
            page.td.close()
            page.tr.close()
            
            count += 1
        page.table.close()

        with open("./files/"+domain+".html", 'w') as new_file:
            new_file.write(str(page))


def document_format(link):
    match = re.search('(?<=\.)\w+$', link)
    if match:
        return match.group(0)
    else:
        return False


# Function map_color_type_link: recommended (re), no recommended (no_re), standard (st), no standard (no_st)
# return RGB color
def map_color_type_link(link):
    map_group = {    're': {'color': "#7DD7FD", 'ext': ['pdf']},
                  'no_re': {'color': "#FA964A", 'ext': ['docx', 'xlsx', 'pptx']},
                     'st': {'color': "#6BE666", 'ext': ['odt', 'ods', 'odg', 'odp']},            
                  'no_st': {'color': "#EF5555", 'ext': ['doc', 'xls', 'ppt']}  
                }
    
    for group_ext in map_group.keys():
        for ext in map_group[group_ext]['ext']:
            if document_format(link) == ext:
                return map_group[group_ext]['color']

    return "#FFFFAA"



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
