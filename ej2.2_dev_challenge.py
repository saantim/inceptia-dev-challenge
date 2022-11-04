import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})

def is_product_available(product_name, quantity):
    df = _PRODUCT_DF

    if product_name not in list(df["product_name"]):
        print("Por favor ingresar un producto de la siguiente lista: ",  ', '.join(list(df["product_name"])))
        return False

    product_quantity = int(df[df["product_name"] == product_name]["quantity"])

    if product_quantity < quantity:
        print(f"Lamentablemente no hay suficiente stock de {product_name}, sólo nos quedan {product_quantity} productos.")
        return False

    return True

if __name__ == "__main__":
    print(is_product_available("Limona", 10))
    print(is_product_available("Dulce de Leche", 10))
