import random

questions = {
    "sweet": "Do ye like your drinks sweet?",
    "sour": "Would ye like some sourness with yer poison?",
    "strong": "Are ye a buccaneer who likes a strong drink?",
    "salty": "Ahoy, Matey do ye like it with a salty tang?",
    "spicy": "Are ye a lubber who likes it spicy?",
}


ingredients = {
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "sour": ["shake of grapefuit liquer", "splash of tonic", "lime juice"],
    "strong": ["glug of rum", "splash of absinthe", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "spicy": ["two jalapeno peppers", "slug of tequila", "splash of gin"],
}

def get_drink():
    value = False 
    customer_preference = {}
    for option in questions:
                preference = input(questions[option]+ 'y = yes + n = no : ')
                if preference == 'y':
                    value = True 
                else:
                    value = False
                    
                customer_preference.update({option:value})  
    return customer_preference 

    
def create_drinks(customer_preference):
    drinks = []
    for stuff in customer_preference:
              if customer_preference[stuff] == True:
                  ingredient = random.choice(ingredients[stuff])
                  drinks.append(ingredient)
    return drinks
 
                 
if __name__ == '__main__':
    choice = get_drink()
    print(choice)
    customer_drink = create_drinks(customer_preference)
    print(customer_drink)
    
    
    
    
    
    
    
    

    
    
    

        
    
    
    
    
    
                
                
    
    



    

    
    
    
