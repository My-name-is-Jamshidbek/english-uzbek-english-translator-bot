# ✨ English–Uzbek Translator Bot 🤖🌐

Welcome to your brand-new **Telegram translation wizard**! With a sprinkle of Python magic and Aiogram sorcery, this bot effortlessly flips your text between English and Uzbek—faster than you can say “abracadabra”! 🪄


## 🛠️ Features & Spells

- 🗣️ **Two-Way Translation**  
  - **English → Uzbek**  
  - **Uzbek → English**

- 🔄 **Inline & Reply Keyboards**  
  Pick your direction with a tap—no fumbling for commands!

- 🧩 **State Management**  
  Powered by Aiogram’s FSM to keep track of your translation quests.

- 💾 **Persistent History**  
  Every phrase you translate is saved in a cozy SQLite den (`botbaza.db`).

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/My-name-is-Jamshidbek/english-uzbek-english-translator-bot.git
cd english-uzbek-english-translator-bot
```

### 2. Set Up Virtual Environment
```bash
python3.11 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

1. Create a `config.py` in the project root:

   ```python
   # config.py
   BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
   ```

2. (Optional) Tinker with **Pytesseract** settings if you dare to add image-to-text magic! 🧙‍♂️

---

## ▶️ Usage

Fire up your translation genie:

```bash
python main.py
```

Then in Telegram:

1. Tap **“Translate English→Uzbek”** or **“Translate Uzbek→English”** ✍️  
2. Send your sentence.  
3. 🪄 Watch it transform—and check your saved history whenever you like!

---

## 📁 Project Structure

```
.
├── data/                # 📂 Static assets (images, docs…)
├── app.py               # 🚀 Launches the Aiogram executor
├── loader.py            # 🤖 Bot & dispatcher setup
├── config.py            # 🔑 Your secret token + settings
├── states.py            # 📊 FSM state definitions
├── main.py              # 🔗 Handler registration & entrypoint
├── inlinebuttons.py     # 📱 Inline keyboard layouts
├── replybuttons.py      # 📲 Reply keyboard layouts
├── translator.py        # 🌐 Google Translate & OCR logic
├── baza.py              # 🗃️ SQLite database operations
├── botbaza.db           # 🗄️ Your translation history
└── requirements.txt     # 📦 Python dependencies
```

---

## 🤝 Contributing

We love new wizards in the circle! 🎉 Please open an issue or PR to:

- Add more language pairs 🌏  
- Enhance error-handling 🛡️  
- Integrate caching or rate-limiting ⚡  

Happy translating! ✨📝  