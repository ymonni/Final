from datetime import datetime
import csv

class Item:
    def init(self, itemID, itemType,manufacturername,damage,price):
        self.manufacturername = manufacturername
        self.itemID = itemID
        self.ItemType=itemType
        self.price=price
        self.damage=damage


def getprice(itemid):
    index=0
    max=-1
    preader = csv.reader(open('PriceList.csv', 'r'))
    preader=list(preader)
    for prow in preader:
        if itemid in prow[0]:
            if max < int(prow[1]):
                max= int(prow[1])
            index=index+1

    return max



def checkdate(itemid):
    check =0
    sreader = csv.reader(open('ServiceDatesList.csv', 'r'))
    sreader=list(sreader)
    for srow in sreader:
        if itemid in srow[0]:
            if srow[1] < datetime.datetime.today().strftime('%m/%d/%Y'):
                check=1

    return check



while 1:
    m_name=input("Enter Manufacturer name:")
    item_type=input("Enter Item Type")

    reader = csv.reader(open('ManufacturerList.csv', 'r'))
    reader=list(reader)
    flag=0
    for row in reader:
        if m_name in row[1] and item_type in row[2]:
            flag=1
            if row[3] not in "damaged" and checkdate(row[0])==0:
                print("Item Id=%s \n Manufacturer Name=%s \n Item Type= %s \n Price=%d" % row[0],row[1],row[2],getprice(row[0]))
        if item_type in row[2]:
            flag=1
            print("\n Other Manufacturers: \n")
            if row[3] not in "damaged" and checkdate(row[0])==0:
                print("Item Id=%d \n Manufacturer Name=%s \n Item Type= %s \n Price=%d" % row[0],row[1],row[2],getprice(row[0]))


    if flag==0:
        print("No such item in inventory")

    inp=input("Enter Q to Exit")
    if inp == "Q" or inp=="q":
        break