# form.py
import re

from selenium.webdriver.common.by import By

from utils.generate_email import generate_random_email
from utils.text_analysis import text_analysis


class ContactForm:
    def __init__(self, driver):
        self.driver = driver

    def fill_dynamic_form(self):
        self.driver.get('http://localhost:3000/contact')

        # Trova tutti gli input di tipo testo, textarea e altri elementi compilabili
        form_elements = self.driver.find_elements(By.CSS_SELECTOR, 'input, textarea, select, h1, h2, h3, h4, h5, h6')

        index = 0
        while index < len(form_elements):
            element = form_elements[index]
            try:
                # Se è un tag di intestazione (h1, h2, h3, h4, h5, h6), analizza il contenuto del testo
                if element.tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    index = text_analysis(element, index, form_elements)
                if element.tag_name == 'input':
                    input_id = element.get_attribute('id')
                    input_name = element.get_attribute('name')
                    print(f"ID: {input_id}, Name: {input_name}")

                    # Ricerca tramite ID
                    if input_id:  # Se c'è un ID, usalo
                        if 'email' in input_id.lower():
                            email = generate_random_email()
                            element.send_keys(email)
                        elif 'name' in input_id.lower():
                            element.send_keys('Testo bellissimo')
                        elif 'subject' in input_id.lower():
                            element.send_keys('Ciao bello come stai')
                elif element.tag_name == 'textarea':
                    element.send_keys('Questo è.')

                elif element.tag_name == 'select':
                    options = element.find_elements(By.TAG_NAME, 'option')
                    if options:
                        options[1].click()  # Seleziona la seconda opzione, o la prima disponibile
                    print("Ho selezionato il campo select")

                # Se è una checkbox o radio button, clicca per selezionarlo
                elif element.get_attribute('type') in ['checkbox', 'radio']:
                    if not element.is_selected():
                        element.click()
                    print("Ho selezionato il campo checkbox/radio")

            except Exception as e:
                print(f"Errore durante l'interazione con il campo {element}: {e}")

            # Incrementa l'indice al termine dell'iterazione
            index += 1

        # Dopo aver compilato il modulo, invia il modulo (se c'è un pulsante di invio)
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"], input[type="submit"]')
        if submit_button:
            submit_button.click()
