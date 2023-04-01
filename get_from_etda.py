import os
import re
import pandas as pd
from submodule_get_ta_details_etda import*
from submodule_get_ta_etda import*
from submodule_process_etda import*
from submodule_extract_mitre_id import*

def get_from_etda(industry_list, dt_string, filepath):

    #----------------------------Variable Declaration----------------------------#

    threat_actors_lst = []
    url_lst = []
    country_lst = []
    motivation_lst = []
    first_seen_lst = []
    sponsor_lst=[]
    description_lst = []
    observed_sector_lst = []
    observed_countries_lst = []
    tools_lst = []
    information_lst = []
    mitre_attack_lst = []
    playbook_lst = []
    industry_name_lst = []
    id_lst = []
    associated_group_list = []

    for industry in industry_list:

        industry_name_list = []

        print("query: " + str(industry))

        url = "https://apt.etda.or.th/cgi-bin/listgroups.cgi?c=&v=&s=" + str(industry) + "&m=&x="

        #----------------------------Get Threat Actor----------------------------#

        threat_actors_list, url_list = get_threat_actor_combined(url)

        # ----------------------------Get Threat Actor details----------------------------#

        country_list, motivation_list, first_seen_list, sponsor_list, description_list, observed_sector_list, observed_countries_list, tools_list, information_list, mitre_attack_list, playbook_list = get_threat_actor_details_combined(url_list)


        for i in range(len(country_list)):
            industry_name_list.append(industry)

        country_lst.append(country_list)
        motivation_lst.append(motivation_list)
        first_seen_lst.append(first_seen_list)
        sponsor_lst.append(sponsor_list)
        description_lst.append(description_list)
        observed_sector_lst.append(observed_sector_list)
        observed_countries_lst.append(observed_countries_list)
        tools_lst.append(tools_list)
        information_lst.append(information_list)
        mitre_attack_lst.append(mitre_attack_list)
        playbook_lst.append(playbook_list)

        industry_name_lst.append(industry_name_list)
        threat_actors_lst.append(threat_actors_list)
        url_lst.append(url_list)

    # ----------------------------Create Dataframe----------------------------#

    threat_actors = threat_actors_lst[0] + threat_actors_lst[-1]
    url = url_lst[0] + url_lst[-1]
    country = country_lst[0] + country_lst[-1]
    motivation = motivation_lst[0] + motivation_lst[-1]
    first_seen = first_seen_lst[0] + first_seen_lst[-1]
    sponsor = sponsor_lst[0] + sponsor_lst[-1]
    description = description_lst[0] + description_lst[-1]
    observed_sector = observed_sector_lst[0] + observed_countries_lst[-1]
    observed_countries = observed_countries_lst[0] + observed_countries_lst[-1]
    tools = tools_lst[0] + tools_lst[-1]
    information = information_lst[0] + information_lst[-1]
    mitre_attack = mitre_attack_lst[0] + mitre_attack_lst[-1]
    playbook = playbook_lst[0] + playbook_lst[-1]
    industry_name = industry_name_lst[0] + industry_name_lst[-1]


    ta_information = {
            'Threat Actor': threat_actors,
            'URL': url,
            'country': country,
            'motivation': motivation,
            'first seen': first_seen,
            'sponsor': sponsor,
            'description': description,
            'observed sector': observed_sector,
            'observed countries': observed_countries,
            'tools': tools,
            'information': information,
            'mitre attack': mitre_attack,
            'playbook': playbook,
            'industry class': industry_name
    }

    df = pd.DataFrame(ta_information)

    print("writing to file......")

    df_dedup = df.drop_duplicates(subset=['Threat Actor'])

    threat_actors_dedup = list(dict.fromkeys(threat_actors))
    for i in range(len(threat_actors_dedup)):

        id = i+10
        id_lst.append(id)
        associated_group_list.append("nil")


    df_dedup["id"] = id_lst

    df_dedup["associated groups"] = associated_group_list

    df_out = submodule_extract_mitre_id(df_dedup)

    print("writing to etda data to excel")

    df_out.to_excel(filepath + str(dt_string) + "_" + "etda.xlsx", index=False)

    return df_out

