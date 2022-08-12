import cv2
from matplotlib import pyplot as plt

class ImageOperator:
    def __init__(self, imagePath):
        '''
            initialize the image path and image object
            imagePath = 'path of the image'
        '''
        print(cv2.__version__)
        self.imagePath = imagePath 
        self.img = cv2.imread(self.imagePath)

        self.shapeDict = {
            'circle' : '''cv2.circle(*args)''',
            'rectangle' : '''cv2.rectangle(*args)'''
        }
        
    def getImgShape(self):
        '''
            Get the shape of the image
        '''
        return self.img.shape
        
    def resize(self, width, height, inplace = True):
        '''
            Resize the image to the given width and height
            width = 'width'
            height = 'height'
            inplace = 'Boolean to indicate if the image should be resized inplace or not'
            returns : 'resized image'
        '''
        # pass
        img = cv2.resize(self.img, (width, height))
        if inplace:
            self.img = img
            return self.img
        return img
    
    def crop(self, origin_point, width, height,  inplace = True):
        '''
            crop the image to the given width and height
            orgin_point = 'origin point of the image from top left corner'
            width = 'width of the image'
            height = 'height of the image'
            inplace = 'Boolean to indicate if the image should be resized inplace or not'
            returns : 'cropped image'
        '''
        img = self.img[origin_point[1]:origin_point[1]+height, origin_point[0]:origin_point[0]+width]
        if inplace:
            self.img = img
            return self.img
        return img
    
    def putLabel(self, label, origin_point, color = (255, 0, 0), thickness = 2,  inplace = True):
        '''
            Put the label on the image
            label = 'label to be put on the image'
            origin_point = 'origin point of the label from top left corner'
            color = 'color of the label'
            thickness = 'thickness of the label'
            returns : 'image with the label'
        '''
        img = cv2.putText(self.img, label, origin_point, cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)
        if inplace:
            self.img = img
            return self.img
        return img
        
    def save(self, savePath):
        '''
            Save the image to the given path
            savePath = 'path to save the image'
        '''
        cv2.imwrite(savePath, self.img)
        
    
    def putShape(self, shape, args, inplace = True):
        '''
            Put the shape on the image
            shape = 'shape to be drawn'
            args = 'list of the argument to be passed to the function'
            returns : 'image with the shape'

            Note : Please have a look at the opencv documentation for the 'args' 
            'args' must match with the number of parameters with the respective function
        '''
        if inplace:
            args = [self.img] +args
        else:
            args = [self.img.copy()] + args
        
        if shape in self.shapeDict.keys():
            img = eval(self.shapeDict[shape])
            return img
        else:
            print('Please check for shape')
            print('we provide following shapes \n' + '\n'.join(self.shapeDict.keys()))
            return None
    
    def monoColor(self):
        '''
            Check if the image is monochrome or not
        '''
        pass
    
    def showImageCLI(self, label = 'image'):
        '''
            Show the image on python console
        '''
        cv2.imshow(label, self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def showImageNotebook(self, label = 'image'):
        '''
            show the image on Jupyter Notebook
            problem with plt imshow 
            image is change
        '''
        plt.imshow(self.img)
        plt.show()
    
    
if __name__ == '__main__':
    ImgOperator = ImageOperator('/home/adithya/imp_repos/opencvLearning/Image/test.jpg')    
    
    ImgOperator.showImageCLI(label = 'Original Image')
    
    print('Shape of image before resizing' + str(ImgOperator.getImgShape()))
    
    ImgOperator.resize(500, 500, inplace = True)
    
    print('Shape of image after resizing' + str(ImgOperator.getImgShape()))
    
    ImgOperator.showImageCLI(label = 'Resized Image')
    
    ImgOperator.crop((200, 200), 400, 400, inplace = True)
    
    ImgOperator.showImageCLI(label = 'Cropped Image')
    
    ImgOperator.putLabel('Rose', (50, 50), color = (0, 255, 0), thickness = 2, inplace = True)
    
    ImgOperator.showImageNotebook(label = 'Image with Label')
    