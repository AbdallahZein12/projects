from app.amazon import Amazon

with Amazon.from_patcher() as bot: 
    # bot.land_first_page()
    bot.lookup(keywords="Leather Jackets Men",start_page=1, end_page=1,strict=True)
    print("Exiting...")

