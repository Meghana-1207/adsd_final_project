from bottle import route, post, run, template, redirect, request, Bottle
import database

app = Bottle()

@app.route("/")
def get_index():
    redirect("/list")

@app.route("/list")
def get_list():
    search_query = request.query.get("search", "")
    items = database.get_items(database.sample_restaurants.restaurants, search_query)
    return template("list.tpl", shopping_list=items, search=search_query)

@app.route("/add")
def get_add():
    return template("add_restaurant.tpl")

@app.post("/add")
def post_add():
    name = request.forms.get("name")
    borough = request.forms.get("borough")
    cuisine = request.forms.get("cuisine")
    description = request.forms.get("description")

    # Add restaurant item
    restaurant_data = {
        "name": name,
        "borough": borough,
        "cuisine": cuisine
    }
    database.add_item(database.sample_restaurants.restaurants, restaurant_data)

    # Add description item
    description_data = {
        "restaurant_id": str(restaurant_data["_id"]),
        "description": description
    }
    database.add_item(database.sample_restaurants.descriptions, description_data)

    redirect("/list")

@app.route("/delete/<id>")
def get_delete(id):
    database.delete_item(database.sample_restaurants.restaurants, id)
    redirect("/list")

@app.route("/update/<id>")
def get_update(id):
    items = database.get_items(database.sample_restaurants.restaurants, id)
    if len(items) != 1:
        redirect("/list")
    description = items[0].get('description', '')
    return template("update_item.tpl", id=id, description=description)

@app.post("/update")
def post_update():
    description = request.forms.get("description")
    id = request.forms.get("id")
    database.update_item(database.sample_restaurants.restaurants, id, description)
    redirect("/list")

if __name__ == "__main__":
    run(app, host='localhost', port=8080)
