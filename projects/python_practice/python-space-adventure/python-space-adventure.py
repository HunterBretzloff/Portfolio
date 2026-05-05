# print image.
print(''' 
                .          .          .      
          .          .                  .          .
    .          .              .                 .
             _________          _          .
   .        |         |      _.-"-._               .
            |_________|    .'       '.      .
    .      _|         |_  /           \\                .
          | |_________| | |           |       .
   .      | |         | | \\          /            .
          |_|_________|_|  '.       .'                     .
            |         |      '._.-'._
    .       |_________|          |   '-._          .
            |         |          |       '                .
  ------------------------------------------------------------
''')

# print introduction.
print("Welcome to the Juno Deep-Space Sector.")
print("Your mission is to recover the Lost Star Core.")
choice = input(' "Your ship is low on fuel at a cosmic fork. Where do you steer?" Type "left" or "right": ').lower()

# start adventure / get users input
if choice == "left":
    choice = input(
        'You’ve entered the rings of a gas giant. The Juno Station is in sight.\n Type "wait" to engage the tractor beam. Type "drift" to use your thrusters and fly across\n ').lower()

    if choice == "wait":
        # Using a new variable name for the door to keep the logic clean
        door = int(input('You dock at the station safely. There is a corridor with three airlocks.\n Airlock 1 is "Red" | Airlock 2 is "Yellow" | Airlock 3 is "Blue"\n Which airlock do you enter? (Type 1, 2, or 3):\n'))

        if door == 1:
            print("The airlock malfunctions and vents you into a Supernova. Game Over!")
        elif door == 2:
            print("The vault opens! You’ve recovered the Star Core. Mission Accomplished, Commander!")
        elif door == 3:
            print("You enter a dark bay full of Hive-Mind Aliens. Game Over!")
        else:
            print("You entered a ghost code. The station self-destructs. Game Over!")

    elif choice == "drift":
        print('You get caught in a Space-Slug swarm! "Game Over!"')
    else:
        print("Your navigation computer glitched. You drifted into a Black Hole. Game Over!")

elif choice == "right":
    print('You flew straight into an Asteroid Belt. "Game Over!"')
else:
    print("Invalid coordinates. Your ship ran out of oxygen in deep space. Game Over!")