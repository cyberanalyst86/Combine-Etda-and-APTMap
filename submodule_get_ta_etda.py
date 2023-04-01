import requests
import re

def get_threat_actor_combined(url):

    # -------------------------Variable Declaration------------------------#

    main_url = "https://apt.etda.or.th/cgi-bin/showcard.cgi?g="

    threat_actors_list = []

    url_list = []

    #-------------------------Web Request-------------------------#

    page = requests.get(url)

    threat_actors = re.findall(r"Show the card .* class", page.text)

    # -------------------------Iterate Web Content-------------------------#

    for ta in threat_actors:

        threat_actor = ta.split(" class")[0].split("for ")[1].replace('\"', '')

        threat_actors_list.append(threat_actor.replace("Subgroup: ",""))

        #--------------------------threat actor url--------------------------#

        query = threat_actor.replace(',', "%2C").replace(" ", "%20")

        url_list.append(main_url + str(query))

    return threat_actors_list, url_list