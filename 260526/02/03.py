reduce=int(input("탄소 절감률을 입력하세요:"))
if reduce>=10:
  mileage="3만 마일리지"
elif reduce>=5:
  mileage="1만 마일리지"
else:
  mileage="마일리지 없음"
print(f"지급된 에코 마일리지: {mileage}")