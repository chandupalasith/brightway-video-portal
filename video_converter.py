import moviepy.editor as mp


def video_converter(file_path, file_id, video_quality):
    clip = mp.VideoFileClip(file_path)
    clip_resized = clip.resize(height=video_quality)
    clip_resized.write_videofile("output/" + file_id + "-" + str(video_quality) + ".mp4")
