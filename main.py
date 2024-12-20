import os
import random


def cls(): os.system('cls' if os.name == 'nt' else 'clear')

# === Start of UserStats Class ===
class UserStats:
    def __init__(self):
        self.coin = 1000
        self.day = 1
        self.financial = {
            1: {
                'Profit': 0,
                'Expense': 0
            }
        }

    def next_day(self):
        self.day += 1
        self.financial[self.day] = {
            'Profit': 0,
            'Expense': 0
        }
        market.sell.update_price()

    def profit(self, amount):
        self.coin += amount
        self.financial[self.day]["Profit"] += amount

    def expense(self, amount):
        if self.coin - amount < 0:
            return False

        self.coin -= amount
        self.financial[self.day]["Expense"] += amount
        return True
    
    def check_progress(self):
        if self.day == 4:
            seeds.list['Potato Seed']['unlocked'] = True
            inventory.list['Potato Seed']['quantity'] = 5
            market_items.list['Potato Seed']['unlocked'] = True
            market.sell.list['Potato']['unlocked'] = True

            print('> 🥳 Congratulations! You have reached Day 4.')
            print('> 🥔 Potato Seed is now unlocked. You received 5 potato seeds.')
            print('-' * 80)

            return

        if self.day == 6:
            market_items.list['Cow']['unlocked'] = True
            market.sell.list['Cow']['unlocked'] = True

            print('> 🥳 Congratulations! You have reached Day 6.')
            print('> 🐮 Cow is now unlocked. You can buy them at the market.')
            print('-' * 80)

            return

        if self.coin > 1100 and seeds.list['Tomato Seed']['unlocked'] is False:
            seeds.list['Tomato Seed']['unlocked'] = True
            inventory.list['Tomato Seed']['quantity'] = 5
            market_items.list['Tomato Seed']['unlocked'] = True
            market.sell.list['Tomato']['unlocked'] = True

            print('> 🥳 Congratulations! You have got more than 1100 🪙.')
            print('> 😄 For this achievement, you will receive Tomato Seed!')
            print('> 🍅 Tomato Seed is now unlocked. You received 5 tomato seeds.')
            print('-' * 80)

            return

        if self.coin > 1500 and inventory.list['Corn']['quantity'] >= 15 and inventory.list['Potato']['quantity'] >= 10 and inventory.list['Tomato']['quantity'] >= 5 and seeds.list['Carrot Seed']['unlocked'] is False:
            seeds.list['Carrot Seed']['unlocked'] = True
            inventory.list['Carrot Seed']['quantity'] = 5
            market_items.list['Carrot Seed']['unlocked'] = True
            market.sell.list['Carrot']['unlocked'] = True

            print('> 🥳 Congratulations! You have reached the following conditions:')
            print('\t- You have more than 1500 🪙')
            print('\t- You have at least 15 corns in your inventory 🌽')
            print('\t- You have at least 10 potatoes in your inventory 🥔')
            print('\t- You have at least 5 tomatoes in your inventory 🍅')
            print('> 🥕 Carrot Seed is now unlocked. You received 5 carrot seeds.')
            print('-' * 80)

            return
# === End of UserStats Class ===


# === Start of Barn Class ===
class Barn:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_animals(self, index):
        count = 0
        for animal in self.animals:
            count += 1
            if count == index:
                if animal.feeded == True: continue
                animal.feeded = True
                animal.feeded_days += 1
                if animal.health + 10 <= 100: animal.health += 10
                else: animal.health = 100
                if animal.feeded_days >= 3: animal.collectable = True

    def update_status(self):
        dead = 0
        for animal in self.animals:
            if animal.feeded == False:
                animal.feeded_days = 0
                if animal.health - 20 >= 0: animal.health -= 20
                else:
                    self.animals.remove(animal)
                    dead += 1
            else: animal.feeded = False
        return dead
# === End of Barn Class ===

