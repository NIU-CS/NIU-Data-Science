# 602

cards = [input() for _ in range(5)]
values = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
total = sum(values[card] if card in values else int(card) for card in cards)
print(total)
