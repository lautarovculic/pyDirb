print("> pyDirb  Lautaro Villarreal Culic' <")
print("-------------------------------------")
print("||||| https://lautarovculic.com |||||")
print("-------------------------------------")

import requests 
import sys 

#"wordlist.txt" must be in the same dir that pyDirb.py
sub_list = open("wordlist.txt").read() 
directories = sub_list.splitlines()

for dir in directories:
    #Change the URL.
    dir_enum = "https://lautarovculic.com/" + dir
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Directory:" ,dir_enum)
