#Take input from user
inputsize = input("How big your house (in square feet):")
# Turn string into number
squate_feet = int(inputsize) 
square_meter = squate_feet/10.8
print(f"{squate_feet} square feets is {square_meter:.2f}square_meter")