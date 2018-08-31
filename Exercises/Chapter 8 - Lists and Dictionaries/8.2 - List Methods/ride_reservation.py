
riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '5':
    if user_input == '1':  # Add rider 
        name = input('Enter name:').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        print('FIXME: Add new VIP')
        name = input('Enter name:').strip().lower()
        line.insert(num_vips, name)
        # Add new rider behind last VIP in line
        # Hint: Insert the VIP into the line at position num_vips.
        #Don't forget to increment num_vips.

    elif user_input == '3':  # Dispatch ride
        print('FIXME: Remove riders from the front of the line.')
        line.pop(0)
        if(num_vips > 0):
            num_vips -=1
        # Remove last riders_per_ride from front of line.
        # Don't forget to decrease num_vips, if necessary.

    elif user_input == '4':  # Print riders waiting in line
        print('%d person(s) waiting:' % len(line), line)

    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
    print(user_input)