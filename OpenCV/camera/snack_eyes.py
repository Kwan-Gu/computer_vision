import cv2
from skimage.metrics import structural_similarity

from copy import copy

x0 = 200
x1 = 440
y0 = 200
y1 = 280

threshold = 0.9

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


def draw_bbox(mode: str, frame, x0: int, x1: int, y0: int, y1: int, score: float = 0.):
    if mode == "normal":
        color = (0, 255, 0)
        sentence = "Detect Area"
    else:
        color = (0, 0, 255)
        sentence = "Snack Detected!"
    cv2.rectangle(frame, (x0, y0), (x1, y1), color, thickness=2)
    cv2.putText(frame, f"{sentence}\nScore: {score:.2f}",
                (x1 + 5, y1), 0, 0.3, color)


def detect_change(prev_frame, frame, x0: int, x1: int, y0: int, y1: int):
    gray_prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)[y0:y1, x0:x1]
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)[y0:y1, x0:x1]
    mssim = structural_similarity(gray_prev_frame, gray_frame)
    return mssim


i = 0
while cv2.waitKey(100) < 0:
    detected = False
    if i == 0:
        ret, frame = capture.read()
        draw_bbox("normal", frame, x0, x1, y0, y1)
    else:
        prev_frame = copy(frame)
        ret, frame = capture.read()
        similarity_score = detect_change(prev_frame, frame, x0, x1, y0, y1)
        if similarity_score >= threshold:
            mode = "normal"
        else:
            mode = "detect"
        draw_bbox(mode, frame, x0, x1, y0, y1, score=similarity_score)
    cv2.imshow("Snack Eyes", frame)
    i += 1

capture.release()
cv2.destroyAllWindows()
