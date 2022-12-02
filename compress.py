import numpy as np 
from numpy.linalg import svd
import cv2
import sys
from PIL import Image, ImageDraw, ImageFont

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def compress(img, k):
    U, s, V = svd(img, full_matrices=False)
    # reconstruct the image
    img_recon = np.dot(U[:, :k], np.dot(np.diag(s[:k]), V[:k, :]))
    return img_recon

def compression_ratio(img, img_recon, k):
    # m*n vs k*(m+n+1)
    return round((1 - (k*(img.shape[0]+img.shape[1]+1))/(img.shape[0]*img.shape[1])) * 100, 2)

def handler(file_name, img, k):
    image_reconst_layers = [compress(img[:,:,i],k) for i in range(3)]
    image_reconst = np.zeros(img.shape)
    for i in range(3):
        image_reconst[:,:,i] = image_reconst_layers[i]

    image_reconst = image_reconst.astype(np.uint8)

    cr = compression_ratio(img, image_reconst, k)
    # now add margin to image
    im_new = Image.fromarray(image_reconst.astype('uint8'))
    im_new = add_margin(im_new, 0, 0, 50, 0, (255, 255, 255))
    draw = ImageDraw.Draw(im_new)
    font = ImageFont.truetype("Arial.ttf", 45)
    draw.text((im_new.size[0]-150, im_new.size[1]-50), "k = {}".format(k), (0, 0, 0), font=font)
    draw.text((25, im_new.size[1]-50), "Compression Ratio = {}%".format(cr), (0, 0, 0), font=font)
    im_new.save("compressed-{}-{}".format(k, file_name))
    return cr

def read_image(file_name):
    return np.asarray(Image.open(file_name))

if __name__ == "__main__":
    file_name = ""
    k = 0
    if len(sys.argv) != 3:
        file_name = input("Enter the file name: ")
        k = int(input("Enter the number of singular values to keep: "))
    else:
        file_name = sys.argv[1]
        k = int(sys.argv[2])
    
    img = read_image(file_name)
    compression_ratio = handler(file_name, img, k)
    print("Compression ratio: {}".format(compression_ratio))
    
    

