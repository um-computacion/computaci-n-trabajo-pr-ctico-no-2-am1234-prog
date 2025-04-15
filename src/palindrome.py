def is_palindrome(text):
    # Sacamos espacios, signos y pasamos todo a minúsculas
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
