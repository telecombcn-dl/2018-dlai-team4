import xlrd
import os
from shutil import copy

treshold=20
number_of_pict=treshold

src=os.path.dirname(__file__)+"\\all_pict"
dest=os.path.dirname(__file__)+"\\filtered_pict_"+str(treshold)+"\\"
wb = xlrd.open_workbook('ordered_name.xlsx')

sh = wb.sheet_by_name(u'Feuil2')


for Nrow in range(1,500):
    if sh.row_values(Nrow,1,2)[0]>=treshold:
        name=sh.row_values(Nrow,0,1)[0]
        try:
            os.makedirs(dest+name)
        except:
            "files already created"
        for i in range (1,number_of_pict+1):
            try:
                copy(src+"/"+name+"/"+name+"_"+str(i).zfill(4)+".jpg", dest+name)
            except IOError as e:
                print("Unable to copy file. %s" % e)
            except:
                print("Unexpected error:", sys.exc_info())
