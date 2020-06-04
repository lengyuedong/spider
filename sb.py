import cv2
import os

if not os.path.exists('./output'):
    os.makedirs('./output')

for root, dirs, files in os.walk("./images"):
    for file in files:
        aa = (root + '\\' + file)
        bk_img = cv2.imread(aa)
        cv2.putText(bk_img, file[:-4], (300, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imwrite("./output" + '\\' + file, bk_img)

print('complete')
