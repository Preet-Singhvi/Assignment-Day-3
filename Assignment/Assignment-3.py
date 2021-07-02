altitude = int(input("Enter the Altitude of the plane:"))
if altitude <= 1000:
    print("Safe to land")
elif 1000 < altitude <= 5000:
    print("Bring down to 1000")
else:
    print("Turn around")