# === Start of Chicken Barn Class ===
class ChickenBarn(Barn):
    def __init__(self):
        super().__init__()
        self.animals.append(Chicken('Chic'))

    def show_chickens(self):
        if len(self.animals) == 0:
            print('> 🐔 There are no chickens in the chicken barn...')
            print('-' * 80)
            return

        print('> 🐔 List of chickens in the chicken barn:')
        print('-' * 80)
        count = 0
        for animal in self.animals:
            count += 1
            print(f'> {count}. ')
            print(f'> 🐤 Name: {animal.name}')
            print(f'> ⏳ Age: {animal.age}')
            print(f'> ❤️ Health: {animal.health}')
            print(f'> 🍚 Feeded Today: {'Yes' if animal.feeded == True else 'No'}')
            print(f'> 🍚 Feeded Streak: {animal.feeded_days} day(s)')
            print('-' * 80)

        return count

    def collect_egg(self):
        egg = 0
        for animal in self.animals:
            if animal.collectable == True:
                egg += 1
                animal.collectable = False
        inventory.list['Egg']['quantity'] += egg
        return egg
# === End of Chicken Barn Class ===

# === Start of Cow Barn Class ===
class CowBarn(Barn):
    def __init__(self):
        super().__init__()

    def show_cows(self):
        if len(self.animals) == 0:
            print('> 🐄 There are no cows in the cow barn...')
            print('-' * 80)
            return

        print('> 🐄 List of cows in the cow barn:')
        print('-' * 80)

        for animal in self.animals:
            print(f'> 🐮 Name: {animal.name}')
            print(f'> ⏳ Age: {animal.age}')
            print(f'> ❤️ Health: {animal.health}')
            print(f'> 🍚 Feeded Today: {'Yes' if animal.feeded == True else 'No'}')
            print(f'> 🍚 Feeded Streak: {animal.feeded_days} day(s)')
            print('-' * 80)

    def collect_milk(self):
        milk = 0
        for animal in self.animals:
            if animal.collectable == True:
                milk += 1
                animal.collectable = False
        inventory.list['Milk']['quantity'] += milk
        return milk
# === End of Cow Barn Class ===

# === Start of Chicken Class === 
class Chicken:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 100
        self.feeded = False
        self.feeded_days = 0
        self.collectable = False
# === End of Chicken Class ===

# === Start of Cow Class ===
class Cow:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 100
        self.feeded = False
        self.feeded_days = 0
        self.collectable = False
# === End of Cow Class ===


# === Start of Inventory Class ===

class Inventory:
    def __init__(self):

        self.list = {
            'Corn Seed': {
                'quantity': 5,
                'icon': '🌽',
                'type': 'seed'
            },
            'Corn': {
                'quantity': 0,
                'icon': '🌽',
                'type': 'crop'
            },
            'Potato Seed': {
                'quantity': 0,
                'icon': '🥔',
                'type': 'seed'
            },
            'Potato': {
                'quantity': 0,
                'icon': '🥔',
                'type': 'crop'
            },
            'Tomato Seed': {
                'quantity': 0,
                'icon': '🍅',
                'type': 'seed'
            },
            'Tomato': {
                'quantity': 0,
                'icon': '🍅',
                'type': 'crop'
            },
            'Carrot Seed': {
                'quantity': 0,
                'icon': '🥕',
                'type': 'seed'
            },
            'Carrot': {
                'quantity': 0,
                'icon': '🥕',
                'type': 'crop'
            },
            'Egg': {
                'quantity': 0,
                'icon': '🥚',
                'type': 'product'
            },
            'Milk': {
                'quantity': 0,
                'icon': '🥛',
                'type': 'product'
            },
            'Chicken Feed': {
                'quantity': 0,
                'icon': '🫘',
                'type': 'stock'
            },
        }

    def print_inventory(self):
        for item_name in self.list:
            item = self.list[item_name]
            if item['quantity'] > 0: print(f'> {item['icon']} {item_name}: {item['quantity']}')

    def print_sellable_items(self):
        for item_name in self.list:
            item = self.list[item_name]
            if item['type'] in ['crop', 'product'] and item['quantity'] > 0: 
                print(f'> {item['icon']} {item_name}: {item['quantity']}')

