import spacy

from getProductName import getProductName

# Load the English language model
nlp = spacy.load("en_core_web_sm")


def generate_meaningful_description(product):
    product_name = getProductName(product["src"])
    title_doc = nlp(product["title"])
    subtitle_doc = nlp(product["subtitle"])
    product_doc = nlp(product_name)

    # Extract meaningful keywords from title and subtitle
    keywords = set()
    for token in title_doc:
        if token.is_alpha:
            keywords.add(token.text)
    for token in subtitle_doc:
        if token.is_alpha:
            keywords.add(token.text)
    for token in product_doc:
        if token.is_alpha:
            keywords.add(token.text)

    # Create a description using the keywords
    description = f"Introducing the {product['title']} – a fashion-forward addition to your wardrobe. " \
        f"Immerse yourself in its {', '.join(keywords)} design, offering a truly unique look. " \
        f"All this style, and it's yours for just {product['price']}!"

    return description
