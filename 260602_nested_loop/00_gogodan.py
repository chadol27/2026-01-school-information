while True:
  try:
    dan = int(input("단 입력(0은 종료): "))
    if dan == 0:
      print("프로그램이 종료됩니다")
      break

    for i in range(10):
      print(f"{dan} x {i} = {dan*i}")
  except ValueError: continue