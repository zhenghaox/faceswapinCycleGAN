import sys
sys.path.append('../src')
from src import detect_faces
import getrawface as gf
import os 
import numpy as np
from IPython.display import display
from PIL import Image

def outputmask(imgpath, savepath):
    for img in os.listdir(imgpath):
        imgname = imgpath + img
        imgloaded = Image.open(imgname)
   
        boundingbox, landmarks = detect_faces(imgloaded)
        eyemask = np.zeros(imgloaded.size).astype('uint8')[:,:,None]
        if isinstance(landmarks, np.ndarray):
            if landmarks.shape[0] > 0:
                interval = int(landmarks.shape[1]/2)
                eyeisat = [[int(landmarks.flatten()[i]), int(landmarks.flatten()[i+interval])] for i in range(2)]
        #print(eyeisat)
        eyemask = gf.getEyeMask(eyemask, eyeisat)
#         display(imgloaded)
#         display(Image.fromarray(eyemask))
        Image.fromarray(eyemask).save(savepath+img)
        
if __name__ == '__main__':
    dirAimg = '../faceA/rgb/'
    dirBimg = '../faceB/rgb/'
    dirAsavepath = '../faceA/eyemask/'
    dirBsavepath = '../faceB/eyemask/'
    outputmask(dirAimg, dirAsavepath)
    outputmask(dirBimg, dirBsavepath)
