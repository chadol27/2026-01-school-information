numbers = range(1, 13)
even_count = 0
odd_count = 0
for item in numbers:
  if item % 2 == 0:
    even_count += 1
  else:
    odd_count += 1
print(f"짝수의 개수: {even_count}\n홀수의 개수: {odd_count}")