'''Append Method'''
lst1=[10,12,14]
lst1.append(25)
print(lst1)

'''Extend Method'''
prime=[2,3,5]
even=[4,6,8]
prime.extend(even)
print(prime)

'''Insert Method'''
vowel=['a','e','i','u']
vowel.insert(3,'o')
print(vowel)

'''Remove'''
prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.remove(9)
print(prime_numbers)

'''Count'''
numbers = [2, 3, 5, 2, 11, 2, 7]
count = numbers.count(2)
print('Count of 2:', count)

'''Pop'''
prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

'''Reverse'''
prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()
print('Reversed List:', prime_numbers)

'''Sort'''
prime_numbers = [11, 3, 7, 5, 2]
prime_numbers.sort()
print(prime_numbers)
