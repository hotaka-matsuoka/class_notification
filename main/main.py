import date
import schedule
import time
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from settings import YOUR_CHANNEL_ACCESS_TOKEN, YOUR_CHANNEL_SECRET, USER_ID
from scrapy import scrapy

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///class_notification.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(7), nullable=False)
    password = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def send_message(list):
    content = f"{date.month}月{date.day}日({date.day_of_week}) おはようございます!\n\n【 本日の時間割 】\n"
    for dict in list:
        content += f"{dict['priod']}限 : {dict['subject']}\n {dict['classroom']}\n {dict['information']}\n\n"
    message = TextSendMessage(text=content)
    line_bot_api.push_message(USER_ID, message)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if ('@' in text) and (text.count('@')) == 2:
        user_information_dict = text.replace('@', '').split()
        student_id = user_information_dict[0]
        password = user_information_dict[1]
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"学籍番号とパスワードを登録しました\n学籍番号: {student_id}\nパスワード: {password}")
            )
        student_information = Student(student_id=student_id, password=password, user_id=event.source.userId)
        db.session.add(student_information)
        db.session.commit()


if __name__ == "__main__":
    app.run()
    # port = int(os.getenv("PORT"))
    # app.run(host="0.0.0.0", port=port)
    class_information_list = scrapy()
    if not len(class_information_list) == 0:
        send_message(class_information_list)
