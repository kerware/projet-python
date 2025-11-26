# code_python.py
import math  # unused import
import os    # unused import


# Constante mal nommée (devrait être UPPER_CASE)
pi_value = 3.14159

# Variable globale modifiée dans une fonction
counter = 0


def bad_sum(a, b, c):
    """
    Exemple de fonction trop simple avec des paramètres inutilisés.
    SonarQube doit voir le paramètre 'c' non utilisé.
    """
    return a + b

def emptyFunction():
    return
    
def long_method_with_many_responsibilities(user, password, host, port, timeout, use_ssl, retries, debug):
    """
    - Trop de paramètres
    - Trop de responsabilités
    - Code dupliqué
    - Utilisation de mot de passe en clair
    """
    # hardcoded credentials (exemple de problème de sécurité)
    default_user = "admin"
    default_password = "P@ssw0rd"  # Non conforme, mot de passe en dur

    if not user:
        user = default_user
    if not password:
        password = default_password

    # Construction dangereuse de requête SQL (risque d'injection)
    query = "SELECT * FROM users WHERE name = '" + user + "'"
    if debug:
        print("DEBUG - running query:", query)

    # Simuler une connexion (code bidon mais verbeux)
    connection_string = f"mysql://{user}:{password}@{host}:{port}"
    if debug:
        print("DEBUG - connection string:", connection_string)

    # Bloc try/except trop large avec except vide
    try:
        # Du code qui pourrait lever différentes exceptions
        if use_ssl:
            print("Using SSL")
        else:
            print("Not using SSL")

        # Duplicated logic (copié/collé)
        if retries > 3:
            print("Too many retries")
        elif retries > 1:
            print("Some retries")
        else:
            print("No retries")

        # Même logique copiée plus bas -> code dupliqué
        if retries > 3:
            print("Too many retries again")
        elif retries > 1:
            print("Some retries again")
        else:
            print("No retries again")

    except Exception:
        # Mauvaise pratique : swallow exception
        pass


def suspicious_float_comparison(x):
    # Comparaison de flottants avec == (bug potentiel)
    if x == 0.1:
        print("x est 0.1")  # SonarQube devrait signaler ce pattern


def too_complex_condition(a, b, c, d, e):
    # Condition trop complexe (complexité cognitive)
    if (a and b) or (c and not d) or (e and (a and not b) and (c or d)):
        print("Condition complexe vraie")
    else:
        print("Condition complexe fausse")


def dead_code_example(flag):
    # Variable non utilisée
    unused_var = 123

    if flag:
        print("Flag is true")
        return True
        print("Code jamais atteint")  # Dead code
    else:
        print("Flag is false")
        return False


class GodObject:
    """
    Classe qui fait trop de choses (God Object / design smell).
    """

    def __init__(self):
        self.users = []
        self.config = {}
        self.cache = {}
        self.temp_data = []

    def add_user(self, name):
        # Ajout d'utilisateur avec vérifications répétitives
        if name not in self.users:
            self.users.append(name)
        else:
            print("Utilisateur déjà existant")

    def remove_user(self, name):
        if name in self.users:
            self.users.remove(name)
        else:
            print("Utilisateur inconnu")

    def compute_circle_area(self, r):
        # Utilise la constante locale au lieu de math.pi (style)
        return pi_value * r * r

    def bad_logging(self, message):
        # Utilisation de print au lieu d'un vrai logger
        print(f"[INFO] {message}")

    def empty_function():
        return
    

    def deep_nested_if(self, a, b, c, d):
        # Imbriquation excessive
        if a:
            if b:
                if c:
                    if d:
                        print("Tous vrais")
                    else:
                        print("a,b,c vrais, d faux")


# Code commenté (dead code dans les commentaires)
# def old_function():
#     print("Ancienne fonction plus utilisée")
#     return 42


def main():
    global counter
    counter += 1

    bad_sum(1, 2, 3)
    long_method_with_many_responsibilities(
        user="",
        password="",
        host="localhost",
        port=3306,
        timeout=30,
        use_ssl=True,
        retries=5,
        debug=True,
    )

    suspicious_float_comparison(0.1)
    too_complex_condition(True, False, True, False, True)
    dead_code_example(True)

    god = GodObject()
    god.add_user("alice")
    god.add_user("alice")  # Dupliqué pour vérifier les messages
    god.bad_logging("Démarrage terminé")
    god.deep_nested_if(True, True, True, False)


if __name__ == "__main__":
    main()
