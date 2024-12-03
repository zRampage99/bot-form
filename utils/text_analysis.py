import re

def text_analysis(element, index, form_elements):
    header_text = element.text
    print(f"Trovato tag {element.tag_name}: {header_text}")

    # Regex per trovare "numero operatore numero" ovunque nel testo
    match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', header_text)
    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))

        # Calcola il risultato in base all'operatore
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2 if num2 != 0 else 'undefined'  # Gestisce la divisione per zero
        else:
            result = 'undefined'

        print(f"Domanda aritmetica trovata: {num1} {operator} {num2} = {result}")

        # Verifica che ci sia un campo successivo e che sia un input
        if index + 1 < len(form_elements):  # Assicurati che l'elemento successivo esista
            next_element = form_elements[index + 1]

            # Se il prossimo elemento è un campo di input, inserisci il risultato
            if next_element.tag_name == 'input':
                next_element.clear()  # Pulisce il campo se già contiene qualcosa
                next_element.send_keys(str(result))  # Inserisce il risultato
                index += 1  # Incrementa l'indice
                print(f"Ho inserito la risposta {result} nel campo successivo")
    return index
