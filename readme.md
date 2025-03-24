# MessageBot 🤖

Hey, welcome to **MessageBot**—your goofy Instagram DM pal! This lil’ bot can chat like your bestie, your boyfriend, or just some rando, depending on your mood. It’s not fancy, but it’s a total blast to mess around with! 

## What's This About? 🤔

MessageBot is a quirky side project that uses Playwright and some AI magic to handle your Instagram DMs. It takes screenshots of your chats, figures out what’s going on, and fires back replies in whatever style you pick—like “BestFriend” or “Boyfriend.” It’s a bit janky sometimes, but that’s part of the fun!

## Cool Stuff It Does ✨

- **Sneaks into Instagram** and watches your DMs.
- **Personality swap**: Pick from General, BestFriend, Boyfriend, and more!
- **AI chatter**: Tries to sound human (and sometimes nails it).
- **Screenshot skills**: Reads your convo to keep things rolling.
- **Make it yours**: Play with the prompts to tweak its vibe.

## What You’ll Need 🛠️

- **Python 3** (language)
- **Playwright** (for browser tricks)
- **Google Gemini API key** (the AI juice)
- **An Instagram account** (obviously!)

## Getting Started 🚀

1. **Grab the code**:
   ```
   git clone https://github.com/pr45h4nt/messagebot.git
   cd messagebot
   ```

2. **Load up the tools**:
   ```
   pip install playwright
   pip install google-generativeai
   pip install pillow
   ```
   or

   ```
   pip install -r requirements.txt
   ```


3. **Set up Playwright**:
   ```
   python -m playwright install
   ```

## Setting It Up 🛠️

### API Keys and Prompts

- There’s a `config.py` file with some starter prompts. Mess with ‘em—the crazier, the better!
- Pop your Gemini API key in there too:
  ```python
  GEMINI_API_KEY = "your-gemini-api-key"
  ```

### Main Script

Tweak `main.py` with your Instagram details and the chat you wanna hit up:
```python
from core import MessageBoy

# Your Instagram login stuff
username = 'your_instagram_username'
password = 'your_instagram_password'

# Pick a vibe (like 'BestFriend' or 'Boyfriend')
chat_bot = MessageBoy(username=username, password=password, mode='BestFriend')
# Add headless=False if you don't want the browser window

# The DM link you’re targeting
chat_bot.target_page = "https://www.instagram.com/direct/t/your_conversation_id"

# Hit play!
chat_bot.run()
```

## How to Play With It 🕹️

1. Fill out `main.py` with your info.
2. Kick it off:
   ```
   python main.py
   ```
3. Watch it go:
   - Logs into Instagram.
   - Jumps into your chat.
   - Waits for messages.
   - Fires back replies in your chosen style.

## What’s in the Box 📦

- **`main.py`**: Your control center.
- **`core.py`**: The guts of the bot.
- **`ai_response.py`**: Where the AI brain lives.
- **`config.py`**: Prompts and keys hang out here.

## Make It Your Own 🎨

### Change the Mood

Swap the `mode` in `main.py`:
```python
chat_bot = MessageBoy(username=username, password=password, mode='Boyfriend')
```

**Vibes to choose from**:
- `'General'` - Easygoing and chill.
- `'BestFriend'` - Your digital BFF.
- `'Boyfriend'` - Sweet and flirty.
- `'Girlfriend'` - More flirty goodness.
- `'CollegeFriend'` - That wild college buddy.

### Invent a New Vibe

Add your own in `config.py`:
```python
prompts = {
    # Other prompts...
    'Pirate': """
    Reply like a pirate, arrgh! Keep it salty, matey!
    """
}
```
**Hot tip**: Go nuts with prompts for maximum laughs! Make it as personalized as you can for the best responses.

## Logging 📝

It’ll spill all the details to the console and a `messageboy.log` file. If it acts weird, peek there.

## Heads Up! ⚠️

- This is purely for giggles—don’t get too serious with it.
- Instagram might squint at bots, so use it sneaky-like.
- Keep your login and API stuff hush-hush. Better if you hide it in 'env' file and load it from there.

## Troubleshooting 🛠️

- **No replies?** Check your chat link.
- **Talking nonsense?** Fiddle with the prompts.
- **Won’t log in?** Double-check your creds.

## Little Disclaimer 🙃

MessageBot is just a silly toy, not a pro tool. Have fun, but don’t cry to us if Instagram gets mad or your DMs turn awkward. You’re on your own, buddy!

---
