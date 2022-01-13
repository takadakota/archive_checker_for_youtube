import pytchat
import time

chat = pytchat.create(video_id="nNKg8nHG9Fc")
while chat.is_alive():
    print(chat.get().json())
    time.sleep(5)
    '''
    # Each chat item can also be output in JSON format.
    for c in chat.get().items:
        print(c.json())
    '''