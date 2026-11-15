#String Type

str_length = input("Please enter the length:\n")
str_width = input("Please enter the width:\n")
str_price = input("How much does 1 square meter cost?\n")
#Convert Type to float

length = float(str_length)
width = float(str_width)
price = float(str_price)

area = (length*width)
total = (length*width*price)

#Convert Type to string

str_area = str(area)
str_total = str(total)

print("The total area is: " + (str_area))
print("The total cost is: $" + (str_total))
