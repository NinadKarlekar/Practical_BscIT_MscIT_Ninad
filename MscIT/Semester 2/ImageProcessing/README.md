# Image Processing

M. Sc (Information Technology)
PSIT2P4 Image Processing

## Index

| Sr.No. | Name | README |
|---	|---	|---	|
| [Prac1A](/MscIT/Semester%202/ImageProcessing/Practical%201/)  <br> [Prac1B](/MscIT/Semester%202/ImageProcessing/Practical%201/) | 1A. **Upsampling and downsampling** on Image/speech Signal. <br> 1B. **Fast Fourier Transform** to compute DFT. 	| [Prac1A](#prac1A) <br> [Prac1B](#prac1B) |
| [Prac2](/MscIT/Semester%202/ImageProcessing/Practical%202/) 	| 2. Write program to perform **Convolution and correlation of gray scale image**. 	| [Prac2](#prac2) 	|
|  [Prac3](/MscIT/Semester%202/ImageProcessing/Practical%203/)	|  3. Write program to perform the **DFT of 4x4 Gray Scale Image**. 	| [Prac3](#prac3) 	|
| [Prac4A](/MscIT/Semester%202/ImageProcessing/Practical%201/)  <br> [Prac4B](/MscIT/Semester%202/ImageProcessing/Practical%201/) <br> [Prac4C](/MscIT/Semester%202/ImageProcessing/Practical%201/) <br> [Prac4D](/MscIT/Semester%202/ImageProcessing/Practical%201/)	| 4A. Log and Power-law transformations <br> 4B. Contrast adjustments <br> 4C. Histogram equalization <br> 4D. Thresholding, and halftoning operations 	|  [Prac4A](#prac4A) <br> [Prac4B](#prac4B)	<br> [Prac4C](#prac4C) <br> [Prac4D](#prac4D) |
|  [Prac5](/MscIT/Semester%202/ImageProcessing/Practical%205/)	| 5. Write a program to apply various enhancements on images using image derivatives by implementing **Gradient and Laplacian operations**. 	|  [Prac5](#prac5)	|
| [Prac6](/MscIT/Semester%202/ImageProcessing/Practical%206/) 	| 6. Write a program to apply various image enhancement using image derivatives by implementing **smoothing, sharpening, and unsharp masking filters** for generating suitable images for specific application requirements. 	| [Prac6](#prac6) 	|
| [Prac7](/MscIT/Semester%202/ImageProcessing/Practical%207/) 	| 7. Write a program to Apply **edge detection techniques such as Sobel and Canny** to extract meaningful information from the given image samples. 	|  [Prac7](#prac7)	|
|  [Prac8](/MscIT/Semester%202/ImageProcessing/Practical%208/)	| 8. Write the program to implement various **morphological image processing techniques**.**`(EROSION & DIALATION , OPENING & CLOSING)`** 	| [Prac8](#prac8) 	|
|  [Prac9](/MscIT/Semester%202/ImageProcessing/Practical%209/)	| 9. **Image Segmentation**. 	| [Prac9](#prac9) 	|


******************
---------------------

## prac1A

1A. **Upsampling and downsampling** on Image/speech Signal.


<details>
<summary>CODE</summary>


```python
# Downsampling

import os 
os.sys.path 
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

img1 = cv2.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/nativeplace.jpg', 0) 
[m, n] = img1.shape 
print('Original Image Shape:', m, n) 
print('Original Image:') 
plt.imshow(img1, cmap="gray") 
f = 4
img2 = np.zeros((m//f, n//f), dtype=int)
for i in range(0, m, f): 
 for j in range(0, n, f): 
  try: 
   img2[i//f][j//f] = img1[i][j] 
  except IndexError: 
   pass 	

[a, b] = img2.shape 
print('Down Sampled Image Shape:', a, b) 
print("-----------------------")
print('Down Sampled Image:') 
plt.imshow(img2, cmap="gray")


```

```python

# Upsampling
img3 = np.zeros((m, n), dtype=int)

for i in range(0, m-1, f): 
    for j in range(0, n-1, f): 
        try:
            img3[i, j] = img2[i//f][j//f]
        except IndexError: 
            pass	

for i in range(1, m-(f-1), f): 
    for j in range(0, n-(f-1)): 
        img3[i:i+(f-1), j] = img3[i-1, j] 

for i in range(0, m-1): 
    for j in range(1, n-1, f): 
        img3[i, j:j+(f-1)] = img3[i, j-1] 

[c, d] = img3.shape 

print('Original Image Shape:', m, n)
print("-----------------------") 
print('Down Sampled Image Shape:', a, b) 
print("-----------------------") 
print('UP Sampled Image Shape:', c, d) 
print("-----------------------") 

print('Up Sampled Image:') 
plt.imshow(img3, cmap="gray")


```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/e091006b-da31-4b50-a876-47b35522faf3" width="400px"  alt ="DIP_prac1A_1">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/409e6978-39f3-424f-89d5-b22451734957" width="400px"  alt ="DIP_prac1A_2">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/2cedeb09-766b-4bc2-972b-9cf5c6b55ad6" width="400px"  alt ="DIP_prac1A_3">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/fdbd751b-41d3-46b5-aa78-fac723631b32" width="400px"  alt ="DIP_prac1A_4">


</details>


[🔝](#index)

**************

## prac1B

1B. Fast Fourier Transform to compute DFT.


<details>
<summary>CODE</summary>


```python
import os 
os.sys.path 
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

# scipy.stats.signaltonoise() was deprecated in scipy 0.16.0 and removed in 1.0.0. 
import numpy as np
def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

im = np.array(Image.open('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/elephant.jpg').convert('L'))
freq = np.fft.fft2(im)
im1 = np.fft.ifft2(freq).real
snr = signaltonoise(im1, axis=None)

print('SNR for the image obtained after reconstruction = ' + str(snr))
assert(np.allclose(im, im1))

plt.figure(figsize=(20, 10))
plt.subplot(121), plt.imshow(im, cmap='gray'), plt.axis('off')
plt.title('Original Image', size=20)
plt.subplot(122), plt.imshow(im1, cmap='gray'), plt.axis('off')
plt.title('Image Obtained after Reconstruction', size=20)
plt.show()

```



</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/2a6b831f-212e-44c1-a0e6-b22cf5d56047" width="600px"  alt ="DIP_prac1B_1">




</details>


[🔝](#index)

**************

## prac2

2. Write program to perform **Convolution and correlation of gray scale image**.


<details>
<summary>CODE</summary>


```python
# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/nativeplace.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots(1, figsize=(12,8))
plt.imshow(image)

abc=np.ones((3,3))
kernel = np.ones((3, 3), np.float32) / 9
img = cv2.filter2D(image, -1, kernel)
fig, ax = plt.subplots(1,2,figsize=(10,6))
ax[0].imshow(image)
ax[1].imshow(img)

#Sharpning
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
img = cv2.filter2D(image, -1, kernel)
fig, ax = plt.subplots(1,2,figsize=(10,6))
ax[0].imshow(image)
ax[1].imshow(img)
```


</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/8fd2643f-9df2-4ce0-833e-f758900cc1b6" width="600px"  alt ="DIP_prac2_1">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/2b019fb5-a0bf-4f92-b66e-063452c476ce" width="600px"  alt ="DIP_prac2_2">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/8fd2643f-9df2-4ce0-833e-f758900cc1b6" width="600px"  alt ="DIP_prac2_3">


</details>


[🔝](#index)

**************

## prac3

3. Write program to perform the **DFT of 4x4 Gray Scale Image**. 


<details>
<summary>CODE</summary>


```python
#importing packages 
import numpy as np
import cv2
from matplotlib import pyplot as plt

#getting the input image and convert to grayscale 
img = cv2.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/Dog.jpg', 0)

# Transform the image to improve the speed in the Fourier transform calculation
rows, cols = img.shape
optimalRows = cv2.getOptimalDFTSize(rows)
optimalCols = cv2.getOptimalDFTSize(cols)
optimalImg = np.zeros((optimalRows, optimalCols))
optimalImg[:rows, :cols] = img

# Calculate the discrete Fourier transform
dft = cv2.dft(np.float32(optimalImg), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# output of CV2.dft() function will be 3-D numpy array, for 2-D Output, 2D DFT as two-part complex and real part.
f_complex = dft_shift[:, :, 0] + 1j * dft_shift[:, :, 1]
f_abs = np.abs(f_complex) + 1 # lie between 1 and 1e6
f_bounded = 20 * np.log(f_abs)
f_img = 255 * f_bounded / np.max(f_bounded)
f_img = f_img.astype(np.uint8)


# Reconstruct the image using the inverse Fourier transform
i_shift = np.fft.ifftshift(dft_shift)
result = cv2.idft(i_shift)
result = cv2.magnitude(result[:, :, 0], result[:, :, 1])

# #Displaying input image, grayscale image, DFT of the Input Image 
images = [optimalImg, f_img, result]
imageTitles = ['Input image', ' DFT ', 'Reconstructed image']

for i in range(len(images)):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(imageTitles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
# for hold the Display until key press 
cv2.waitKey()
cv2.destroyAllWindows()
```



</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/9cd931f0-f6e0-410a-9378-084d058763f3" width="600px"  alt ="DIP_prac3_1">



</details>


[🔝](#index)

**************

## prac4A

4A. Log and Power-law transformations 


<details>
<summary>CODE</summary>


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Open the image.
img = cv2.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/sample.jpg')

# Apply log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)

# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)

# Save the output.
cv2.imwrite('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/log_transformed.jpg', log_transformed)

plt.imshow(img)
plt.show()
plt.imshow(log_transformed)
plt.show()

```

```python

import cv2
import numpy as np
  
# Open the image.
img = cv2.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/sample.jpg')
plt.imshow(img)
plt.show()
# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2,5]:
      
    # Apply gamma correction.
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
  
    # Save edited images.
    cv2.imwrite('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)

    plt.imshow(gamma_corrected)
    plt.show()
```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/50e0bfd1-b04d-45f3-b6f3-ad1124bbdcfc" width="300px"  alt ="DIP_prac4A_1">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/a22adcbe-1222-417c-9b72-d475378a3e26" width="300px"  alt ="DIP_prac4A_2">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/b3f52dee-90c1-4f60-93ff-4d6c9b6f83cc" width="300px"  alt ="DIP_prac4A_3">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/1330874b-8c21-45d0-867d-2884472a831a" width="300px"  alt ="DIP_prac4A_4">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/ac290902-7762-4426-ad30-1f3382ec4182" width="300px"  alt ="DIP_prac4A_5">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/25698af8-f0b0-488c-bed1-99339e3bcd48" width="300px"  alt ="DIP_prac4A_6">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/4ba08f1b-2ec9-4a87-851e-5c5e9873a0be" width="300px"  alt ="DIP_prac4A_7">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/a6d301b9-183c-4c88-adc4-80bc73c79c7a" width="300px"  alt ="DIP_prac4A_8">


</details>


[🔝](#index)

**************

## prac4B

4B. Contrast adjustments


<details>
<summary>CODE</summary>


```python
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import data, img_as_float, img_as_ubyte, exposure, io, color
from PIL import Image, ImageEnhance, ImageFilter
from scipy import ndimage, misc 
import matplotlib.pyplot as pylab 
import cv2

def plot_image(image, title=""):
  pylab.title(title, size=10) 
  pylab.imshow(image) 
  pylab.axis('off')

def plot_hist(r,g,b,title=""):
   r,g,b=img_as_ubyte(r),img_as_ubyte(g),img_as_ubyte(b) 
   pylab.hist(np.array(r).ravel(),bins=256, range=(0,256),color='r',alpha=0.3) 
   pylab.hist(np.array(g).ravel(),bins=256, range=(0,256),color='g',alpha=0.3)
   pylab.hist(np.array(b).ravel(),bins=256, range=(0,256),color='b',alpha=0.3)
   pylab.xlabel('Pixel Values', size=20) 
   pylab.ylabel('Frequency',size=20)
   pylab.title(title,size=10)

im=Image.open('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/Dog.jpg') 
im_r,im_g,im_b=im.split() 
pylab.style.use('ggplot')
pylab.figure(figsize=(15,5))
pylab.subplot(121) 
plot_image(im)
pylab.subplot(122)
plot_hist(im_r,im_g,im_b)
pylab.show()
def contrast(c):
  return 0 if c<50 else (255 if c>150 else int((255*c-22950)/48))


imc=im.point(contrast) 
im_rc,im_gc,im_bc=imc.split() 
pylab.style.use('ggplot')
pylab.figure(figsize=(15,5))
pylab.subplot(121)
plot_image(imc) 
pylab.subplot(122) 
plot_hist(im_rc,im_gc,im_bc)
pylab.yscale('log')
pylab.show()
```



</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/dff31b49-617a-4e85-839c-06618c1ffc06" width="600px"  alt ="DIP_prac4B_1">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/d56f5c24-395c-47f6-b512-ed3a42c576d9" width="600px"  alt ="DIP_prac4B_2">


</details>


[🔝](#index)

**************

## prac4C

4C. Histogram equalization


<details>
<summary>CODE</summary>


```python
#Histogram equalization
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/Dog.jpg',0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
eq = cv2.equalizeHist(img)
cdf = hist.cumsum()
cdfnmhist = cdf * hist.max()/ cdf.max()
histeq = cv2.calcHist([eq],[0],None,[256],[0,256])
cdfeq = histeq.cumsum()
cdfnmhisteq = cdfeq * histeq.max()/ cdf.max()
plt.subplot(221), plt.imshow(img,'gray')
plt.subplot(222), plt.plot(hist), plt.plot(cdfnmhist)
plt.subplot(223), plt.imshow(eq,'gray')
plt.subplot(224), plt.plot(histeq), plt.plot(cdfnmhisteq)
plt.xlim([0,256])

```



</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/934c0ac1-a761-47df-8e76-13ae0731168f" width="600px"  alt ="DIP_prac4C_1">




</details>


[🔝](#index)

**************

## prac4D

4D. Thresholding, and halftoning operations 


<details>
<summary>CODE</summary>


```python
#4D. Thresholding, and halftoning operations 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/sunflower.jpg',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
```



</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/1a7c14ef-0c99-442c-a0c4-55e19a367fbf" width="600px"  alt ="DIP_prac4D_1">




</details>


[🔝](#index)

**************

## prac5

5.Write a program to apply various enhancements on images using image derivatives by implementing **Gradient and Laplacian operations**. 


<details>
<summary>CODE</summary>


```python
import numpy as np
from scipy import signal, misc, ndimage
from skimage import filters, feature, img_as_float 
from skimage.io import imread
from skimage.color import rgb2gray 
from PIL import Image, ImageFilter 
import matplotlib.pylab as pylab
from skimage.transform import rescale

def plot_image(image, title=""):
 pylab.title(title, size=20),
 pylab.imshow(image) 
 pylab.axis('off')
def plot_hist(r,g,b,title=""):
   r,g,b=img_as_ubyte(r),img_as_ubyte(g),img_as_ubyte(b) 
   pylab.hist(np.array(r).ravel(),bins=256, range=(0,256),color='r',alpha=0.3) 
   pylab.hist(np.array(g).ravel(),bins=256, range=(0,256),color='g',alpha=0.3)
   pylab.hist(np.array(b).ravel(),bins=256, range=(0,256),color='b',alpha=0.3)
   pylab.xlabel('Pixel Values', size=20) 
   pylab.ylabel('Frequency',size=20)
   pylab.title(title,size=10)
ker_x=[[-1,1]]
ker_y=[[-1],[1]] 
im=rgb2gray(imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/sunflower.jpg')) 
im_x=signal.convolve2d(im,ker_x,mode='same') 
im_y=signal.convolve2d(im,ker_y,mode='same')
im_mag=np.sqrt(im_x**2+im_y**2) 
im_dir=np.arctan(im_y/im_x)
pylab.gray() 
pylab.figure(figsize=(30,20))
pylab.subplot(231)
plot_image(im,'Original') 
pylab.subplot(232) 
plot_image(im_x,'Gradian_x') 
pylab.subplot(233) 
plot_image(im_y,'Grad+y') 
pylab.subplot(234)
plot_image(im_mag,'||grad||') 
pylab.subplot(235) 
plot_image(im_dir, r'$\theta$') 
pylab.subplot(236)
pylab.plot(range(im.shape[1]), im[0,:], 'b-', label=r'$f(x,y)|_{x=0}$', linewidth=5)
pylab.plot(range(im.shape[1]), im_x[0,:], 'r-', label=r'$grad_x (f(x,y))|_{x=0}$') 
pylab.title(r'$grad_x (f(x,y))|_{x=0}$',size=30)
pylab.legend(prop={'size':20}) 
pylab.show()
```

```python
#LAPLACIAN
ker_laplacian=[[0,-1,0],
[-1,4,-1],
[0,-1,0]]
im=rgb2gray(imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/sunflower.jpg')) 
im1=np.clip(signal.convolve2d(im, ker_laplacian, mode='same'),0,1) 
pylab.gray()
pylab.figure(figsize=(20,10)) 
pylab.subplot(121)
plot_image(im, 'Original')
pylab.subplot(122)
plot_image(im1,'laplacian Convolved') 
pylab.show()

```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/17b6e6b1-7584-41b8-a46f-4d31ccbfb8cf" width="600px"  alt ="DIP_prac5_1">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/acab5f97-16b6-4871-9498-563c41a7c817" width="600px"  alt ="DIP_prac5_2">


</details>


[🔝](#index)

**************

## prac6

6.Write a program to apply various image enhancement using image derivatives by implementing **smoothing, sharpening, and unsharp masking filters** for generating suitable images for specific application requirements. 


<details>
<summary>CODE</summary>


```python
import numpy as np
from scipy import signal, misc, ndimage
from skimage import filters, feature, img_as_float 
from skimage.io import imread
from skimage.color import rgb2gray 
from PIL import Image, ImageFilter 
import matplotlib.pylab as pylab
from skimage.transform import rescale

def plot_hist(r,g,b,title=""):
   r,g,b=img_as_ubyte(r),img_as_ubyte(g),img_as_ubyte(b) 
   pylab.hist(np.array(r).ravel(),bins=256, range=(0,256),color='r',alpha=0.3) 
   pylab.hist(np.array(g).ravel(),bins=256, range=(0,256),color='g',alpha=0.3)
   pylab.hist(np.array(b).ravel(),bins=256, range=(0,256),color='b',alpha=0.3)
   pylab.xlabel('Pixel Values', size=20) 
   pylab.ylabel('Frequency',size=20)
   pylab.title(title,size=10)

def plot_image(image, title=""):
  pylab.title(title, size=10)
  pylab.imshow(image) 
  pylab.axis('off')

# sharpening of images
from skimage.filters import laplace 
im=rgb2gray(imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/sunflower.jpg')) 
im1=np.clip(laplace(im)+im,0,1) 
pylab.figure(figsize=(10,15))
pylab.subplot(121), plot_image(im, 'Original Image') 
pylab.subplot(122), plot_image(im1,'Sharpened Image') 
pylab.tight_layout()
pylab.show()

```


</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/3c35b047-8b53-4819-87ac-9213fedc74d9" width="600px"  alt ="DIP_prac6_1">


</details>


[🔝](#index)

**************

## prac7

7.Write a program to Apply **edge detection techniques such as Sobel and Canny** to extract meaningful information from the given image samples. 


<details>
<summary>CODE</summary>


```python
import numpy as np
from scipy import signal, misc, ndimage
from skimage import filters, feature, img_as_float 
from skimage.io import imread
from skimage.color import rgb2gray 
from PIL import Image, ImageFilter 
import matplotlib.pylab as pylab
from skimage.transform import rescale

def plot_image(image, title=""):
  pylab.title(title, size=10)
  pylab.imshow(image) 
  pylab.axis('off')

def plot_hist(r,g,b,title=""):
   r,g,b=img_as_ubyte(r),img_as_ubyte(g),img_as_ubyte(b) 
   pylab.hist(np.array(r).ravel(),bins=256, range=(0,256),color='r',alpha=0.3) 
   pylab.hist(np.array(g).ravel(),bins=256, range=(0,256),color='g',alpha=0.3)
   pylab.hist(np.array(b).ravel(),bins=256, range=(0,256),color='b',alpha=0.3)
   pylab.xlabel('Pixel Values', size=20) 
   pylab.ylabel('Frequency',size=20)
   pylab.title(title,size=10)


# Edge Detectors with scikit-image-Prewitt, roberts, sobel, scharr, laplace 
im=Image.open('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/sunflower.jpg').convert('L')
im = img_as_float(im)  # convert to floating point dtype
pylab.gray() 
pylab.figure(figsize=(15,15))
pylab.subplot(3,2,1), plot_image(im,'Original Image') 
edges=filters.roberts(im)
pylab.subplot(3,2,2), plot_image(edges,'Roberts')

edges=filters.scharr(im)
pylab.subplot(3,2,3), plot_image(edges,'Scharr')

edges=filters.sobel(im)
pylab.subplot(3,2,4), plot_image(edges,'Sobel')

edges=filters.prewitt(im)
pylab.subplot(3,2,5), plot_image(edges,'Prewitt')

edges=np.clip(filters.laplace(im), 0,1) 
pylab.subplot(3,2,6), plot_image(edges,'Laplace') 
pylab.subplots_adjust(wspace=0.1,hspace=0.1) 
pylab.show()

```

```python
#SOBEL
im = Image.open('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/sunflower.jpg').convert('L') 
im_array = np.array(im)
pylab.gray()
pylab.figure(figsize=(15,15)) 
pylab.subplot(2,2,1), plot_image(im,'Original')
pylab.subplot(2,2,2) 
edges_x=filters.sobel_h(im_array) 
plot_image(np.clip(edges_x,0,1),'sobel_x')

pylab.subplot(2,2,3) 
edges_y=filters.sobel_v(im_array) 
plot_image(np.clip(edges_y,0,1),'Sobel_y')

pylab.subplot(2,2,4) 
edges=filters.sobel(im_array) 
plot_image(np.clip(edges,0,1),'Sobel')

pylab.subplots_adjust(wspace=0.1,hspace=0.1)
pylab.show()

```

```python
#CANNY
import matplotlib.pyplot as plt 
from scipy import ndimage as ndi
from skimage.util import random_noise 
from skimage import feature

# Generate noisy image of a square
image = np.zeros((128, 128), dtype=float) 
image[32:-32, 32:-32] = 1

image = ndi.rotate(image, 15, mode='constant') 
image = ndi.gaussian_filter(image, 4)
image = random_noise(image, mode='speckle', mean=0.05)

# Compute the Canny filter for two values of sigma 
edges1 = feature.canny(image)
edges2 = feature.canny(image, sigma=3)

# display results
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax[0].imshow(image, cmap='gray') 
ax[0].set_title('noisy image', fontsize=10)

ax[1].imshow(edges1, cmap='gray') 
ax[1].set_title(r'Canny filter, $\sigma=1$', fontsize=10)

ax[2].imshow(edges2, cmap='gray') 
ax[2].set_title(r'Canny filter, $\sigma=3$', fontsize=10)

for a in ax: 
    a.axis('off')
fig.tight_layout() 
plt.show()

```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/67f15e6b-2ad2-4736-8150-a71aaf0f3520" width="600px"  alt ="DIP_prac7_1">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/b241b5e8-73d2-46f6-9e66-8bab252c4f3b" width="600px"  alt ="DIP_prac7_2">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/3184f134-e572-4208-9aad-701796bce436" width="600px"  alt ="DIP_prac7_3">


</details>


[🔝](#index)

**************

## prac8

8. Write the program to implement various **morphological image processing techniques**.**`(EROSION & DIALATION , OPENING & CLOSING)`**


<details>
<summary>CODE</summary>


```python
import cv2
import numpy as np
from matplotlib import pyplot as plt 

# For colab
# from google.colab.patches import cv2_imshow 

%matplotlib inline

from matplotlib import pyplot as plt
img = cv2.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/411525.jpg', 0) 
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
 
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(img, kernel,iterations=1)
img_dilation = cv2.dilate(img, kernel,iterations=1)
  
plt.figure(figsize=(5,5))
plt.imshow(img,cmap="gray")
plt.axis('off')
plt.title("ORIGINAL IMAGE")
plt.show()

plt.figure(figsize=(5,5))
plt.imshow(img_erosion,)
plt.axis('off')
plt.title("EROSION")
plt.show()

plt.figure(figsize=(5,5))
plt.imshow(img_dilation,cmap="gray")
plt.axis('off')
plt.title("DILATION")
plt.show()
cv2.waitKey(0)

```

```python
#Image opening and closing

from skimage.morphology import binary_opening, binary_closing, binary_erosion, binary_dilation, disk 
from skimage.color import rgb2gray 
from skimage.io import imread
from PIL import Image, ImageFilter 
import matplotlib.pylab as pylab
from skimage.transform import rescale
import numpy as np
from scipy import signal, misc, ndimage
from skimage import filters, feature, img_as_float

def plot_image(image, title=""):
  pylab.title(title, size=10)
  pylab.imshow(image) 
  pylab.axis('off')


im = rgb2gray(imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/circles1.jpg'))
im[im <= 0.5] = 0
im[im > 0.5] = 1 
pylab.gray() 
pylab.figure(figsize=(20,10))
pylab.subplot(1,3,1), plot_image(im, 'original') 
im1 = binary_opening(im, disk(6))
pylab.subplot(1,3,2), plot_image(im1, 'opening with disk size ' + str(10))
im1 = binary_closing(im, disk(6))
pylab.subplot(1,3,3), plot_image(im1, 'closing with disk size ' + str(6)) 
pylab.show()

```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/a527c438-68a2-48a3-a97e-2b801b67631a" width="600px"  alt ="DIP_prac8_1">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/ec29b2c8-a4db-4992-8f48-e75b5d151b48" width="600px"  alt ="DIP_prac8_2">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/23aa626e-ede4-42d2-8d45-90175cc7268e" width="600px"  alt ="DIP_prac8_3">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/35ea21f2-d715-49e0-9d79-d248ed6064f6" width="600px"  alt ="DIP_prac8_4">


</details>


[🔝](#index)

**************

## prac9

9. **Image Segmentation**.

<details>
<summary>CODE</summary>


```python
#Loading original image
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('F:/GitHub/Practical_BscIT_MscIT_Ninad/MscIT/Semester 2/ImageProcessing/Dataset/Original_img_segmentation.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8,8))
plt.imshow(img,cmap="gray")
plt.axis('off')
plt.title("Original Image")
plt.show()

#Converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(8,8))
plt.imshow(gray,cmap="gray")
plt.axis('off')
plt.title("GrayScale Image")
plt.show()

#Converting to binary inverted image
ret, thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)
plt.figure(figsize=(8,8))
plt.imshow(thresh,cmap="gray")
plt.axis('off')
plt.title("Threshold Image")
plt.show()

#Segmenting the images
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel, iterations = 15)
bg = cv2.dilate(closing, kernel, iterations = 1)
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)
#cv2.imshow('image', fg)
plt.figure(figsize=(8,8))
plt.imshow(fg,cmap="gray")
plt.axis('off')
plt.title("Segmented Image")
plt.show()


#Final code
plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.axis('off')
plt.title("Original Image")
plt.imshow(img,cmap="gray")

plt.subplot(2,2,2)
plt.imshow(gray,cmap="gray")
plt.axis('off')
plt.title("GrayScale Image")

plt.subplot(2,2,3)
plt.imshow(thresh,cmap="gray")
plt.axis('off')
plt.title("Threshold Image")

plt.subplot(2,2,4)
plt.imshow(fg,cmap="gray")
plt.axis('off')
plt.title("Segmented Image")

plt.show()

```



</details>



<details>
<summary>OUTPUT</summary>

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/cb87a2d5-4b62-4953-8c75-90d568de7233" width="600px"  alt ="DIP_prac9_1">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/09c45a55-9395-4091-bfa1-bfc7e56ddfbc" width="600px"  alt ="DIP_prac9_2">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/1cc9f584-8e4c-4c64-ad72-c0b7364cb9af" width="600px"  alt ="DIP_prac9_3">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/8cd098bf-e249-4dc2-81bd-c20a02c10ca8" width="600px"  alt ="DIP_prac9_4">

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/98a5d366-e1a9-4b96-a917-dbc618b0cd58" width="600px"  alt ="DIP_prac9_5">


</details>

[🔝](#index)

**************