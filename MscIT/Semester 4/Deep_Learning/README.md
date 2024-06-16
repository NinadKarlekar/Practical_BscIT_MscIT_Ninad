# Deep Learning

M. Sc (Information Technology)
Deep Learning



## Index




| Sr.No. | Name | README | DOWNLOAD |
| --- | --- | --- | --- |
| [Prac1](/MscIT/Semester%204/Deep_Learning/Practical01/) | 1. Performing matrix multiplication and finding eigen vectors and eigen values using TensorFlow.. | [Prac1](#prac1) |  [Download](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/MscIT/Semester%204/Deep_Learning/Practical01/DL_1.py) |


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