import random
import json
from uuid import uuid4

from textGen import generate_meaningful_description

category_match = {
    1: "shirts",
    2: "bottoms",
    3: "knits",
    4: "denim",
    5: "outwear",
    6: "sweaters",
    7: "accessories",
    8: "footwear"
}


def printJson(value):
    print(json.dumps(value, indent=2))


with open("product.json", "r") as file:
    data = json.load(file)


shirts = data["products"]["shirts"]
bottoms = data["products"]["bottoms"]
knits = data["products"]["knits"]
denim = data["products"]["denim"]
outwear = data["products"]["outwear"]
sweaters = data["products"]["sweaters"]
accessories = data["products"]["accessories"]
footwear = data["products"]["footwear"]

categories = [shirts, bottoms, knits, denim, outwear, sweaters, accessories, footwear]

new_products = []
for index, category in enumerate(categories):
    index += 1
    id = 1
    for product in category:
        description = generate_meaningful_description(product)
        converted_product = {
            "_id": uuid4().hex,
            "title": product["title"],
            "subtitle": product["subtitle"],
            "description": description,
            "price": float(random.randint(100, 200)),
            "category": f"{category_match[index]}",
            "sizeOptions": ["small", "medium", "large", "extralarge", "xxl"],
            "inventoryCount": random.randint(5, 100),  # You can set this based on your inventory data
            "images": [product["src"], product["src2"]],
            "ratings": {"stars": random.randint(1, 5), "reviewCount": random.randint(10, 100)}
        }

        id += 1
        new_products.append(converted_product)

with open("converted_product.json", "w") as newfile:
    json.dump(new_products, newfile, indent=4)
