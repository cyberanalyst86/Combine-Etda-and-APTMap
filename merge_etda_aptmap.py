import pandas as pd

def process(a, b):

    lst = list((a + ", " + b).split(", "))

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
            return str1.replace(", nil", "")

        else:

            listToStr = "".join([str(elem) for elem in dedup_list])

            str1 = listToStr

            return str1.replace(", nil", "")

    else:

        # return string
        return dedup_list.replace(", nil", "")

def merge_etda_aptmap(id_list , df_aptmap, df_append, dt_string, filepath):

    df_append.set_index('id',inplace = True)
    #df_aptmap.set_index('id2',inplace = True)

    #df.loc[10, ['Threat Actor']] = ["APT 20, Violin Panda"]

    for id in id_list:

        print("---------" + str(id) + "---------")
        print(df_append["Threat Actor"].loc[id])
        print(df_aptmap["Threat Actor"].loc[id])
        df_append.loc[id, ['Threat Actor']] = \
            [process(df_append["Threat Actor"].loc[id], df_aptmap["Threat Actor"].loc[id])]

        df_append.loc[id, ['motivation']] = \
            [process(df_append["motivation"].loc[id], df_aptmap["motivation"].loc[id])]

        df_append.loc[id, ['first seen']] = \
            [process(df_append["first seen"].loc[id], df_aptmap["first seen"].loc[id])]

        df_append.loc[id, ['sponsor']] = \
            [process(df_append["sponsor"].loc[id], df_aptmap["sponsor"].loc[id])]

        df_append.loc[id, ['observed sector']] = \
            [process(df_append["observed sector"].loc[id], df_aptmap["observed sector"].loc[id])]

        df_append.loc[id, ['observed countries']] = \
            [process(df_append["observed countries"].loc[id], df_aptmap["observed countries"].loc[id])]

        df_append.loc[id, ['tools']] = \
            [process(df_append["tools"].loc[id], df_aptmap["tools"].loc[id])]

        df_append.loc[id, ['associated groups']] = \
            [process(df_append["associated groups"].loc[id], df_aptmap["associated groups"].loc[id])]

    print("writing to etda data to excel")

    df_append.to_excel(filepath + str(dt_string) + "_" + "final.xlsx", index=False)

    return


