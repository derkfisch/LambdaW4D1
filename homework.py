#Question 1

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
 #filter method from todays lecture
def empty_string(place):
    return place != ' '

empty_string_filter = list(filter(empty_string, places))
print(empty_string_filter)

#not sure why im geting the three empty strings still between San Diego and Boston

#Question 2

# to call for the last name i set each first and last name to variables
authors = [('Joel', 'Carter'), ('Victor', 'aNisimov'), ('Andrew P.', 'Garfield'), ('David', 'hassELHOFF'), ('Gary A.J.' 'Bernstein')]

#I attemped to create a sorted_authors and lambda method to grab the name at index 1 and sort it.
sorted_authors = authors.sort(lambda name: name[1], authors)

print(sorted_authors)

#Question 3

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]
#map method from lecture
#place at index 1 should be equal to the tempurature
#set up place at index 1 to go through the Farenheit equation
list(map(lambda place: place[1] * (9 / 5) + 32, places))

#Question 4

def fib(num):
    #tried to set this one up like the add_nums example from class
    if num <= 1:
        print(f"Interation {num}: {num}")
        return num
    elif num > 1 and num < 5:
        print(f"Interation {num}: (int{num - 1})")
        return num
    elif num == 5:
        print(f"Interation {num}: {num}")
        return num
    else:
        print(f"Interation 6: 8")
    
fib(5)

#Question 5

def square_generator(start, stop, step=1):

    while start > stop:
        yield start ** 2
        start += step
        
square_generator(100, 0)

for num in square_generator(100, 0, -1):
    print(num)
