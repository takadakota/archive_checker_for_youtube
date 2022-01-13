import pytchat
import time

chat = pytchat.create(video_id="nNKg8nHG9Fc")
while chat.is_alive():
    # チャットデータの取得
    chatdata = chat.get()
    for c in chatdata.items:
        print(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
        '''
        JSON文字列で取得:
        print(c.json())
        '''
    time.sleep(0.1)