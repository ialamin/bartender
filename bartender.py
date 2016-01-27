import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

responses = {}

def order():
    for i in questions:
        responses[i] = (raw_input(questions[i]).lower())
        
    preference= {}
    for i in responses:
        if responses[i] == 'yes':
            preference[i] = True
        elif responses[i] == 'no':
            preference[i] = False
        else:
            preference[i] = "Not an acceptable answer"
            
    return preference
    
    
def make(preference):
    recipe = []
    for i in preference:
        if preference[i] == True:
            recipe.append(random.choice(ingredients[i]))
    print(recipe)
    

drink = order()

def another():
    # havent been able to get this block to work right
    #It is supposed to make another round of drinks
    print("Would you like another?")
    another = raw_input().lower
    if another == "yes":
        make(drink)
    elif another == "no":
        print("ok thanks")
    else:
        print("Now where's my tip?")


def main():
    make(drink)
    another()
    
    

if __name__ == '__main__':
    
    main()
  
