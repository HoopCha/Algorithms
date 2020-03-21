#!/usr/bin/python

import argparse

def find_max_profit(prices):
    #Set the variable for the max profit
    max_profit = 0
    #For each price in the list
    for i in range(0, len(prices)):
        #Set the current price of the current object
        current_price = prices[i]
        #For each of the remaining prices check:
        for j in range(i, len(prices)):
            #Set what the next price is
            next_price = prices[j]
            #Compute the profit between the current price and the next price
            current_profit = next_price - current_price
            # Check if current profit is better than max profit, if it is, set it
            if current_profit > max_profit:
                max_profit = current_profit
    #If its losses all day, you simply buy cheapest (last one) to minimize loss
    if max_profit == 0:
        return prices[-1] * -1
    return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))