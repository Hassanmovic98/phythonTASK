while True:
    print("Welcome to Nokia 3310")
    print("""
       1. Phone Book
       2. Messages
       3. Chat
       4. Call Register
       5. Tones
       6. Settings
       7. Call Divert
       8. Games
       9. Calculator
       10. Reminder
       11. Clock
       12. Profiles
       13. Sim Services
       0. Exit
    """)
    menu_choice = input("Choose between 0 - 13: ")

    if menu_choice == "0":
        print("switch off,bye!")
        break

    elif menu_choice == "1":
        while True:
            print("""
            phonebook
            1. Search
            2. Service Nos
            3. Add Name
            4. Erase
            5. Edit
            6. Assign Tone
            7. Send B Card
            8. Options
            9. Speed Dials
            10. Voice Tags
            0. Back
            """)
            choice = input("Choose 0 - 10: ")
            if choice == "0":
                break
            print(f"You choosed: {choice}")

    elif menu_choice == "2":
        while True:
            print("""
            MESSAGES
            1. Write Messages
            2. Inbox
            3. Outbox
            4. Picture Message
            5. Templates
            6. Smileys
            7. Message Settings
            8. Info Services
            9. Voice Mailbox Number
            10. Service Command Editor
            0. Back
            """)
            choice = input("Choose 0 - 10: ")
            if choice == "0":
                break
            print(f"You choosed: {choice}")

    elif menu_choice == "3":
        while True:
            print("chat\n0. Back")
            choice = input("Enter choice: ")
            if choice == "0":
                break
            print("You choosed Chat")

    elif menu_choice == "4":
        while True:
            print("""
            call register
            1. Missed Calls
            2. Received Calls
            3. Dialled Numbers
            4. Erase Recent Call List
            5. Show Call Duration
            6. Show Call Costs
            7. Prepaid Credit
            0. Back
            """)
            choice = input("Choose 0 - 7: ")
            if choice == "0":
                break
            print(f"You choosed: {choice}")

    elif menu_choice == "5":
        while True:
            print("""
            tones
            1. Ringing Tone
            2. Ringing Volume
            3. Incoming Call Alert
            4. Composer
            5. Message Alert Tone
            6. Keypad Tones
            7. Warning And Game Tones
            8. Vibrating Alert
            9. Screen Saver
            0. Back
            """)
            choice = input("Choose 0 - 9: ")
            if choice == "0":
                break
            print(f"You choosed: {choice}")

    elif menu_choice == "6":
        while True:
            print("""
            SETTINGS
            1. Call Settings
            2. Phone Settings
            3. Security Settings
            4. Restore Factory Settings
            0. Back
            """)
            choice = input("Choose 0 - 4: ")
            if choice == "0":
                break
            print(f"You choosed: {choice}")

    elif menu_choice == "7":
        while True:
            print("""
		   call divert
		   1. Call Divert
		   0. Back
		""")
            choice = input("Choose 0 - 1: ")
            if choice == "0":
                break
            print("You choosed: Call Divert")

    elif menu_choice == "8":
        while True:
            print("""
		   games
		   1.games
		   0. Back
			""")
            choice = input("Choose 0 - 1: ")
            if choice == "0":
                break
            print("You choosed: Games")

    elif menu_choice == "9":
        while True:
            print("CALCULATOR\n1. Calculator\n0. Back")
            choice = input("Choose 0 - 1: ")
            if choice == "0":
                break
            print("You selected: Calculator")

    elif menu_choice == "10":
        while True:
            print("""
		  reminder
		  1.Reminder
		  0. Back""")
            choice = input("Choose 0 - 1: ")
            if choice == "0":
                break
            print("You selected: Reminder")

    elif menu_choice == "11":
        while True:
            print("""
            clock
            1. Alarm Clock
            2. Clock Settings
            3. Date Settings
            4. Stopwatch
            5. Countdown Timer
            6. Auto Update of Date and Time
            0. Back
            """)
            choice = input("Choose 0 - 6: ")
            if choice == "0":
                break
            print(f"You choosed: {choice}")

    elif menu_choice == "12":
        while True:
            print("""
		profile
		1.profiles
		0. Back
		""")
            choice = input("Choose 0 - 1: ")
            if choice == "0":
                break
            print("You choosed: Profiles")

    elif menu_choice == "13":
        while True:
            print("""sim services
		   1. SIM Services
		   0. Back""")
            choice = input("Choose 0 - 1: ")
            if choice == "0":
                break
            print("You choosed: SIM Services")

    else:
        print("Invalid choice. Try again.")

   