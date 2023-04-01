import requests
import re
from urllib.request import urlopen
import json

def los(row):
    # initialize an empty string
    str1 = ""

    if type(row) == list:
     # traverse in the string

        listToStr = '~'.join([str(elem) for elem in row])

        str1 = listToStr.replace("~", ", ")
        # return string
        return str1

    else:

        # return string
        return row

def get_threat_actor_details_combined(url_list):
    country_list = []
    motivation_list = []
    first_seen_list = []
    sponsor_list = []
    description_list = []
    observed_sector_list = []
    observed_countries_list = []
    tools_list = []
    information_list = []
    mitre_attack_list = []
    playbook_list = []

    # -------------------------Variable Declaration------------------------#

    detail_main_url = "https://apt.etda.or.th"


    for url in url_list:

        # -------------------------Web Request-------------------------#

        page = requests.get(url)

        download_statement = re.findall(r" or <a.href=.*title", page.text)

        query = download_statement[0].split("\"")[1]

        response = urlopen(detail_main_url + query)

        data_json = json.loads(response.read())

        # -------------------------Get Data-------------------------#

        if "country" in data_json["values"][0]:
            #print(data_json["values"][0]["country"])
            country_list.append(los(data_json["values"][0]["country"]))

        else:
            country_list.append("nil")

        if "motivation" in data_json["values"][0]:
            #print(data_json["values"][0]["motivation"])
            motivation_list.append(los(data_json["values"][0]["motivation"]))

        else:
            motivation_list.append("nil")

        if "first-seen" in data_json["values"][0]:
            #print(data_json["values"][0]["first-seen"])
            first_seen_list.append(los(data_json["values"][0]["first-seen"]))

        else:
            first_seen_list.append("nil")


        if "sponsor" in data_json["values"][0]:
            #print(data_json["values"][0]["sponsor"])
            sponsor_list.append(los(data_json["values"][0]["sponsor"]))
        else:
            sponsor_list.append("nil")

        if "description" in data_json["values"][0]:
            #print(data_json["values"][0]["description"])
            description_list.append(los(data_json["values"][0]["description"]))

        else:
            description_list.append("nil")

        if "observed-sectors" in data_json["values"][0]:
            # print(data_json["values"][0]["observed-countries"])
            observed_sector_list.append(los(data_json["values"][0]["observed-sectors"]))

        else:
            observed_countries_list.append("nil")

        if "observed-countries" in data_json["values"][0]:
            #print(data_json["values"][0]["observed-countries"])
            observed_countries_list.append(los(data_json["values"][0]["observed-countries"]))

        else:
            observed_countries_list.append("nil")

        if "tools" in data_json["values"][0]:
            #print(data_json["values"][0]["tools"])
            tools_list.append(los(data_json["values"][0]["tools"]))
        else:
            tools_list.append("nil")


        if "information" in data_json["values"][0]:
            #print(data_json["values"][0]["information"])
            information_list.append(los(data_json["values"][0]["information"]))
        else:
            information_list.append("nil")


        if "mitre-attack" in data_json["values"][0]:
            #print(data_json["values"][0]["mitre-attack"])
            mitre_attack_list.append(los(data_json["values"][0]["mitre-attack"]))
        else:
            mitre_attack_list.append("nil")

        if "playbook" in data_json["values"][0]:
            #print(data_json["values"][0]["Playbook"])
            playbook_list.append(los(data_json["values"][0]["playbook"]))
        else:
            playbook_list.append("nil")



    return country_list, motivation_list, first_seen_list, sponsor_list, description_list, observed_sector_list, observed_countries_list, tools_list, information_list, mitre_attack_list, playbook_list