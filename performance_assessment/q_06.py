sum_number = 0
number = 1
while number <= 10:
  if number % 2 == 1:
    sum_number += number
  print(f"{number}까지 홀수의 합은 {sum_number}")
  number += 1
