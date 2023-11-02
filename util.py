def increment_id(identifier):
    return identifier + 1


def validate_inteiro(inteiro):
        try:
            int(inteiro)
            return True
        except ValueError:
            print("Apenas são permitidos valores inteiros")
            return False


from datetime import date
def validate_data(nova_data_de_nascimento):
    try:
        date.fromisoformat(nova_data_de_nascimento)
        return True
    except ValueError:
        print("Data não válida!")
        return False