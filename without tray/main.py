import os

File = "alarms.txt"


def main():
    while True:
        
        print("\nAlarm Management System")
        print("1. Set Alarm")
        print("2. View Alarms")
        print("3. Delete Alarm")
        print("4. Exit")
        choice = input("Enter your choice: ")
        # clear the cmd terminal
        os.system("cls" if os.name == "nt" else "clear")

        if choice == "1":
            set_alarm()
        elif choice == "2":
            # reading from the file and displaying alarms
            alarms = view_alarms()
            if alarms:
                print("Current Alarms:")
                for i, alarm in enumerate(alarms, start=1):
                    print(f"{i}. {alarm.strip()}")
            else:
                print("No alarms set.")
        elif choice == "3":
            delete_alarm()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def view_alarms():
    # returning in the form of a list
    if not os.path.exists(File):
        print("No alarms set.")
        return

    with open(File, "r") as f:
        alarms = f.readlines()
    return alarms


def delete_alarm():
    
    alarms = view_alarms()
    if not alarms:
        return
    # displaying the alarms to the user for deletion
    print("Select an alarm to delete:")
    for i, alarm in enumerate(alarms, start=1):
        print(f"{i}. {alarm.strip()}")

    alarm_to_delete = input("Select the alarm number to delete (eg 1,2 or all): ")
    # if the user wants to delete all alarms
    if alarm_to_delete.lower() == "all":
        with open(File, "w") as f:
            f.write("")
            os.system("cls" if os.name == "nt" else "clear")
            print("All alarms deleted.")
            return

    # check if the input is a valid number and within the range of alarms
    if alarm_to_delete.isdigit() and 1 <= int(alarm_to_delete) <= len(alarms):
        del alarms[int(alarm_to_delete) - 1]
        with open(File, "w") as f:
            f.writelines(alarms)
        os.system("cls" if os.name == "nt" else "clear")
        print("Alarm deleted.")
        return
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Invalid alarm number.")
        return


def set_alarm():
    alarm_time = input("Enter the time for the alarm (HH:MM): ")
    # validate the time format and also account for missing 0 before single digit hours.
    if not validate_time_format(alarm_time):
        return

    # check if alarm already exists if not then append to the file
    with open(File, "r") as f:
        existing_alarms = f.readlines()
    if alarm_time + "\n" in existing_alarms:
        print("Alarm already set.")
        return

    with open(File, "a") as f:
        f.write(alarm_time + "\n")

    print("Alarm set.")


def validate_time_format(time_str):
    # print errors at each if below
    parts = time_str.split(":")
    if len(parts) != 2 or len(time_str) != 5:
        print("Time must be in HH:MM format.")
        return False

    hours, minutes = parts
    # account for missing 0 before single digit hours and minutes
    if len(hours) == 1 or len(minutes) == 1:
        print("Hours and minutes should be in two-digit format (e.g., 01:05).")
        return False
    # validate that hours and minutes are digits and within valid ranges
    if not (hours.isdigit() and minutes.isdigit()):
        print("Hours and minutes must be numeric.")
        return False
    if not (0 <= int(hours) < 24 and 0 <= int(minutes) < 60):
        print("Hours must be between 00 and 23, and minutes must be between 00 and 59.")
        return False
    return True


if __name__ == "__main__":
    main()
