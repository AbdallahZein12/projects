from app.amazon import Amazon

with Amazon.from_patcher() as bot: 
    bot.land_first_page()
    
    print("Exiting...")

