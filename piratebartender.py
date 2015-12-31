
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
                preference = input(questions[option] + 'y = yes + n = no : ')
                if preference == 'y':
                    value = True 
                else:
                    value = False
                    
                customer_preference.update({option:value})  
    return customer_preference 
if __name__ == '__main__':
    print("preference")
    
def drinks(customer_preference, drink = ()):
    
    import random 
    ingredients = {"sweet","sour","strong","salty","spicy"}
    
    print(random.choice(ingredients))
    return drinks 
if __name__ == '__main__':
    print(ingredients)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    

        
    
    
    
    
    
                
                
    
    



    

    
    
    