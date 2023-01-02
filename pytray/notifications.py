import logging
import os
from winotify import Notification, audio

username = os.getlogin()
icon_path = fr"C:\Users\{username}\Documents\PyTray\pytray\images\icon.png"
app_name = "PyTray"


def about():
    try:
        about_toast = Notification(app_id=app_name,
                                   title="PyTray",
                                   msg="Dev in Python by @ASJordi",
                                   duration="short",
                                   icon=icon_path)

        about_toast.set_audio(audio.Default, loop=False)
        about_toast.add_actions(label="Website", launch="https://asjordi.dev")

        about_toast.show()
    except Exception as e:
        logging.error(e)
