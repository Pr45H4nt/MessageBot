from core import MessageBoy

# Your Instagram Username and Password
username = 'your_instagram_username'
password = 'your_instagram_password'

# Create an instance with desired conversation mode
chat_bot = MessageBoy(username=username, password=password, mode='BestFriend')

# DM link of the target conversation
chat_bot.target_page = "https://www.instagram.com/direct/t/your_conversation_id"

# Run the bot
chat_bot.run()