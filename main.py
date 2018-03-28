# Assignment 1
# ICS3U
# <Qudrat Fazli>
# March 28, 2018

def CtoF (C):
    """Enter a temperature in celsius to recieve the same temperature in farenheight."""
    F = (1.8) * C + 32
    return F

def FtoC (F):
    """Enter a temperature in farenheight to recieve the same temperature in celsius."""
    C = (0.55556) * (F-32)
    return C

print('Enter 1 to convert a temperature to celsius and Enter 2 to convert a temperature to farenheight. Then enter the temperature to convert.')
choice = int(input())
temperature = int(input('now enter temperature:'))
if choice == 1 and temperature >= -273.15:
    print(CtoF(temperature))
elif choice == 2 and temperature >= -459.67:
    print(FtoC(temperature))
else:
    print('Please enter a temperature value > -273.15 if trying to convert celsius to farenheit and a temperature value > -459.67 to convert farenheight to celsius. Also enter either 1 to 2 for your choice.')
    

