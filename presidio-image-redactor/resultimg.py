from PIL import Image
from presidio_image_redactor import ImageRedactorEngine,ImageAnalyzerEngine
# Get the image to redact using PIL lib (pillow)
image = Image.open(r"C:\Users\Anupam\Documents\presidio\aadhartest.jpg")
image.show()
Analyzer=ImageAnalyzerEngine()
# Initialize the engine
engine = ImageRedactorEngine()


# Redact the image with black color
redacted_image = engine.redact(image, (0, 0, 0))

# save the redacted image
redacted_image.save("new_image.png")
# uncomment to open the image for viewing
redacted_image.show()