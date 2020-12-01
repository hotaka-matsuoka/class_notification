from flask import Flask, request, abort
import os
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

# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["LINE_BOT_CHANNEL_TOKEN"]
# YOUR_CHANNEL_SECRET = os.environ["LINE_BOT_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def send_message(period, subject, classroom, info):
    text_content = f"おはようございます!\n【本日の時間割】\n {period}限 : {subject}\n {classroom}\n {info}"
    message = TextSendMessage(text=text_content)
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
    class_info_ary = scrapy()
    class_info = class_info_ary[0]
    period = class_info[0]
    subject = class_info[1]
    classroom = class_info[2]
    info = class_info[3]
    send_message(period, subject, classroom, info)
