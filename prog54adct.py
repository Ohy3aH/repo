car1 = {
  "miles": 286,
  "gallons": 9
}

car2 = {
  "miles": 412,
  "gallons": 40
}

car3 = {
  "miles": 361
  "gallons": 18
}

car4 = {
  "miles": 161
  "gallons": 11
}

cars = {
  "1970 VW Bug": car1,
  "1979 Firebird": car2,
  "9180 Sabaru": car3,
  "1975 Cutleass": car4
}
print("choose a car from the following", cars.keys())
mycar = imput()
carselected = cars[mycar]
miles = carselected["miles"]
gallons = carselected["gallons"]
mpg = float(miles) / gallons

print("miles", miles)
print("gallons", gallons)
print("MPG", round(mpg, 10))