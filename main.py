import multiprocessing
import webbrowser
import tkinter as tk
import uuid
from tkinter import filedialog
from video_converter import video_converter
from video_uploader import video_uploader

root = tk.Tk()
root.withdraw()


if __name__ == "__main__":

    file_path = filedialog.askopenfilename()
    file_id = uuid.uuid4().hex

    # creating converting processes
    converter_720p = multiprocessing.Process(target=video_converter(file_path, file_id, 720))
    converter_480p = multiprocessing.Process(target=video_converter(file_path, file_id, 480))
    converter_360p = multiprocessing.Process(target=video_converter(file_path, file_id, 360))
    converter_240p = multiprocessing.Process(target=video_converter(file_path, file_id, 240))

    # creating uploading processes
    upload_1080p = multiprocessing.Process(target=video_uploader(file_path, file_id, "1080"))
    upload_720p = multiprocessing.Process(target=video_uploader("output/"+file_id+"-720.mp4", file_id, "720"))
    upload_480p = multiprocessing.Process(target=video_uploader("output/" + file_id + "-480.mp4", file_id, "480"))
    upload_360p = multiprocessing.Process(target=video_uploader("output/" + file_id + "-360.mp4", file_id, "360"))
    upload_240p = multiprocessing.Process(target=video_uploader("output/" + file_id + "-240.mp4", file_id, "240"))

    # start process
    upload_1080p.start()        # upload 1080p video

    converter_720p.start()      # start video converting
    converter_480p.start()
    converter_360p.start()
    converter_240p.start()

    converter_720p.join()       # wait until converting process finish
    converter_480p.join()
    converter_360p.join()
    converter_240p.join()

    upload_720p.start()         # start upload remaining videos
    upload_480p.start()
    upload_360p.start()
    upload_240p.start()

    upload_1080p.join()         # wait finish all uploads
    upload_720p.join()
    upload_480p.join()
    upload_360p.join()
    upload_240p.join()
    

    url = "http://localhost:8888/lms/portal/upload_paid_lesson.php?id="+file_id 

    print(url) #print url
