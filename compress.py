import numpy as np 
from numpy.linalg import svd
import cv2
import sys

def compress(img, k):
    U, s, V = svd(img, full_matrices=False)
    # reconstruct the image
    img_recon = np.dot(U[:, :k], np.dot(np.diag(s[:k]), V[:k, :]))
    return img_recon

if __name__ == "__main__":
    file_name = ""
    k = 0
    if len(sys.argv) != 3:
        file_name = input("Enter the file name: ")
        k = int(input("Enter the number of singular values to keep: "))
    else:
        file_name = sys.argv[1]
        k = int(sys.argv[2])
    img = cv2.imread(file_name)
    image_reconst_layers = [compress(img[:,:,i],k) for i in range(3)]
    image_reconst = np.zeros(img.shape)
    for i in range(3):
        image_reconst[:,:,i] = image_reconst_layers[i]
    cv2.imwrite("compressed-{}-{}".format(k, file_name), image_reconst)

