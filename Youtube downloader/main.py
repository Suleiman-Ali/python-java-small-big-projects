from pytube import YouTube

url = ""
video = YouTube(url)
astrek = "*"*30
print(astrek + " Video Title " + astrek)
print(video.title)
print(astrek + " Video resolution " + astrek)
print(video.streams.get_highest_resolution().resolution)
video.streams.get_highest_resolution().download("C:/Users/lenovo/videos")
