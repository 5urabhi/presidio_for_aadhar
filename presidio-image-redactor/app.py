"""REST API server for image redactor."""
import logging
import os

from PIL import Image
from flask import Flask, request, jsonify, Response

from presidio_image_redactor import ImageRedactorEngine
from presidio_image_redactor.entities import InvalidParamException
from presidio_image_redactor.entities.api_request_convertor import (
    get_json_data,
    image_to_byte_array,
    color_fill_string_to_value,
)

DEFAULT_PORT = "3000"

WELCOME_MESSAGE = r"""
 _______  _______  _______  _______ _________ ______  _________ _______
(  ____ )(  ____ )(  ____ \(  ____ \\__   __/(  __  \ \__   __/(  ___  )
| (    )|| (    )|| (    \/| (    \/   ) (   | (  \  )   ) (   | (   ) |
| (____)|| (____)|| (__    | (_____    | |   | |   ) |   | |   | |   | |
|  _____)|     __)|  __)   (_____  )   | |   | |   | |   | |   | |   | |
| (      | (\ (   | (            ) |   | |   | |   ) |   | |   | |   | |
| )      | ) \ \__| (____/\/\____) |___) (___| (__/  )___) (___| (___) |
|/       |/   \__/(_______/\_______)\_______/(______/ \_______/(_______)
"""


class Server:
    """Flask server for image redactor."""

    def __init__(self):
        self.logger = logging.getLogger("presidio-image-redactor")
        self.app = Flask(__name__)
        self.logger.info("Starting image redactor engine")
        self.engine = ImageRedactorEngine()
        self.logger.info(WELCOME_MESSAGE)

        @self.app.route("/health")
        def health() -> str:
            """Return basic health probe result."""
            return "Presidio Image Redactor service is up"

        @self.app.route("/redact", methods=["POST"])
        def redact():
            """Return a redacted image."""
            params = get_json_data(request.form.get("data"))
            color_fill = color_fill_string_to_value(params)
            image_file = request.files.get("image")

            print(image_file.show())
            if not image_file:
                raise InvalidParamException("Invalid parameter, please add image data")
            im = Image.open(image_file)

            redacted_image = self.engine.redact(im, color_fill)

            img_byte_arr = image_to_byte_array(redacted_image, im.format)
            print("yes")
            return Response(img_byte_arr, mimetype="application/octet-stream")

        @self.app.errorhandler(InvalidParamException)
        def invalid_param(err):
            self.logger.warning(
                f"failed to redact image with validation error: {err.err_msg}"
            )
            return jsonify(error=err.err_msg), 422

        @self.app.errorhandler(Exception)
        def server_error(e):
            self.logger.error(f"A fatal error occurred during execution: {e}")
            return jsonify(error="Internal server error"), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", DEFAULT_PORT))
    server = Server()
    server.app.run(host="0.0.0.0", port=port)