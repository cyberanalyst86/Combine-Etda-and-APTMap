

def submodule_extract_mitre_id(df):

    index_list = df.index.tolist()

    for id in index_list:

        df.loc[id, ['mitre attack']] = df["mitre attack"].loc[id].replace("https://attack.mitre.org/groups/", "").replace("/", "")

    return df