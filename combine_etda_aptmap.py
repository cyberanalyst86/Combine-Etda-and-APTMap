import time
import datetime
from get_from_etda import *
from get_from_aptmap import *
from combine import*
from extract_difference import *
from merge_etda_aptmap import *

# ----------------------------Output File Directory Creation----------------------------#

now = datetime.datetime.now()
dt_string = now.strftime("%d-%m-%Y")

dt = datetime.datetime.today()
month_number = dt.month
year = dt.year

month_dict = {1: 'January', 2: 'Febuary', 3: 'March',
              4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September',
              10: 'October', 11: 'November', 12: 'December'}

for key in month_dict:
    if month_number == key:
        month = month_dict[key]
    else:
        msg = "error"

filepath = "C:\\Users\\Admin\\Downloads\\Combined" + "\\" + month + "_" + str(year) + "\\"

isExist = os.path.exists(filepath)

if isExist == False:

    os.mkdir(filepath)

else:

    error = "error"

#--------------------------------Call Modules------------------------------------#
start = time.time()

industry_list = ['Aviation', 'Aerospace']

print("--------------------Get from etda--------------------")
df_etda = get_from_etda(industry_list, dt_string, filepath)


print("--------------------Get from aptmap--------------------")
df_aptmap = get_from_aptmap(industry_list, dt_string, filepath)


print("--------------------append difference to etda--------------------")

df_append, df_aptmap_id, id_list = append_difference_to_etda(df_aptmap, df_etda, dt_string, filepath)


print("--------------------merge etda and aptmap--------------------")

merge_etda_aptmap(id_list, df_aptmap_id, df_append, dt_string, filepath)


#--------------------------------Calculate Processing Time------------------------------------#
start
end = time.time()
elapsed = (end-start)/60
print(str(elapsed) + " mins")

