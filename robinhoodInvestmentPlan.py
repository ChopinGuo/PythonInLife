#!/usr/bin/env python3
# This pragrame is used to caculate how much money I should invest
# in Bitcoin and ETH if big fluctuation occurs
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

if remainingDays == 0:
    balanceLastMonth = float(input("Enter the balance in the last month: $"))
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
