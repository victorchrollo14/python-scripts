import random
import json

from textGen import generate_meaningful_description

category_match = {
    1: "shirts",
    2: "bottoms",
    3: "knits",
    4: "denim",
    5: "sweaters",
    6: "accessories",
    7: "footwear"
}


def printJson(value):
    print(json.dumps(value, indent=2))


with open("product.json", "r") as file:
    data = json.load(file)


shirts = data["products"]["shirts"]
bottoms = data["products"]["bottoms"]
knits = data["products"]["knits"]
denim = data["products"]["denim"]
sweaters = data["products"]["sweaters"]
accessories = data["products"]["accessories"]
footwear = data["products"]["footwear"]

categories = [shirts, bottoms, knits, denim, sweaters, accessories, footwear]

new_products = []
for index, category in enumerate(categories):
    index += 1
    id = 1
    for product in category:
        description = generate_meaningful_description(product)
        converted_product = {
            "_id": id,
            "Title": product["title"],
            "Subtitle": product["subtitle"],
            "Description": description,
            "price": float(product["price"].strip("$")),
            "category": f"{category_match[index]}",
            "sizeOptions": ["small", "medium", "large", "extralarge", "xxl"],
            "InventoryCount": 100,  # You can set this based on your inventory data
            "Images": [product["src"], product["src2"]],
            "ratings": [{"stars": random.randint(1, 5), "reviewCount": random.randint(10, 100)}]
        }
        id += 1
        new_products.append(converted_product)

with open("converted_product.json", "a") as newfile:
    json.dump(new_products, newfile, indent=4)
