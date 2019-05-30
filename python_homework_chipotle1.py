'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

# specify that the delimiter is a tab character
# make sure that the path in Spyder (top right hand corner) is set to to dataset folder
with open('chipotle.tsv', 'r') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]



'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

# Assigns first row as header

header = data[0]

# Separates Header and the data
data.pop(0)

# Verifies if header and data have been split
data[0]


# Code not working completely
header = tsvReader.next()

first_data = []
f = open("chipotle.tsv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    first_data.append(split_row)



'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

# Number of unique order ID's 
num_uniqueids = len(set([row[0] for row in data]))

# List of prices 
list_prices = [float(row[4][1:-1]) for row in data] 

# Average Price of an order
sum(list_prices)/num_uniqueids



'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''


# If item_name column contains 'Canned' value , include 'choice_description' value to sods field
sodas = []
for row in data:
    if 'Canned' in row[2]:
        sodas.append(row[3][1:-1])     
        
# List of sodas        
sodas = [row[3][1:-1] for row in data if 'Canned' in row[2]]

# Displays list of sodas
unique_sodas = set(sodas)




'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''



'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
