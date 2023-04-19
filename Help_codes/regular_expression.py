import re

#regex = r"umg_\w{1,10}|\nslot.\d{1,2}\ne63|slot.\d{1,2}.\ns4l"

list_filter = []

def find_regex(regex,filename):

    with open("test.txt","r") as file:
        #print(re.findall(regex,file.readline))
        f = file.read()
        for i in re.findall(regex,f):
            list_filter.append(i.strip())
        
    for i in list_filter:
        print(i.strip())

    with open(f"{filename}.txt","w") as file2:
        file2.write("\n".join(list_filter))

find_regex("umg_\w{1,10}|\nslot.\d{1,2}\ne63|slot.\d{1,2}.\ns4l","result1")