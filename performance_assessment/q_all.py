##########
# 주의: 틀린 거 있을 수 있음
##########

# 문제 1번
print("풀꽃\n자세히 보아야 예쁘다\n오래 보아야 사랑스럽다\n너도 그렇다")

# 문제 2번
name = input("이름은?")
school_number = input("학번은?")
print(f"학번 {school_number}의 이름은 {name}입니다")

# 문제 3번
number = int(input("정수를 입력하세요"))
if number % 2 == 0:
  print("짝수입니다")
else:
  print("홀수입니다")

# 문제 4번
sum_number = 0
for i in range(1, 10+1):
  sum_number += i
print(sum_number)

# 문제 5번
stars = int(input("출력하고 싶은 별의 개수는?"))
for i in range(stars):
  print("*"*(i+1))

# 문제 6번
sum_number = 0
number = 1
while number <= 10:
  if number % 2 == 1:
    sum_number += number
  print(f"{number}까지 홀수의 합은 {sum_number}")
  number += 1

# 문제 7번
for _ in range(3):
  score = int(input("점수를 입력하세요"))
  if score >= 80:
    print("참 잘했어요")
  elif score >= 60:
    print("잘했어요")
  else:
    print("좀 더 노력하세요")
  print()

# 문제 8번
for i in range(2, 9+1):
  print(f"{i} 단")
  for j in range(1, 9+1):
    print(f"{i} x {j} = {i*j}")
  print()
