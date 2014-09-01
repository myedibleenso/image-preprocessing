import cv2
import os
import numpy
from matplotlib import pyplot as plt
import matplotlib.cm as cm

class ImagePreprocessor(object):
  def __init__(self, images):
    self.images = self.get_images(images)
    self.destination = None

  def get_images(self, images):
    image_extensions = [".png", ".jpg"]

    # is it a path?
    if type(images) == str:
      return [cv2.imread(os.path.join(images, i), 0) for i in os.listdir(images) if os.path.splitext(i)[-1].lower() in image_extensions]

    # is it a list of filenames?
    if type(images) == list and type(images[0]) == str:
      return [cv2.imread(i, 0) for i in images]

    # is it a list of arrays?
    if type(images[0] == numpy.ndarray):
      return images

  def view_image(self, img):
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    """
    WINDOW_NAME = 'Preprocessed Image'
    cv2.namedWindow(WINDOW_NAME, cv2.CV_WINDOW_AUTOSIZE)
    cv2.startWindowThread()
    cv2.imshow(WINDOW_NAME,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

  def view_sequence(self):
    plt.ion()
    plt.xticks([]), plt.yticks([])
    # show as grayscale
    im = plt.imshow(self.images[1], cmap = cm.Greys_r)
    for i in self.images[1:]:
      im.set_data(i)
      plt.draw()

  def save_images(self, imdest):
    destinations = [os.path.join(dest, os.path.basename(i)) for i in self.images]
    for i in range(len(destinations)):
      cv2.imwrite(images[i], thresholded_images[i][-1])

  def gaussian_blur(self):
    # TODO: add options for degree of blur
    return [cv2.GaussianBlur(img,(5,5),0) for img in self.images]

  def otsu_thresholding(self):
    # TODO: adjust threshold parameters?
    return [cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[-1] for img in self.images]

  def preprocess_images(self):
    imgs = self.images[:]
    techniques = [self.gaussian_blur, self.otsu_thresholding]
    for t in techniques:
      imgs = t()
    return imgs
