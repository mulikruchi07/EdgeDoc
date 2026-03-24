from matplotlib import lines

from camera import capture_image
from preprocess import preprocess_image
from ocr_engine import extract_text
from extractor import extract_dynamic_fields, filter_important_fields
from button import wait_for_press
from display import display_data
import cv2
import os
os.environ['PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK'] = 'True'
def main():
    print("Starting system...")

    img_path = capture_image()

    processed = preprocess_image(img_path)
    cv2.imwrite("processed.jpg", processed)

    print("Running OCR...")
    lines = extract_text(img_path)
    lines = [l.replace(".", "").strip() for l in lines]

    print("\n--- OCR LINES ---")
    for l in lines:
        print(l)

    data = extract_dynamic_fields(lines)
    if data is None:
        data = {}
    data = filter_important_fields(data)

    print("\nExtracted Data:\n", data)

    wait_for_press()

    display_data(data)

if __name__ == "__main__":
    main()
