def blackjack(cards):
    total_sum = sum(cards)
    return total_sum > 21

# for example:
card_values = [10, 5, 7]
result = blackjack(card_values)
print(result)  # Ожидаемый результат: False

card_values = [10, 8, 4]
result = blackjack(card_values)
print(result)  # Ожидаемый результат: True
