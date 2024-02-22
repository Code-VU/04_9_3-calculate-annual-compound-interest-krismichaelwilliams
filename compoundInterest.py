def calculateCompoundInterest():
    numOfClients = 3
    clientInfo = []

    for client in range(numOfClients):

        principal = float(input("Principle (amount): "))
        time = float(input("Time:               "))
        rate = float(input("Rate:               "))
        totalAmount = principal * (1 + (rate / 100)) ** time

        print("Compound Interest: " + str(round(totalAmount - principal, 2)))
        if client < numOfClients - 1:
            print("---")

    # end assignment


## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
