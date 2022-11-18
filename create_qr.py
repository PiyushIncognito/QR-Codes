import os
import cv2
import numpy as np
import qrcode

FOLDER = 'qr_dataset'

if not os.path.isdir(FOLDER):
    os.mkdir(FOLDER)

for data in np.random.choice(np.arange(1000, 10000), size=2500, replace=False):
    for version in [1, 2, 3, 4]:
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color='black', back_color='white')
        img = np.float32(np.asarray(img)) * 255
        img = np.dstack((img, img, img))

        cv2.imwrite(os.path.join(FOLDER, f"{data}-v{version}.png"), img)

