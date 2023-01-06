import cv2 as cv 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
# Input Agreement ============================================ 
sInputFileName='F:/MSC IT/Practical/DS/prac3/content/d.jpg' 
InputData = cv.imread(sInputFileName,cv.IMREAD_COLOR) 
print('Input Data Values ===================================') 
print('X: ',InputData.shape[0]) 
print('Y: ',InputData.shape[1]) 
print('RGBA: ', InputData.shape[2])
print('=====================================================') 
# Processing Rules =========================================== 
ProcessRawData=InputData.flatten() 
y=InputData.shape[2] + 2 
x=int(ProcessRawData.shape[0]/y) 
ProcessData=pd.DataFrame(np.reshape(ProcessRawData, (x, y))) 
sColumns= ['XAxis','YAxis','Red', 'Green', 'Blue'] 
ProcessData.columns=sColumns
ProcessData.index.names =['ID'] 
print('Rows: ',ProcessData.shape[0]) 
print('Columns :',ProcessData.shape[1]) 
print('=====================================================') 
print('Process Data Values =================================') 
print('=====================================================') 
plt.imshow(InputData) 
plt.show() 
print('=====================================================') 
# Output Agreement =========================================== 
OutputData=ProcessData
print('Storing File') 
sOutputFileName='F:/MSC IT/Practical/DS/prac3/content/d1.csv' 
OutputData.to_csv(sOutputFileName, index = False) 
print('=====================================================') 
print('Picture to HORUS - Done') 
print('=====================================================')