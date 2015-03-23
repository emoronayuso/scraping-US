#/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json
import re

root_directory = '/home/kike/scraping-US/spider-ENI-SOLFA/'

def document_format(link):
    match = re.search('(?<=\.)\w+$', link)
    if match:
        return match.group(0)
    else:
        return False

def extract_json_data():
    with open(root_directory+'scraper/documents.json') as data_file:
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


# Function map_color_type_link: recommended (re), no recommended (no_re), standard (st), no standard (no_st)
# return RGB color
def map_color_type_link(exten):
    map_group = {    're': {'color': "#7DD7FD", 'ext': ['pdf']},
                  'no_re': {'color': "#FA964A", 'ext': ['docx', 'xlsx', 'pptx']},
                     'st': {'color': "#6BE666", 'ext': ['odt', 'ods', 'odg', 'odp']},            
                  'no_st': {'color': "#EF5555", 'ext': ['doc', 'xls', 'ppt']}  
                }
    
    for group_ext in map_group.keys():
        for ext in map_group[group_ext]['ext']:
            if exten == ext:
                return map_group[group_ext]['color']

    return "#FFFFAA"



def generate_graphs():

    domains,total = extract_json_data()

    del domains['www.mediacioncivilymercantil.cfp.us.es']

    for domain in domains:

        #del domains[domain]['pdf']

        rects = plt.bar(range(len(domains[domain].keys())),
                domains[domain].values(), align='center')

        plt.xticks(range(len(domains[domain].keys())), domains[domain].keys())

        plt.title(str(domain))

        st_patch = mpatches.Patch(color='#6BE666', label="Est"+u"á"+"ndar")
        no_st_patch = mpatches.Patch(color='#EF5555', label="No est"+u"á"+"ndar")
        re_patch = mpatches.Patch(color='#7DD7FD', label="Recomendado")
        no_re_patch = mpatches.Patch(color='#FA964A', label='No recomendado')
        plt.legend(loc=2, handles=[st_patch, no_st_patch, re_patch, no_re_patch])

        count = 0
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., int(height), '%d'% int(height),
                    ha='center')

            extension_ = domains[domain].keys()[count]

            rect.set_color(map_color_type_link(extension_))
            count += 1

        
        plt.ylabel("Cantidad de ficheros")

        plt.ylim(0.0,plt.ylim()[1]+2)

        plt.savefig(root_directory+'html/files/graphs/grafica_de_'+domain+'.png')

        plt.close()

if __name__ == "__main__":
    generate_graphs()

