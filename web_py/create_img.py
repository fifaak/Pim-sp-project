from PIL import Image, ImageDraw, ImageFont
import os

def create_marker_images():
    # Ensure the 'icons' directory exists
    os.makedirs('./icons', exist_ok=True)
    
    # Define marker names and colors
    markers = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4"]
    colors = {
        "A": "blue",
        "B": "red"
    }
    
    # Define the size of the icons
    size = (30, 30)

    for marker in markers:
        # Create an image with white background
        img = Image.new('RGBA', size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        # Draw a white circle
        draw.ellipse((0, 0, size[0], size[1]), fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))

        # Define the text and color
        text = marker
        color = colors[marker[0]]

        # Load a font
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except IOError:
            font = ImageFont.load_default()

        # Calculate text size and position
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)

        # Draw the text on the image
        draw.text(text_position, text, font=font, fill=color)

        # Save the image
        img.save(f'./icons/{marker}.png')

create_marker_images()
