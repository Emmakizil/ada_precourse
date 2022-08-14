"""Write a function icecream_sundae that takes two arguments, one list of ice cream flavors and one list of toppings, and returns a new list that contains all of the possible ice cream sundae combinations that can be made by combining each flavor with each toppings. If the flavors are "vanilla" and "chocolate" and the toppings are "chocolate sauce" and "berry sauce", the output list should contain "vanilla with chocolate sauce", "vanilla with berry sauce", "chocolate with chocolate sauce", "chocolate with berry sauce".

Note the addition of the word "with" in the combined version. You can assume that both of the input lists only contain strings."""

def icecream_sundae(flavors, toppings):
    icecreams = []
    for flavor in flavors:
        for topping in toppings:
            icecreams.append(f"{flavor} with {topping}")

    return icecreams

flavors = ["vanilla", "chocolate", "strawberry"]
toppings = ["whipped cream", "nuts", "a cherry"]
print(icecream_sundae(flavors, toppings))   