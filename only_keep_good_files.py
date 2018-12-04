import xlrd
import os
from shutil import copy

def create_new_parse(treshold,number_of_pict,all_per_person,everyone):

    #database http://vis-www.cs.umass.edu/lfw/
    #Labeled Faces in the Wild (LFW)
    #13.000 images of faces collected from the web,
    #1.680 of the people pictured have two or more
    src=os.getcwd()+"/all_pict"
    dest=os.getcwd()+"/filtered_pict_"
    if everyone :
        dest+="everyone"
    else:
        dest+=str(treshold)

    dest+="_"
    if all_per_person:
        dest+="every-picture"
    else :
        dest+=str(number_of_pict)
    dest+="/"
    wb = xlrd.open_workbook('ordered_name.xlsx')

    sh = wb.sheet_by_name(u'Feuil2')

    if everyone :
        for Nrow in range(1, 5750):
            name = sh.row_values(Nrow, 0, 1)[0]
            try:
                os.makedirs(dest + name)
            except:
                print("files already created")
            if all_per_person:
                while True:
                    try:
                        copy(src + "/" + name + "/" + name + "_" + str(i).zfill(4) + ".jpg", dest + name)
                    # except IOError as e:
                    # print("Unable to copy file. %s" % e)
                    except:
                        # print("Unexpected error:", sys.exc_info())
                        break;
            else:
                for i in range(1, number_of_pict + 1):
                    try:
                        copy(src + "/" + name + "/" + name + "_" + str(i).zfill(4) + ".jpg", dest + name)
                    # except IOError as e:
                    # print("Unable to copy file. %s" % e)
                    except:
                        # print("Unexpected error:", sys.exc_info())
                        break;
    else :
        for Nrow in range(1,612):
            if sh.row_values(Nrow,1,2)[0]>=treshold:
                name=sh.row_values(Nrow,0,1)[0]
                try:
                    os.makedirs(dest+name)
                except:
                    print("files already created")
                if all_per_person :
                    i=1
                    while True :
                        try:
                            copy(src + "/" + name + "/" + name + "_" + str(i).zfill(4) + ".jpg", dest + name)
                        except IOError as e:
                            print("Unable to copy file. %s" % e)
                            break;
                        except:
                            print("Unexpected error:")
                            break;
                        i+=1
                else :
                    for i in range (1,number_of_pict+1):
                        try:
                            copy(src+"/"+name+"/"+name+"_"+str(i).zfill(4)+".jpg", dest+name)
                        #except IOError as e:
                            #print("Unable to copy file. %s" % e)
                        except:
                            #print("Unexpected error:", sys.exc_info())
                            break;
            else :
                break

