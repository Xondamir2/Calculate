
while True:
    a = int(input('enter a number: '))
    if a == 0:
        print('0 represents a backslash !')
        continue
    b = int(input('enter a number: '))
    if b == 0:
        print('0 represents a backslash !')
        continue

    amal = input('do : ')

    if amal == 'Comands':
        print(' (-) subtract (+) add (/) divide (*) multiply ✔ ')


    if amal == 'stop':
       print('the program has been stopped :')
       break
    c = a + b
    d = a - b
    e = a / b
    f = a * b


    if amal == '+':
     print(c)

    if amal == '-':
     print(d)

    if amal == '/':
     print(e)

    if amal == '*':
     print(f)



