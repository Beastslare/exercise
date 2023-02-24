from datetime import date

dt = date.today().strftime('%A')
print(dt)
name =input('input day')
if name =="Thursday":
    print("true")
else:
    print("false")