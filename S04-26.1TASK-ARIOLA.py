from datetime import datetime

first = input("First name: ").strip()
last = input("Last name: ").strip()
section = input("Section: ").strip()
event = input("Event name: ").strip()

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

name = (first + " " + last).title()
date_obj = datetime(year, month, day)

print("Name:", name)
print("Name Code:", name.upper())
print("Section:", section.upper())
print("Event:", event.title())
print("Event Date:", date_obj.strftime("%B %d, %Y"))
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")