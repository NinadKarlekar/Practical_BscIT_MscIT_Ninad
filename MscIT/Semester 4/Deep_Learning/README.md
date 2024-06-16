# Deep Learning

M. Sc (Information Technology)
Deep Learning



## Index




| Sr.No. | Name | README |
| --- | --- | --- |
| [Prac1](/MscIT/Semester%204/Deep_Learning/Practical01/) | Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow. | [Prac1](#prac1) |
| [Prac2](/MscIT/Semester%204/Deep_Learning/Practical02/) | Solving XOR problem using deep feed forward network. | [Prac2](#prac2) |
| [Prac3](/MscIT/Semester%204/Deep_Learning/Practical03/) | Implementing deep neural network for performing binary classification task. | [Prac3](#prac3) |
| [Prac4A](/MscIT/Semester%204/Deep_Learning/Practical04/) <br> [Prac4B](/MscIT/Semester%204/Deep_Learning/Practical04/) <br> [Prac4C](/MscIT/Semester%204/Deep_Learning/Practical04/) | a) Using deep feed forward network with two hidden layers for performing multiclass classification and predicting the class. <br> b) Using a deep feed forward network with two hidden layers for performing classification and predicting the probability of class. <br> c) Using a deep feed forward network with two hidden layers for performing linear regression and predicting values. | [Prac4A](#prac4) <br> [Prac4B](#prac4) <br> [Prac4C](#prac4) |
| [Prac5A](/MscIT/Semester%204/Deep_Learning/Practical05/) <br> [Prac5B](/MscIT/Semester%204/Deep_Learning/Practical05/) | a) Evaluating feed forward deep network for regression using KFold cross validation. <br> b) Evaluating feed forward deep network for multiclass Classification using KFold cross-validation. | [Prac5A](#prac5) <br> [Prac5B](#prac5) |
| [Prac6A](/MscIT/Semester%204/Deep_Learning/Practical06/) <br> [Prac6B](/MscIT/Semester%204/Deep_Learning/Practical06/) <br> [Prac6C](/MscIT/Semester%204/Deep_Learning/Practical06/) | a) Implementing regularization to avoid overfitting in binary classification. <br> b) Implement 12 regularization with alpha=0.001 <br> c) Replace 12 regularization with l2 regularization. | [Prac6A](#prac6) <br> [Prac6B](#prac6) <br> [Prac6C](#prac6) |
| [Prac7](/MscIT/Semester%204/Deep_Learning/Practical07/) | Demonstrate recurrent neural network that learns to perform sequence analysis for stock price. | [Prac7](#prac7) |
| [Prac8](/MscIT/Semester%204/Deep_Learning/Practical08/) | Performing encoding and decoding of images using deep autoencoder. | [Prac8](#prac8) |
| [Prac9](/MscIT/Semester%204/Deep_Learning/Practical09/) | Implementation of convolutional neural network to predict numbers from number images. | [Prac9](#prac9) |
| [Prac10](/MscIT/Semester%204/Deep_Learning/Practical10/) | Denoising of images using autoencoder. | [Prac10](#prac10) |



******************
---------------------

## Prac1

1. Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow.



<details>
<summary>CODE</summary>

```python
# Aim: Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow.

import tensorflow as tf

print("Matrix Multiplication Demo")
x = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
print(x)

y = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
print(y)

z = tf.matmul(x, y)
print("Product:", z)

e_matrix_A = tf.random.uniform(
    [2, 2], minval=3, maxval=10, dtype=tf.float32, name="matrixA"
)
print("Matrix A:\n{}\n\n".format(e_matrix_A))
eigen_values_A, eigen_vectors_A = tf.linalg.eigh(e_matrix_A)
print(
    "Eigen Vectors:\n{}\n\nEigen Values:\n{}\n".format(eigen_vectors_A, eigen_values_A)
)


```

</details>


******************************************************

<!-- | Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1](/MscIT/Semester%204/Deep_Learning/Practical01/) | 1. Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow.. | [Prac1](#prac1) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%204/Deep_Learning/Practical01/DL_1.py) | -->