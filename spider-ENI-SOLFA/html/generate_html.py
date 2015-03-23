#!/usr/bin/python
# -*- coding: utf-8 -*-

import markup
import os
import json
import re
import datetime

root_directory = '/home/kike/scraping-US/spider-ENI-SOLFA/'

def generate_html():
    page = markup.page()
    page.init(title="Informe de tipos de archivos en la US",
              charset="utf-8",
              lang="es")
    page.body(style="background-color: #FFFFFF;")

    page.div(style="text-align:center;")
    page.img(src="http://solfa.us.es/solfa/themes/danland/danblog/logo.png")
    page.div.close()
    
    page.div(style="float: right; border: 0px coral solid; width: 30%;")
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

    domains, total_link = extract_json_links()

    hour = datetime.datetime.now().strftime('%H:%M')
    day = datetime.datetime.now().strftime('%d/%m/%y')

    page.div(style="border: 0px solid; width: 34%; float: right; display: block; text-align:center;")
    page.h4("N&uacute;mero de enlaces: "+str(total_link))
    page.h3("&Uacute;ltima actualizaci&oacute;n")
    page.h4("El d&iacute;a "+day+" a las "+hour)
    page.div.close()
    
    page.div(style="border: 0px solid; width: 35%; text-align:center; display: block;")
    page.h3("Listado de enlaces a documentos de los distintos dominios de la US")
    page.h3.close()
    page.div.close()
    page.div(style="border: 0px solid; width: 35%;")
    page.ul()

    del domains['www.mediacioncivilymercantil.cfp.us.es']

    for domain in domains:
        page.li()
        page.a("Documentos en: " + domain, href='./links/'+domain+'.html')
        page.li.close()
    page.ul.close()
    page.div.close()

    page.div(style="height: 30px ; width: 100%; border: 0px solid; text-align:center;  background-color: #dd9900;")
    page.h2("Resumen del informe")
    page.h2.close()
    page.div.close()


    #list_dir = os.listdir("./files/graphs")
    list_dir = os.listdir(root_directory+"html/files/graphs")
    for dir_ in list_dir:
        page.img(src="./graphs/"+dir_, style="text-align: center; margin-left: auto; margin-right: auto; display: block;")
   
    #with open("./files/index.html", 'w') as new_file:
    with open(root_directory+"html/files/index.html", 'w') as new_file:

        new_file.write(str(page))

    for domain in domains:
        page = markup.page()
        page.init(title=domain, charset="utf-8", lang="es")

        links = domains[domain]

        count = 0
        page.table(summary="Services, or Links box template", style=" border: 1px none black;")
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

        #with open("./files/links/"+domain+".html", 'w') as new_file:
        with open(root_directory+"html/files/links/"+domain+".html", 'w') as new_file:
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
    #with open("../scraper/documents.json") as data_file:
    with open(root_directory+"scraper/documents.json") as data_file: 
        data = json.load(data_file)

    domains = {}
    count = 0

    for element in data:
        if not domains.has_key(element["domain"]):
            domains[element["domain"]] = []

        domains[element["domain"]].append((element["link"],
            element["location"]))

        count += 1

    return domains, count

if __name__ == "__main__":
    generate_html()
