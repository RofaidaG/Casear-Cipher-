enc=input("enter the text to dycrpt:")
for j in range(1, 26):
    for i in enc:
        if ord(i) != 32:
            uni = int(ord(i)) + int(j)
            if 97 <= ord(i) <= 122 and uni > 122:
                uni2 = uni - 26
                decyrpt = chr(uni2)
                print(decyrpt, end='')
            elif 97 <= uni <= 122 and 97 <= ord(i) <= 122:
                uni2 = uni
                decyrpt = chr(uni2)
                print(decyrpt, end='')
            elif 65 <= ord(i) <= 90 and 65 <= uni <= 90:
                uni2 = uni
                decyrpt = chr(uni2)
                print(decyrpt, end='')
            elif 65 <= ord(i) <= 90 and uni > 90:
                uni2 = uni - 26
                decyrpt = chr(uni2)
                print(decyrpt, end='')
        else:
            decyrpt = chr(32)
            print(decyrpt, end='')

    print("\n")

