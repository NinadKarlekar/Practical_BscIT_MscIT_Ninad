# Data Science Practicals

M. Sc (Information Technology) <br>
PSIT1P2 Data Science 2022-2023



## Index

| Sr.No. | Name | Copy |
| --- | --- | --- |
| [Prac1A-i](/MscIT/Semester%201/Data_Science/Practical%201/) <br> [Prac1A-ii](/MscIT/Semester%201/Data_Science/Practical%201/) <br>  [Prac1A-iii](/MscIT/Semester%201/Data_Science/Practical%201/)| A.	Perform error management on the given data using pandas package. <br>  i.	Drop the Columns Where All Elements Are Missing Values <br> ii.	Drop the Columns Where Any of the Elements Is Missing Values <br> iii.	Keep Only the Rows That Contain a Maximum of Two Missing Values | [prac1A-I](#prac1a-i)<br> [prac1A-II](#prac1a-ii)<br> [prac1A-III](#prac1a-iii) |
| [Prac1B](/MscIT/Semester%201/Data_Science/Practical%201/)| B.	Write Python / R program to create the network routing diagram from the given data on routers. | [Prac1B](#prac1b) |
| [Prac2A](/MscIT/Semester%201/Data_Science/Practical%202/)| A.	Text delimited CSV to HORUS format. | [Prac2A](#prac2a) |
| [Prac2B](/MscIT/Semester%201/Data_Science/Practical%202/)| B. JSON to HORUS Format | [Prac2B](#prac2b) |
| [Prac3C](/MscIT/Semester%201/Data_Science/Practical%203/)| C.	IMG to HORUS Format | [Prac3C](#prac3c) |
| [Prac3D](/MscIT/Semester%201/Data_Science/Practical%203/)| D.	Conversion from Video/Audio to HORUS | [Prac3D](#prac3d) |
| [Prac3E](/MscIT/Semester%201/Data_Science/Practical%203/)| E.	XML to HORUS Format | [Prac3E](#prac3e) |
| [Prac4A](/MscIT/Semester%201/Data_Science/Practical%204/)|4.  Utilities and Auditing <br> A.	Fixers utilities | [Prac4A](#prac4a) |
| [Prac4B](/MscIT/Semester%201/Data_Science/Practical%204/)| B.	Data Binning or Bucketing | [Prac4B](#prac4b) |
| [Prac4C](/MscIT/Semester%201/Data_Science/Practical%204/)| C.	Averaging of data | [Prac4C](#prac4c) |
| [Prac4D](/MscIT/Semester%201/Data_Science/Practical%204/)| D.	Outlier Detection | [Prac4D](#prac4d) |
| [Prac4E](/MscIT/Semester%201/Data_Science/Practical%204/)| E.	Audit – Logging | [Prac4E](#prac4e) |
| [Prac5A](/MscIT/Semester%201/Data_Science/Practical%205/)| A.	Program to retrieve different types of attributes | [Prac5A](#prac5a) |
| [Prac5B](/MscIT/Semester%201/Data_Science/Practical%205/)| B.	Data Pattern | [Prac5B](#prac5b) |
| [Prac5C](/MscIT/Semester%201/Data_Science/Practical%205/)| C.	Loading IP_DATA_ALL | [Prac5C](#prac5c) |
| [Prac6](/MscIT/Semester%201/Data_Science/Practical%206/)| Organizing Data <br>(Organize- Horizontal style, Vertical style, Island style and Secure Vault style) | [Prac6](#prac6) |
| Prac7| Data Visualization with Power BI | |
| [Prac8A](/MscIT/Semester%201/Data_Science/Practical%208/)| 8. Transforming Data <br> A.	Building data warehouse | [Prac8A](#prac8a) |
| [Prac8B](/MscIT/Semester%201/Data_Science/Practical%208/)| B.	Simple Linear Regression | [Prac8B](#prac8b) |
| [Prac9A](/MscIT/Semester%201/Data_Science/Practical%209/)| 9. Generating Reports <br> A.	Vermeulen PLC | [Prac9A](#prac9a) |
| [Prac9B](/MscIT/Semester%201/Data_Science/Practical%209/)|  B.	Krennwallner AG | [Prac9B](#prac9b) |
| [Prac10A](/MscIT/Semester%201/Data_Science/Practical%2010/)| 10. Processing Data <br> A.	Build the time Hub, Link and Satellite | [Prac10A](#prac10a) |
| [Prac10B](/MscIT/Semester%201/Data_Science/Practical%2010/)| B.	Human-Environment Interaction | [Prac10B](#prac10b) |
| [Prac10C](/MscIT/Semester%201/Data_Science/Practical%2010/)| C.	Forecasting | [prac10C](#prac10c) |



*******************

## prac1A-i

- Assessing Data
- Drop the columns where all element is missing values.

```python
#C:\VKHCG\01-Vermeulen\02-Assess\Assess-Good-Bad-01.py
################### Assess-Good-Bad-01.py########################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
##############Enter required path###########################
Base='C:/VKHCG'
################################################################
print("i. Drop the Columns Where All Elements Are Missing Values")
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sInputFileName='Good-or-Bad.csv'
sOutputFileName='Good-or-Bad-01.csv'
Company='01-Vermeulen'
################################################################
Base='C:/VKHCG'
################################################################
sFileDir=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
 os.makedirs(sFileDir)
################################################################
### Import Warehouse
################################################################
sFileName=Base + '/' + Company + '/00-RawData/' + sInputFileName
RawData=pd.read_csv(sFileName,header=0)
print('################################')
print('## Raw Data Values')
print('################################')
print(RawData)
print('################################')
print('## Data Profile')
print('################################')
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sInputFileName
RawData.to_csv(sFileName, index = False)
################################################################
TestData=RawData.dropna(axis=1, how='all')
################################################################
print('################################')
print('## Test Data Values')
print('################################')
print(TestData)
print('################################')
print('## Data Profile')
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sOutputFileName
TestData.to_csv(sFileName, index = False)
################################################################
print('################################')
print('### Done!! #####################')
print('################################')
```

- **OUTPUT**



*******************

## prac1A-ii

- Drop the columns where any of the element is missing.

```python
#C:\VKHCG\01-Vermeulen\02-Assess\Assess-Good-Bad-02.py
import sys
import os
import pandas as pd
##############Enter required path###########################
Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sInputFileName='Good-or-Bad.csv'
sOutputFileName='Good-or-Bad-01.csv'
Company='01-Vermeulen'
################################################################
Base='C:/VKHCG'
################################################################
sFileDir=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
 os.makedirs(sFileDir)
################################################################
### Import Warehouse
################################################################
sFileName=Base + '/' + Company + '/00-RawData/' + sInputFileName
RawData=pd.read_csv(sFileName,header=0)
print('################################')
print('## Raw Data Values')
print('################################')
print(RawData)
print('################################')
print('## Data Profile')
print('################################')
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sInputFileName
RawData.to_csv(sFileName, index = False)
################################################################
TestData=RawData.dropna(axis=1, how='any')
################################################################
print('################################') 
print('## Test Data Values')
print('################################')
print(TestData)
print('################################')
print('## Data Profile')
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sOutputFileName
TestData.to_csv(sFileName, index = False)
################################################################
print('################################')
print('### Done!! #####################')
print('################################')
```

- **OUTPUT**



*******************

## prac1A-iii

- Keep only the rows that contain a maximum of two missing values.

```python
#C:\VKHCG\01-Vermeulen\02-Assess\Assess-Good-Bad-03.py
import sys
import os
import pandas as pd
##############Enter required path###########################
Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sInputFileName='Good-or-Bad.csv'
sOutputFileName='Good-or-Bad-01.csv'
Company='01-Vermeulen'
################################################################
Base='C:/VKHCG'
################################################################
sFileDir=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
 os.makedirs(sFileDir)
################################################################
### Import Warehouse
################################################################
sFileName=Base + '/' + Company + '/00-RawData/' + sInputFileName
RawData=pd.read_csv(sFileName,header=0)
sFileName=Base + '/' + Company + '/00-RawData/' + sInputFileName
print('Loading :',sFileName)
RawData=pd.read_csv(sFileName,header=0)
print('################################')
print('## Raw Data Values')
print('################################')
print(RawData)
print('################################')
print('## Data Profile')
print('################################')
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sInputFileName
RawData.to_csv(sFileName, index = False)
################################################################
TestData=RawData.dropna(thresh=6)
print('################################')
print('## Test Data Values')
print('################################')
print(TestData)
print('################################')
print('## Data Profile')
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
sFileName=sFileDir + '/' + sOutputFileName
TestData.to_csv(sFileName, index = False)
################################################################

print('### Done!! #####################')
print('################################')
################################################################
```

<details>
<summary>OUTPUT</summary>
![MSCIT_DSprac1A_iii_1](https://user-images.githubusercontent.com/88243315/214916010-1958ffeb-3f2f-456d-9f9a-7eec672a6a15.png)
![MSCIT_DSprac1A_iii_2](https://user-images.githubusercontent.com/88243315/214916076-c710409d-534b-4258-9c0f-8a668cadb42a.png)

</details>


*******************

## prac1B

- Create a network routing diagram from the given data on the routers. (Assess- Company, Customer and Node)

```python
#C:\VKHCG\01-Vermeulen\02-Assess\Assess-Network-Routing-Company.py
import sys
import os
import pandas as pd

pd.options.mode.chained_assignment = None

Base='C:/VKHCG'

print('################################')
print('Working Base :',Base, ' using Windows')

sInputFileName1='01-Retrieve/01-EDS/01-R/Retrieve_Country_Code.csv'
sInputFileName2='01-Retrieve/01-EDS/02-Python/Retrieve_Router_Location.csv'
sInputFileName3='01-Retrieve/01-EDS/01-R/Retrieve_IP_DATA.csv'

sOutputFileName='Assess-Network-Routing-Company.csv'
Company='01-Vermeulen'

### Import Country Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName1

print(sFileName)

print('Loading :',sFileName)
print('################################')
CountryData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
print('Loaded Country:',CountryData.columns.values)

## Assess Country Data
################################################################
print('################################')
print('Changed :',CountryData.columns.values)
CountryData.rename(columns={'Country': 'Country_Name'}, inplace=True)
CountryData.rename(columns={'ISO-2-CODE': 'Country_Code'}, inplace=True)
CountryData.drop('ISO-M49', axis=1, inplace=True)
CountryData.drop('ISO-3-Code', axis=1, inplace=True)
CountryData.drop('RowID', axis=1, inplace=True)
print('To :',CountryData.columns.values)

### Import Company Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName2

print('################################')
print('Loading :',sFileName)
print('################################')
CompanyData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
print('Loaded Company :',CompanyData.columns.values)

## Assess Company Data
################################################################
print('################################')
print('Changed :',CompanyData.columns.values)
CompanyData.rename(columns={'Country': 'Country_Code'}, inplace=True)
print('To :',CompanyData.columns.values)
print('################################')

### Import Customer Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName3
print('################################')
print('Loading :',sFileName)

CustomerRawData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
print('################################')
print('Loaded Customer :',CustomerRawData.columns.values)
print('################################')

CustomerData=CustomerRawData.dropna(axis=0, how='any')
print('################################')
print('Remove Blank Country Code')
print('Reduce Rows from', CustomerRawData.shape[0],' to ', CustomerData.shape[0])

print('################################')
print('Changed :',CustomerData.columns.values)
CustomerData.rename(columns={'Country': 'Country_Code'}, inplace=True)
print('To :',CustomerData.columns.values)
print('################################')

print('Merge Company and Country Data')
print('################################')
CompanyNetworkData=pd.merge(
    CompanyData,
    CountryData,
    how='inner',
    on='Country_Code'
    )
################################################################
print('################################')

print('Change ',CompanyNetworkData.columns.values)
for i in CompanyNetworkData.columns.values:
    j='Company_'+i
    CompanyNetworkData.rename(columns={i: j}, inplace=True)
    print('To ', CompanyNetworkData.columns.values)
    print('################################')

sFileDir=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
sFileName=sFileDir + '/' + sOutputFileName
print('################################')
print('Storing :', sFileName)
print('################################')

CompanyNetworkData.to_csv(sFileName, index = False, encoding="latin-1")
print('### Done!! #####################')
```

- **OUTPUT**



*******************

## prac2A

- Conversion different data format to HORUS format
- a. Conversion from CSV to HORUS
```python
# Utility Start CSV to HORUS =================================
# Standard Tools
print("Text delimited CSV to HORUS format.")
import pandas as pd
# Input Agreement ============================================
sInputFileName=r"F:\MSC IT\Practical\DS\Prac2\Country_Code.csv"
InputData = pd.read_csv(sInputFileName,encoding="latin-1")
print('Input Data Values ===================================')
print(InputData)
# Processing Rules ===========================================
ProcessData=InputData
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-Code',axis=1,inplace=True)
# Rename Country and ISO-M49
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)
# Set new Index
ProcessData.set_index('CountryName',inplace=True)
# Sort data by CurrencyName
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)
print("**************************************************************************")
print("ProcessData")
print(ProcessData)
OutputData=ProcessData
sOutputFileName =r"F:\MSC IT\Practical\DS\Prac2\HORUSCountry_Code.csv"
OutputData.to_csv(sOutputFileName, index = False)
print('CSV to HORUS - Done')
```

- **OUTPUT**



*******************

## prac2B

- b. Conversion from JSON to HORUS

```python
# Utility Start JSON to HORUS ================================= 
# # Standard Tools 
# #============================================================ 
print("C. JSON to HORUS Format")
import pandas as pd
# Input Agreement ============================================ 
sInputFileName=r"F:\MSC IT\Practical\DS\Prac2\Country_Code.json"
InputData=pd.read_json(sInputFileName, orient='index', encoding="latin-1")
print('Input Data Values ===================================') 
print(InputData)
# Processing Rules ===========================================
ProcessData=InputData
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True) 
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True) 
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)
# Sort data by CountryName 
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True) 
print('Process Data Values =================================')
print(ProcessData) 
print('=====================================================')
# Output Agreement =========================================== 
OutputData=ProcessData 
sOutputFileName=r"F:\MSC IT\Practical\DS\Prac2\HORUS-JSON-Country.csv" 
OutputData.to_csv(sOutputFileName, index = False)
print('JSON to HORUS - Done') 
# Utility done ===============================================

```

- **OUTPUT**



*******************

## prac3C

- c. Conversion from JPG/Images to HORUS

```python
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
```

- **OUTPUT**



*******************

## prac3D

- d1. Conversion from Audio to HORUS

```python
# Utility Start Audio to HORUS ===============================
# Standard Tools
# =============================================================
from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =============================================================
def show_info(aname, a, r):
    print("----------------")
    print("Audio:", aname)
    print("----------------")
    print("Rate:", r)
    print("----------------")
    print("shape:", a.shape)
    print("dtype:", a.dtype)
    print("min, max:", a.min(), a.max())
    print("----------------")
    plot_info(aname, a, r)


# =============================================================
def plot_info(aname, a, r):
    sTitle = "Signal Wave - " + aname + " at " + str(r) + "hz"
    plt.title(sTitle)
    sLegend = []
    for c in range(a.shape[1]):
        sLabel = "Ch" + str(c + 1)
        sLegend = sLegend + [str(c + 1)]
        plt.plot(a[:, c], label=sLabel)
    plt.legend(sLegend)
    plt.show()

# =============================================================
sInputFileName = "C:/VKHCG/05-DS/9999-Data/2ch-sound.wav"
print("=====================================================")
print("Processing : ", sInputFileName)
print("=====================================================")
InputRate, InputData = wavfile.read(sInputFileName)
show_info("2 channel", InputData, InputRate)
ProcessData = pd.DataFrame(InputData)
sColumns = ["Ch1", "Ch2"]
ProcessData.columns = sColumns
OutputData = ProcessData
sOutputFileName = "Audio-to-HORUS-outputG-2ch.csv"
OutputData.to_csv(sOutputFileName, index=False)
# =============================================================
sInputFileName = "C:/VKHCG/05-DS/9999-Data/4ch-sound.wav"
print("=====================================================")
print("Processing : ", sInputFileName)
print("=====================================================")
InputRate, InputData = wavfile.read(sInputFileName)
show_info("4 channel", InputData, InputRate)
ProcessData = pd.DataFrame(InputData)
sColumns = ["Ch1", "Ch2", "Ch3", "Ch4"]
ProcessData.columns = sColumns
OutputData = ProcessData
sOutputFileName = "Audio-to-HORUS-outputG-4ch.csv"
OutputData.to_csv(sOutputFileName, index=False)
# =============================================================
sInputFileName = "C:/VKHCG/05-DS/9999-Data/6ch-sound.wav"
print("=====================================================")
print("Processing : ", sInputFileName)
print("=====================================================")
InputRate, InputData = wavfile.read(sInputFileName)
show_info("6 channel", InputData, InputRate)
ProcessData = pd.DataFrame(InputData)
sColumns = ["Ch1", "Ch2", "Ch3", "Ch4", "Ch5", "Ch6"]
ProcessData.columns = sColumns
OutputData = ProcessData
sOutputFileName = "Audio-to-HORUS-outputG-6ch.csv"
OutputData.to_csv(sOutputFileName, index=False)
# =============================================================
sInputFileName = "C:/VKHCG/05-DS/9999-Data/8ch-sound.wav"
print("=====================================================")
print("Processing : ", sInputFileName)
print("=====================================================")
InputRate, InputData = wavfile.read(sInputFileName)
show_info("8 channel", InputData, InputRate)
ProcessData = pd.DataFrame(InputData)
sColumns = ["Ch1", "Ch2", "Ch3", "Ch4", "Ch5", "Ch6", "Ch7", "Ch8"]
ProcessData.columns = sColumns
OutputData = ProcessData
sOutputFileName = "Audio-to-HORUS-outputG-8ch.csv"
print("=====================================================")
print("Audio to HORUS - Done")
OutputData.to_csv(sOutputFileName, index=False)

```

- **OUTPUT**



- d2. Conversion from Video to HORUS

```python
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

```

- **OUTPUT**



*******************

## prac3E

- e. Conversion from XML to HORUS

```python
# Utility Start XML to HORUS =================================
# Standard Tools
print("B.	XML to HORUS Format")
import pandas as pd
import xml.etree.ElementTree as ET
def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    for row in range(data.shape[0]):
        entry = ET.SubElement(root, 'entry')
        for index in range(data.shape[1]):
            schild = str(header[index])
            child = ET.SubElement(entry, schild)
            if str(data[schild][row]) != 'nan':
                child.text = str(data[schild][row])
            else:
                child.text = 'n/a'
            entry.append(child)
    result = ET.tostring(root)
    return result

def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)
sInputFileName = r"F:\MSC IT\Practical\DS\Prac2\Country_Code.xml"
InputData = open(sInputFileName).read()
print('=====================================================')
print('Input Data Values ===================================')
print('=====================================================')
print(InputData)
print('=====================================================')
#============================================================
# # Processing Rules ===========================================
# #============================================================  
ProcessDataXML = InputData
# # XML to Data Frame
ProcessData = xml2df(ProcessDataXML)
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1, inplace=True)
ProcessData.drop('ISO-3-Code', axis=1, inplace=True)
# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)
# Sort data by CurrencyNumberProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print('=====================================================')
print('Process Data Values =================================')
print('=====================================================')
print(ProcessData)
print('=====================================================')
OutputData = ProcessData
sOutputFileName = r"F:\MSC IT\Practical\DS\Prac2\HORUS-XML-Country.csv"
OutputData.to_csv(sOutputFileName, index=False)
print('=====================================================')
print('XML to HORUS - Done')
print('=====================================================')
# Utility done ===============================================

```

- **OUTPUT**



*******************

## prac4A

- Utilities and Auditing
    - a. Fixers utilities

```python
#---------------------------- Program to Demonstrate Fixers utilities -------------------
print('4A. Fixers Utilities:')
import string
import datetime as dt
# 1 Removing leading or lagging spaces from a data entry
print('#1 Removing leading or lagging spaces from a data entry');
baddata = " Hello My name is abc xyz "
print('>',baddata,'<')
cleandata=baddata.strip()
print('>',cleandata,'<')

print("********************************************************")

# 2 Removing nonprintable characters from a data entry
print('#2 Removing nonprintable characters from a data entry')
printable = set(string.printable)
baddata = "Data\x00Science with\x02 funny characters is \x10bad!!!"
cleandata=''.join(filter(lambda x: x in string.printable,baddata))
print('Bad Data : ',baddata);
print('Clean Data : ',cleandata)

print("********************************************************")

# 3 Reformatting data entry to match specific formatting criteria.
# Convert YYYY/MM/DD to DD Month YYYY
print('# 3 Reformatting data entry to match specific formatting criteria.')
baddate = dt.date(2001, 1, 1)
baddata=format(baddate,'%Y-%m-%d')
gooddate = dt.datetime.strptime(baddata,'%Y-%m-%d')
gooddata=format(gooddate,'%d %B %Y')
print('Bad Data : ',baddata)
print('Good Data : ',gooddata)

```

- **OUTPUT**



*******************

## prac4B

- b. Data Binning or Bucketing

```python
#Jupyter notebook
print('4B. Data Binning or Bucketing')
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
np.random.seed(0)
# example data
mu = 90 # mean of distribution
sigma = 25 # standard deviation of distribution
x = mu + sigma * np.random.randn(5000)
num_bins = 25
fig, ax = plt.subplots()
# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=1)
# add a 'best fit' line
y = stats.norm.pdf(bins, mu, sigma)
# mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Example Data')
ax.set_ylabel('Probability density')
sTitle=r'Histogram ' + str(len(x)) + ' entries into ' + str(num_bins) + ' Bins: $\mu=' + str(mu)
+ '$, $\sigma=' + str(sigma) + '$'
ax.set_title(sTitle)
fig.tight_layout()
sPathFig='C:/VKHCG/05-DS/4000-UL/0200-DU/DU-Histogram.png'
fig.savefig(sPathFig)
plt.show()

```

- **OUTPUT**



*******************

## prac4C

- c. Averaging of data

```python
# C:\VKHCG\05-DS\4000-UL\0200-DU\DU-Mean.py
import pandas as pd
################################################################
InputFileName='IP_DATA_CORE.csv'
OutputFileName='Retrieve_Router_Location.csv'
Base='C:/VKHCG'
print('4C. Averaging of Data')
print('################################')
print('Working Base :',Base, ' using ')
print('################################')
sFileName=Base + '/01-Vermeulen/00-RawData/' + InputFileName
print('Loading :',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False,
usecols=['Country','Place Name','Latitude','Longitude'], encoding="latin-1")
IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
AllData=IP_DATA_ALL[['Country', 'Place_Name','Latitude']]
print(AllData)
MeanData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
print(MeanData)
```

- **OUTPUT**



*******************

## prac4D

- d. Outlier Detection

```python
# C:\VKHCG\05-DS\4000-UL\0200-DU\DU-Outliers.py
import pandas as pd
################################################################
print('4D. Outlier Detection')
InputFileName='IP_DATA_CORE.csv'
OutputFileName='Retrieve_Router_Location.csv'
Base='C:/VKHCG'
print('################################')
print('Working Base :',Base)
print('################################')
################################################################
sFileName=Base + '/01-Vermeulen/00-RawData/' + InputFileName
print('Loading :',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False,
usecols=['Country','Place Name','Latitude','Longitude'], encoding="latin-1")
IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
LondonData=IP_DATA_ALL.loc[IP_DATA_ALL['Place_Name']=='London']
AllData=LondonData[['Country', 'Place_Name','Latitude']]
print('All Data')
print(AllData)
MeanData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
StdData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].std()
print('Outliers')
UpperBound=float(MeanData+StdData)
print('Higher than ', UpperBound)
OutliersHigher=AllData[AllData.Latitude>UpperBound]
print(OutliersHigher)
LowerBound=float(MeanData-StdData)
print('Lower than ', LowerBound)
OutliersLower=AllData[AllData.Latitude<LowerBound]
print(OutliersLower)
print('Not Outliers')
OutliersNot=AllData[(AllData.Latitude>=LowerBound) & (AllData.Latitude<=UpperBound)]
print(OutliersNot)

```

- **OUTPUT**



*******************

## prac4E

- e. Audit – Logging

```python
# C:\VKHCG\77-Yoke\Yoke_Logging.py
import sys
import os
import logging
import uuid
import shutil
import time

############################################################
if sys.platform == "linux":
    Base = os.path.expanduser("~") + "/VKHCG"
else:
    Base = "C:/VKHCG"
############################################################
sCompanies = ["01-Vermeulen", "02-Krennwallner", "03-Hillman", "04-Clark"]
sLayers = [
    "01-Retrieve",
    "02-Assess",
    "03-Process",
    "04-Transform",
    "05-Organise",
    "06-Report",
]
sLevels = ["debug", "info", "warning", "error"]

for sCompany in sCompanies:
    sFileDir = Base + "/" + sCompany
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    for sLayer in sLayers:
        log = logging.getLogger()  # root logger
        for hdlr in log.handlers[:]:  # remove all old handlers
            log.removeHandler(hdlr)
        ############################################################
        sFileDir = Base + "/" + sCompany + "/" + sLayer + "/Logging"
        if os.path.exists(sFileDir):
            shutil.rmtree(sFileDir)
        time.sleep(2)
        if not os.path.exists(sFileDir):
            os.makedirs(sFileDir)
        skey = str(uuid.uuid4())
        sLogFile = (
            Base + "/" + sCompany + "/" + sLayer + "/Logging/Logging_" + skey + ".log"
        )
        print("Set up:", sLogFile)
        # set up logging to file - see previous section for more details
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            datefmt="%m-%d %H:%M",
            filename=sLogFile,
            filemode="w",
        )
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger("").addHandler(console)

        # Now, we can log to the root logger, or any other logger. First the root...
        logging.info("Practical Data Science is fun!.")

        for sLevel in sLevels:
            sApp = "Apllication-" + sCompany + "-" + sLayer + "-" + sLevel
            logger = logging.getLogger(sApp)

            if sLevel == "debug":
                logger.debug("Practical Data Science logged a debugging message.")

            if sLevel == "info":
                logger.info("Practical Data Science logged information message.")

            if sLevel == "warning":
                logger.warning("Practical Data Science logged a warning message.")

            if sLevel == "error":
                logger.error("Practical Data Science logged an error message.")

############################################################


```

- **OUTPUT**



*******************

## prac5A

- Retrieving Data
- a. Program to retrieve different types of attributes

```python
################################################################
# -*- coding: utf-8 -*-
### C:\ VKHCG\01-Vermeulen\01-Retrieve\Retrive_IP_DATA_ALL.py###
################################################################
import sys
import os
import pandas as pd
print("5A. Topic: Program to retrieve different types of attributes")
################################################################
Base='C:/VKHCG'
################################################################
sFileName=Base + '/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'
print('Loading :',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
################################################################
sFileDir=Base + '/01-Vermeulen/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)

print('Rows:', IP_DATA_ALL.shape[0])
print('Columns:', IP_DATA_ALL.shape[1])
print('### Raw Data Set #####################################')
for i in range(0,len(IP_DATA_ALL.columns)):
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
print('### Fixed Data Set ###################################')
IP_DATA_ALL_FIX=IP_DATA_ALL
for i in range(0,len(IP_DATA_ALL.columns)):
    cNameOld=IP_DATA_ALL_FIX.columns[i] + '     '
    cNameNew=cNameOld.strip().replace(" ", ".")
    IP_DATA_ALL_FIX.columns.values[i] = cNameNew
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
################################################################
#print(IP_DATA_ALL_FIX.head())
################################################################
print('Fixed Data Set with ID')
IP_DATA_ALL_with_ID=IP_DATA_ALL_FIX
IP_DATA_ALL_with_ID.index.names = ['RowID']
#print(IP_DATA_ALL_with_ID.head())

sFileName2=sFileDir + '/Retrieve_IP_DATA.csv'
IP_DATA_ALL_with_ID.to_csv(sFileName2, index = True, encoding="latin-1")

print('### Done!! ############################################')
################################################################
```

- **OUTPUT**



*******************

## prac5B

- b. Data Pattern

```r

# R language
# R studio
print('5B. Data Pattern')
library(readr)
library(data.table)
FileName=paste0('c:/VKHCG/01-Vermeulen/00-RawData/IP_DATA_ALL.csv')
IP_DATA_ALL <- read_csv(FileName)
hist_country=data.table(Country=unique(IP_DATA_ALL$Country))
pattern_country=data.table(Country=hist_country$Country,
PatternCountry=hist_country$Country)
oldchar=c(letters,LETTERS)
newchar=replicate(length(oldchar),"A")
for (r in seq(nrow(pattern_country))){
    s=pattern_country[r,]$PatternCountry;
    for (c in seq(length(oldchar))){
        s=chartr(oldchar[c],newchar[c],s)
    };
    for (n in seq(0,9,1)){
        s=chartr(as.character(n),"N",s)
    };
    s=chartr(" ","b",s)
    s=chartr(".","u",s)
    pattern_country[r,]$PatternCountry=s;
};
View(pattern_country)
```

- **OUTPUT**



*******************

## prac5C

- c. Loading IP_DATA_ALL

```python
################################################################
# -*- coding: utf-8 -*
# C:\VKHCG\01-Vermeulen\01-Retrieve\Retrieve-IP_DATA_ALL.py
################################################################
print("5C. Loading IP_DATA_ALL")
import sys
import os
import pandas as pd
################################################################
Base='C:/VKHCG'
################################################################
sFileName=Base + '/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'
print('Loading :',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
################################################################
sFileDir=Base + '/01-Vermeulen/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)

print('Rows:', IP_DATA_ALL.shape[0])
print('Columns:', IP_DATA_ALL.shape[1])
print('### Raw Data Set #####################################')
for i in range(0,len(IP_DATA_ALL.columns)):
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
print('### Fixed Data Set ###################################')
IP_DATA_ALL_FIX=IP_DATA_ALL
for i in range(0,len(IP_DATA_ALL.columns)):
    cNameOld=IP_DATA_ALL_FIX.columns[i] + '     '
    cNameNew=cNameOld.strip().replace(" ", ".")
    IP_DATA_ALL_FIX.columns.values[i] = cNameNew
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
################################################################
#print(IP_DATA_ALL_FIX.head())
################################################################
print('Fixed Data Set with ID')
IP_DATA_ALL_with_ID=IP_DATA_ALL_FIX
IP_DATA_ALL_with_ID.index.names = ['RowID']
#print(IP_DATA_ALL_with_ID.head())

sFileName2=sFileDir + '/Retrieve_IP_DATA.csv'
IP_DATA_ALL_with_ID.to_csv(sFileName2, index = True, encoding="latin-1")

################################################################
print('### Done!! ############################################')
################################################################
```

- **OUTPUT**



*******************

## prac6

- Organizing Data (Organize- Horizontal style, Vertical style, Island style and Secure Vault style)

1. <b>Horizontal style</b>
```python
# C:\VKHCG\01-Vermeulen\05-Organise\ Organize-Horizontal.py
import sys
import os
import pandas as pd
import sqlite3 as sq

print("6A. Horizontal style")
if sys.platform == "linux":
    Base = os.path.expanduser("~") + "/VKHCG"
else:
    Base = "C:/VKHCG"
print("################################")
print("Working Base :", Base, " using ", sys.platform)
print("################################")
Company = "01-Vermeulen"
sDataWarehouseDir = Base + "/99-DW"
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)
sDatabaseName = sDataWarehouseDir + "/datawarehouse.db"
conn1 = sq.connect(sDatabaseName)
sDatabaseName = sDataWarehouseDir + "/datamart.db"
conn2 = sq.connect(sDatabaseName)
print("################")
sTable = "Dim-BMI"
print("Loading :", sDatabaseName, " Table:", sTable)
sSQL = "SELECT * FROM [" + sTable + "];"
PersonFrame0 = pd.read_sql_query(sSQL, conn1)
print("################################")
sTable = "Dim-BMI"
print("Loading :", sDatabaseName, " Table:", sTable)
print("################################")
sSQL = "SELECT PersonID,\
       Height,\
       Weight,\
       bmi,\
       Indicator\
  FROM [Dim-BMI]\
  WHERE \
  Height > 1.5 \
  and Indicator = 1\
  ORDER BY  \
       Height,\
       Weight;"
PersonFrame1 = pd.read_sql_query(sSQL, conn1)
DimPerson = PersonFrame1
DimPersonIndex = DimPerson.set_index(["PersonID"], inplace=False)
sTable = "Dim-BMI-Horizontal"
print("\n#################################")
print("Storing :", sDatabaseName, "\n Table:", sTable)
print("\n#################################")
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")
print("################################")
sTable = "Dim-BMI-Horizontal"
print("Loading :", sDatabaseName, " Table:", sTable)
print("################################")
sSQL = "SELECT * FROM [" + sTable + "];"
PersonFrame2 = pd.read_sql_query(sSQL, conn2)
print("################################")
print("Full Data Set (Rows):", PersonFrame0.shape[0])
print("Full Data Set (Columns):", PersonFrame0.shape[1])
print("################################")
print("Horizontal Data Set (Rows):", PersonFrame2.shape[0])
print("Horizontal Data Set (Columns):", PersonFrame2.shape[1])

print("################################")

```

- **OUTPUT**




2. <b>Vertical style</b>
```python
# C:\VKHCG\01-Vermeulen\05-Organise\ Organize-Vertical.py
import sys
import os
import pandas as pd
import sqlite3 as sq
print("6B. Vertical style")
Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
Company='01-Vermeulen'
sDataWarehouseDir=Base + '/99-DW'
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)
sDatabaseName=sDataWarehouseDir + '/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)
sDatabaseName=sDataWarehouseDir + '/datamart.db'
conn2 = sq.connect(sDatabaseName)
print('################################')
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
print('################################')
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
print('################################')
sSQL="SELECT \
       Height,\
       Weight,\
       Indicator\
  FROM [Dim-BMI];"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)
sTable = 'Dim-BMI-Vertical'
print('\n#################################')
print('Storing :',sDatabaseName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")
print('################')  
sTable = 'Dim-BMI-Vertical'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI-Vertical];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)
print('################################')
print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('################################')
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])
print('################################')
```

- **OUTPUT**



3. <b>Island style</b>

```python
# C:\VKHCG\01-Vermeulen\05-Organise\Organize-Island.py
import sys
import os
import pandas as pd
import sqlite3 as sq
Base='C:/VKHCG'
print("6C. Island style")
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
Company='01-Vermeulen'
sDataWarehouseDir=Base + '/99-DW'
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)
sDatabaseName=sDataWarehouseDir + '/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)
sDatabaseName=sDataWarehouseDir + '/datamart.db'
conn2 = sq.connect(sDatabaseName)
print('################')  
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
print('################')  
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)

sSQL="SELECT \
       Height,\
       Weight,\
       Indicator\
  FROM [Dim-BMI]\
  WHERE Indicator > 2\
  ORDER BY  \
       Height,\
       Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)
sTable = 'Dim-BMI-Vertical'
print('\n#################################')
print('Storing :',sDatabaseName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")
print('################################')
sTable = 'Dim-BMI-Vertical'
print('Loading :',sDatabaseName,' Table:',sTable)
print('################################')
sSQL="SELECT * FROM [Dim-BMI-Vertical];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)
print('################################')
print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('################################')
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])
print('################################')
```

- **OUTPUT**



4. <b>Secure Vault style</b>

```python
# C:\VKHCG\01-Vermeulen\05-Organise\Organize-Secure-Vault.py
import sys
import os
import pandas as pd
import sqlite3 as sq
print("6D. Secure Vault style")
Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
Company='01-Vermeulen'
sDataWarehouseDir=Base + '/99-DW'
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)
sDatabaseName=sDataWarehouseDir + '/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)
sDatabaseName=sDataWarehouseDir + '/datamart.db'
conn2 = sq.connect(sDatabaseName)
print('################')  
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
print('################')  
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)

sSQL="SELECT \
       Height,\
       Weight,\
       Indicator,\
       CASE Indicator\
       WHEN 1 THEN 'Pip'\
       WHEN 2 THEN 'Norman'\
       WHEN 3 THEN 'Grant'\
       ELSE 'Sam'\
       END AS Name\
  FROM [Dim-BMI]\
  WHERE Indicator > 2\
  ORDER BY  \
       Height,\
       Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)
sTable = 'Dim-BMI-Secure'
print('\n#################################')
print('Storing :',sDatabaseName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")
print('################################')
sTable = 'Dim-BMI-Secure'
print('Loading :',sDatabaseName,' Table:',sTable)
print('################################')
sSQL="SELECT * FROM [Dim-BMI-Secure] WHERE Name = 'Sam';"
PersonFrame2=pd.read_sql_query(sSQL, conn2)
print('################################')
print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('################################')
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])
print('Only Sam Data')
print(PersonFrame2.head())
print('################################')
```

- **OUTPUT**



*******************

## prac8A

- Transforming Data
- a. Building data warehouse

```python

import sys
import os
from datetime import datetime
from pytz import timezone
import pandas as pd
import sqlite3 as sq
import uuid
print("8A. Building data warehouse")
pd.options.mode.chained_assignment = None
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
Company='01-Vermeulen'
sDataBaseDir=Base + '/' + Company + '/04-Transform/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName=sDataBaseDir + '/Vermeulen.db'
conn1 = sq.connect(sDatabaseName)
################################################################
sDataVaultDir=Base + '/88-DV'
if not os.path.exists(sDataVaultDir):
    os.makedirs(sDataVaultDir)
################################################################
sDatabaseName=sDataVaultDir + '/datavault.db'
conn2 = sq.connect(sDatabaseName)
################################################################
sDataWarehouseDir=Base + '/99-DW'
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)
################################################################
sDatabaseName=sDataWarehouseDir + '/datawarehouse.db'
conn3 = sq.connect(sDatabaseName)
################################################################
sSQL=" SELECT DateTimeValue FROM [Hub-Time];"
DateDataRaw=pd.read_sql_query(sSQL, conn2)
DateData=DateDataRaw.head(1000)
print(DateData)
################################################################
print('\n#################################')
print('Time Dimension')
print('\n#################################')
t=0
mt=DateData.shape[0]
for i in range(mt):
    BirthZone = ('Atlantic/Reykjavik','Europe/London','UCT')
    for j in range(len(BirthZone)):    
        t+=1
        print(t,mt*3)
        BirthDateUTC = datetime.strptime(DateData['DateTimeValue'][i],"%Y-%m-%d %H:%M:%S") 
        BirthDateZoneUTC=BirthDateUTC.replace(tzinfo=timezone('UTC')) 
        BirthDateZoneStr=BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S") 
        BirthDateZoneUTCStr=BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")
        BirthDate = BirthDateZoneUTC.astimezone(timezone(BirthZone[j])) 
        BirthDateStr=BirthDate.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")
        BirthDateLocal=BirthDate.strftime("%Y-%m-%d %H:%M:%S")
        ################################################################
        IDTimeNumber=str(uuid.uuid4()) 
        TimeLine=[('TimeID', [str(IDTimeNumber)]),
                  ('UTCDate', [str(BirthDateZoneStr)]),
                  ('LocalTime', [str(BirthDateLocal)]),
                  ('TimeZone', [str(BirthZone)])] 
        if t==1:
            TimeFrame = pd.DataFrame.from_dict(dict(TimeLine)) 
        else:
            TimeRow = pd.DataFrame.from_dict(dict(TimeLine))
            TimeFrame = pd.concat([TimeFrame, TimeRow])
################################################################
DimTime=TimeFrame
DimTimeIndex=DimTime.set_index(['TimeID'],inplace=False)
################################################################
sTable = 'Dim-Time'
print('\n#################################')
print('Storing :',sDatabaseName,'\n Table:',sTable)
print('\n#################################')
DimTimeIndex.to_sql(sTable, conn1, if_exists="replace")
DimTimeIndex.to_sql(sTable, conn3, if_exists="replace")
################################################################
sSQL=" SELECT " + \
      " FirstName," + \
      " SecondName," + \
      " LastName," + \
      " BirthDateKey " + \
      " FROM [Hub-Person];"
PersonDataRaw=pd.read_sql_query(sSQL, conn2)
PersonData=PersonDataRaw.head(1000)
################################################################
print('\n#################################')
print('Dimension Person')
print('\n#################################')
t=0
mt=DateData.shape[0]
for i in range(mt): 
    t+=1
    print(t,mt) 
    FirstName = str(PersonData["FirstName"])
    SecondName = str(PersonData["SecondName"])
    if len(SecondName) > 0:
        SecondName=""
    LastName = str(PersonData["LastName"])
    BirthDateKey = str(PersonData["BirthDateKey"])
    ###############################################################
    IDPersonNumber=str(uuid.uuid4()) 
    PersonLine=[('PersonID', [str(IDPersonNumber)]),
                  ('FirstName', [FirstName]),
                  ('SecondName', [SecondName]),
                  ('LastName', [LastName]),
                  ('Zone', [str('UTC')]),
                  ('BirthDate', [BirthDateKey])] 
    if t==1:
        PersonFrame = pd.DataFrame.from_dict(dict(PersonLine)) 
    else:
        PersonRow = pd.DataFrame.from_dict(dict(PersonLine)) 
        PersonFrame = pd.concat([PersonFrame, PersonRow])
################################################################
DimPerson=PersonFrame
print(DimPerson)
DimPersonIndex=DimPerson.set_index(['PersonID'],inplace=False)
################################################################
sTable = 'Dim-Person'
print('\n#################################')
print('Storing :',sDatabaseName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn1, if_exists="replace")
DimPersonIndex.to_sql(sTable, conn3, if_exists="replace")
###############################################################
sTable.dtypes

```

- **OUTPUT**



*******************

## prac8B

- b. Simple Linear Regression

```python
################################################################
# C:\VKHCG\01-Vermeulen\04-Transform\ Transform-BMI.py
################################################################
import sys
import os
import pandas as pd
import sqlite3 as sq
import matplotlib.pyplot as plt
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
################################################################
Company='01-Vermeulen'
################################################################
sDataBaseDir=Base + '/' + Company + '/04-Transform/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName=sDataBaseDir + '/Vermeulen.db'
conn1 = sq.connect(sDatabaseName)
################################################################
sDataVaultDir=Base + '/88-DV'
if not os.path.exists(sDataVaultDir):
    os.makedirs(sDataVaultDir)
################################################################
sDatabaseName=sDataVaultDir + '/datavault.db'
conn2 = sq.connect(sDatabaseName)
################################################################
sDataWarehouseDir=Base + '/99-DW'
if not os.path.exists(sDataWarehouseDir):
    os.makedirs(sDataWarehouseDir)
################################################################
sDatabaseName=sDataWarehouseDir + '/datawarehouse.db'
conn3 = sq.connect(sDatabaseName)
################################################################
t=0
tMax=((300-100)/10)*((300-30)/5)
for heightSelect in range(100,300,10):
    for weightSelect in range(30,300,5):
        height = round(heightSelect/100,3)
        weight = int(weightSelect)
        bmi = weight/(height*height)        
        if bmi <= 18.5:
            BMI_Result=1    
        elif bmi > 18.5 and bmi < 25:
            BMI_Result=2    
        elif bmi > 25 and bmi < 30:
            BMI_Result=3    
        elif bmi > 30:
            BMI_Result=4    
        else:
            BMI_Result=0
        PersonLine=[('PersonID', [str(t)]),
                        ('Height', [height]),
                        ('Weight', [weight]),
                        ('bmi', [bmi]),
                        ('Indicator', [BMI_Result])
        ] 
        t+=1
        print('Row:',t,'of',tMax)
        if t==1:
            PersonFrame = pd.DataFrame.from_dict(dict(PersonLine)) 
        else:
            PersonRow = pd.DataFrame.from_dict(dict(PersonLine)) 
            PersonFrame = pd.concat([PersonFrame, PersonRow])
################################################################
DimPerson=PersonFrame
DimPersonIndex=DimPerson.set_index(['PersonID'],inplace=False)
################################################################
sTable = 'Transform-BMI'
print('\n#################################')
print('Storing :',sDatabaseName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn1, if_exists="replace")
################################################################
################################################################
sTable = 'Person-Satellite-BMI'
print('\n#################################')
print('Storing :',sDatabaseName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")
################################################################
################################################################
sTable = 'Dim-BMI'
print('\n#################################')
print('Storing :',sDatabaseName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn3, if_exists="replace")
################################################################

fig = plt.figure()

PlotPerson=DimPerson[DimPerson['Indicator']==1]
x=PlotPerson['Height']
y=PlotPerson['Weight']
plt.plot(x, y, ".")
PlotPerson=DimPerson[DimPerson['Indicator']==2]
x=PlotPerson['Height']
y=PlotPerson['Weight']
plt.plot(x, y, "o")
PlotPerson=DimPerson[DimPerson['Indicator']==3]
x=PlotPerson['Height']
y=PlotPerson['Weight']
plt.plot(x, y, "+")
PlotPerson=DimPerson[DimPerson['Indicator']==4]
x=PlotPerson['Height']
y=PlotPerson['Weight']
plt.plot(x, y, "^")
plt.axis('tight')
plt.title("BMI Curve")
plt.xlabel("Height(meters)")
plt.ylabel("Weight(kg)")
plt.plot()

```

- **OUTPUT**



*******************

## prac9A

- Generating Reports
- a. Vermeulen PLC

```python
################################################################
# C:\VKHCG\01-Vermeulen\06-Report\Raport-Network-Routing-Customer.py
######################################################################
print('9A. Vermeulen PLC')
import sys
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
################################################################
pd.options.mode.chained_assignment = None
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + 'VKHCG'
else:
    Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sInputFileName='02-Assess/01-EDS/02-Python/Assess-Network-Routing-Customer.csv'
################################################################
sOutputFileName1='06-Report/01-EDS/02-Python/Report-Network-Routing-Customer.gml'
sOutputFileName2='06-Report/01-EDS/02-Python/Report-Network-Routing-Customer.png'
Company='01-Vermeulen'
################################################################
################################################################
### Import Country Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
CustomerDataRaw=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
CustomerData=CustomerDataRaw.head(100)
print('Loaded Country:',CustomerData.columns.values)
print('################################')
################################################################
print(CustomerData.head())
print(CustomerData.shape)
################################################################
G=nx.Graph()
for i in range(CustomerData.shape[0]):
    for j in range(CustomerData.shape[0]):
        Node0=CustomerData['Customer_Country_Name'][i]
        Node1=CustomerData['Customer_Country_Name'][j]
        if Node0 != Node1:
            G.add_edge(Node0,Node1)

for i in range(CustomerData.shape[0]):
    Node0=CustomerData['Customer_Country_Name'][i]
    Node1=CustomerData['Customer_Place_Name'][i] + '('+ CustomerData['Customer_Country_Name'][i] + ')'
    Node2='('+ "{:.9f}".format(CustomerData['Customer_Latitude'][i]) + ')\
    ('+ "{:.9f}".format(CustomerData['Customer_Longitude'][i]) + ')'
    if Node0 != Node1:
        G.add_edge(Node0,Node1)
    if Node1 != Node2:
        G.add_edge(Node1,Node2)

print('Nodes:', G.number_of_nodes())   
print('Edges:', G.number_of_edges()) 
################################################################ 
sFileName=Base + '/' + Company + '/' + sOutputFileName1
print('################################')
print('Storing :',sFileName)
print('################################')
nx.write_gml(G, sFileName)      
################################################################
sFileName=Base + '/' + Company + '/' + sOutputFileName2
print('################################')
print('Storing Graph Image:',sFileName)
print('################################')

plt.figure(figsize=(25, 25))
pos=nx.spectral_layout(G,dim=2)
nx.draw_networkx_nodes(G,pos, node_color='k', node_size=10, alpha=0.8)
nx.draw_networkx_edges(G, pos,edge_color='r', arrows=False, style='dashed')
nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif',font_color='b')
plt.axis('off')
plt.savefig(sFileName,dpi=600)
plt.show()
################################################################
print('################################')
print('### Done!! #####################')
print('################################')
################################################################
```

- **OUTPUT**



*******************

## prac9B

- b. Krennwallner AG

```python
################################################################
# -*- coding: utf-8 -*-
# C:\VKHCG\02-Krennwallner\06-Report\Report_Billboard.py
################################################################
print('9B. Krennwallner AG')
import sys
import os
import pandas as pd
from folium.plugins import FastMarkerCluster, HeatMap
from folium import Marker, Map
import webbrowser
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################

sFileName=Base+'/02-Krennwallner/01-Retrieve/01-EDS/02-Python/Retrieve_DE_Billboard_Locations.csv'
df = pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
df.fillna(value=0, inplace=True)
print(df.shape)
################################################################
t=0
for i in range(df.shape[0]):
    try:
        sLongitude=df["Longitude"][i]
        sLongitude=float(sLongitude)
    except Exception:
        sLongitude=float(0.0)
        
    try:
        sLatitude=df["Latitude"][i]
        sLatitude=float(sLatitude)
    except Exception:
        sLatitude=float(0.0)
        
    try:
        sDescription=df["Place_Name"][i] + ' (' + df["Country"][i]+')'
    except Exception:
        sDescription='VKHCG'
    
    if sLongitude != 0.0 and sLatitude != 0.0:
        DataClusterList=list([sLatitude, sLongitude])
        DataPointList=list([sLatitude, sLongitude, sDescription])
        t+=1
        if t==1:
            DataCluster=[DataClusterList]
            DataPoint=[DataPointList]
        else:
            DataCluster.append(DataClusterList)
            DataPoint.append(DataPointList)
data=DataCluster
pins=pd.DataFrame(DataPoint)
pins.columns = [ 'Latitude','Longitude','Description']
################################################################
stops_map1 = Map(location=[48.1459806, 11.4985484], zoom_start=5)
marker_cluster = FastMarkerCluster(data).add_to(stops_map1)
sFileNameHtml=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/Billboard1.html'
stops_map1.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))
################################################################
stops_map2 = Map(location=[48.1459806, 11.4985484], zoom_start=5)
for name, row in pins.iloc[:100].iterrows():
    Marker([row["Latitude"],row["Longitude"]], popup=row["Description"]).add_to(stops_map2)
sFileNameHtml=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/Billboard2.html'
stops_map2.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))
################################################################
stops_heatmap = Map(location=[48.1459806, 11.4985484], zoom_start=5)
stops_heatmap.add_child(HeatMap([[row["Latitude"], row["Longitude"]] for name, row in pins.iloc[:100].iterrows()]))
sFileNameHtml=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/Billboard_heatmap.html'
stops_heatmap.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))
################################################################
print('### Done!! ############################################')
################################################################
```

- **OUTPUT**



*******************

## prac10A

- Processing Data
- a. Build the time Hub, Link and Satellite

```python
################################################################
# -*- coding: utf-8 -*-
# C:\VKHCG\01-Vermeulen\03-Process\Process_Time.py
################################################################

import sys
import os
from datetime import datetime
from datetime import timedelta
from pytz import timezone, all_timezones
import pandas as pd
import sqlite3 as sq
from pandas.io import sql
import uuid

print("10A. Build the time Hub, Link and Satellite")
pd.options.mode.chained_assignment = None
################################################################
if sys.platform == "linux":
    Base = os.path.expanduser("~") + "/VKHCG"
else:
    Base = "C:/VKHCG"
print("################################")
print("Working Base :", Base, " using ", sys.platform)
print("################################")
################################################################
Company = "01-Vermeulen"
InputDir = "00-RawData"
InputFileName = "VehicleData.csv"
################################################################
sDataBaseDir = Base + "/" + Company + "/03-Process/SQLite"
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName = sDataBaseDir + "/Hillman.db"
conn1 = sq.connect(sDatabaseName)
################################################################
sDataVaultDir = Base + "/88-DV"
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName = sDataVaultDir + "/datavault.db"
conn2 = sq.connect(sDatabaseName)
################################################################
base = datetime(2018, 1, 1, 0, 0, 0)
numUnits = 10 * 365 * 24
################################################################
date_list = [base - timedelta(hours=x) for x in range(0, numUnits)]
t = 0
for i in date_list:
    now_utc = i.replace(tzinfo=timezone("UTC"))
    sDateTime = now_utc.strftime("%Y-%m-%d %H:%M:%S")
    print(sDateTime)
    sDateTimeKey = sDateTime.replace(" ", "-").replace(":", "-")
    t += 1
    IDNumber = str(uuid.uuid4())
    TimeLine = [
        ("ZoneBaseKey", ["UTC"]),
        ("IDNumber", [IDNumber]),
        ("nDateTimeValue", [now_utc]),
        ("DateTimeValue", [sDateTime]),
        ("DateTimeKey", [sDateTimeKey]),
    ]
    if t == 1:
        TimeFrame = pd.DataFrame.from_dict(TimeLine)
    else:
        TimeRow = pd.DataFrame.from_dict(TimeLine)
        TimeFrame = TimeFrame.append(TimeRow)
################################################################
TimeHub = TimeFrame[["IDNumber", "ZoneBaseKey", "DateTimeKey", "DateTimeValue"]]
TimeHubIndex = TimeHub.set_index(["IDNumber"], inplace=False)
################################################################
TimeFrame.set_index(["IDNumber"], inplace=True)
################################################################
sTable = "Process-Time"
print("Storing :", sDatabaseName, " Table:", sTable)
TimeHubIndex.to_sql(sTable, conn1, if_exists="replace")
################################################################
sTable = "Hub-Time"
print("Storing :", sDatabaseName, " Table:", sTable)
TimeHubIndex.to_sql(sTable, conn2, if_exists="replace")
################################################################
active_timezones = all_timezones
z = 0
for zone in active_timezones:
    t = 0
    for j in range(TimeFrame.shape[0]):
        now_date = TimeFrame["nDateTimeValue"][j]
        DateTimeKey = TimeFrame["DateTimeKey"][j]
        now_utc = now_date.replace(tzinfo=timezone("UTC"))
        sDateTime = now_utc.strftime("%Y-%m-%d %H:%M:%S")
        now_zone = now_utc.astimezone(timezone(zone))
        sZoneDateTime = now_zone.strftime("%Y-%m-%d %H:%M:%S")
        print(sZoneDateTime)
        t += 1
        z += 1
        IDZoneNumber = str(uuid.uuid4())
        TimeZoneLine = [
            ("ZoneBaseKey", ["UTC"]),
            ("IDZoneNumber", [IDZoneNumber]),
            ("DateTimeKey", [DateTimeKey]),
            ("UTCDateTimeValue", [sDateTime]),
            ("Zone", [zone]),
            ("DateTimeValue", [sZoneDateTime]),
        ]
        if t == 1:
            TimeZoneFrame = pd.DataFrame.from_dict(TimeZoneLine)
        else:
            TimeZoneRow = pd.DataFrame.from_dict(TimeZoneLine)
            TimeZoneFrame = TimeZoneFrame.append(TimeZoneRow)

    TimeZoneFrameIndex = TimeZoneFrame.set_index(["IDZoneNumber"], inplace=False)
    sZone = zone.replace("/", "-").replace(" ", "")
    #############################################################
    sTable = "Process-Time-" + sZone
    print("Storing :", sDatabaseName, " Table:", sTable)
    TimeZoneFrameIndex.to_sql(sTable, conn1, if_exists="replace")
    #################################################################
    #############################################################
    sTable = "Satellite-Time-" + sZone
    print("Storing :", sDatabaseName, " Table:", sTable)
    TimeZoneFrameIndex.to_sql(sTable, conn2, if_exists="replace")
#################################################################
print("################")
print("Vacuum Databases")
sSQL = "VACUUM;"
sql.execute(sSQL, conn1)
sql.execute(sSQL, conn2)
print("################")
#################################################################
print("### Done!! ############################################")
#################################################################
```

- **OUTPUT**



*******************

## prac10B

- b. Human-Environment Interaction

```python
################################################################
# -*- coding: utf-8 -*-
# C:\VKHCG\01-Vermeulen\03-Process\Process_Location.py
################################################################
import sys
import os
import pandas as pd
import sqlite3 as sq
from pandas.io import sql
import uuid

print("10B. Human-Environment Interaction")
################################################################
if sys.platform == "linux":
    Base = os.path.expanduser("~") + "/VKHCG"
else:
    Base = "C:/VKHCG"
print("################################")
print("Working Base :", Base, " using ", sys.platform)
print("################################")
################################################################
Company = "01-Vermeulen"
InputAssessGraphName = "Assess_All_Animals.gml"
EDSAssessDir = "02-Assess/01-EDS"
InputAssessDir = EDSAssessDir + "/02-Python"
################################################################
sFileAssessDir = Base + "/" + Company + "/" + InputAssessDir
if not os.path.exists(sFileAssessDir):
    os.makedirs(sFileAssessDir)
################################################################
sDataBaseDir = Base + "/" + Company + "/03-Process/SQLite"
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName = sDataBaseDir + "/Vermeulen.db"
conn1 = sq.connect(sDatabaseName)
################################################################
sDataVaultDir = Base + "/88-DV"
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName = sDataVaultDir + "/datavault.db"
conn2 = sq.connect(sDatabaseName)
################################################################
t = 0
tMax = 360 * 180
################################################################
for Longitude in range(-180, 180, 10):
    for Latitude in range(-90, 90, 10):
        t += 1
        IDNumber = str(uuid.uuid4())
        LocationName = (
            "L"
            + format(round(Longitude, 3) * 1000, "+07d")
            + "-"
            + format(round(Latitude, 3) * 1000, "+07d")
        )
        print("Create:", t, " of ", tMax, ":", LocationName)
        LocationLine = [
            ("ObjectBaseKey", ["GPS"]),
            ("IDNumber", [IDNumber]),
            ("LocationNumber", [str(t)]),
            ("LocationName", [LocationName]),
            ("Longitude", [Longitude]),
            ("Latitude", [Latitude]),
        ]
        if t == 1:
            LocationFrame = pd.DataFrame.from_dict(LocationLine)
        else:
            LocationRow = pd.DataFrame.from_dict(LocationLine)
            LocationFrame = LocationFrame.append(LocationRow)

################################################################
LocationHubIndex = LocationFrame.set_index(["IDNumber"], inplace=False)
################################################################
sTable = "Process-Location"
print("Storing :", sDatabaseName, " Table:", sTable)
LocationHubIndex.to_sql(sTable, conn1, if_exists="replace")
#################################################################
sTable = "Hub-Location"
print("Storing :", sDatabaseName, " Table:", sTable)
LocationHubIndex.to_sql(sTable, conn2, if_exists="replace")
#################################################################
print("################")
print("Vacuum Databases")
sSQL = "VACUUM;"
sql.execute(sSQL, conn1)
sql.execute(sSQL, conn2)
print("################")
################################################################
print("### Done!! ############################################")
################################################################
```

- **OUTPUT**



*******************

## prac10C

- c. Forecasting

```python
################################################################
# C:\VKHCG\01-Vermeulen\03-Process\Process_Location.py
##################################################################
import sys
import os
import sqlite3 as sq
import quandl
import pandas as pd
print("10C. Forecasting")
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
    
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
Company='04-Clark'
sInputFileName='00-RawData/VKHCG_Shares.csv'
sOutputFileName='Shares.csv'
################################################################
sDataBaseDir=Base + '/' + Company + '/03-Process/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir) 
################################################################
sFileDir1=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir1):
    os.makedirs(sFileDir1) 
################################################################
sFileDir2=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir2):
    os.makedirs(sFileDir2) 
################################################################
sFileDir3=Base + '/' + Company + '/03-Process/01-EDS/02-Python'
if not os.path.exists(sFileDir3):
    os.makedirs(sFileDir3) 
################################################################
sDatabaseName=sDataBaseDir + '/clark.db'
conn = sq.connect(sDatabaseName)
################################################################
### Import Share Names Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
RawData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
RawData.drop_duplicates(subset=None, keep='first', inplace=True)
print('Rows   :',RawData.shape[0])
print('Columns:',RawData.shape[1])
print('################')   
################################################################
sFileName=sFileDir1 + '/Retrieve_' + sOutputFileName
print('################################')
print('Storing :', sFileName)
print('################################')
RawData.to_csv(sFileName, index = False)
print('################################')  
################################################################
sFileName=sFileDir2 + '/Assess_' + sOutputFileName
print('################################')
print('Storing :', sFileName)
print('################################')
RawData.to_csv(sFileName, index = False)
print('################################')  
################################################################
sFileName=sFileDir3 + '/Process_' + sOutputFileName
print('################################')
print('Storing :', sFileName)
print('################################')
RawData.to_csv(sFileName, index = False)
print('################################')
################################################################
### Import Shares Data Details
################################################################
nShares=RawData.shape[0]
#nShares=6
for sShare in range(nShares):
    sShareName=str(RawData['Shares'][sShare])
    ShareData = quandl.get(sShareName)
    UnitsOwn=RawData['Units'][sShare]
    ShareData['UnitsOwn']=ShareData.apply(lambda row:(UnitsOwn),axis=1)
    ShareData['ShareCode']=ShareData.apply(lambda row:(sShareName),axis=1)
    print('################') 
    print('Share  :',sShareName) 
    print('Rows   :',ShareData.shape[0])
    print('Columns:',ShareData.shape[1])
    print('################')  
    #################################################################
    print('################')  
    sTable=str(RawData['sTable'][sShare])
    print('Storing :',sDatabaseName,' Table:',sTable)
    ShareData.to_sql(sTable, conn, if_exists="replace")
    print('################')  
    ################################################################
    sOutputFileName = sTable.replace("/","-") + '.csv'
    sFileName=sFileDir1 + '/Retrieve_' + sOutputFileName
    print('################################')
    print('Storing :', sFileName)
    print('################################')
    ShareData.to_csv(sFileName, index = False)
    print('################################')
    ################################################################
    sOutputFileName = sTable.replace("/","-") + '.csv'
    sFileName=sFileDir2 + '/Assess_' + sOutputFileName
    print('################################')
    print('Storing :', sFileName)
    print('################################')
    ShareData.to_csv(sFileName, index = False)
    print('################################')
    ################################################################
    sOutputFileName = sTable.replace("/","-") + '.csv'
    sFileName=sFileDir3 + '/Process_' + sOutputFileName
    print('################################')
    print('Storing :', sFileName)
    print('################################')
    ShareData.to_csv(sFileName, index = False)
    print('################################')
################################################################
################################################################
print('### Done!! ############################################')
################################################################
```

- **OUTPUT**



*******************

### [Go To Top](#data-science-practicals)











