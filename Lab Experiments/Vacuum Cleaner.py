# Vacuum Cleaner Problem

def vacuum_cleaner(room_a, room_b, location):
    print("Initial State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Location:", location)
    print()

    if location == 'A':
        if room_a == 'Dirty':
            print("Room A is dirty. Cleaning Room A.")
            room_a = 'Clean'

        print("Moving to Room B.")
        location = 'B'

    if location == 'B':
        if room_b == 'Dirty':
            print("Room B is dirty. Cleaning Room B.")
            room_b = 'Clean'

    print("\nFinal State:")
    print("Room A:", room_a)
    print("Room B:", room_b)

    if room_a == 'Clean' and room_b == 'Clean':
        print("Both rooms are clean!")


vacuum_cleaner('Dirty', 'Dirty', 'A')
