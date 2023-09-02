def myName():
    print("my name is nawal")
myName()

def myMeal(food, drink):
    return f"i like to eat {food} while drinking {drink}"

result = myMeal("fish", "cola")
print(result)

def cube(number):
    return number**3
print(cube(2))


def by_three(number):
    if number%3==0:
        return cube(number)
    
    else:
        return False
print(by_three(3)) 