"""Fizzbuzz Grid

We're going to use a Windowing library, guizero, to create a 10x10 grid of
numbers, with each number in a separate cell, but we're also going to set the
color of the number based on the following rules:

* If the number is evenly divisible by 5, print '🦡'
* If the number is evenly divisible by 3, print '🍄'
* If the number is evenly divisible by 15, print '🐍'
* If it is divisible by neither, print the number.

Additionally, If you are displaying a number  color the numbers as follows:

* If the sum of the digits of the number is even, color the number blue
* If the sum of the digits of the number is odd, color the number red

Here is how you can display a number in your grid. Call this function in your loop
to display the number in the grid cell at the row and column you specify.

    Text(app, text=str(number), grid=[col, row], color=color)

Or to display a badger: 
    
    Text(app, text='🦡', grid=[col, row], color=color)

HINT: You can use % and // to get the first and last digit of a number, 
our you can convert the number to a string and iterate over the digits

"""
from guizero import App, Box, Text



app = App("Numbers Grid", layout="grid")
# box = Box(app)

# Create a 10x10 grid using nested loops
# Or you can use a single loop and calculate the row and column

i = 50

for col in range(10):
    for row in range(10):
        # print(f"col is {col} | row is {row} | i is {i}")
        if i % 15 == 0:
            Text(app, text='🐍', grid=[col, row])
        elif i % 5 == 0:
            Text(app, text='🦡', grid=[col, row])
        elif i % 3 == 0:
            Text(app, text='🍄', grid=[col, row])
        else:
            sum = 0
            for num in str(i):
                sum += int(num)
            
            if sum % 2 == 0: 
                Text(app, text=str(i), grid=[col, row], color="blue")
            else:
                Text(app, text=str(i), grid=[col, row], color="red")
        
        i += 1

# In the loop, calculate or increment the number

# Use % determing the display, using fizzbuzz rules

# If you are displaying a number, calculate the sum of the digits and determine the color

# Call Text(app, text='...', grid=[col, row], color=...) to display something. 

app.display()
