johnPorkHouseCoord = (-1020303, 1230405)
townCoord = (123456, 654321)
empireStateBuildingCoord = (40.748817, -73.985428)
newYorkCityCoord = (40.712776, -74.005974)
torontoCoord = (43.651070, -79.347015)
parisCoord = (48.856613, 2.352222)


while True:

   ChooseLocation = input("What coordinates would you like to visit? The locations are: John Pork's House, The Town, The Empire State Building, New York City, Toronto, and Paris. ").lower()

   if ChooseLocation == "john pork's house":
      print(f"You have chosen to visit John Pork's House, which is located at {johnPorkHouseCoord}.")
      break
   elif ChooseLocation == "the town":
      print(f"You have chosen to visit The Town, which is located at {townCoord}.")
      break
   elif ChooseLocation == "the empire state building":
      print(f"You have chosen to visit The Empire State Building, which is located at {empireStateBuildingCoord}.")
      break
   elif ChooseLocation == "new york city":
      print(f"You have chosen to visit New York City, which is located at {newYorkCityCoord}.")
      break
   elif ChooseLocation == "toronto":
      print(f"You have chosen to visit Toronto, which is located at {torontoCoord}.")
      break
   elif ChooseLocation == "paris":
      print(f"You have chosen to visit Paris, which is located at {parisCoord}.")
      break
   else:
      print("That is not a valid location. Please choose from the list provided or check your spelling and try again.") 
      