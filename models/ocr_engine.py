import easyocr
import cv2

reader = easyocr.Reader(['en'])

def extract_text(image_path):

    image = cv2.imread(image_path)

    texts = []

    rotations = [
        image,
        cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE),
        cv2.rotate(image, cv2.ROTATE_180),
        cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    ]

    for img in rotations:

        result = reader.readtext(
            img,
            paragraph=True,
            detail=0
        )

        text = " ".join(result)

        texts.append(text)

    best_text = max(
        texts,
        key=len
    )

    return best_text