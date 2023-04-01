from selenium import webdriver
import pandas as pd
import datetime
import re


def get_from_aptmap(industry_list, dt_string, filepath):
    #------------------------------Declare Variables------------------------------#

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
    associated_groups_lst =[]


    #----------------------------APTMap Query URL------------------------------#

    url = "https://andreacristaldi.github.io/APTmap/"

    for industry in industry_list:

        print("query: " + str(industry))

        # ----------------------------Initialize the Chrome Driver------------------------------#

        driver = webdriver.Chrome(r"chromedriver")

        # ------------------------------Get into APT MAP------------------------------#

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(0.5)

        # ------------------------------Click on Go To Map------------------------------#

        driver.find_element("id", "start-globe").click()
        driver.implicitly_wait(0.5)
        # ------------------------------Click on Search------------------------------#
        xpath = "//*[@id=\"search\"]/h3"
        driver.find_elements("xpath", xpath)[0].click()
        driver.implicitly_wait(0.5)

        #------------------------------Click on Search (by filter)------------------------------#
        driver.find_element("id", "searchTarget").send_keys(industry)
        driver.implicitly_wait(0.5)
        driver.find_element("id", "btnsearch").click()
        driver.implicitly_wait(0.5)


        #------------------------------Scrap Data------------------------------#
        #aviation 1 - 13
        #aerospace 1 - 22

        if industry == "Aviation":

            rg = 13

        elif industry == "Aerospace":

            rg = 22

        else:

            error = "error"

        for i in range(1, rg):

            xpath = "//*[@id=\"searchPlaceHolder\"]/li[" + str(i) + "]"
            info = driver.find_elements("xpath", xpath)[0].text

            APT = list(info.split("\n"))[0]

            try:

                Other_names = re.findall(r"Other names:.*", info)[0].replace("Other names: ", "")

                threat_actors = (APT + ", " + Other_names)

            except IndexError:

                threat_actors = APT

            threat_actors_lst.append(threat_actors.replace("APT", "APT "))

            try:

                Location_lst = re.findall(r"Location:.*", info)[0].replace("Location: ", "")

            except IndexError:

                Location_lst = "nil"


            country_lst.append(Location_lst)

            try:

                Description= re.findall(r"Description:.*", info)[0].replace("Description: ", "")

            except IndexError:
                Description = "nil"

            description_lst.append(Description)

            try:

                Associated_group = re.findall(r"Associated groups:.*", info)[0].replace("Associated groups: ", "")

            except IndexError:
                Associated_group = "nil"

            associated_groups_lst.append(Associated_group)

            try:

                First_seen = re.findall(r"First seen:.*", info)[0].replace("First seen: ", "")

            except IndexError:
                First_seen = "nil"

            first_seen_lst.append(First_seen)

            try:

                Sponsor = re.findall(r"Sponsor:.*", info)[0].replace("Sponsor: ", "")

            except IndexError:
                Sponsor = "nil"

            sponsor_lst.append(Sponsor)

            try:

                Motivation = re.findall(r"Motivation:.*", info)[0].replace("Motivation: ", "")

            except IndexError:
                Motivation = "nil"

            motivation_lst.append(Motivation)

            try:

                Sector_lst = re.findall(r"Targets:.*:", info)[0].replace("Targets: ", "").replace("Sectors: ", "").replace(". Countries:", "").replace(" and", ",")

            except IndexError:
                Sector_lst = "nil"

            observed_sector_lst.append(Sector_lst)

            try:

                Country_lst = re.findall(r"Countries:.*", info)[0].replace("Countries: ", "").replace(" and", ",").replace(".", "")

            except IndexError:
                Country_lst = "nil"

            observed_countries_lst.append(Country_lst)

            try:

                Tools_lst = re.findall(r"Tools:.*", info)[0].replace("Tools: ", "").replace(" and", ",").replace(".", "")

            except IndexError:
                Tools_lst = "nil"

            tools_lst.append(Tools_lst)

            industry_name_lst.append(industry)

        # close the driver`
        driver.implicitly_wait(1)
        driver.close()

    for i in range(len(threat_actors_lst)):
        url_lst.append("nil")
        information_lst.append("nil")
        mitre_attack_lst.append("nil")
        playbook_lst.append("nil")

    # ------------------------------Create Dataframe------------------------------#
    ta_information = {
            'Threat Actor': threat_actors_lst,
            'URL': url_lst,
            'country': country_lst,
            'motivation': motivation_lst,
            'first seen': first_seen_lst,
            'sponsor': sponsor_lst,
            'description': description_lst,
            'observed sector': observed_sector_lst,
            'observed countries': observed_countries_lst,
            'tools': tools_lst,
            'information': information_lst,
            'mitre attack': mitre_attack_lst,
            'playbook': playbook_lst,
            'industry class': industry_name_lst,
            'associated groups' : associated_groups_lst
    }

    df = pd.DataFrame(ta_information)

    #------------------------------Output Dataframe to Excel------------------------------#
    output_filepath = filepath + str(dt_string) + "_" +"aptmap.xlsx"
    df_drop_duplicated = df.drop_duplicates(subset=['Threat Actor'])

    df_drop_duplicated.to_excel(output_filepath, index=False)

    return df_drop_duplicated