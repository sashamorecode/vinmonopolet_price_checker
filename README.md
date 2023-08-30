# vinmonopolet_price_checker
Grabs all prices, alcoholvolume values for products on vinmonopolet computes the Price per liter of just the alcohol and exports them to a csv file.
1. first run grab links which uses selium to grab the links to every drink and adds them to a pickel
2. run wither grabPrices.py or grabPricesSignle.py, the singe tends to run into less issues


Requirments:  
  pickle, multiprocessing, requests, json, selenium


