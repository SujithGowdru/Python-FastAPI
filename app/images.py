from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

# imagekitio>=5.x expects only `private_key` here
imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
)

# Optional (not used by the SDK constructor)
IMAGEKIT_PUBLIC_KEY = os.getenv("IMAGEKIT_PUBLIC_KEY")
IMAGEKIT_URL_ENDPOINT = os.getenv("IMAGEKIT_URL") or os.getenv("IMAGEKIT_URL_ENDPOINT")