import pandas as pd

def process(lst):

    lower = (map(lambda x: x.lower(), lst))
    lowered = list(lower)

    dedup = list(dict.fromkeys(lowered))

    return dedup

def combine(df_aptmap, df_etda, dt_string, filepath):

    #-----------------------------------Define Variables-------------------------------#

    Threat_Actor_list = []
    country_list = []
    motivation_list = []
    first_seen_list = []
    sponsor_list = []
    description_list = []
    observed_sector_list = []
    observed_countries_list = []
    tools_list = []
    industry_name_list = []
    id_lst = []

    URL_list = []
    information_list = []
    mitre_attack_list = []
    playbook_list = []

    id_lst_aptmap = []

    #-----------------------------------Define Filepaths-------------------------------#
    input_filepath_etda = "C:\\Users\\Admin\\Downloads\\Threat_actor\\March_2023\\24-03-2023_combined_threat_actor.xlsx"
    input_filepath_aptmap = "C:\\Users\\Admin\\Downloads\\aptmap\\24_03_2023_apt_map.xlsx"
    #output_filepath = "C:\\Users\\Admin\\Downloads\\aptmap\\aviation_aerospace.xlsx"

    #-----------------------------------Read Dataframe-------------------------------#

    df_etda = pd.read_excel(input_filepath_etda)
    df_aptmap = pd.read_excel(input_filepath_aptmap)

    #----------------------------------Get Max ID----------------------------------------#

    max_id = max(df_etda["id"].values.tolist())

    #-----------------------------------process----------------------------------------#
    for index, row in df_aptmap.iterrows():

        aptmap_apt = list(row["Threat Actor"].split(", "))
        aptmap_lower = (map(lambda x: x.lower(), aptmap_apt))
        aptmap_lowered = list(aptmap_lower)

        a_set = set(aptmap_lowered)

        check = []
        id_list = []
        for index2, row2 in df_etda.iterrows():

            etda_apt = list(row2["Threat Actor"].split(", "))

            etda_apt_lower = (map(lambda x: x.lower(), etda_apt))
            etda_apt_lowered = list(etda_apt_lower)

            b_set = set(etda_apt_lowered)

            if (a_set & b_set):

                id_list.append(row2["id"])
                check.append(1)

            else:

                id_list.append(0)
                check.append(0)

        id_list_dedup = list(dict.fromkeys(id_list))
        unify_id = sum(id_list_dedup)

        if sum(check) == 0:

            Threat_Actor_list.append(row["Threat Actor"])
            country_list.append(row["country"])
            motivation_list.append(row["motivation"])
            first_seen_list.append(row["first seen"])
            sponsor_list.append(row["sponsor"])
            description_list.append(row["description"])
            observed_sector_list.append(row["observed sector"])
            observed_countries_list.append(row["observed countries"])
            tools_list.append(row["tools"])
            industry_name_list.append(row['industry class'])
            max_id+=1
            id_lst.append(max_id)

            id_lst_aptmap.append(max_id)

            URL_list.append("")
            information_list.append("")
            mitre_attack_list.append("")
            playbook_list.append("")

        else:

            id_lst_aptmap.append(unify_id)

    df_aptmap["id"] = id_lst_aptmap

    df_new = pd.DataFrame({
                'Threat Actor': Threat_Actor_list,
                'URL': URL_list,
                'country': country_list,
                'motivation': motivation_list,
                'first seen': first_seen_list,
                'sponsor': sponsor_list,
                'description': description_list,
                'observed sector': observed_sector_list,
                'observed countries': observed_countries_list,
                'tools': tools_list,
                'information': information_list,
                'mitre attack': mitre_attack_list,
                'playbook': playbook_list,
                'industry class': industry_name_list,
                'id': id_lst
            })

    df_concat = pd.concat([df_etda, df_new])

    #-----------------------------------process2----------------------------------------#

    Threat_Actor_list = []
    country_list = []
    motivation_list = []
    first_seen_list = []
    sponsor_list = []
    description_list = []
    observed_sector_list = []
    observed_countries_list = []
    tools_list = []
    industry_name_list = []
    id_lst = []

    URL_list = []
    information_list = []
    mitre_attack_list = []
    playbook_list = []

    id_lst_aptmap = []

    for index, row in df_aptmap.iterrows():

        aptmap_id = row["id"]

        check = []

        for index2, row2 in df_concat.iterrows():

            concat_id = row2["id"]


            if (aptmap_id == concat_id):
                check.append(1)

                #print(list((row["Threat Actor"] + ", " + row2["Threat Actor"]).split(", ")))
                #print(process(list((row["Threat Actor"] + ", " + row2["Threat Actor"]).split(", "))))

                #print(process(list((row["country"] + ", " + row2["country"]).split(", "))))
                print(process(list((row["motivation"] + ", " + row2["motivation"]).split(", "))))
                #process(list((row["first seen"] + ", " + row2["first seen"]).split(", ")))
                #process(list((row["Sponsor"] + ", " + row2["Sponsor"]).split(", ")))
                #process(row["observed sector"] + row2["observed sector"])
                #process(row["observed countries"] + row2["observed countries"])
                #process(row["tools"] + ", " + row2["tools"])






            else:

                check.append(0)
