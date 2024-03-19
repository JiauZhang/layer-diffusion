from glob import glob
import cv2

images = glob('image/*.png')
for image in images:
    data = cv2.imread(image)
    h, w = data.shape[:2]
    if w > 512:
        scale = w / 512
        h = int(h / scale)
        data = cv2.resize(data, (512, h))
        cv2.imwrite(image, data)
