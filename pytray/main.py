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
        pystray.MenuItem("Programs", pystray.Menu(
            pystray.MenuItem('Chrome', on_launch),
            pystray.MenuItem('Firefox', on_launch),
            pystray.MenuItem('Brave', on_launch),
            pystray.MenuItem('VS-Code', on_launch),
            pystray.MenuItem('Terminal', on_launch),
            pystray.MenuItem('Intellij', on_launch)
        )),
        pystray.MenuItem('About', notifications.about),
        pystray.MenuItem('Exit', on_quit)
    ))

    icon.run()
    pass


def on_launch(icon, item):
    try:
        if str(item) == "Chrome":
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            logging.info("Launched Chrome")
        elif str(item) == "Firefox":
            os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")
            logging.info("Launched Firefox")
        elif str(item) == "Brave":
            os.startfile(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
            logging.info("Launched Brave")
        elif str(item) == "VS-Code":
            os.startfile(fr"C:\Users\{username}\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            logging.info("Launched VS-Code")
        elif str(item) == "Terminal":
            os.startfile(fr"C:\Users\{username}\AppData\Local\Microsoft\WindowsApps\Microsoft.WindowsTerminal_8wekyb3d8bbwe\wt.exe")
            logging.info("Launched Terminal")
        elif str(item) == "Intellij":
            os.startfile(r"C:\Program Files\JetBrains\IntelliJ IDEA 2022.2\bin\idea64.exe")
            logging.info("Launched Intellij")
        else:
            logging.info("Not implemented yet")
    except Exception as e:
        logging.error(e)

        
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
