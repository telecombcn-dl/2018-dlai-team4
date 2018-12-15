import xlrd
import os
from shutil import copy


def create_new_parse(threshold, number_of_pict, all_picture_per_person, everyone):
    # (int) threshold = the minimal number of picture the celebrity need to have
    # (int) number_of_pict = maximal number of picture kept for each celebrity (if less in databased take them all)
    # (boolean) all_picture_per_person = ignore the "number_of_pict" parameter and take all the available picture
    # (boolean) everyone = ignore the "threshold" parameter and take all the available celebrity in the database

    # database http://vis-www.cs.umass.edu/lfw/
    # Labeled Faces in the Wild (LFW)
    # 13.000 images of faces collected from the web,
    # 1.680 of the people pictured have two or more

    # Define the extraction point and the destination
    src = os.getcwd() + "/all_pict"
    dest = os.getcwd() + "/filtered_pict_"

    # Adapt the name of the output folder depending on the characteristic "filtered_pict_'threshold'_'number_of_pict'"
    if everyone:
        dest += "everyone"
    else:
        dest += str(threshold)
    dest += "_"
    if all_picture_per_person:
        dest += "every-picture"
    else:
        dest += str(number_of_pict)
    dest += "/"

    # Open and read the file with the number of picture for each celebrity (ordered by decreasing number of picture)
    wb = xlrd.open_workbook('ordered_name.xlsx')
    sh = wb.sheet_by_name(u'Feuil2')

    # Different case depending if we select the celebrity or take "everyone"
    if everyone:
        # For each line of the spreadsheet we extract the name...
        for Num_row in range(1, 5750):
            name = sh.row_values(Num_row, 0, 1)[0]
            # ... create a new folder if it's not already created.
            try:
                os.makedirs(dest + name)
            except:
                print("files already created")

            # We take all the pictures until we reach the end of the boundary or there is no more picture we stop
            # The name of the new file is always name_"numero-of-picture".jpg
            if all_picture_per_person:
                i = 1
                while True:
                    try:
                        copy(src + "/" + name + "/" + name + "_" + str(i).zfill(4) + ".jpg", dest + name)
                        i += 1
                    except:
                        break
            else:
                for i in range(1, number_of_pict + 1):
                    try:
                        copy(src + "/" + name + "/" + name + "_" + str(i).zfill(4) + ".jpg", dest + name)
                    except:
                        break
    else:
        for Num_row in range(1, 612):
            if sh.row_values(Num_row, 1, 2)[0] >= threshold:
                name = sh.row_values(Num_row, 0, 1)[0]
                try:
                    os.makedirs(dest + name)
                except:
                    print("files already created")
                if all_picture_per_person:
                    i = 1
                    while True:
                        try:
                            copy(src + "/" + name + "/" + name + "_" + str(i).zfill(4) + ".jpg", dest + name)
                            i += 1
                        except:
                            break

                else:
                    for i in range(1, number_of_pict + 1):
                        try:
                            copy(src + "/" + name + "/" + name + "_" + str(i).zfill(4) + ".jpg", dest + name)
                        except:
                            break
            else:
                break
