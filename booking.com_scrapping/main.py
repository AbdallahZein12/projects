from booking.booking import Booking
import time
from PIL import Image
import os

try:
    print("\033[25l",end='')
    print("\033[31m",end='')
    os.system('cls')
    with Image.open('logo.png') as im:
        im = im.convert('L')
        im = im.resize((210,20))
        chars = '.:-=+*#%@'
        for y in range(im.size[1]):
            time.sleep(0.05)
            for x in range(im.size[0]):
                gray = im.getpixel((x,y))
                char = chars[gray * len(chars) // 355]
                
                print(char,end='')
            print()

    print("\033[0m",end='')
    print("\033[?25h",end='')
    print()
    print()
    
    with Booking() as bot: 
        bot.land_first_page()
        bot.change_currency(input("Currency (Format: U.S. Dollar)> ").strip())
        bot.select_place_to_go(input("Location> ").strip())
        bot.select_dates(check_in_date=input("Check in Date (Format: 26 July 2023)> ").strip(),check_out_date=input("Check out Date (Format: 26 July 2023)> ").strip())
        adults = input("Num of Adults> ").strip()
        children = int(input("Num of Children> "))
        if children > 0:
            ages = [input("Age of Child (Up to 17)> ").strip() for i in range(children)]
        else:
            ages = []
                
        bot.select_adults(adults=adults,children=children,ages=ages,rooms=input("Num of Rooms> "))
        bot.click_search()
        bot.apply_filtration()
        time.sleep(15)
        bot.report_results()
except Exception as e:
    if "needs to be in PATH" in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
    