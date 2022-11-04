_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]
    
def validate_discount_code(discount_code):
    discount_code = set(discount_code)
    for code in _AVAILABLE_DISCOUNT_CODES:
        set_code = set(code)
        if len(discount_code ^ set_code) < 3:
            return True
    return False

if __name__ == "__main__":
    print(validate_discount_code("primavera2021"))
