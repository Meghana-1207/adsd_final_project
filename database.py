from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mramired:meghana@cluster0.gusxjgg.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

sample_restaurants = client.sample_restaurants

def setup_database():
    # Drop both collections
    sample_restaurants.restaurants.drop()
    sample_restaurants.descriptions.drop()

def get_items(collection, id=None):
    if id is None:
        items = collection.find({})
    else:
        items = collection.find({"_id": ObjectId(id)})

    items = list(items)
    for item in items:
        item["id"] = str(item["_id"])
    return items

def add_item(collection, data):
    collection.insert_one(data)

def delete_item(collection, id):
    collection.delete_one({"_id": ObjectId(id)})

def update_item(collection, id, description):
    where = {"_id": ObjectId(id)}
    updates = {"$set": {"description": description}}
    collection.update_one(where, updates)

def get_combined_data():
    restaurants = sample_restaurants.restaurants.find({})
    descriptions = sample_restaurants.descriptions.find({})
    combined_data = []

    for restaurant in restaurants:
        restaurant["id"] = str(restaurant["_id"])
        combined_data.append({
            "id": restaurant["id"],
            "description": restaurant.get("description", ""),
            "restaurant_data": restaurant,
            "descriptions": []
        })

    for description in descriptions:
        description["id"] = str(description["_id"])
        for combined_item in combined_data:
            if description.get("restaurant_id") == combined_item["id"]:
                combined_item["descriptions"].append({
                    "id": description["id"],
                    "description": description.get("description", "")
                })

    return combined_data

def test_setup_database():
    print("testing setup_database()")
    setup_database()
    restaurants_items = get_items(sample_restaurants.restaurants)
    descriptions_items = get_items(sample_restaurants.descriptions)
    assert len(restaurants_items) == 0
    assert len(descriptions_items) == 0

def test_get_items():
    print("testing get_items()")
    setup_database()
    restaurants_items = get_items(sample_restaurants.restaurants)
    descriptions_items = get_items(sample_restaurants.descriptions)
    assert type(restaurants_items) is list
    assert type(descriptions_items) is list
    assert len(restaurants_items) == 0
    assert len(descriptions_items) == 0

def test_add_item():
    print("testing add_item()")
    setup_database()
    restaurants_items = get_items(sample_restaurants.restaurants)
    descriptions_items = get_items(sample_restaurants.descriptions)
    assert len(restaurants_items) == 0
    assert len(descriptions_items) == 0

    # Add a restaurant item
    restaurant_data = {
        "name": "Sample Restaurant",
        "borough": "Brooklyn",
        "cuisine": "American"
    }
    add_item(sample_restaurants.restaurants, restaurant_data)

    restaurants_items = get_items(sample_restaurants.restaurants)
    descriptions_items = get_items(sample_restaurants.descriptions)
    assert len(restaurants_items) == 1
    assert len(descriptions_items) == 0

    # Add a description item
    description_data = {
        "restaurant_id": restaurants_items[0]["id"],
        "description": "This is a sample description"
    }
    add_item(sample_restaurants.descriptions, description_data)

    restaurants_items = get_items(sample_restaurants.restaurants)
    descriptions_items = get_items(sample_restaurants.descriptions)
    assert len(restaurants_items) == 1
    assert len(descriptions_items) == 1

def test_delete_item():
    print("testing delete_item()")
    setup_database()
    # Add a restaurant item
    restaurant_data = {
        "name": "Sample Restaurant",
        "borough": "Brooklyn",
        "cuisine": "American"
    }
    add_item(sample_restaurants.restaurants, restaurant_data)

    restaurants_items = get_items(sample_restaurants.restaurants)
    assert len(restaurants_items) == 1

    # Add a description item
    description_data = {
        "restaurant_id": restaurants_items[0]["id"],
        "description": "This is a sample description"
    }
    add_item(sample_restaurants.descriptions, description_data)

    descriptions_items = get_items(sample_restaurants.descriptions)
    assert len(descriptions_items) == 1

    # Delete the restaurant item
    delete_item(sample_restaurants.restaurants, restaurants_items[0]["id"])

    restaurants_items = get_items(sample_restaurants.restaurants)
    descriptions_items = get_items(sample_restaurants.descriptions)
    assert len(restaurants_items) == 0
    assert len(descriptions_items) == 0

def test_update_item():
    print("testing update_item()")
    setup_database()
    # Add a restaurant item
    restaurant_data = {
        "name": "Sample Restaurant",
        "borough": "Brooklyn",
        "cuisine": "American"
    }
    add_item(sample_restaurants.restaurants, restaurant_data)

    restaurants_items = get_items(sample_restaurants.restaurants)
    assert len(restaurants_items) == 1

    # Add a description item
    description_data = {
        "restaurant_id": restaurants_items[0]["id"],
        "description": "This is a sample description"
    }
    add_item(sample_restaurants.descriptions, description_data)

    descriptions_items = get_items(sample_restaurants.descriptions)
    assert len(descriptions_items) == 1

    # Update the restaurant item
    update_item(sample_restaurants.restaurants, restaurants_items[0]["id"], "Updated Restaurant Name")

    restaurants_items = get_items(sample_restaurants.restaurants)
    descriptions_items = get_items(sample_restaurants.descriptions)
    assert len(restaurants_items) == 1
    assert len(descriptions_items) == 1
    assert restaurants_items[0].get("description", "") == "Updated Restaurant Name"

if __name__ == "__main__":
    test_setup_database()
    test_get_items()
    test_add_item()
    test_delete_item()
    test_update_item()

    # Test get_combined_data
    combined_data = get_combined_data()
    print("\nCombined Data:")
    for item in combined_data:
        print(item)
    print("done.")