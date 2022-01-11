import pytchat
import time
import datetime

# PytchatCoreオブジェクトの取得
# force_replay=True は対象URLがアーカイブの場合つけるとよい
livechat = pytchat.create(video_id = "nNKg8nHG9Fc", force_replay=True)
comment_list = []
while livechat.is_alive():
    # チャットデータの取得
    chatdata = livechat.get()
    for c in chatdata.items:
        # datetimeよりelapsedTimeで動画の時間指定のほうがよさそう
        comment_list.append(f"{c.datetime}, {c.message}")
    time.sleep(0.1)

start_time = datetime.datetime(2021, 1, 30, 15, 43)
end_time = datetime.datetime(2021, 1, 30, 18, 38)
check_time_front = start_time
check_time_back = start_time + datetime.timedelta(minutes = 1)
while check_time_front < end_time:
    comment_count = 0
    check_time_front += datetime.timedelta(minutes = 1)
    check_time_back += datetime.timedelta(minutes = 1)
    for c in comment_list:
        comment_datetime = c.split(", ")
        chat_time = datetime.datetime.strptime(comment_datetime[0], '%Y-%m-%d %H:%M:%S')
        if check_time_front <= chat_time <= check_time_back:
            comment_count += 1
            continue
        elif check_time_back < chat_time:
            break
    if comment_count > 0:
        print("時刻: " + str(check_time_front) + ", コメント数: " + str(comment_count))