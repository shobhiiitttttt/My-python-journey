# You cna also create if elif ladder using multiple conditions of
# elif.j
# @ For understanding solve this questionj
# @ take the input of temperature in celsiusX
# @ Below 0°C → "Freezing Cold b
# @ 0°C to 10°C → "Very Cold b
# @ 10°C to 20°C → "Cold b
# @ 20°C to 30°C → "Pleasant b
# @ 30°C to 40°C → "Hot b
# @ Above 40°C → "Very Hot "
# Some Questions on Conditional

# answer

t = int(input("What is the temperature outside :- "))

if t < 0:
    print("Freezing Cold")
elif t >=0 and t<10:
    print("Very Cold")
elif t >=10 and t<20:
    print("Cold")
elif t >=20 and t<30:
    print("Pleasant")
elif t >=30 and t<40:
    print("Hot")
else:
    print("Very Hot")