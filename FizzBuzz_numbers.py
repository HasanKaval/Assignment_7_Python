# Print the FizzBuzz numbers.

numbers = list(range(1,101))
for i in numbers:
  if i % 15 == 0 :
    print("FizzBuzz")
  elif i % 3 == 0 :
    print("Fizz")
  elif i % 5 == 0 :
    print("Buzz")
  else :
    print(i)
