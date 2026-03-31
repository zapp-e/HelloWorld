print('Hello World')

## Variables
age=20
print(age)


##Input
name = input('What is your name?')

print('Hello' + name)

##Type Conversion


birth_year = input('What is your birth year?')
age = 2026 - int(birth_year)

print(age)

## Strings

course = 'Python for Beginners'

print(course.upper()) ## Makes all uppercase

print(course.find('f'))  ## Find index of the character or word. Case-sensitive

print(course.replace('for', '4'))  # Replaces character or word with new character or word

print('Python' in course)   # Determines if the character or word is in variable

# Arithmetic Operators

print(10+3) #addition

print(10-3) #subtraction

print(10*3) #multiplication

print(10 / 3) #division. Returns float ex. 3.33...

print(10 // 3) #division. Returns integer ex. 3

print(10 % 3) #Returns Remainder

print(10 ** 3) #Exponent operator. 10^3
