

place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input ("light a torch or proceed in the dark")
if action == "light a torch":
    print("You can see but attract bugs")
    if action == "proceed in the dark":
        print ("be careful where you walk")
    pass

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


def food ():
    return input("Would you like vegetarian? (yes/no): ")
print ("Veggie Delight Cater") if choice == "yes" else print ("Gourmet meals")
