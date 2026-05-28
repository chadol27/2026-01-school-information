import random
CLASS_COUNT = 10
PICK_COUNT = 10

print("=== 01 ===")
for i in range(PICK_COUNT):
  pick = random.randint(1, CLASS_COUNT)
  print(pick, end=" ")
print()

print("=== 02 ===")
class_1 = []
for i in range(PICK_COUNT):
  pick = random.randint(1, CLASS_COUNT)
  if pick not in class_1:
    class_1.append(pick)
print(class_1)

print("=== 03 ===")
class_1 = []
while len(class_1) < PICK_COUNT:
  pick = random.randint(1, CLASS_COUNT)
  if pick not in class_1:
    class_1.append(pick)
print(class_1)