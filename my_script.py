hello_file = open("hello.txt", "w")
ga_intro = "Hello to all of my GA family"
hello_file.write(ga_intro)
# print(hello_file.read())
hello_file.close()

car_file = open("car.txt", 'w')
new_car_list = 'Tesla Model S\nMercedes C300\nToyota Camry'
car_file.write(new_car_list)
# print(car_file.read())
car_file.close()

# Create a file
# my_new_file = open('person.txt', "r+")
# my_new_file.write('Richard\nMike\nDexter\nPete')
# # print(my_new_file.readlines())
# my_new_file.close()

with open('person.txt') as people:
  people_list = people.readlines()
  
  for each_person in people_list:
    print(each_person)
    
# read the file and print and the number and multiply it by 2
# print(num * 2)

def multiply_by_two(num):
  return num * 2

# with open('prime_numbers.txt') as prime_numbers:
#   prime_list = prime_numbers.readlines()
#   for num in prime_list:
#     print(multiply_by_two(int(num)))
    
# with open('one_to_hundred.txt') as numbers_file:
#   numbers = numbers_file.readlines()
#   result = []
#   for num_text in numbers:
#     if 'Fifteen' in num_text:
#       result.append(num_text[:-1])
#     elif 'Five' in num_text:
#       result.append(num_text[:-1])
#   print(result)
    
  


# person_file = open('person.txt')
# print(person_file.read())
# person_file.close()

# with open('person.txt', 'w') as person_file:
#   person_file.write('Pete')

# # Append to a file
# with open('person.txt', 'a') as person_file:
#   person_file.write('\nMike\nDexter')

# with open('person.txt', 'r+') as person_file:
#   # person_file.write('\nYvonne')
#   # print(person_file.read())
#   print(person_file.read())
# # come back here.
# # txt_list = hello_file.read().split(' ')
# # print(txt_list)

# with open('hello.txt', 'w+') as hello_file:
#   print(hello_file.read())