# 1804667 Justine Arzola

import csv
from datetime import datetime # for date comparisons

 #create class to make output files from the inventory
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
        today = datetime.now().date() # gets today's date to be able to compare to service date


        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacturer_name = items[item]['manufacturer']
                item_type = items[item]['item type']
                price = items[item]['price']
                service_date = items[item]['service date']
                damaged = items[item]['damaged']
                pastdate1 = datetime.strptime(service_date, "%m/%d/%Y").date()
                if pastdate1 < today: # compares date, if less than today it is past due

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
                if damaged: # determines whether or not to write to damaged inventory
                    file.write(
                        '{},{},{},{},{}\n'.format(id, manufacturer_name, item_type, price, service_date))














if __name__ == '__main__': #take csv files and read then write to files
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



    output = OutputInventory(items)
    output.fullinventory()
    output.by_type()
    output.pastdate()
    output.notgood()
