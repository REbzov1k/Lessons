print("1.AUDI_RS7\n2.BMW_M8\n3.MERCEDES_G-class\n4.PORSCHE_911_gt3_RS")
number_of_auto = int(input("Введіть ноер машини щоб дізнатись скільки вона коштує:"))
if number_of_auto == 1:
    print("150.000-usd")
elif number_of_auto == 2:
    print("220.000-usd")
elif number_of_auto == 3:
    print("225.000-usd")
elif number_of_auto == 4:
    print("320.000-usd")
else:
    print("Немає машини під заданим номером")