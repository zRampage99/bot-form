# Funzione per calcolare la risposta del captcha (somma)
def solve_captcha(captcha_question):
    # Esamina la domanda e calcola la risposta
    parts = captcha_question.split(" ")
    num1 = int(parts[2])
    num2 = int(parts[4][:-1])
    return num1 + num2
