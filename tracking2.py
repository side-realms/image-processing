import cv2
import os

mov = './video.mp4'
template = './ball.png'
output = './video_out.mp4'


def judge_match(frame, template):
    result = cv2.matchTemplate(frame, template, cv2.TM_CCORR_NORMED)
    h, w = template.shape[:2]
    # マッチング結果を類似度最小、最大、最小の座標、最大の座標
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
 
    if 0.80<maxVal:
        cv2.rectangle(frame, (maxLoc[0], maxLoc[1]), (maxLoc[0]+w, maxLoc[1]+h), (0, 255, 0) )

    return frame

def save_sec_interval(mov, template, video):
    template = cv2.imread(template)
    tmp_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    _, tmp_binary = cv2.threshold(tmp_gray, 0, 255, cv2.THRESH_OTSU)


    mov = cv2.VideoCapture(mov)
    fps = mov.get(cv2.CAP_PROP_FPS)
    frame = mov.get(cv2.CAP_PROP_FRAME_COUNT)
    len_sec = round(frame / fps)
    width = int(mov.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(mov.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v') # コーデックの指定
    video = cv2.VideoWriter('video_out.mp4', fourcc, fps,(width, height), True)

    while True:
        check, frame = mov.read()
        if not check:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        #cv2.imwrite('result/'+ str(i) +'pk.png', binary)
        new_frame = judge_match(frame, template)

        video.write(new_frame)

save_sec_interval(mov, template, output)
