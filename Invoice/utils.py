import os, secrets
from flask import request
from PIL import Image
from flask_uploads import extension
from invoice import image as img

def save_image(image, folder):
    filename = f'{secrets.token_hex(12)}.{extension(image.filename)}'  
    img.save(image, folder=folder, name=filename)

    filename = compress_image(filename=filename, folder=folder)
    return filename

def compress_image(filename, folder):
    file_path = img.path(filename=filename, folder=folder)
    image = Image.open(file_path)
    
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    if max(image.width, image.height) > 1600:
        maxsize = (1600, 1600)
        image.resize(maxsize)
        
    compressed_filename = f'{secrets.token_hex(12)}.jpg'
    print(compressed_filename)
    compressed_file_path = img.path(filename=compressed_filename, folder=folder)

    image.save(compressed_file_path, optimize=True, quality=85)
    
    os.remove(file_path)
    
    return compressed_filename


def paginate(query, per_page):
    page = request.args.get('page', 1, type=int)
    paginated = query.paginate(page=page, per_page=per_page)
    
    return paginated
    
    