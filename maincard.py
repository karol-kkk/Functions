# main.py
from card_mask import hide

card_number = "5290312400019022"
masked_card = hide(card_number)

print(f"Masked card number: {masked_card}")