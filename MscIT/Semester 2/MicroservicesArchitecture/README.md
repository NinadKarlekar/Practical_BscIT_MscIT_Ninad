# Microservices Architecture

M. Sc (Information Technology)
PSIT2P3 Microservices Architecture



## Index

| Sr.No. | Name | README |
| --- | --- | --- |
| [Prac1](/MscIT/Semester%202/BigDataAnalytics/Practical%201/) | 1. Building First Console App. | [Prac1](#prac1) |



******************
---------------------

## Prac1

1. Building First Console App .


<details>
<summary>STEPS</summary>



***.Net SDK Download Link:***
<br>
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

Steps:

1. Download and install
    - To start building .NET apps you just need to download and install the .NET SDK (Software Development Kit).

2. Check everything installed correctly
    - Once you've installed, open a new command prompt and run the following command:
        ```
        dotnet
        ```


    - <img src="https://user-images.githubusercontent.com/88243315/221396880-b7c9e8a9-46c7-4c37-a8a8-57596a66cf5e.png" width="600px"   alt ="MA_prac1_1">

3. Create your app
    - In your command prompt, run the following commands:
        ```
        dotnet new console -o myApp
        ```
        ```
        cd myApp
        ```
	
    - <img src="https://user-images.githubusercontent.com/88243315/221396891-29cca43e-ecd5-4f0e-aa8e-c2df2cd083ed.png" width="600px"   alt ="MA_prac1_2">

    - The main file in the myApp folder is Program.cs. By default, it already contains the necessary code to write "Hello World!" to the Console.

    - `Program.cs` Code

        ```cs
        using System;
        namespace myApp
        {
            class Program
            {
                static void Main(string[] args)
                {
                    Console.WriteLine("Hello World!");
                }
            }
        }
        ```

4. Run your app
    - In your command prompt, run the following command:
        ```
        dotnet run
        ```


    
    - <img src="https://user-images.githubusercontent.com/88243315/221396899-642b64c2-dcb6-43ae-8967-8974e80093c8.png" width="600px"  alt ="MA_prac1_3">


5. To Change Content/output of program open `Program.cs` and do necessary changes

6. After Changes save file and in ***CMD*** run following command to ***restore changes***
    ```
    dotnet restore
    ```
<br>

********************

## Print even odd number from 1 to 30

Code:

```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace myevenodd
{    
    class Program
    {
        static void Main(string[] args)
        {
            int i     = 0;
		    Console.WriteLine("Print even odd number from 1 to 30");
		    Console.WriteLine("\nNinad Karlekar 22306A1012");

            Console.WriteLine("\nEven Numbers :");
            for (i = 1; i <= 30; i++)
            {   
                if( i%2 == 0 )
                {
                    Console.Write(i + " ");
                }
            }
            Console.WriteLine("\nOdd Numbers :");
            for (i = 1; i <= 30; i++)
            {
                if (i % 2 != 0)
                {
                    Console.Write(i + " ");
                }
            }
            Console.WriteLine();
        }
    }
}
```

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/221396904-9e2ca734-06bd-4be4-8f14-291d8c480e14.png" width="600px" alt ="MA_prac1_4"> 
<img src="https://user-images.githubusercontent.com/88243315/221396909-cf2d7474-bda7-4a47-8ec8-c0ba0cc1e5d7.png" width="600px" alt ="MA_prac1_5"> 


</details>

<br>

[🔝](#index)

**************









<!-- 
## Index

| Sr.No. | Name | ReadME |
| --- | --- | --- |
| [Prac1A-i](/MscIT/Semester%202/BigDataAnalytics/) <br> [Prac1A-ii](/MscIT/Semester%201/Soft_Computing_Techniques/Practical%201/)| 1A-i. Design a **simple linear neural network** model. <br> 1A-ii. Calculate the **output** of **neural net** for given data. | [Prac1A-i](#prac1a-i) <br>  [Prac1A-ii](#prac1a-ii) | 

*************************
***********************

<BR>

## Prac1A-i

- 1A-i. Heading .

```python

```

<details>
<summary>OUTPUT</summary>

![]()
![]()



</details>


[🔝](#index)

**************


**************

### [Go To Top](#soft-computing-techniques)
 -->
