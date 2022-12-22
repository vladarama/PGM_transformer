from matplotlib import pyplot as plt

#note: must install matplotlib

def show_image(image):
    plt.imshow(image, interpolation='nearest')
    plt.show()