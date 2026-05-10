inventory = ["sword", "axe", "bow", "dagger"]

print ("These are the things in your inventory:")
print (inventory)

equipped_weapon = "Fists" 

while True:

    chosen_item = input("Choose an item to equip: ").lower()

    if chosen_item in inventory:

        inventory.append(equipped_weapon)
    

        inventory.remove(chosen_item)
    
        before_equipped = equipped_weapon

        equipped_weapon = chosen_item
    
        print(f"You put away {before_equipped} and equipped the {equipped_weapon}!")
        print(f"Your inventory contains: {inventory}")

    else:
        print(f"The item, {chosen_item}, is not in your inventory.")
   