import os

menu = [
    ("A1", "sprite", 0.75),
    ("A2", "fanta", 0.75),
    ("A3", "coke", 0.75),
    ("A4", "shaani", 1.00),
    ("A5", "redbull", 1.25),
]

balance = 0
buy = False

while True:
    while buy is False:
        os.system("cls")
        print("Credit: £" + str(balance))
        for item in menu:
            print(item[0], item[1], "£" + str(item[2]))

        coin = str(input("enter coins (1p , 2p, 5p, 10p ,20p, 50p , £1 , £2), Enter q to quit.: "))


        match coin:
            case "1p" :
                balance += 0.01
            case "2p" :
                balance += 0.02
            case "5p" :
                balance += 0.05
            case "10p" :
                balance += 0.10
            case "20p" :
                balance += 0.20
            case "50p" :
                balance += 0.50
            case "£1" :
                balance += 1.00
            case "£2" :
                balance += 2.00
            case "q" :
                buy = True
                break 
            case _:
                print(f"coin not valid, returning {coin}")

    os.system("cls")

    for item in menu:
        print(item[0], item[1], "£" + str(item[2]))

    print (balance)

    desired_item = input("Enter what item you want with the corresponding code: ")

    #vendingstock =    
    # ("A1", "sprite", 0.75),
    # ("A2", "fanta", 0.75),
    # ("A3", "coke", 0.75), 
    # ("A4", "shaani", 1.00),
    # ("A5", "redbull", 1.25),

    avaliable = False
    for item in menu:
        if desired_item.upper() == item[0]:
            avaliable = True
            if balance >= item[2]:
                balance -= item[2]
                print("Dispensing", item[1])
                print("Here is your change", balance)
                input("Please enter.")
                buy = False
            else:
                print("Insufficient funds, returning £", balance)
                input("Please enter.")
                buy = False

    if avaliable == False:
        print("Item not found, returning £", balance)
        input("Please enter.")
        buy = False