# === End of Inventory Class ===


# === Start of Farm Class ===
class Farm:
    def __init__(self):
        self.size = 3
        self.field = [['No seed' for _ in range(self.size)] for _ in range(self.size)]
        self.field_detail = [['' for _ in range(self.size)] for _ in range(self.size)]
        self.field_day = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def update_field(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.field_detail[row][col] == '': continue
                self.field_day[row][col] += 1
                if self.field_day[row][col] == seeds.list[self.field_detail[row][col]]['grow_time']:
                    self.field[row][col] = seeds.list[self.field_detail[row][col]]['icon']

    def print_field(self):
        print(f'> 🌽 Current field size: {self.size} x {self.size}\n')
        for row in self.field:
            count = 0
            for col in row:
                count += 1
                if col == 'No seed': print(f'{col:^9}', end='')
                else: print(f'{col:^8}', end='')
                if count < self.size: print('|', end='')
            print()
        print()

    def plant_seed(self, row, col, seed_name):
        if self.field_detail[row][col] == '':
            self.field_detail[row][col] = seed_name
            self.field[row][col] = '🌱'
            print(f'> 🌱 {seed_name} planted successfully!')
            return True

        print('> 🌱 There is already a seed in this field.')
        return False

    def harvest(self):
        crops = {
            'Corn': 0,
            'Potato': 0,
            'Tomato': 0,
            'Carrot': 0
        }

        for row in range(self.size):
            for col in range(self.size):
                seed_name = self.field_detail[row][col]
                if seed_name == '': continue
                seed = seeds.list[seed_name]
                if self.field_day[row][col] >= seed['grow_time']:
                    self.field[row][col] = 'No seed'
                    self.field_detail[row][col] = ''
                    self.field_day[row][col] = 0
                    crop_name = seed_name.replace(' Seed', '')
                    inventory.list[crop_name]['quantity'] += 1
                    crops[crop_name] += 1

        return crops

# === End of Farm Class ===


# === Start of Seeds Class ===

class Seeds:
    def __init__(self):
        self.list = {
            'Corn Seed': {
                'code': 1,
                'icon': '🌽',
                'grow_time': 3,
                'unlocked': True 
            },
            'Potato Seed': {
                'code': 2,
                'icon': '🥔',
                'grow_time': 4,
                'unlocked': False
            },
            'Tomato Seed': {
                'code': 3,
                'icon': '🍅',
                'grow_time': 4,
                'unlocked': False
            },
            'Carrot Seed': {
                'code': 4,
                'icon': '🥕',
                'grow_time': 3,
                'unlocked': False
            }
        }


    def count(self):
        count = 0
        for seed_name in self.list:
            seed = self.list[seed_name]
            if seed['unlocked'] == True: count += 1
        return count

    def print_seeds_list(self):
        print('> 🌱 List of unlocked seed(s):')
        print('-' * 80)

        count = 0
        for seed_name in self.list:
            seed = self.list[seed_name]
            if seed['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {seed['icon']} {seed_name}: {inventory.list[seed_name]['quantity']} seed(s) left.')

        print()

# === End of Seeds Class ===


# === Start of Market Item Class ===

class MarketItems:
    def __init__(self):
        self.list = {
            'Corn Seed': {
                'icon': '🌽',
                'price': 25,
                'unlocked': True
            },
            'Potato Seed': {
                'icon': '🥔',
                'price': 45,
                'unlocked': False
            },
            'Tomato Seed': {
                'icon': '🍅',
                'price': 60,
                'unlocked': False
            },
            'Carrot Seed': {
                'icon': '🥕',
                'price': 45,
                'unlocked': False
            },
            'Chicken': {
                'icon': '🐔',
                'price': 120,
                'unlocked': True
            },
            'Cow': {
                'icon': '🐄',
                'price': 180,
                'unlocked': True
            },
            'Chicken Feed': {
                'icon': '🫘',
                'price': 15,
                'unlocked': True
            }
        }

# === End of Market Item Class ===


# === Start of Market Class ===

class Market:
    def __init__(self):
        self.buy = Buy()
        self.sell = Sell()

# === End of Market Class ===



# === Start of Buy (Market) Class ===

class Buy:
    def __init__(self): pass

    def show_items(self):
        print('-' * 80)
        print(f'{'🏪 Buy Item 🏪':^80}')
        print('-' * 80)
        print(f'You currently have {stats.coin} 🪙')
        print('-' * 80)

        print('> 🌽 List of available item(s):')
        print('-' * 80)

        count = 0
        for item_name in market_items.list:
            item = market_items.list[item_name]
            if item['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {item['icon']} {item_name}: {item['price']} 🪙')

        print('-' * 80)
        return count

    def get_item(self, index):
        count = 0
        for item_name in market_items.list:
            item = market_items.list[item_name]
            if item['unlocked'] == False: continue
            count += 1
            if count == index:
                return item_name, item

        return False, False

# === End of Buy (Market) Class ===


# === Start of Sell (Market) Class ===

class Sell:
    def __init__ (self): # Adjust the random price
        self.list = {
            'Corn': {
                'icon': '🌽',
                'price': random.randint(45, 55)
            },
            'Potato': {
                'icon': '🥔',
                'price': random.randint(45, 55)
            },
            'Tomato': {
                'icon': '🍅',
                'price': random.randint(45, 55)
            },
            'Carrot': {
                'icon': '🥕',
                'price': random.randint(45, 55)
            },
            'Egg': {
                'icon': '🥚',
                'price': random.randint(45, 55)
            },
            'Milk': {
                'icon': '🥛',
                'price': random.randint(45, 55)
            }
        }

    def update_price(self):
        for item_name in self.list:
            self.list[item_name]['price'] = random.randint(45, 55)

    def print_price(self):
        count = 0
        for item_name in self.list:
            item = self.list[item_name]
            count += 1
            print(f'> {count}. {item['icon']} {item_name}: {item['price']} 🪙')

        return count

    def get_item(self, index):
        count = 0
        for item_name in self.list:
            item = self.list[item_name]
            count += 1
            if count == index:
                return item_name, item

        return False, False


# === End of Sell (Market) Class ===

# User Instances
stats = UserStats()
inventory = Inventory()

# Farm Instances
farm = Farm()
seeds = Seeds()

# Barn Instances
chicken_barn = ChickenBarn()
cow_barn = CowBarn()

# Market Instances
market = Market()
market_items = MarketItems()

# === Start of Farm Menu ===

def farm_menu():
    print('-' * 80)
    print(f'{'🌽 Farm 🌽':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80)
    print('1. Plant Seed 🌱')
    print('2. Harvest 🌾')
    print('3. Back to Main Menu 👈')

    print('-' * 80)

    choice = input('> Enter menu number: ')

    if choice not in ['1', '2', '3']:
        print('> ❗ Invalid option!\n')
        return

    if choice in ['1', '2']: cls()

    if choice == '1': farm_plant_menu()
    elif choice == '2': farm_harvest_menu()
    else:
        print('-' * 80)
        return

# === End of Farm Menu ===

# === Start of Farm Plant Menu ===

def farm_plant_menu():
    print('-' * 80)
    print(f'{'🌱 Plant Seed 🌱':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80 + '\n')

    seeds.print_seeds_list()

    seed_count = 0
    for seed_name in seeds.list:
        seed = seeds.list[seed_name]
        if seed['unlocked'] == True: seed_count += inventory.list[seed_name]['quantity']

    if seed_count == 0:
        print('> 🌱 There are no seeds left to be planted. You can buy them at the market.')
        print('-' * 80)
        return

    valid = False
    while valid is False:
        choice = input('> ❓ Do you want to plant any seed? (y/n): ').lower()
        try:
            if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
            if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')
            valid = True
        except ValueError as e:
            print(str(e))

    print()

    if choice == 'n': return

    valid = False
    while valid is False:
        seed_code = input('> 🌱 Enter seed code number: ')
        try:
            if seed_code == '': raise ValueError('> ❗ Seed code may not be empty!\n')
            if not seed_code.isnumeric(): raise ValueError('> ❗ Seed code must be a number!\n')

            seed_code = int(seed_code)

            if seed_code < 1 or seed_code > seeds.count(): raise ValueError('> ❗ Invalid seed code!\n')

            if seed_code == 1: seed_name = 'Corn Seed'
            elif seed_code == 2: seed_name = 'Potato Seed'
            elif seed_code == 3: seed_name = 'Tomato Seed'
            elif seed_code == 4: seed_name = 'Carrot Seed'

            if inventory.list[seed_name]['quantity'] == 0: raise ValueError(f'> ❗ There are no {seed_name} left to be planted. You can buy them at the market.\n')
            # seed_code = seed_code
            valid = True

        except ValueError as e:
            print(str(e))

    print()

    valid = False
    while valid is False:
        row = input('> 🌱 Enter row number: ')
        try:
            if row == '': raise ValueError('> ❗ Row number may not be empty!\n')
            if not row.isnumeric(): raise ValueError('> ❗ Row number must be a number!\n')
            row = int(row)
            if row < 1 or row > farm.size: raise ValueError('> ❗ Invalid row number!\n')
            row -= 1
            valid = True
        except ValueError as e:
            print(str(e))

    print()

    valid = False
    while valid is False:
        col = input('> 🌱 Enter column number: ')
        try:
            if col == '': raise ValueError('> ❗ Column number may not be empty!\n')
            if not col.isnumeric(): raise ValueError('> ❗ Column number must be a number!\n')
            col = int(col)
            if col < 1 or col > farm.size: raise ValueError('> ❗ Invalid column number!\n')
            col -= 1
            valid = True
        except ValueError as e:
            print(str(e))

    print()

    valid = farm.plant_seed(row, col, seed_name)
    print('-' * 80)

    if valid:
        inventory.list[seed_name]['quantity'] -= 1
        print()
        farm.print_field()
        print('-' * 80)

# === End of Farm Plant Menu ===


# === Start of Farm Harvest Menu ===

def farm_harvest_menu():
    print('-' * 80)
    print(f'{'🌾 Harvest 🌾':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80)

    harvestable_count = 0

    for row in range(farm.size):
        for col in range(farm.size):
            if farm.field_detail[row][col] == '': continue
            if farm.field_day[row][col] >= seeds.list[farm.field_detail[row][col]]['grow_time']:
                harvestable_count += 1

    if harvestable_count == 0:
        print('> 🌾 There are no crops to be harvested')
        print('-' * 80)
        return

    print(f'> 🌾 There are {harvestable_count} crops to be harvested')
    input('> 🌽 Press any key to harvest all...')

    print('-' * 80)

    crop_quantity = farm.harvest()

    for crop_name in crop_quantity:
        seed_name = crop_name + ' Seed'
        if crop_quantity[crop_name] > 0: print(f'> {seeds.list[seed_name]['icon']} You harvested {crop_quantity[crop_name]} {crop_name}')

    print('-' * 80)

# === End of Farm Harvest Menu ===


# === Start of End Day Function ===

def end_day():
    print(f'\n> 🌙 End of Day {stats.day}')
    stats.next_day()
    print(f'> 🌞 Start of Day {stats.day}')
    print('-' * 80)

    farm.update_field()

    stats.check_progress()

    dead_chicken = chicken_barn.update_status()
    if dead_chicken > 0:
        print(f'> 🐔 Oh, no! {dead_chicken} chicken(s) died today. Remember to feed your animals!')
        print('-' * 80)

    dead_cow = cow_barn.update_status()
    if dead_cow > 0:
        print(f'> 🐄 Oh, no! {dead_cow} cow(s) died today. Remember to feed your animals!')
        print('-' * 80)

# === End of End Day Function ===


# === Start of Market Menu ===

def market_menu():
    print('-' * 80)
    print(f'{'🏪 Market 🏪':^80}')
    print('-' * 80)

    print('> 1. Buy 🌽')
    print('> 2. Sell 🪙')
    print('> 3. Back to Main Menu 👈')

    print('-' * 80)

    valid = False

    while valid is False:
        choice = input('> Enter menu number: ')

        try:
            if choice not in ['1', '2', '3']:
                raise ValueError('> ❗ Invalid option!\n')
            valid = True
        except ValueError as e:
            print(str(e))

    if choice in ['1', '2']: cls()

    if choice == '1': market_buy_menu()
    elif choice == '2': market_sell_menu()
    else:
        print('-' * 80)
        return

# === End of Market Menu ===


# === Start of Market Buy Menu ===

def market_buy_menu():
    itemCount = market.buy.show_items()

    valid = False

    while valid is False:
        choice = input('> Enter item code that you want to buy: ')

        try:
            if choice == '': raise ValueError('> ❗ Item code may not be empty!\n')
            if not choice.isnumeric(): raise ValueError('> ❗ Item code must be a number!\n')

            choice = int(choice)

            if choice < 1 or choice > itemCount: raise ValueError('> ❗ Invalid item code!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    valid = False

    while valid is False:
        quantity = input('> Enter quantity: ')

        try:
            if quantity == '': raise ValueError('> ❗ Quantity may not be empty!\n')    
            if not quantity.isnumeric(): raise ValueError('> ❗ Quantity must be a number!\n')

            quantity = int(quantity)
            if quantity < 1: raise ValueError('> ❗ Quantity must be at least 1!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    print()

    item_name, item = market.buy.get_item(choice)

    if item_name == False:
        print('> ❗ There is no such item in the market!')
    else:
        total_price = item['price'] * quantity

        possible_to_buy = stats.expense(total_price)

        if possible_to_buy == False:
            print('> ❗ You do not have enough coin to buy this item!')
        else:
            if item_name in ['Chicken', 'Cow']: 
                for i in range (quantity):
                    chicken_name = input('> 🐔 What do you want to name?: ').title()
                    chicken_barn.add_animal(Chicken(chicken_name))

            else: 
                inventory.list[item_name]['quantity'] += quantity

            print(f'> 💰 You bought {quantity} {item['icon']} {item_name} for {total_price} 🪙')

    print()

# === End of Market Buy Menu ===


# === Start of Market Sell Menu ===

def market_sell_menu():
    print('-' * 80)
    print(f'{"Sales Price":^80}')
    print('-' * 80)
    item_count = market.sell.print_price()
    print('-' * 80)

    valid = False
    while valid == False:
        choice = input('> ❓ Do you want to sell items (y/n)? ').lower()

        try:
            if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
            if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')

            valid = True

        except ValueError as e:
            print(str(e))
    print()
    print()
    if choice == 'y':
        print('-' * 80)
        print('> 📦 Items in Inventory:')
        inventory.print_sellable_items()
        print('-' * 80)

        valid = False

    while valid is False:
        choice = input('> Enter item code that you want to sell: ')

        try:
            if choice == '': raise ValueError('> ❗ Item code may not be empty!\n')
            if not choice.isnumeric(): raise ValueError('> ❗ Item code must be a number!\n')

            choice = int(choice)

            if choice < 1 or choice > item_count: raise ValueError('> ❗ Invalid item code!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    valid = False

    while valid is False:
        quantity = input('> Enter quantity: ')

        try:
            if quantity == '': raise ValueError('> ❗ Quantity may not be empty!\n')    
            if not quantity.isnumeric(): raise ValueError('> ❗ Quantity must be a number!\n')

            quantity = int(quantity)
            if quantity < 1: raise ValueError('> ❗ Quantity must be at least 1!\n')

            valid = True

        except ValueError as e:
            print(str(e))

    print()

    item_name, item = market.sell.get_item(choice)
    print(f'item name {item_name}')
    print("qty", inventory.list[item_name]['quantity'])
    if inventory.list[item_name]['quantity'] - quantity < 0:
        print('> ❗ You do not have enough of this item in your inventory!')
    else:
        total_price = item['price'] * quantity
        inventory.list[item_name]['quantity'] -= quantity
        stats.profit(total_price)
        print(f'> 💰 You sold {quantity} {item["icon"]} {item_name} for {total_price} 🪙')

    print()

# === End of Market Sell Menu ===


# === Start of Show Inventory Function ===

def show_inventory():
    print('-' * 80)
    print(f'{'📦 Inventory 📦':^80}')
    print('-' * 80)
    inventory.print_inventory()
    print('-' * 80)

# === End of Show Inventory Function ===


# === Start of Statistics Menu ===
def statistics():
    print('-' * 80)
    print(f'{'📊 Statistics 📊':^80}')
    print('-' * 80)

    print(f'> 📅 Day: {stats.day}')
    print(f'> 🪙 Coins: {stats.coin}')
    print()

    print('> 💰 Financial State:')
    print('-' * 80)
    for day in stats.financial:
        data = stats.financial[day]
        print(f'🌞 Day {day}')
        print(f'🟩 Profit: {data['Profit']}')
        print(f'🟥 Expense: {data['Expense']}')
        print('-' * 80)
# === End of Statistics Menu ===

# === Start of Barn Menu ===
def barn_menu():
    print('-' * 80)
    print(f'{'🐮🐔 Barn 🐔🐮':^80}')
    print('-' * 80)

    print('1. Chicken Barn 🐔')
    print('2. Cow Barn 🐮')
    print('3. Back to Main Menu 👈')

    print('-' * 80)

    choice = input('> Enter menu number: ')

    if choice not in ['1', '2', '3']:
        print('> ❗ Invalid option!\n')
        return

    if choice in ['1', '2']: cls()

    if choice == '1': chicken_barn_menu()
    elif choice == '2': cow_barn_menu()
    else:
        print('-' * 80)
        return
# === End of Barn Menu ===

# === Start of Chicken Barn Menu ===
def chicken_barn_menu():
    print('-' * 80)
    print(f'{'🐔 Chicken Barn 🐔':^80}')
    print('-' * 80)

    chicken_barn.show_chickens()

    if len(chicken_barn.animals) == 0: return

    print('1. Feed Chicken 🍚')
    print('2. Collect Egg 🥚')
    print('3. Go back to Main Menu 👈')

    print('-' * 80)

    valid = False

    while valid is False:
        choice = input('> Enter menu number: ')
        try:
            if choice == '': raise ValueError('> ❗ Menu number may not be empty!\n')
            if choice not in ['1', '2', '3']:
                raise ValueError('> ❗ Invalid option!\n')
            valid = True
        except ValueError as e:
            print(str(e))

    if choice == '1':
        cls()
        print('-' * 80)
        print(f'{'🐔 Chicken Barn 🐔':^80}')
        print('-' * 80)
        count_chicken = chicken_barn.show_chickens()
        print('-' * 80)
        print(f'You have {inventory.list['Chicken Feed']['quantity']} Chicken Feed left')
        
        valid = False
        while valid is False:
            choice = input('Do you want to feed all chickens (y/n)? ')
            try:
                if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
                if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')
                valid = True
            except ValueError as e:
                print(str(e))

        if choice == 'y':
            if inventory.list['Chicken Feed']['quantity'] - count_chicken < 0: print("You don't have enough chicken feed!")
            else:
                for index in range(1, count_chicken+1):
                    chicken_barn.feed_animals(index)
                inventory.list['Chicken Feed']['quantity'] -= count_chicken
                print('-' * 80)
                print('> 🐔 You fed all chickens!')

        elif choice == 'n':
            valid = False
            while valid is False:
                choice = input('Do you want to feed some of the chickens (y/n)? ')
                try:
                    if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
                    if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')
                    valid = True
                except ValueError as e:
                    print(str(e))

            if choice == 'y':
                valid = False
                while valid is False:   
                    index = input('> Enter the index of the chicken you want to feed (single line seperated by space): ').split()

                    try:
                        if index == '': raise ValueError('> ❗ Index may not be empty!\n')
                        for i in index:
                            if not i.isnumeric(): raise ValueError('> ❗ Index must be a number!\n')
                            num = int(i)
                            if num < 1 or num > count_chicken: raise ValueError('> ❗ Invalid index!\n')

                        valid = True
                    except ValueError as e:
                        print(str(e))
                        
                if inventory.list['Chicken Feed']['quantity'] - len(index) < 0: 
                    print("You don't have enough chicken feed!")
                else:
                    for i in index:
                        chicken_barn.feed_animals(int(i))
                    inventory.list['Chicken Feed']['quantity'] -= len(index)
                    print(f'> {len(index)} chicken has been fed!')

            elif choice == 'n':
                print('-' * 80)
        
    elif choice == '2':
        egg = chicken_barn.collect_egg()
        print('-' * 80)
        if egg == 0: print('> 🥚 There are no eggs that are ready to be collected...')
        else: print(f'> 🥚 You collected {egg} eggs!')
        print('-' * 80)
    else:
        print('-' * 80)
        return
# === End of Chicken Barn Menu ===

# === Start of Cow Barn Menu ===
def cow_barn_menu():
    print('-' * 80)
    print(f'{'🐮 Cow Barn 🐮':^80}')
    print('-' * 80)

    cow_barn.show_cows()

    if len(cow_barn.animals) == 0: return

    print('1. Feed Cow 🍚')
    print('2. Collect Milk 🥛')
    print('3. Go back to Main Menu 👈')

    print('-' * 80)

    valid = False

    while valid is False:
        choice = input('> Enter menu number: ')
        try:
            if choice not in ['1', '2', '3']:
                raise ValueError('> ❗ Invalid option!\n')
            valid = True
        except ValueError as e:
            print(str(e))

    if choice == '1':
        cow_barn.feed_animals()
        print('-' * 80)
        print('> 🍚 Cow feeded!')
        print('-' * 80)
    elif choice == '2':
        milk = cow_barn.collect_milk()
        print('-' * 80)
        if milk == 0: print('> 🥛 There are no milk that are ready to be collected...')
        else: print(f'> 🥛 You collected {milk} milk!')
        print('-' * 80)
    else:
        print('-' * 80)
        return
# === End of Cow Barn Menu === 


if __name__ == '__main__':
    while True:
        cls()

        print('-' * 80)
        print(f'{'🌽 Welcome to PyFarm 🌽':^80}')
        print('-' * 80)
        print(f'Coins: {stats.coin} 🪙')
        print(f'Day: {stats.day}')
        print('-' * 80)

        print('> 1. Farm 🌽')
        print('> 2. Barn 🐮')
        print('> 3. End the Day (Go to Next Day) 🌙')
        print('> 4. Market 🏪')
        print('> 5. Inventory 📦')
        print('> 6. Statistic 📊')
        print('> 7. Exit ⛔')

        print('-' * 80)

        choice = input('> Enter menu number: ')

        if choice in ['1', '2', '4', '5', '6']: cls()

        if choice == '1':
            farm_menu()
        elif choice == '2':
            barn_menu()
        elif choice == '3':
            end_day()
        elif choice == '4':
            market_menu()
        elif choice == '5':
            show_inventory()
        elif choice == '6':
            statistics()
        elif choice == '7':
            print('> Thank you for playing 🎉\n')
            break
        else:
            print('Invalid option!')

        input('> Press any key to continue...')
