import re


def getProductName(src_string):
    # Regex pattern to extract the portion between common patterns
    pattern = r'instock_m_q\d+_(.*?)_\d+_530x.progressive.jpg'

    # Use regex to extract the desired portion
    match = re.search(pattern, src_string)

    if match:
        extracted_text = match.group(1)
        return extracted_text
    else:
        return src_string
