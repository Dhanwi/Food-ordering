print("Welcome to the H_Resto ! ")
print("")
print("")
print("Delivery Available in areas:   ")
print("110096")
print("110052")
print("110091")
print("110058")
print("")
print("")
area1=input("Enter the region where the food needs to be delivered:   ")
print("")
print("")
address=input("Enter your address : ")
print("")
print("")

print("Available Cuisine :  ")
print("South Indian \n North Indian")
cuisine=input("Enter your favourite cuisine:   ")
print("")
print("")


print("Select your food from the menu")
if cuisine == "South Indian":
    print("SD1 (50) \n SD2 (100) \n SD3 (60)")
if cuisine == "North Indian":
    print("ND1 (100) \n ND2 (40) \n ND3 (10) \n ND4 (80)")
b="a"
orderlist=[]
while (b!="No"):
    order = input("Enter your dish:  ")
    orderlist.append(order)
    print("")
    print("")
#orderlist = ["ND2","ND3"]
    b=input("Enter 'No' to complete the list and get the bill or 'Yes' to add more: ")
dish=["SD1","SD2","ND1","ND2","ND3","ND4","ND5"]
price=[50,100,100,40,60,10,80]
bill=0
for a in orderlist:
    c=dish.index(a)
    bill+=price[c]
print("")
print("")
print("")
tip=0
print("Your Order has been placed! ")
tip = input("Enter the Tip for the Rider :")
bill+=int(tip) + 40
print("")
print("")
print("Delivery Charges == 40")
print("")
print("")
print("")
print("Total Bill = "+ str(bill))
print("Thank You for order \U0001F600 . \n Your order will be delivered soon \U0001F618 \n Stay home Stay safe \U0001F637")
c=input("")