from booking.booking import Booking
try:
    with Booking() as bot: 
        bot.land_first_page()
        bot.change_currency(currency="U.S. Dollar")
        bot.select_place_to_go("Egypt")
        bot.select_dates(check_in_date="26 July 2023",check_out_date="4 September 2023")
        bot.select_adults(adults=5,children=3,ages=[5,6,12],rooms=3)
        bot.click_search()
        bot.apply_filtration()
        bot.refresh()
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
    