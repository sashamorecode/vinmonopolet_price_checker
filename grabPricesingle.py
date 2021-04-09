import json, requests
import pickle
import numpy as np
import pandas as pd
from csv import writer
import multiprocessing
import math


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

links = pickle.load(open( "links.pkl", "rb") )
print(len(links))

for link in links:
    try:
        id = link.rsplit("/p/")[1]
        baseApi = "https://www.vinmonopolet.no/api/products/" + str(id)
        pppApi = baseApi +  "?fields=litrePrice"
        alcVolApi = baseApi +  "?fields=alcohol"
        ppp = requests.get(pppApi).json()
        ppp = ppp["litrePrice"]["value"]
        alcVol = requests.get(alcVolApi).json()
        alcVol = alcVol["alcohol"]["value"]
        priesperliterAlc = (ppp/(alcVol/100))

    except:
        alcVol = "na"
        ppp = "na"
        priesperliterAlc = "na"
        print("error in link" + link)

    drink = [ppp, alcVol, priesperliterAlc, link]
    print(drink)
    append_list_as_row("dataSingleThred.csv",drink)
    #with open('data1.pkl', 'ab') as f:
        #pickle.dump(drink, f)





#export = np.array(allInfo)
#np.savetxt("Data.csv", export, delimiter=",")
