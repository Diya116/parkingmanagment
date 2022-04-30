import cv2
import pickle

width, height = 107, 48

try:

    with open('CarParkPos', 'rb') as f:
        position = pickle.load(f)
except:
    position = []






def mouseclick(event,x,y,flags,parameters):
    if event == cv2.EVENT_LBUTTONDOWN:
        position.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:

        for i, pos in enumerate(position):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                position.pop(i)
    with open('CarParkPos', 'wb') as f:
        pickle.dump(position, f)

while True:
    img = cv2.imread('carParkImg.png')

    for pos in position:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 3)


    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image", mouseclick)
    cv2.waitKey(1)
