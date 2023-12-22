def can_share_coins_equally(coins, num_children):
    total_coins = sum(coins)

    if total_coins % num_children == 0:
        return True
    else:
        return False

coins_array = [3, 5, 2, 8]
children_count = 3
result = can_share_coins_equally(coins_array, children_count)
if result:
    print("Монеты можно распределить поровну между детьми.")
else:
    print("Нельзя поровну распределить монеты между детьми.")
