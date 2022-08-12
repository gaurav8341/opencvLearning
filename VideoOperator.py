import cv2
import os
import glob

class VideoOperator:
    def __init__(self, vidPath = None):
        '''
            vidPath = 'Path of the video file or image sequence directory'
        '''
        self.vc = None
        if vidPath is not None:
            self.vc = cv2.VideoCapture(vidPath)
        
    def createFramesfromVideo(self, dirPath):
        '''
            dirPath = 'Path of the directory where images will be stored'
        '''
        if self.vc is not None:
            count = 0
            while self.vc.isOpened():
                ret, frame = self.vc.read()
                if ret:
                    cv2.imwrite(dirPath + '/Frame_'+str(count)+'.jpg', frame)
                    count += 1
            self.vc.release()


    def concatenateVids(self, vidPath, savePath):
        '''
            vidPath = 'Path of the directory where video files needed to concatenate are stored'
        '''
        # refine this code such that only video file come into array
        # videos = os.listdir(vidPath)
        types = ['*.mp4', '*.avi']
        videos = []
        for t in types:
            videos.extend(glob.glob(os.path.join(vidPath, t)))

        print(videos)

        frame_width = 0
        frame_height = 0
        fps = 0
        for v in videos:
            vc = cv2.VideoCapture(v)
            frame_width = max(frame_width, int(vc.get(3)))
            frame_height = max(frame_height, int(vc.get(4)))
            fps = max(fps, int(vc.get(cv2.CAP_PROP_FPS)))
            

        op = cv2.VideoWriter(savePath,cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))
        print(op)
        for v in videos:
            vc = cv2.VideoCapture(v)
            print(vc)
            while vc.isOpened():
                ret, frame = vc.read()
                if ret:
                    op.write(frame)
                else:
                    break
            vc.release()
        op.release

        

    def convertVideoFormat(self, reqdFormat = 'avi'):
        '''
            convert to desired video format
        '''
        pass

    def playVideo(self):
        '''
            play the video
        '''
        if self.vc is not None:
            while self.vc.isOpened():
                ret, frame = self.vc.read()
                if ret:
                    cv2.imshow('Frame', frame)
                    k = cv2.waitKey(20)

                    if k == 113:
                        break
                else:
                    break
            
            self.vc.release()
            cv2.destroyAllWindows()
    
    def saveVideo(self, savePath):
        '''
            Save the video created
            todo : write code to get from user what should be fromat of the video
        '''
        frame_size = (int(self.vc.get(3)), int(self.vc.get(4)))
        fps = self.vc.get(cv2.CAP_PROP_FPS)
        print(fps)

        op = cv2.VideoWriter(savePath, cv2.VideoWriter_fourcc(*'XVID'), fps, frame_size)

        if self.vc is not None:
            while self.vc.isOpened():
                ret, frame = self.vc.read()
                if ret:
                    op.write(frame)
                else:
                    break
            self.vc.release()
            op.release()
