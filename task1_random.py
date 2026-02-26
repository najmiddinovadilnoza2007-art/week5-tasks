from random import randint
numbers = [randint(10, 50) for _ in range(5)]
print("List:", numbers)
print("Max:", max(numbers))
print("Average:", sum(numbers) / len(numbers))