import csv
import re
import numpy as np
import time
from pytube import YouTube
from tqdm import tqdm

with open("links.csv", 'r') as links:
    csv_reader = csv.reader(links)
    for link in tqdm(links, total=86):

        vid_link = YouTube(link)
        # print(f"vid_link:  {vid_link}\n\n")

        streams = vid_link.streams.filter(file_extension="mp4")
        # print(f"streams:  {streams}\n\n")

        available_resolutions = [re.findall('\d+|$', str(stream))[2] for stream in streams]
        # print(f"available_resolutions:  {available_resolutions}\n\n")

        # max_resolution_index = np.asarray(available_resolutions).argmax()
        # print(f"max_resolution_index:  {max_resolution_index}\n\n")

        itags = [re.findall('\d+|$', str(stream))[0] for stream in streams]
        # print(f"itags:  {itags}\n\n")

        vid_link.streams.get_by_itag(itags[np.asarray(available_resolutions).argmax()]).download()

        time.sleep(300)

