price=1200
amount=12
dc_rate=20/100
total=price*amount
print("전체 금액:", total)

dc=int(total*dc_rate)
total=total - dc
print("할인 금액:", dc)
print("최종 금액:", total)