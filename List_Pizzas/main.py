# Pizza Types
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Pizza Prices in Dollars
prices = [2, 6, 1, 3, 2, 7, 2]

# Using the count method
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
print()
# Print Out: 3

# Using the length Method
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")
print()
# Print Out: We sell 7 different kinds of pizza!

# Creating a two-dimensional List
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2,"olives"], [7, "anchovies"], [2,"mushrooms"]]
print(pizza_and_prices)
print()
# Print Out: [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

# Sorting and Slicing

# Using the Sort() method
pizza_and_prices.sort()
print(pizza_and_prices)
print()
# Print Out: [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]

# Selecting a List item
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
print()
# Print Out: [1, 'cheese']

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
print()
# Print Out: [7, 'anchovies']

# Using the pop() method
pizza_and_prices.pop()
print(pizza_and_prices)
print()
# Print Out: [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple']]

# Using the insert Method
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
print()
# Print Out: [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [2.5, 'peppers'], [3, 'sausage'], [6, 'pineapple']]

# Sliding through a List
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
print()
# Print Out: [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives']]
