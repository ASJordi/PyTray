import sys
import pystray
import PIL.Image
import os
import logging
import notifications  # Path: notifications.py

username = os.getlogin()


def main():
    image = PIL.Image.open(fr'C:\Users\{username}\Documents\PyTray\pytray\images\icon.png')

    logging.basicConfig(filename=fr'C:\Users\{username}\Documents\PyTray\pytray\logs\main.log', level=logging.INFO, format='%(message)s %(asctime)s',
                        datefmt='%m/%d/%Y %I:%M:%S')
    logging.info("Started pytray")

    icon = pystray.Icon("PyTray", image, "PyTray", menu=pystray.Menu(
        pystray.MenuItem('About', notifications.about),
        pystray.MenuItem('Exit', on_quit)
    ))

    icon.run()
    pass


def on_quit(icon):
    try:
        logging.info("Exited pytray")
        icon.stop()
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()

if sys.executable.endswith("pythonw.exe"):
    sys.stdout = open(os.devnull, "w")
    sys.stderr = open(os.path.join(os.getenv("TEMP"), "stderr-" + os.path.basename(sys.argv[0])), "w")
