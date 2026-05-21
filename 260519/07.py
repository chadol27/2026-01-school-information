bankbook = 15000
person = input("받는 사람 이름을 입력하세요:")
money = input("이체 금액을 입력하세요:")
money=int(money)
bankbook = bankbook - money
print(person, "님에게", money, "원 이체되었습니다")
print("현재 잔액은", bankbook, "원입니다")