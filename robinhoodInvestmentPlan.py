#!/usr/bin/env python3
# This pragrame is used to caculate how much money I should invest
# in Bitcoin and ETH if big fluctuation occurs

fobj = open("initialization.txt", 'r')
Data = []
for line in fobj:
    Data.append(line)
#    Data.append(float(line))
# planInvestment = float(fobj.read(1))
# print("{:.2f}".format(planInvestment))
print(type(Data[0]))
print(Data[0])
# data1 = Data[0].lstrip(' \' ')
data1 = Data[0]
# data1 = data1.rstrip(' \' ')
print(data1[1:4])
fobj.close()

portfolioValue = float(input("Enter the portfolio value: $"))
remainingDays = int(input("Enter the remaining work days of this month: "))
planInvestment = 900
planDailyInvestment = planInvestment / 20
print("Current Cash in Plan is: ${:.2f}".format(planDailyInvestment * remainingDays))
planEthEquity = (portfolioValue - planDailyInvestment * remainingDays) / 9
planBitcoinEquity = 2 * planEthEquity
print("Current Bitcoin Equity in Plan is: ${:.2f}".format(planBitcoinEquity))
print("Current ETH Equity in Plan is: ${:.2f}".format(planEthEquity))

currentBitcoinEquity = float(input("Enter the current Bitcoin Equity: $"))
print("You should trade ${:.2f}".format(planBitcoinEquity - currentBitcoinEquity))
currentEthEquity = float(input("Enter the current ETH Equity: $"))
print("You should trade ${:.2f}".format(planEthEquity - currentEthEquity))
option = str(input("Do you wnt to calculate the profit in this month? (y/n)"))

if remainingDays == 0 or option == 'y':
    # balanceLastMonth = float(input("Enter the balance in the last month: $"))
    balanceLastMonth = 11889.73
    profit = portfolioValue - balanceLastMonth
    print("The profit in this month is: ${:.2f}".format(profit))
    print("The profit ratio in the  past month: {:.2f}%".format(profit * 100 / balanceLastMonth))
    currentQqqEquity = float(input("Enter the current QQQ equity: $"))
    print("QQQ equity in plan: ${:.2f}".format(2 * planEthEquity))
    print("You should trade ${:.2f}".format(2 * planEthEquity - currentQqqEquity))
    currentSpyEquity = float(input("Enter the current SPY equity: $"))
    print("SPY equity in plan: ${:.2f}".format(4 * planEthEquity))
    print("You should trade ${:.2f}".format(4 * planEthEquity - currentSpyEquity))
    end = str(input("Press Any Key to Exit."))
else:
    end = str(input("Press Any Key to Exit."))
