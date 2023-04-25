from booking.booking import Booking
import time
try:
    with Booking() as bot: 
        bot.land_first_page()
        bot.change_currency(input("Currency (Format: U.S. Dollar)> "))
        bot.select_place_to_go(input("Location> "))
        bot.select_dates(check_in_date=input("Check in Date (Format: 26 July 2023)> "),check_out_date=input("Check out Date (Format: 4 September 2023)> "))
        adults = input("Num of Adults> ")
        children = int(input("Num of Children> "))
        if children > 0:
            ages = [input("Age of Child (Up to 17)> ") for i in range(children)]
        else:
            ages = []
                
        bot.select_adults(adults=adults,children=children,ages=ages,rooms=input("Num of Rooms> "))
        bot.click_search()
        bot.apply_filtration()
        bot.refresh()
        time.sleep(5)
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
    