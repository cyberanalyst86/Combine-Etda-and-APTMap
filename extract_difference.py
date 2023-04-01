import pandas as pd

def dedup(lst):

    lower = (map(lambda x: x.lower(), lst))
    lowered = list(lower)

    dedup_list = list(dict.fromkeys(lowered))

    # initialize an empty string
    str1 = ""

    if type(dedup_list) == list:
    # traverse in the string

        if len(dedup_list ) > 1:

            listToStr = '~'.join([str(elem) for elem in dedup_list ])


            str1 = listToStr.replace("~", ", ")

            # return string
            return str1.replace("nil, ", "")

        else:

            listToStr = "".join([str(elem) for elem in dedup_list])

            str1 = listToStr

            return str1.replace("nil, ", "")

    else:

        # return string
        return dedup_list.replace("nil, ", "")

def dedup_list(lst):

    dedup_list = list(dict.fromkeys(lst))

    return dedup_list

def check_intersection(a_set, b_set, check, id_list, id):

    if (a_set & b_set):

        id_list.append(id)
        check.append(1)

    else:

        id_list.append(0)
        check.append(0)

    return id_list, check

def lower_case(lst):
    lower = (map(lambda x: x.lower(), lst))
    lowered = list(lower)

    return lowered


def append_difference_to_etda(df_aptmap, df_etda, dt_string, filepath):
    # -----------------------------------Define Variables-------------------------------#

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
    associated_groups_lst = []

    URL_list = []
    information_list = []
    mitre_attack_list = []
    playbook_list = []

    id_lst_aptmap = []

    # ----------------------------------Get Max ID----------------------------------------#

    max_id = max(df_etda["id"].values.tolist())

    # -----------------------------------Extract difference to etda----------------------------------------#
    for index, row in df_aptmap.iterrows():

        aptmap_ta_lowercase = lower_case(list(row["Threat Actor"].split(", ")))

        a_set = set(aptmap_ta_lowercase)

        check = []
        id_list = []

        for index2, row2 in df_etda.iterrows():

            etda_ta_lowercase = lower_case(list(row2["Threat Actor"].split(", ")))

            b_set = set(etda_ta_lowercase)

            id_list, check = check_intersection(a_set, b_set, check, id_list, row2["id"])

        id_list_dedup = dedup_list(id_list)
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
            industry_name_list.append(row["industry class"])
            associated_groups_lst.append(row["associated groups"])

            max_id += 1

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
        'id': id_lst,
        'associated groups': associated_groups_lst
    })

    df_concat = pd.concat([df_etda, df_new])

    print("writing to appended etda data to excel")

    df_concat.to_excel(filepath + str(dt_string) + "_" + "appended_etda.xlsx", index=False)

    # ---------------------------------------------------------------------------------------------------#

    df_aptmap["id2"] = id_lst_aptmap

    id_list = df_aptmap["id"].values.tolist()

    # -----------------------------------dedup the aptmap with id----------------------------------------#

    df_dedup =  df_aptmap.groupby(['id']).agg(lambda col: ','.join(col))

    df_dedup_new = dedup_within(df_dedup)

    df_dedup_new.to_excel(filepath + str(dt_string) + "_" + "df_aptmap_w_id.xlsx")

    return df_concat, df_dedup_new , id_list


def dedup_within(df):

    index_list = df.index.tolist()

    for id in index_list:

        df.loc[id, ['Threat Actor']] = dedup(df["Threat Actor"].loc[id].split(","))
        df.loc[id, ['URL']] = dedup(df["URL"].loc[id].split(","))
        df.loc[id, ['country']] = dedup(df["country"].loc[id].split(","))
        df.loc[id, ['motivation']] = dedup(df["motivation"].loc[id].split(", "))
        df.loc[id, ['first seen']] = dedup(df["first seen"].loc[id].split(","))
        df.loc[id, ['sponsor']] = dedup(df["sponsor"].loc[id].split(","))
        df.loc[id, ['description']] = dedup(df["description"].loc[id].split(","))
        df.loc[id, ['observed sector']] = dedup(df["observed sector"].loc[id].split(","))
        df.loc[id, ['observed countries']] = dedup(df["observed countries"].loc[id].split(","))
        df.loc[id, ['tools']] = dedup(df["tools"].loc[id].split(","))
        df.loc[id, ['information']] = dedup(df["information"].loc[id].split(","))
        df.loc[id, ['mitre attack']] = dedup(df["mitre attack"].loc[id].split(","))
        df.loc[id, ['playbook']] = dedup(df["playbook"].loc[id].split(","))
        df.loc[id, ['industry class']] = dedup(df["industry class"].loc[id].split(","))
        df.loc[id, ['associated groups']] = dedup(df["associated groups"].loc[id].split(","))

    return df