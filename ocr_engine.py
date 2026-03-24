from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text(image_path):
    result = ocr.ocr(image_path, cls=True)

    lines = []

    for line in result:
        for word in line:
            text = word[1][0]
            lines.append(text)

    return lines   
