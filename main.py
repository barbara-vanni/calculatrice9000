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
    else:
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


def stock_calcul(history, expression, result):
    history.append((expression, result))


def afficher_historique(history):
    if not history:
        print("L'historique est vide.")
    else:
        print("Historique des calculs :")
        for i, (expression, result) in enumerate(history, 1):
            print(f"|{i}| {expression} = {result}")


def effacer_historique(history):
    history.clear()
    print("L'historique a été effacé.")


def main():
    history = []

    while True:
        num1 = valid_input("Entrez votre premier nombre: ")
        operator = input("Entrez votre opérateur: ")
        num2 = valid_input("Entrez votre deuxième nombre: ")

        while operator not in ['/', '*', '-', '+', '%']:
            print("Erreur : Veuillez saisir un opérateur valide (+, -, *, /, %)")
            operator = input("Entrez votre opérateur: ")

        result = calcule(num1, operator, num2)
        print(result)

        stock_calcul(history, f"{num1} {operator} {num2}", result)



        choix = input("Voulez-vous afficher l'historique ? (O/N) ").lower()
        if choix == 'o':
            afficher_historique(history)
            choix = input("Voulez-vous effacer l'historique ? (O/N) ").lower()
            if choix == 'o':
                effacer_historique(history)
            else :
                continuer = input("Voulez-vous continuer ? (O/N) ").lower()
            if continuer != 'o':
                break
        elif choix != 'o':
            continuer =input("Voulez-vous continuer ? (O/N) ").lower()
            if continuer != 'o':
                break
        else :
            continuer = input("Voulez-vous continuer ? (O/N) ").lower()
            if continuer != 'o':
                break



main()
