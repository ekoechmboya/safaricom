# Task 1
numbers = input("Enter integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Convert input to a list of integers
print(f"The sum of the integers is: {sum(numbers)}")

# Task 2
favorite_books = ("The Alchemist", "1984", "To Kill a Mockingbird", "Sapiens", "The Great Gatsby")

print("My favorite books:")
for book in favorite_books:
    print(book)

# Task 3
person = {}
person['name'] = input("Enter your name: ")
person['age'] = int(input("Enter your age: "))
person['favorite_color'] = input("Enter your favorite color: ")

print("Person information:")
print(person)

# Task 4
set1 = set(map(int, input("Enter integers for the first set (separated by spaces): ").split()))
set2 = set(map(int, input("Enter integers for the second set (separated by spaces): ").split()))

common_elements = set1 & set2  # Intersection of both sets
print(f"Common elements: {common_elements}")

# Task 5
words = input("Enter words separated by spaces: ").split()
odd_length_words = [word for word in words if len(word) % 2 != 0]

print(f"Words with an odd number of characters: {odd_length_words}")
