import cv2
from pedestrian_detection_ssdlite import api


video = cv2.VideoCapture('pedestrian_video.mp4')

while True:
    (read_successful, frame) = video.read()

    if read_successful is not True:
        break

    bbox_list = api.get_person_bbox(frame, thr=0.6)
    print(bbox_list)

    for i in bbox_list:

        cv2.rectangle(frame, i[0], i[1], (125, 255, 51), thickness=2)
        cv2.putText(frame, 'Person', (i[0][0], i[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (36,255,12), thickness=2)
    
    cv2.imshow('Pedestrain detector ', frame)

    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

video.release()

