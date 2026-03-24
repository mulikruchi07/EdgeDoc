# from RPLCD.i2c import CharLCD
# import time

# lcd = CharLCD('PCF8574', 0x27)

# def display_data(data):
#     lcd.clear()

#     for key, value in data.items():
#         lcd.write_string(f"{key}: {value}")
#         time.sleep(2)
#         lcd.clear()
def display_data(data):
    print("\n=== DISPLAY OUTPUT ===")
    for key, value in data.items():
        print(f"{key}: {value}")