# 1804667 Justine Arzola

import csv
from datetime import datetime  # for date comparisons

  # create class to make output files from the inventory
class OutputInventory:

    def __init__(self, item_list):

        self.item_list = item_list

    def fullinventory(self):
        # creates full inventory
        items  = self.item_list
        keys = sorted(items)


        with open('FullInventory.csv', 'w') as file:

            for item in keys:
                id = item
                manufacturer_name = items[item]['manufacturer']
                item_type = items[item]['item type']
                price = items[item]['price']
                service_date = items[item]['service date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id, manufacturer_name, item_type, price, service_date, damaged))

    def by_type(self):
        # for sorting items by their type to different csv files
        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item type']
            if item_type not in types:
                types.append(item_type)
        for bytype in types:
            file_name = bytype.capitalize() + 'Inventory.csv'
            with open (file_name, 'w') as file:
                for item in keys:
                    id = item
                    manufacturer_name = items[item]['manufacturer']

                    price = items[item]['price']
                    service_date = items[item]['service date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item type']

                    if bytype == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, manufacturer_name, price, service_date, damaged))

    def pastdate(self):
        # used to write service dates that are past due to their own csv file
        items = self.item_list
        keys = sorted(items.keys())
        today = datetime.now().date()  # gets today's date to be able to compare to service date


        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacturer_name = items[item]['manufacturer']
                item_type = items[item]['item type']
                price = items[item]['price']
                service_date = items[item]['service date']
                damaged = items[item]['damaged']
                pastdate1 = datetime.strptime(service_date, "%m/%d/%Y").date()
                if pastdate1 < today:  # compares date, if less than today it is past due

                    file.write('{},{},{},{},{},{}\n'.format(id, manufacturer_name, item_type, price, service_date, damaged))

    def notgood(self):
        # used to determine if item is damaged for the damaged inventory file
        items = self.item_list
        keys = sorted(items.keys())
        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacturer_name = items[item]['manufacturer']
                item_type = items[item]['item type']
                price = items[item]['price']
                service_date = items[item]['service date']
                damaged = items[item]['damaged']
                if damaged:  # determines whether  to write to damaged inventory
                    file.write(
                        '{},{},{},{},{}\n'.format(id, manufacturer_name, item_type, price, service_date))














if __name__ == '__main__':  # take csv files and read then write to files
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manufacturer_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = manufacturer_name.strip()
                    items[item_id]['item type'] = item_type.strip()

                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service date'] = service_date



    output = OutputInventory(items)  # used to create all of the output files
    output.fullinventory()
    output.by_type()
    output.pastdate()
    output.notgood()

    types = []  # creates a list for the item types
    manufacturers = []  # creates a list for the different manufactureres
    for item in items:  # iterates through contents to check for item type and manufacturer
        see_manufacturer = items[item]['manufacturer']
        see_type = items[item]['item type']
        if see_manufacturer not in types:
            manufacturers.append(see_manufacturer)
        if see_type not in types:
            types.append(see_type)

    ask_user = None
    while ask_user != 'q':  # to query user and receive input
        ask_user = input("\nPlease enter a manufacturer and item type or enter 'q' to quit:\n")
        if ask_user == 'q':
            break
        else:
            chosen_manufacturer = None
            chosen_type = None
            ask_user = ask_user.split()
            wrong_entry = False
            for word in ask_user:  # iterates through given input to determine useful contents
                if word in manufacturers:
                    if chosen_manufacturer:

                        wrong_entry = True
                    else:
                        chosen_manufacturer = word
                elif word in types:
                    if chosen_type:

                        wrong_entry = True
                    else:
                        chosen_type = word
            if not chosen_manufacturer or not chosen_type or wrong_entry:  # outputs to user if entry was not valid
                print("No such item in inventory")
            else:


                keys = sorted(items.keys())

                # used to get matching list of items
                equal_items = []

                next_best = {}
                for item in keys:
                    if items[item]['item type'] == chosen_type:
                        # for not including past service date or any damaged items
                        today = datetime.now().date()
                        service_date = items[item]['service date']
                        servicetime = datetime.strptime(service_date, "%m/%d/%Y").date()
                        pastdue = servicetime < today  # for date comparison and determining if past due
                        if items[item]['manufacturer'] == chosen_manufacturer:
                            if not pastdue and not items[item]['damaged']:
                                equal_items.append((item, items[item]))
                        else:
                            if not pastdue and not items[item]['damaged']:
                                next_best[item] = items[item]

                # for outputting items that match
                if equal_items:
                    item = equal_items[0]
                    id = item[0]
                    manufacturer_name = item[1]['manufacturer']
                    item_type = item[1]['item type']
                    price = item[1]['price']
                    print("Your item is: {}, {}, {}, {}\n".format(id, manufacturer_name, item_type, price))

                    if next_best:  # finding the next possible item that could be also considered by comparing prices
                        matched_price = price

                        close_manufacturer = None
                        closest_price = None
                        for item in next_best:
                            if closest_price is None:
                                close_manufacturer = next_best[item]
                                closest_price = abs(int(matched_price) - int(next_best[item]['price']))
                                id = item
                                manufacturer_name = next_best[item]['manufacturer']
                                item_type = next_best[item]['item type']
                                price = next_best[item]['price']
                                continue
                            price_diff = abs(int(matched_price) +-200 ,int(next_best[item]['price']))
                            if price_diff < closest_price:
                                close_manufacturer = item
                                closest_price = price_diff
                                id = item
                                manufacturer_name = next_best[item]['manufacturer']
                                item_type = next_best[item]['item type']
                                price = next_best[item]['price']
                        print("You may, also, consider: {}, {}, {}, {}\n".format(id, manufacturer_name, item_type, price))  # for outputting other considerations
                    else:
                        print("done")













