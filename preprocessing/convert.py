import imageio
import os, sys

class TargetFormat(object):
    GIF = ".gif"
    MP4 = ".mp4"
    AVI = ".avi"

def convertFile(inputpath, targetFormat):
    """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
    outputpath = os.path.splitext(inputpath)[0] + targetFormat
    print("converting\r\n\t{0}\r\nto\r\n\t{1}".format(inputpath, outputpath))

    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']
    fps /= 3

    writer = imageio.get_writer(outputpath, fps=fps)
    for i,im in enumerate(reader):
        sys.stdout.write("\rframe {0}".format(i))
        sys.stdout.flush()
        writer.append_data(im)
    print("\r\nFinalizing...")
    writer.close()
    print("Done.")

convertFile("D:/visint-yolo/runs/detect/video7-uda-AIR/Video00007_combined.avi", TargetFormat.GIF)
# convertFile("D:/visint-yolo/data/LiDAR-videos/Video00017_Ano/Video00017_ambient.avi", TargetFormat.GIF)
# convertFile("D:/visint-mm/Video00001_pred/ambient01.avi", TargetFormat.GIF)