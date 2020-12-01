import os
import date
import schedule
import time
from flask import Flask, request, abort
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

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["LINE_BOT_CHANNEL_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["LINE_BOT_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def send_message(list):
    content = f"{date.month}月{date.day}日({date.day_of_week}) おはようございます!\n\n【 本日の時間割 】\n"
    for l in list:
        content += f"{l[0]}限 : {l[1]}\n {l[2]}\n {l[3]}\n\n"
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    # app.run()
    # port = int(os.getenv("PORT"))
    # app.run(host="0.0.0.0", port=port)

    def start():
        # if date.day_of_week == "水" or date.day_of_week == "日":
        #     pass
        # else:
        class_info_ary = scrapy()
        send_message(class_info_ary)

    schedule.every().day.at("22:50").do(start)
    while True:
        schedule.run_pending()
        time.sleep(1)