from PIL import Image, ImageFont, ImageDraw
import random

class InvalidFilePath(Exception):
    """Exception raised for invalid file paths."""

    def __init__(self, message="Invalid file path provided for image."):
        self.message = message
        super().__init__(self.message)

class MemeEngine:
    """Class to generate actual meme file."""

    def __init__(self, path):
        """Initiate meme engine with path where store produced meme files."""
        self.temp_dir = path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Gernerate Meme with given img, text, and author."""

        meme_path = f"{self.temp_dir}/meme_{random.randint(0, 10000)}.jpg"

        if width >= 500:
            width = 500
        try:
            # Open the image using PIL
            with Image.open(img_path) as image:  # = Image.open(img_path)
                # Resize the image to the specified width while preserving the aspect ratio
                height = int(width / image.width * image.height)
                image = image.resize((int(width), int(height)))
                # Set the font and font size
                font = ImageFont.truetype('C:\WINDOWS\FONTS\TIMES.TTF',size=int(image.height/20))
                # Create a draw object
                draw = ImageDraw.Draw(image)
                # Calculate the position to place the text
                max_x = image.width - font.getsize(text)[0]
                max_y = image.height - font.getsize(text)[1]
                text_x = random.randint(0, max_x)
                text_y = random.randint(0, max_y)
                # Draw the text on the image
                draw.text((text_x, text_y), text, font=font, fill="white")
                # Save the meme image
                image.save(meme_path)

        except IOError:
            raise InvalidFilePath("Invalid file path provided for image.")

        return meme_path
