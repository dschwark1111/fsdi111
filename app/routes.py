from flask import Flask #from the flask mod import from flask class

#OOP object oriented paradigm-programming paradigm 

app = Flask(__name__) #creates instance of flask class/dunder or magic variable
#object 

@app.get("/") #flask decorator that maps view functions to routes
def about_me(): #our view function 
    me = {                   #python dictionary 
        "first_name": "Dorothy",
        "last_name": "Schwark",
        "hobbies": "chickens",
        "is_active": True,
    }

    return me   #return statement (returned to caller)            