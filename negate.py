import cv2
import copy

def negate(img):

    result = copy.deepcopy(img)
    total_channels = result.shape[2]

    # Finding channel depth of image
    bytes = result.itemsize
    MAX_PIXEL_VAL = (2 ** (bytes*8))-1
    for i in range(total_channels):
        result[:, :, i] = MAX_PIXEL_VAL-result[:, :, i]

    return result


if __name__ == "__main__":
    im = cv2.imread('Background.jpg')
    negate(im)
