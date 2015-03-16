#!/usr/bin/python

import matplotlib
import matplotlib.pyplot as plt
import json
import re

def document_format(link):
    match = re.search('(?<=\.)\w+$', link)
    if match:
        return match.group(0)
    else:
        return False

def extract_json_data():
    with open('../scraper/documents.json') as data_file:
        data = json.load(data_file)

    extensions = ['xls', 'xlsx', 'ppt', 'pptx', 'doc', 'docx', 'odt', 'ods',
                  'odg', 'odp', 'pdf']

    domains = {}
    formats_counters = {}
    total = 0
    for extension in extensions:
        formats_counters[extension] = 0

    for element in data:
        if not domains.has_key(element["domain"]):
            domains[element["domain"]] = formats_counters.copy()

        format_ = document_format(element["link"])
        if format_:
            domains[element["domain"]][format_] += 1
            total += 1

    data_file.close()

    return domains, total


def generate_graphs():

    domains,total = extract_json_data()
    for domain in domains:

        #del domains[domain]['pdf']

        rects = plt.bar(range(len(domains[domain].keys())),
                domains[domain].values(), align='center', facecolor='#FE9A2E')

        plt.xticks(range(len(domains[domain].keys())), domains[domain].keys())

        plt.title(str(domain))
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., int(height), '%d'% int(height),
                    ha='center')
        
        plt.ylabel("Cantidad de ficheros")

        plt.ylim(0.0,plt.ylim()[1]+2)

        plt.savefig('img/grafica_de_'+domain+'.png')

        plt.close()

if __name__ == "__main__":
    generate_graphs()

