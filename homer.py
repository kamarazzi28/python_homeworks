"""
Homer's fridge
Course: B0B36ZAL
"""

#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name 
        self.expiration = expiration
#predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

# test vypisu - pri odevzdani smazte, nebo zakomentujte
fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)


"""
Task #1
"""
def maxExpirationDay(fridge):
    max_exp_day = 0
    for food in fridge:
        if food.expiration > max_exp_day:
            max_exp_day = food.expiration
    return max_exp_day

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""
def histogramOfExpirations(fridge):
    max_exp_day = maxExpirationDay(fridge)
    histogram = [0]*(max_exp_day + 1)
    for food in fridge:
        histogram[food.expiration] += 1
    return histogram

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""
def cumulativeSum(histogram):
    cumulative = [0] * len(histogram)
    cumulative[0] = histogram[0]

    for i in range(1, len(histogram)):
        cumulative[i] = cumulative[i - 1] + histogram[i]

    return cumulative

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""
def sortFoodInFridge(fridge):
    histogram = histogramOfExpirations(fridge)
    cumulative_sum = cumulativeSum(histogram)
    sorted_fridge = [None] * len(fridge)

    for food in fridge:
        food_in = cumulative_sum[food.expiration] - 1
        sorted_fridge[food_in] = food
        cumulative_sum[food.expiration] -= 1

    return sorted_fridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""
def reverseFridge(fridge):
    return fridge[::-1]

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""
def eatFood(name, fridge):
    food_fridge = [food for food in fridge if food.name == name]
    
    if not food_fridge:
        return fridge[:]
    min_exp_food = min(food_fridge, key=lambda x: x.expiration)
    new_fridge = fridge[:]
    new_fridge.remove(min_exp_food)
    return new_fridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#     )
# )
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
