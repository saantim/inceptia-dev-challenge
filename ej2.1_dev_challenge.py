import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})

def is_product_available(product_name, quantity):
    df = _PRODUCT_DF
    product_quantity = df[df["product_name"] == product_name]["quantity"]
    return int(product_quantity) >= quantity

if __name__ == "__main__":
    print(is_product_available("Limon", 10))
