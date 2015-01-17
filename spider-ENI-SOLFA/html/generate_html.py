#!/usr/bin/python

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

    domains = extract_json_links()

    for domain in domains:
        page.a("Documentos en: " + domain, href=domain+'.html')
        page.br()

    list_dir = os.listdir("../graphs/img")
    for dir_ in list_dir:
        page.img(src="../../graphs/img/"+dir_)

    with open("./files/informe_extensiones.html", 'w') as new_file:
        new_file.write(str(page))

    for domain in domains:
        page = markup.page()
        page.init(title=domain, charset="utf-8", lang="es")

        links = domains[domain]

        for link in links:
            page.a(link[0], href=link[0])
            page.a('origen', href=link[1])
            page.br()
            page.br()

        with open("./files/"+domain+".html", 'w') as new_file:
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
