import csv
import pytube
from pytube import YouTube
from tqdm import tqdm

with open("links.csv", 'r') as links:
    csv_reader = csv.reader(links)

    for idx, link in enumerate(tqdm(links, total=86)):

        try:

            vid = YouTube(link)
            vid.streams \
                .filter(progressive=True, file_extension="mp4") \
                .get_highest_resolution() \
                .download(output_path="vids_n_trans", filename=str(idx))
            try:
                srt = YouTube(link).captions["en"].generate_srt_captions()
            except KeyError as trans_error:
                print("no transcription available for ", link)
                srt = "no transcription available for this video"
                idx = str(idx) + "_not"
            with open("vids_n_trans/" + str(idx) + ".txt", 'w+') as transcription:
                transcription.write(vid.title + '\n')
                transcription.write(link + '\n')
                transcription.write(srt)
                transcription.close()

        except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable) as lol:
            print("pytube error", lol, '\n')
            continue

links.close()

