
# https://github.com/Sveinbjorn10/Project_04_stock_price/commits/master

condition = True

def shares():
    return int(input("Enter number of shares: "))

def price(shares):
    dollar, nume, deno = input("Enter price (dollars, numerator, denominator): ").split()
    unit_price = int(dollar) + (int(nume)/int(deno))
    total_price = "{0:.2f}".format(unit_price* shares)
    output = str(shares) + " shares with market price " + dollar + " " + nume + "/" + deno + " have value $" + str(total_price)
    print(output)

def continuation():
    while True:
        us_inp = input("Continue: ")
        if (us_inp == "y") or (us_inp == "Y"):
            return True
        elif (us_inp == "n") or (us_inp == "N"): 
            return False
        else:
            print("Press Y or y to continue.")
            print("Press N or n to exit.")

while condition:
    try:
        share_num = shares()
        while True:
            try:
                price(share_num)
                condition = continuation()
                break
            except:
                print("Invalid price!")
    except:
        print("Invalid number!")