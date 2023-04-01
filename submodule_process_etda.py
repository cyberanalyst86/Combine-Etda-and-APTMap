import pandas as pd

def los(elem):
    # initialize an empty string
    str1 = ""

    if type(elem) != str:
     # traverse in the string
        if len(elem) > 1:
            for ele in elem:
                str1 += ele + " "

        else:

            for ele in elem:
                str1 += ele

            # return string
            return str1

    else:

        # return string
        return elem

def process_etda_apt(df):

    country_list = []
    motivation_list = []
    observed_sector_list = []
    observed_countries_list = []
    tools_list = []
    information_list = []
    mitre_attack_list = []
    information_list = []
    playbook_list = []

    for index, row in df.iterrows():

        row_country = los(row["country"])

        country_list.append(row_country)

        row_motivation = los(row["motivation"])

        motivation_list.append(row_motivation)

        row_observed_countries = los(row["observed countries"])

        observed_countries_list.append(row_observed_countries)

        row_observed_sector = los(row["observed sector"])

        observed_countries_list.append(row_observed_sector)

        row_tools = los(row["tools"])

        tools_list.append(row_tools)

        row_information = los(row["information"])

        information_list.append(row_information)

        row_mitre_attack = los(row["mitre attack"])

        mitre_attack_list.append(row_mitre_attack)

        row_playbook = los(row["playbook"])

        playbook_list.append(row_playbook)

    df["country"] = country_list
    df["motivation"] = motivation_list
    df["observed sector"] = motivation_list
    df["observed countries"] = observed_countries_list
    df["tools"] = observed_countries_list
    df["information"] = information_list
    df["mitre attack"] = mitre_attack_list
    df["playbook"] = playbook_list

    return df








