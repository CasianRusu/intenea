import cv2
import numpy as np
import pyautogui


def screen(length, height):
    screen_resolution = (length, height)
    return screen_resolution


def fourcc():
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    return fourcc


def output(fps, screen_size):
    out = cv2.VideoWriter("output.mp4", fourcc(), fps, (screen_size))
    return out


def start_recording(seconds, fps, outting):
    final_seconds = seconds * fps
    count_seconds = 0
    print("The video recording has started")
    while True:
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        outting.write(frame)
        if count_seconds % fps == 0:
            print("Recording video...")
        count_seconds += 1
        if count_seconds == final_seconds:
            print("The video recording has finished!")
            break


def end_recording(out):
    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()


def video_recording_script():
    frame_per_second = 17
    minutes_in_seconds = 25
    resolution = screen(1920, 1080)
    fourcc()
    out_put = output(frame_per_second, resolution)
    start_recording(minutes_in_seconds, frame_per_second, out_put)
    end_recording(out_put)
