#Ymonni Simms 2106646
import csv
from operator import itemgetter

#Lists for the csv data in
ManufacturerList=[]
PriceList=[]
ServiceDataList=[]

#Adding information from cvs to list
with open("ManufacturerList.csv") as manlist:
    ml = csv.reader(manlist)
    for line in ml:
        ManufacturerList.append(line)

with open("PriceList.csv") as pricelist:
    pl = csv.reader(pricelist)
    for line in pl:
        PriceList.append(line)

with open("ServiceDatesList.csv") as sdlist:
    sl = csv.reader(sdlist)
    for line in sl:
        ServiceDataList.append(line)

#sorting the list by the order ID
new_ManufacturerList=(sorted(ManufacturerList, key=itemgetter(0)))
new_PriceList=(sorted(PriceList, key=itemgetter(0)))
new_ServiceDataList=(sorted(ServiceDataList, key=itemgetter(0)))

#adding the prices and service dates to the list
for x in range(0,len(new_ManufacturerList)):
    new_ManufacturerList[x].append(PriceList[x][1])

for x in range(0,len(new_ManufacturerList)):
    new_ManufacturerList[x].append(ServiceDataList[x][1])

final_list = new_ManufacturerList

full_inventory = (sorted(final_list, key=itemgetter(1)))

#writing in the full inventory file
with open('FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)
    for x in range(0, len(full_inventory)):
        fiwrite.writerow(full_inventory[x])

#Making a list for each item type
item_type = final_list
tower = []
laptop = []
phone = []

#finding item types and adding them to their lists
for x in range(0, len(item_type)):
    if item_type[x][2] == "tower":
        tower.append(item_type[x])
    elif item_type[x][2] == "phone":
        phone.append(item_type[x])
    elif item_type[x][2] == "laptop":
        laptop.append(item_type[x])

#creating a file for each item type
with open('LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)
    for x in range(0, len(laptop)):
        liwrite.writerow(laptop[x])

with open('PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)
    for x in range(0, len(phone)):
        piwrite.writerow(phone[x])

with open('TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)
    for x in range(0, len(tower)):
        tiwrite.writerow(tower[x])

#list for damaged products
damagedlist = []

for x in range(0, len(item_type)):
    if item_type[x][3] == "damaged":
        damagedlist.append(item_type[x])

damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))

#creating a damaged products file
with open('DamagedInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)
    for x in range(0, len(damagedlist)):
        diwrite.writerow(damagedlist[x])

#Asking the user to enter their manufacturer and item type
user_manuf=str(input("Enter your manufacturer: "))
user_type = str(input("Please enter your item type: "))
your_item = []

#Q is the exit value so while the input does not equal q, execute the program
while(user_manuf != "q"):
    for x in range(0, len(final_list)):
        if user_manuf in final_list[x] and user_type in final_list[x]:
            your_item.append(final_list[x])

#If nothign was added to the list that means the product does not exist
    if len(your_item)!= 0:
        your_item = sorted(your_item , key=itemgetter(4), reverse=True)
        print("Your Item is: ", your_item[0])
    else:
        print("No such item in Inventory")

    user_manuf=str(input("Enter your manufacturer, or q to exit query:"))

    user_type = str(input("Please enter your item type: "))
