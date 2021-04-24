import cv2


class MyClass:
    x = 5


class ConvertGreyScale:

    def __init__(self, image, comments):
        self.image = image
        self.comments = comments

    def conv2grey(self, image):
        self.comments = "Grey Scaled"
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def display(self):
        cv2.imshow(self.comments, self.image)
        cv2.waitKey()
        cv2.destroyAllWindows()
