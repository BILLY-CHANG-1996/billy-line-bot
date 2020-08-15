from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('UuFC5fbqdgL67j393u+fCS9p1E+D7r4k/YXJre//MSE2DHdSUX2XEXPylVVyHQ92H5OKsaXoKO548DrfAluosEhV7afy1IrAD9aLovhPeWnGsiN8PoHjfkbNf/U6CgAGJ3BC/ZtBcGSpRRFUQu4h6gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2e4fc1cc109dbfb49cd9518122597af8')


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
    msg = event.message.text
    r = '人家聽不懂啦!講人話(怒'
    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒啦幹'
    elif msg == '請問你是處女嗎':
        r = '畜生變態色情狂去死吧'
        
        
        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))
    if '處女' in msg:
        sticker_message = StickerSendMessage(
            package_id='11538',
            sticker_id='51626518'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)


if __name__ == "__main__":
    app.run()