# ============================================================
#  U3B1 — OOP Intro Activity: RPG Guild Manager
#  Principles of Computing | Unit 03 - OOP Foundations
# ============================================================
#  In this activity, you'll build an RPG Guild Management
#  system from scratch using classes, __init__, and self.
#
#  TOTAL: 15 points (7 tasks)
#
#  HOW TO TEST: Run your file after each task. Compare your
#  output to the expected output shown in the comments.
#  Your output should match EXACTLY.
# ============================================================


# ============================================================
# TASK 1: Create the Hero class (2 pts)
# ============================================================
# Define a class called Hero with an __init__ that takes:
#   Parameters: name, role, level, hp
#   Default attributes:
#     - xp = 0
#     - is_alive = True
#
# Then create these 4 heroes and print each one's info:
#   - "Aria",    "Mage",     5,  80
#   - "Kael",    "Warrior",  7,  150
#   - "Mira",    "Healer",   4,  90
#   - "Dax",     "Rogue",    6,  100
#
# Print format for each: "name (role) — Lv.level | HP: hp | XP: xp"

print("=" * 55)
print("TASK 1: Heroes")
print("=" * 55)

# YOUR CODE HERE
class Hero:
    def __init__(self, name, role, level, hp):
        self.name = name
        self.role = role
        self.level = level
        self.hp = hp
        self.xp = 0
        self.is_alive = True

aria = Hero("Aria", "Mage", 5, 80)
Kael = Hero("Kael", "Mage", 7, 150)
Mira = Hero("Mira", "Mage", 4, 90)
Dax = Hero("Dax", "Mage", 6, 100)
print(f"{aria.name} ({aria.role}) - Lv.{aria.level} | Hp: {aria.hp} | XP: {aria.xp}")
print(f"{Kael.name} ({Kael.role}) - Lv.{Kael.level} | Hp: {Kael.hp} | XP: {Kael.xp}")
print(f"{Mira.name} ({Mira.role}) - Lv.{Mira.level} | Hp: {Mira.hp} | XP: {Mira.xp}")
print(f"{Dax.name} ({Dax.role}) - Lv.{Dax.level} | Hp: {Dax.hp} | XP: {Dax.xp}")
# Expected Output:
# =======================================================
# TASK 1: Heroes
# =======================================================
# Aria (Mage) — Lv.5 | HP: 80 | XP: 0
# Kael (Warrior) — Lv.7 | HP: 150 | XP: 0
# Mira (Healer) — Lv.4 | HP: 90 | XP: 0
# Dax (Rogue) — Lv.6 | HP: 100 | XP: 0


# ============================================================
# TASK 2: Create the Weapon class (2 pts)
# ============================================================
# Define a class called Weapon with an __init__ that takes:
#   Parameters: name, damage, weapon_type
#   Default attributes:
#     - is_enchanted = False
#     - enchant_level = 0
#
# Then create these 4 weapons and print each one's info:
#   - "Flame Sword",    45, "Melee"
#   - "Frost Staff",    60, "Magic"
#   - "Shadow Dagger",  35, "Melee"
#   - "Thunder Bow",    50, "Ranged"
#
# Print format: "name (weapon_type) — damage DMG | Enchanted: is_enchanted"

print("\n" + "=" * 55)
print("TASK 2: Weapons")
print("=" * 55)

# YOUR CODE HERE
class Weapon:
    def __init__(self, name, damage, weapon_type):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type
        self.is_enchanted = False
        self.enchantment_level = 0

Flame_Sword = Weapon("Flame Sword", "45", "Melee")
Frost_Staff = Weapon("Frost Staff", "60", "Magic")
Shadow_Dagger = Weapon("Shadow Dagger", "35", "Melee")
Thunder_Bow = Weapon("Thunder Body", "50", "Ranged")

print(f"{Flame_Sword.name} ({Melee.weapon_type}) - 45.damage DMG | Enchanted: is_enchanted")
print(f"{Frost_Staff.name} ({Magic.weapon_type}) - 60.damage DMG | Enchanted: is_enchanted")
print(f"{Shadow_Dagger.name} ({Melee.weapon_type}) - 35.damage DMG | Enchanted: is_enchanted")
print(f"{Thunder_Bow.name} ({Ranged.weapon_type}) - 50.damage DMG | Enchanted: is_enchanted")
# Expected Output:
# =======================================================
# TASK 2: Weapons
# =======================================================
# Flame Sword (Melee) — 45 DMG | Enchanted: False
# Frost Staff (Magic) — 60 DMG | Enchanted: False
# Shadow Dagger (Melee) — 35 DMG | Enchanted: False
# Thunder Bow (Ranged) — 50 DMG | Enchanted: False


# ============================================================
# TASK 3: Create the Potion class (2 pts)
# ============================================================
# Define a class called Potion with an __init__ that takes:
#   Parameters: name, effect, potency
#   Default attributes:
#     - quantity = 1
#
# Create these 3 potions:
#   - "Elixir of Life",   "heal",   50
#   - "Mana Surge",       "mana",   30
#   - "Berserk Brew",     "attack", 20
#
# After creating them, set the Elixir's quantity to 3
# and the Mana Surge's quantity to 5.
#
# Print format: "name (xquantity) — effect +potency"

print("\n" + "=" * 55)
print("TASK 3: Potions")
print("=" * 55)

# YOUR CODE HERE
class Potion:
    def __init__(self, name, effect, potency ):
        self.name = name
        self.effect = effect
        self.potency = potency
        self.quantity = 1

Elixer_of_Life = Potion("Elixer of Life", "heal", "50")
Mana_Surge = Potion("Mana Surge", "mana", "30")
Berserk_Brew = Potion("Berserk Brew", "attack", "20")

print(f"{Elixer_of_Life.name} ({3.quantity}) - heal.effect +potency")
print(f"{Mana_Surge.name} ({5.quantity}) - mana.effect +potency")
print(f"{Berserk_Brew.name} ({0.quantity}) - attack.effect +potency")

# Expected Output:
# =======================================================
# TASK 3: Potions
# =======================================================
# Elixir of Life (x3) — heal +50
# Mana Surge (x5) — mana +30
# Berserk Brew (x1) — attack +20

party = [aria, Kael, Mira, Dax]

for number, hero in enumerate(party):
print(f"[{number}] {hero.name} - {hero.role} (Lv.level)")
