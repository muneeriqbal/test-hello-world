alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0["muneer"] = 'muneer'
(alien_0)


available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping in available_toppings:
     print("Adding " + requested_topping + ".")
 else:
    print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")