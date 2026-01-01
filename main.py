import random

print("======Welcome======")
print("Choose a room type to continue")

print("1.Standard")
print("2.Deluxe")
print("3.Suite")
print("4.Studio")

room_type = input()

if room_type == "Standard":
    print("Standard selected")
elif room_type == "Deluxe":
    print("Deluxe selected")
elif room_type == "Suite":
    print("Suite selected")
elif room_type == "Studio":
    print("Studio selected")
elif room_type == "1":
    room_type = "Standard"
    print("Standard selected")
elif room_type == "2":
    room_type = "Deluxe"
    print("Deluxe selected")
elif room_type == "3":
    room_type = "Suite"
    print("Suite selected")
elif room_type == "4":
    room_type = "Studio"
    print("Studio selected")
else:
    print("Please select a valid room type")
    exit()

print("Room size type")
print("1. Single")
print("2. Double")
print("3. Triple")

room_size = input()

if room_size == "Single":
    print("Single selected")
elif room_size == "Double":
    print("Double selected")
elif room_size == "Triple":
    print("Triple selected")
elif room_size == "1":
    room_size = "Single"
    print("Single selected")
elif room_size == "2":
    room_size = "Double"
    print("Double selected")
elif room_size == "3":
    room_size = "Triple"
    print("Triple selected")
else:
    print("Please select a valid room size type")
    exit()

print(f"Booked {room_size} and {room_type} type room")

number = random.randint(1, 300)
print(f"Here is the room number {number}")

secret_code = random.randint(2000000, 1000000000000)
print(f"Here is the secret code {secret_code}")

print("For more information check the link https://google.com")