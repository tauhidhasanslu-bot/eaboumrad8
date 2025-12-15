import base64
from PIL import Image
from io import BytesIO
def GenerateImage(prompt, client):
    response = client.models.generate_images(
        model="imagen-3.0-generate-001",
        prompt=prompt,
        num_of_images = 1
    )
    image_bytes = response.generated_images[0].image.image_bytes
    image = Image.open(BytesIO(base64.base64decode(image_bytes)))
    return image