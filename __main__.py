from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            print("Catch : " + filename)
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)


folder_to_track = "/Users/theov/Desktop/1"
folder_destination = "/Users/theov/Desktop/2"
eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler, folder_to_track, recursive=True)
observer.start()

for filename in os.listdir(folder_to_track):
    print("Catch : " + filename)
    src = folder_to_track + "/" + filename
    new_destination = folder_destination + "/" + filename
    os.rename(src, new_destination)


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()

