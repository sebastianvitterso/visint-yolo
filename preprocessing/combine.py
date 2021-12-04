import cv2
import numpy as np

INPUT_FOLDER = './data/input'
OUTPUT_FOLDER = './data/output'

# for VIDEO_NUMBER in range(0,1): # If you only want to run one
for VIDEO_NUMBER in range(19): # If you want to run all videos
    BASE_FILENAME = f'Video{VIDEO_NUMBER:05}'
    AMBIENT_FILEPATH =   f'{INPUT_FOLDER}/{BASE_FILENAME}_ambient.avi'
    INTENSITY_FILEPATH = f'{INPUT_FOLDER}/{BASE_FILENAME}_intensity.avi'
    RANGE_FILEPATH =     f'{INPUT_FOLDER}/{BASE_FILENAME}_range.avi'

    ambientCapture = cv2.VideoCapture(AMBIENT_FILEPATH)
    intensityCapture = cv2.VideoCapture(INTENSITY_FILEPATH)
    rangeCapture = cv2.VideoCapture(RANGE_FILEPATH)

    assert ambientCapture.isOpened(), 'Error: ambientCapture'
    assert intensityCapture.isOpened(), 'Error: intensityCapture'
    assert rangeCapture.isOpened(), 'Error: rangeCapture'

    SHOW_VIDEO = True

    frameNum = 0

    # Read until video is completed
    while(ambientCapture.isOpened() and intensityCapture.isOpened() and rangeCapture.isOpened()):
        aSuccess, aFrame = ambientCapture.read()
        iSuccess, iFrame = intensityCapture.read()
        rSuccess, rFrame = rangeCapture.read()

        if not (aSuccess and iSuccess and rSuccess):
            break
        
        outputFrame = aFrame.copy()
        outputFrame[:, :, 1] = iFrame[:, :, 1]
        outputFrame[:, :, 2] = rFrame[:, :, 2]

        path = f'{OUTPUT_FOLDER}/{VIDEO_NUMBER:02}{frameNum:03}.JPG'
        success = cv2.imwrite(path, outputFrame)
        assert success, f'imwrite failed: {path}'

        if SHOW_VIDEO:
            # Display the resulting frame
            cv2.imshow('Output', outputFrame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        frameNum += 1


    # When everything done, release the video capture object
    ambientCapture.release()
    intensityCapture.release()
    rangeCapture.release()

    # Closes all the frames
    cv2.destroyAllWindows()

