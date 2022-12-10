from tkinter import *
from tkinter import filedialog
import os , csv 

#checking if csv createif not creat if yes append to it new address
def choose_file():
    file_path = "data/data.csv"
    folderPath = filedialog.askdirectory()
    folderName = os.path.basename(folderPath)
    id = 0
    update_array = []
    exist = False

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            fields = ('ID', 'FolderName', 'FilePath')
            wr = csv.DictWriter(f , fieldnames=fields, lineterminator = '\n')
            wr.writeheader()
            f.close()

    with open(file_path, "r+" , newline='') as f:
        
        #check if isnt same data already in csv
        f.seek(0)
        reader = csv.reader(f , delimiter=",")
        for row in reader:
            create = True
            if row[0] != "ID":
                if not os.path.exists(row[2]):
                    create = False
                    id -= 1
                if row[0] != id:
                    row[0] = id
                if row[2] == folderPath:
                    exist = True
                id += 1

                #appends data to list to rewrite file
                if create == True:
                    update_array.append([row[0] , row[1] , row[2]])

        if exist == False:
            update_array.append([id , folderName , folderPath])

        f.seek(23)
        csv.writer(f).writerows(update_array)
        f.close()