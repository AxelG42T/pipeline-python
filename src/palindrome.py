def est_palindrome(texte: str) -> bool:
    texte = texte.replace(" ", "").lower()
    return texte == texte[::-1]