import cv2
import numpy as np
import MyFunctions


class ExtractRGB:
    def __init__(self,image,comments):
        self.image = image
        self.comments = comments

    def extractRGBChannels(self):

        B ,G , R = cv2.split(self.image)

        zeros = np.zeros(self.image.shape[:2], np.uint8)

        r_channel = cv2.merge([zeros,zeros,R])
        print("R channel shape", r_channel.shape)
        g_channel = cv2.merge([zeros, G, zeros])
        print("G channel shape", g_channel.shape)
        b_channel = cv2.merge([B, zeros,zeros])
        print("B channel shape", b_channel.shape)

        cv2.imshow("Red", r_channel)
        cv2.waitKey()
        cv2.imshow("Green", g_channel)
        cv2.waitKey()
        cv2.imshow("Blue", b_channel)
        cv2.waitKey()

        cv2.destroyAllWindows()

    def individualChannels(self):
        B , G , R = cv2.split(self.image)

        cv2.imshow("Blue",B)
        cv2.imshow("Green", G)
        cv2.imshow("Red", R)

        cv2.waitKey()
        cv2.destroyAllWindows()

        # Let's re-make the original image,
        merged = cv2.merge([B, G, R])
        cv2.imshow("Merged", merged)

        # Let's amplify the blue color
        merged = cv2.merge([B + 100, G, R])
        cv2.imshow("Merged with Blue Amplified", merged)
        cv2.waitKey(0)

        # Let's amplify the green color
        merged = cv2.merge([B, G + 40, R])
        cv2.imshow("Merged with Green Amplified", merged)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    def hsv_filtering(self):
        # Convert to HSV
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        cv2.imshow("HSV Image",hsv_image)

        cv2.imshow("Hue Image",hsv_image[:,:,0])
        cv2.imshow("Saturation Image", hsv_image[:, :, 1])
        cv2.imshow("value Image", hsv_image[:, :, 2])
        cv2.waitKey()
        cv2.destroyAllWindows()