from chatgpt.chatgpt import ChatGpt

def default_login(email,password):
    with ChatGpt() as bot:
        bot.land_first_page()
        result = bot.default_login(email,password)
        return result
        