print("Welcome to the Grocery Store")
print("Rice -- Rs.50/kg")
print("Sugar -- Rs.40/kg")
print("Milk -- rs.25/litre")
print("Eggs -- rs.6/piece")
dict={"rice":50,"sugar":40,"milk":25,"egg":6}
i=0
total=0
while i==0:
    grocery=input("Enter the item which you want or type exit to quit: ")
    if grocery in dict.keys():
        quant=float(input("Enter the quantity: ")) 
        cost=quant*dict.get(grocery)
        total+=cost
        print(grocery,"added to cart. Amount:",total)
    elif grocery == "exit":
        print("Total Bill is:",total)
        break
    else:
        print("Item Not Available!")