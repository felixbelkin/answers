def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return "Ничья"

    if (player1 == "камень" and player2 == "ножницы") or (player1 == "ножницы" and player2 == "бумага") or (player1 == "бумага" and player2 == "камень"):
        return "Игрок 1 победил"

    return "Игрок 2 победил"

player1_choice = "камень"
player2_choice = "ножницы"

result = rock_paper_scissors(player1_choice, player2_choice)
print(result) 