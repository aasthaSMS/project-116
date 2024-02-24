# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Aastha Shirodkar" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def father():
    father_name = "Mitesh Shirodkar"  
    father_age = "45"  
    return render_template('father.html', father_name=father_name, father_age=father_age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    mother_name = "Aakanksha Shirodkar"  
    mother_age = "42"  
    return render_template('mother.html', mother_name=mother_name, mother_age=mother_age)

# define the route to friends webpage
@app.route("/friends")
def friends():
    friends_list = ["Vrushti", "Pauravi", "Richa", "Tanvi"]  
    return render_template('friends.html', friends_list=friends_list)




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
