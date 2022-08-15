from datetime import datetime
name = input("Enter your name:")
#list of items
list = '''
Rice   Rs 20/kg
Sugar  Rs 30/kg
Salt   Rs 20/kg
Oil    Rs 80/lt
Paneer Rs 110/kg
Maggi  Rs 50/kg
Boost  Rs 90/each
Colgat Rs 85/each
'''
#print(list)
Price = 0
Pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

# rates for items
items = {'Rice':20,'Sugar':30, 'Salt':20,'Oil':80,'Paneer':110,
'Maggi':50,'Boost':90,'Colgate':85}
option = int(input("for list of items press 1: "))
if option == 1:
    print(list)
for i in range(len(items)):
    inp1 = int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input(" enter your items:")
        quantity = int(input("enter your quantity:"))
        if item in items.keys():
            price = quantity * (items[item])
            #print(price)
            Pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalprice = gst + totalprice
        else:
            print("Sorry selected item is not available")
    else:
        print("you entered wrong number")

inp = input("can I bill the items yes or no:")
if inp == "no":
    pass
if inp == "yes":
    if finalprice != 0:
     print (25 * "=","Super Market",25*"=")
     print (25*" ","Lakshmipuram")
     print("Name:",name,30*" ","Date:",datetime.now())
     print(75*"-")
     print("Sno",8*" ","items",8*' ',"Quantity",3*" ","price")
     for i in range (len(Pricelist)):
        print(i+1,10*' ',ilist[i],10*' ',qlist[i],8*" ",plist[i])
     print (75*"-")
     print(50*" ","Total Amount:",'Rs',totalprice)
     print(50*" ","gst amount:",' Rs',gst)
     print(75*"-")
     print(50*" ",'finalamount:','Rs',finalprice)
     print(75*"-")
     print(25*" ", "Thanks for visiting",25*" ")
     print(75*"-")
