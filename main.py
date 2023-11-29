def calcule(num1, operator, num2):
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    
    elif operator == '/':
        if num2 != 0: 
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:  
            return num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else :
        return "L'opérateur n'est pas reconnu (+, -, *, /, %)"


def valid_input(prompt):
    while True:
        user_input = input(prompt)

        try:
            num = float(user_input)
        except ValueError:
            print("Erreur: Veuillez saisir un nombre valide.")
            continue
        return num


def stock_calcul():
    pass

       
def main():
    num1 = valid_input("Entrez votre premier nombre: ")
    operator = input("Entrez votre opérateur: ")
    num2 = valid_input("Entrez votre deuxième nombre: ")

    while operator not in ['/', '*', '-', '+', '%']:
        print("Erreur : Veuillez saisir un opérateur valide (+, -, *, /, %)")
        operator = input("Entrez votre opérateur: ")

    result = calcule(num1, operator, num2)
    print(result)


main()
