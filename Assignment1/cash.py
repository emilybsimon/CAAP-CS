def main():
    change = float(input("How much change is owed?"))
    coins = 0
    while change >= 0.25:
        change -= 0.25
        coins=1

    while change >= 0.10:
        change -= 0.10
        coins=coins+1

    while change >= 0.05:
        change -= 0.05
        coins=coins+1

    while change >= 0.00:
        change -= 0.01
        coins=coins+1

    print (coins)
main ()