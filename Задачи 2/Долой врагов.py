def remove_enemies(names, enemies):
    return [name for name in names if name not in enemies]

all_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
enemy_list = ["Bob", "David"]

result = remove_enemies(all_names, enemy_list)
print(result) 
