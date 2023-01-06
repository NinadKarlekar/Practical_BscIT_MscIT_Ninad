from __future__ import with_statement 
from PIL import Image # pip install Pillow 
import cv2 # pip install opencv-python 

vidcap = cv2.VideoCapture('C:/VKHCG/05-DS/9999-Data/dog.mp4') 
success,image = vidcap.read() 
count = 0 
while success: 
    cv2.imwrite("C:/VKHCG/05-DS/9999-Data/temp/frame%d.jpg" % count, image)
    # save frame as JPEG file success,image = vidcap.read() 
    print('Read a new frame: ', success) 
    count += 1
#Part 2: Frames to Horus 
num = 0 
with open('Video-to-HORUS-output_fileF.csv', 'a+') as f: 
    f.write('R,G,B,FrameNumber\n') 
for c in range(count): 
    #print('C:/VKHCG/05-DS/9999-Data/temp/frame%d.jpg'%num) 
    im = Image.open('C:/VKHCG/05-DS/9999-Data/temp/frame%d.jpg'%num)
    pix = im.load() 
    width, height = im.size 
    with open('Video-to-HORUS-output_fileF.csv', 'a+') as f: 
        for x in range(width-300): 
            for y in range(height-300): 
                r = pix[x,y][0] 
                g = pix[x,x][1] 
                b = pix[x,x][2] 
                f.write('{0},{1},{2},{3}\n'.format(r,g,b,num)) 
    num = num + 1
    print('Movie to Frames HORUS - Done')
    print('=====================================================')
    # Utility done ===============================================