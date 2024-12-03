# main.py
import time
from bot.browser import Browser
from bot.form import ContactForm

class TestBot:
    def __init__(self):
        self.browser = Browser()
        self.form = None

    def run(self):
        # Avvia il browser
        self.browser.start_browser()

        # Crea un'istanza della classe ContactForm con il driver del browser
        self.form = ContactForm(self.browser.driver)

        # Compila il modulo
        self.form.fill_dynamic_form()

        # Aspetta qualche secondo per vedere il risultato (opzionale)
        self.browser.driver.implicitly_wait(10)

        time_for_close_browser = 20
        print(f"Il programma sta aspettando per {time_for_close_browser} secondi...")
        time.sleep(time_for_close_browser)

        # Chiudi il browser
        self.browser.close_browser()


# Questo blocco di codice verrà eseguito solo quando il file main.py viene eseguito direttamente
if __name__ == '__main__':
    bot = TestBot()
    bot.run()
