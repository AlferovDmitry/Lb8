import random

# Списки предметов
common_items = ["Common Item 1", "Common Item 2", "Common Item 3", "Common Item 4", "Common Item 5"]
rare_items = ["Rare Item 1", "Rare Item 2", "Rare Item 3"]
epic_items = ["Epic Item 1", "Epic Item 2"]
legendary_items = ["Legendary Item 1"]

# Шансы выпадения
drop_chances = {
    "common": 0.7,
    "rare": 0.2,
    "epic": 0.1,
    "legendary": 0.05
}

# Функция открытия лутбокса
def open_lootbox():
    result = random.random()
    if result < drop_chances["legendary"]:
        return random.choice(legendary_items)
    elif result < drop_chances["epic"]:
        return random.choice(epic_items)
    elif result < drop_chances["rare"]:
        return random.choice(rare_items)
    else:
        return random.choice(common_items)

# Открытие 20 лутбоксов
loot_results = {"common": 0, "rare": 0, "epic": 0, "legendary": 0}
loot_list = []

for _ in range(20):
    item = open_lootbox()
    loot_list.append(item)
    if item in common_items:
        loot_results["common"] += 1
    elif item in rare_items:
        loot_results["rare"] += 1
    elif item in epic_items:
        loot_results["epic"] += 1
    else:
        loot_results["legendary"] += 1

# Вывод результатов
print("Результаты открытия лутбоксов:")
for rarity, count in loot_results.items():
    print(f"Выпало {count} {rarity} предметов")

if loot_results["epic"] > 3:
    print("\033[95m(Удача!)")
if loot_results["legendary"] > 1:
    print("\033[93m(Большая удача!)")

print("Полученные предметы:")
for item in loot_list:
    if item in common_items:
        print(f"\033[0m{item}")
    elif item in rare_items:
        print(f"\033[94m{item}")
    elif item in epic_items:
        print(f"\033[95m{item}")
    else:
        print(f"\033[93m{item}")
