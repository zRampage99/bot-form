import random
import string


def generate_random_email():
    """Genera una stringa casuale per l'email."""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@example.com"
