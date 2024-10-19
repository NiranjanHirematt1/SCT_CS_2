from PIL import Image
import random

def pixel_shuffle(image_path, output_path, key):
    
    img = Image.open(image_path)
    pixels = list(img.getdata()) 
    
    print(img.size)
    width, height = img.size
    
    total_pixels = width * height
    
    print(total_pixels)
    
    
    indices = list(range(total_pixels))
    
    
    random.seed(key)
    
   
    random.shuffle(indices)
    
    
    shuffled_pixels = [None] * total_pixels
    for i, new_position in enumerate(indices):
        shuffled_pixels[new_position] = pixels[i]
    
    img_shuffled = Image.new(img.mode, img.size)
    img_shuffled.putdata(shuffled_pixels)
    

    img_shuffled.save(output_path)


input_image_path="C:\\Users\\hp\\\Desktop\\credentials\\image t0.jpg"

output_image_path="C:\\Users\\hp\\Desktop\\credentials\\encrypt.jpg"
key = 34561
pixel_shuffle(input_image_path,output_image_path , key)
