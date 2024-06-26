import pytesseract

from presidio_image_redactor import OCR


class TesseractOCR(OCR):
    """OCR class that performs OCR on a given image."""

    def perform_ocr(self, image: object) -> dict:
        """Perform OCR on a given image.

        :param image: PIL Image/numpy array or file path(str) to be processed

        :return: results dictionary containing bboxes and text for each detected word
        """
        output_type = pytesseract.Output.DICT
        print(output_type)
        return pytesseract.image_to_data(image, output_type=output_type)
