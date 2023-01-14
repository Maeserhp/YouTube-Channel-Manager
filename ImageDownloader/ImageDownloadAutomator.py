from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging
import csv
import os
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sourceDir = r"D:\MassProduction\Downloads"
destDir = r"D:\MassProduction\Images"
artistName = ""
websiteName = ""
artistHandel = ""


# supported image types
imageExtensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

class MoverHandler(FileSystemEventHandler):
    count = 1

    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # ? .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(sourceDir) as entries:
            for entry in entries:
                name = entry.name
                self.CheckImageFiles(entry, name)

    def CheckImageFiles(self, entry, name):  # * Checks all Image Files
        for imageExtension in imageExtensions:
            if name.endswith(imageExtension) or name.endswith(imageExtension.upper()):
                oldName = f'{sourceDir}\{entry.name}'
                newName = f'{destDir}\{artistName}-{websiteName}-{artistHandel}-{self.count}{imageExtension}'
                os.rename(oldName, newName)
                logging.info(f"Moved image file: {name}")
                self.count = self.count +1

# ! NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sourceDir
    artistName = input("Input the Artists Name:")
    websiteName = input("Input the Website Name:")
    artistHandel = input("Input the Artists Handel:")
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
