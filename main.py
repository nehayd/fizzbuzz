#Write your code below this row 👇

for n in range(1, 101):
  if (n % 3 == 0) and (n % 5 == 0):
    n = "FizzBuzz"
    print(n)
  elif n % 3 == 0:
    n = "Fizz"
    print(n)
  elif n % 5 == 0:
    n = "Buzz"
    print(n)
  else:
    print(n)
  
