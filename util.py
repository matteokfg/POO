def increment_id(identifier):
    return identifier + 1

def validate_inteiro(inteiro):
        try:
            int(inteiro)
            return True
        except ValueError:
            print("Valor deve ser inteiro!")
            return False