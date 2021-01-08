with open('prime_numbers.txt') as primes:
    primes_numbers = primes.readlines()
    for num in primes_numbers:
        print (int(num) * 2)

with open('one_to_hundred.txt') as numbers_file:
    numbers = numbers_file.readlines()
    result = []
    for num in numbers:
        if 'Five' in num:
            remove_newline_text = num[:-1]
            result.append(remove_newline_text)
        elif 'Fifteen' in num:
            remove_newline_text = num[:-1]
            result.append(remove_newline_text)
    
    print(result)