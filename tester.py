import compress
import sys
import imageio

if __name__ == "__main__":
    file_name = ""
    if len(sys.argv) != 2:
        file_name = input("Enter the file name: ")
    else:
        file_name = sys.argv[1]
    
    filenames = []
    k_values = []
    compression_ratios = []
    img = compress.read_image(file_name)
    for k in range(1, 101, 10):
        compression_ratio = compress.handler(file_name, img, k)
        filenames.append("compressed-{}-{}".format(k, file_name))
        k_values.append(k)
        compression_ratios.append(compression_ratio)
    for k in range(101, 201, 20):
        compression_ratio = compress.handler(file_name, img, k)
        filenames.append("compressed-{}-{}".format(k, file_name))
        k_values.append(k)
        compression_ratios.append(compression_ratio)
    for k in range(201, 301, 50):
        compression_ratio = compress.handler(file_name, img, k)
        filenames.append("compressed-{}-{}".format(k, file_name))
        k_values.append(k)
        compression_ratios.append(compression_ratio)
    for k in range(301, 501, 100):
        compression_ratio = compress.handler(file_name, img, k)
        filenames.append("compressed-{}-{}".format(k, file_name))
        k_values.append(k)
        compression_ratios.append(compression_ratio)

    imageio.mimsave('diag.gif', [imageio.imread(filename) for filename in filenames], duration=1)
