from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import time
import collections

app = Flask(__name__)

# remove before deploy
# This option removes the static file caching
app.config.update(SEND_FILE_MAX_AGE_DEFAULT = 0)
# ------------

# Set up database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.sqlite3'
db = SQLAlchemy(app)

# define database model
class recipes(db.Model):
	id = db.Column('recipe_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100), unique = True)
	ingredients = db.Column(db.Text)
	instructions = db.Column(db.Text)

	def __init__(self, name, ingredients, instructions):
		self.name = name
		self.ingredients = ingredients
		self.instructions = instructions

# functions to supply date and weekday to views
def get_date():
	return time.strftime("%Y-%m-%d")

def get_weekday():
	return time.strftime("%A")


# Views

@app.route('/')
def index():
	return render_template('index.html', 
		date = get_date(), weekday = get_weekday())


@app.route('/food_manager')
def food_manager():
    return render_template('food_manager.html', 
    	date = get_date(), weekday = get_weekday(), 
    	recipes = recipes.query.all())


@app.route('/food_manager/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
    	date = get_date(), weekday = get_weekday())


@app.route('/food_manager/recipe_added', methods = ['POST', 'GET'])
def recipe_added():
	if request.method == 'POST':
		recipe = recipes(request.form['name'], request.form['ingredients'], request.form['instructions'])
		db.session.add(recipe)
		db.session.commit()
		return render_template('recipe_added.html', 
			date = get_date(), weekday = get_weekday())


@app.route('/shopping_list',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        plan = collections.OrderedDict(sorted(request.form.items()))
        del plan['submit']

    shopping_items = []

    for key, value in plan.iteritems():
    	# query database based on the selected recipe name

    	recipe = recipes.query.filter_by(name = value).first()
    	ingreds = recipe.ingredients

    	# clean ingredients string and put its items in a list
    	ingred_items_clean = []
    	ingred_items = ingreds.split(',')
    	for item in ingred_items:
    		ingred_items_clean.append(item.strip())

    	# add to shopping list while checking for duplicates
    	for item in ingred_items_clean:
    		if item not in shopping_items:
    			shopping_items.append(item)


    return render_template('shopping_list.html', 
        	date = get_date(), weekday = get_weekday(), plan = plan, 
        	shopping_items = shopping_items)


if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)