print("Welcome to trip cost callculator")
days = int(input("How many days will the trip last: "))
hotelPrice = float(input("Input the estimated hotel price per day: $"))
flightPrice = float(input("Input the cost of the flight (return ticket inclusive): $"))
carRental = float(input("If you would rent a car, input the rental price per day. Else enter zero: $"))
otherExpenses = float(input("Input other possible expenses: $"))
totalCost = round(float((hotelPrice * days) + flightPrice + (carRental * days) +otherExpenses), 2)
print("The estimated coat of your trip is","$"+str(totalCost))