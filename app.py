operator = ""

while operator.lower() != "exit":
    operator = input ("Masukkan operator : ")
    if operator in ("+", "-", "*", "/"):
        angka1 = int(input("Masukkan angka 1 : "))
        angka2 = int(input("Masukkan angka 2 : "))
        if operator == "+" :
            print (angka1 + angka2)
        elif operator == "-" :
            print (angka1 - angka2)
        elif operator == "*" :
            print (angka1 * angka2)
        elif operator == "/" :
            print (angka1 / angka2)
        else:
            print ("Operator tidak dikenal")
    elif operator.lower() == "exit":
        print ("Terima kasih")
        break
    else:
        print ("Operator tidak dikenal2")
        continue


