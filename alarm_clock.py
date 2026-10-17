import time
from datetime import datetime

# Step 1:input alarm time by user
alarm_time = input("Alarm ka time enter karo (HH:MM:SS): ")

print("Alarm set ho gaya!")
print("Alarm Time:", alarm_time)

# Step 2:  check current time and compare with alarm time 
while True:

    # Get current time
    current_time = datetime.now().strftime("%H:%M:%S")

    # Show current time
    print("Current Time:", current_time)

    # Step 3: Check alarm time 
    if current_time == alarm_time:

        print("Wake Up! Alarm Baj Gaya!")
        
        break

    time.sleep(1)

print("Alarm Clock Program Band Ho Gaya!")