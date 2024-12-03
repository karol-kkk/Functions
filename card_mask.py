# card_mask.py
def hide(card_number):
    # Ensure the card number is exactly 16 digits long
    if len(card_number) == 16:
        return card_number[:2] + '*' * 10 + card_number[-4:]
    else:
        return "Invalid card number"
