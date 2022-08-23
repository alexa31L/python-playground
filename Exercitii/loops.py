animals = ["Dog", "Cat", "Fish"]
for animal in animals:
  print(animal) 


for i in range(3):
  print(i)


fruits = ["apple", "banana", "lemon"]
for index, fruit in enumerate(fruits):
  print(f"Fruit: {fruit}, indexed: {index}.")


# List populated in the for loop
numbers = []
for i in range(1000):
 numbers.append(i)

print(len(numbers))  # Write 1000

# Comprehension list
numbers = [i for i in range(1000)]
print(len(numbers))  # Write 1000