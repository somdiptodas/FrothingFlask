from PIL import Image
from werkzeug.utils import secure_filename
import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
base_image_directory = os.path.join(APP_ROOT, 'images\\base')
product_image_directory = os.path.join(APP_ROOT, 'images\\products')

def saveProductImage(productId, imageFile, filename):
    # Always a good idea to secure a filename before storing it
    filename = secure_filename(filename)
    # This is to verify files are supported
    ext = os.path.splitext(filename)[1][1:].strip().lower()
    if ext in {'jpg', 'jpeg', 'png'}:
        destination = os.path.join(product_image_directory, 'Product_Image_'+str(productId)+'.png')
        # Save original image
        imageFile.save(destination)
        # Save a copy of the thumbnail image
        image = Image.open(destination)
        image.thumbnail((300, 300))
        destination = os.path.join(product_image_directory, 'Thumbnail_Image_'+str(productId)+'.png')
        image.save(destination)
        return True

    return os.error

#image = Image.open('C:\Programming\Projects\FrothingFlask\project\images\\base\FrothingLogo.png')
# #image.show()
# box = (0, 450, 1500, 950)
# cropped_image = image.crop(box)
# cropped_image.save('cropped_image.png')

# image = Image.open('C:\Programming\Projects\FrothingFlask\project\images\\base\VerticalFFstar.jpg')
# # #image.save('FFNavLogo.png','PNG')
# image.thumbnail((1000, 1000))
# image.save('VerticalSideLogo.png')