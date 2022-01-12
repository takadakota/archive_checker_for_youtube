import pytchat
import time
import datetime

# is_alive()でコメント欄を動的な状態に保っていったん欲しいデータをlistに入れる、それを処理で加工する
# force_replay=True は対象URLがアーカイブの場合つけるとよい
livechat = pytchat.create(video_id = "F4SKZ6bR7f0", force_replay=True)
elapsedTime_list = []
comment_list = []
while livechat.is_alive():
    # チャットデータの取得
    chatdata = livechat.get()
    for c in chatdata.items:
        elapsedTime_list.append(c.elapsedTime)
        comment_list.append(c.message)
    time.sleep(0.1)
# 時刻だけのdatetime型を定義、動画の終了時刻は手入力が必要。また日付部分は必須なので適当に22年元旦とする、この日付はこのあとの処理で見ないようにする
start_time = datetime.datetime(2022, 1, 1, 0, 0, 0)
end_time = datetime.datetime(2022, 1, 1, 2, 4, 0)
check_time_front = start_time
check_time_back = check_time_front + datetime.timedelta(minutes = 1)
first_flg = True
while check_time_front < end_time:
    comment_count = 0
    # while文最初のループは任意の時間ずらしを入れない
    if first_flg:
        first_flg = False
    else:
        check_time_front += datetime.timedelta(minutes = 1)
        check_time_back += datetime.timedelta(minutes = 1)
    for elapsedTime in elapsedTime_list:
        # pytchatで取得したelapsedTimeは文字列なので%H:%M:%S型でdatetimeで整形する必要がある
        if len(elapsedTime) == 4:
            chat_time_repair = "00:0" + elapsedTime
            chat_time = datetime.datetime.strptime(chat_time_repair, '%H:%M:%S')
        elif len(elapsedTime) == 5:
            # 待機枠のコメントは配信開始直前のものは-0:09みたいな感じで保存されてるぽいので、うまく処理する必要がある。
            if "-" in elapsedTime:
                elapsedTime = elapsedTime.replace("-", "0")
                chat_time_repair = "00:" + elapsedTime
                chat_time = datetime.datetime.strptime(chat_time_repair, '%H:%M:%S')
            else:
                chat_time_repair = "00:" + elapsedTime
                chat_time = datetime.datetime.strptime(chat_time_repair, '%H:%M:%S')
        elif len(elapsedTime) == 7:
            chat_time_repair = "0" + elapsedTime
            chat_time = datetime.datetime.strptime(chat_time_repair, '%H:%M:%S')
        else:
            chat_time = datetime.datetime.strptime(elapsedTime, '%H:%M:%S')
        # time型で比較する
        if check_time_front.time() <= chat_time.time() <= check_time_back.time():
            comment_count += 1
            continue
        elif check_time_back < chat_time:
            break
    if comment_count > 0:
        print("動画時間: " + str(check_time_front).split(" ")[1] + "〜" + str(check_time_back).split(" ")[1] + ", コメント数: " + str(comment_count))
    print("コメント総数: " + str(len(comment_list)))