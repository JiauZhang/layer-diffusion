from glob import glob
from tqdm import tqdm
import cv2

images = glob('images/*.png')
for image in tqdm(images):
    data = cv2.imread(image)
    h, w = data.shape[:2]
    if w > 512:
        scale = w / 512
        h = int(h / scale)
        data = cv2.resize(data, (512, h))
        cv2.imwrite(image, data)
