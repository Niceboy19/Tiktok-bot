import os
import requests
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        data = request.get_json()
        message = data.get("message", {})
        chat_id = message.get("chat", {}).get("id")
        text = message.get("text", "")

        if text:
            username = text.replace("@", "").strip()
            reply = get_tiktok_info(username)
            send_message(chat_id, reply)

        return "ok"
    return "Bot is running!"

def send_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

def get_tiktok_info(username):
    return f"👤 اسم المستخدم: {username}\n📊 المتابعين: 120K\n❤️ الإعجابات: 1.1M\n📄 الوصف: (بيانات وهمية)"

if __name__ == "__main__":
    app.run()
