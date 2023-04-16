# Microservices Architecture

M. Sc (Information Technology)
PSIT2P3 Microservices Architecture



## Index

| Sr.No. | Name | README |
| --- | --- | --- |
| [Prac1](/MscIT/Semester%202/BigDataAnalytics/Practical%201/) | 1. Building First Console App. <br> - Print even odd number from 1 to 30 `(TakeHomeTask)` | [Prac1](#prac1) <br> [Prac1(TakeHomeTask)](#print-even-odd-number-from-1-to-30-takehometask) |
| [Prac2](/MscIT/Semester%202/BigDataAnalytics/Practical%202/) | 2. Building First ASP.NET MVC App.***`(Symbol,Price)`*** <br> - Building First ASP.NET Core App ***`(Name,RollNo)`*** `(TakeHomeTask)` | [Prac2](#prac2) <br> [Prac2(TakeHomeTask)](#building-first-aspnet-core-app-namerollno-takehometask) |




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

## Print even odd number from 1 to 30 (TakeHomeTask)

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

## Prac2

<details>
<summary>STEPS</summary>



Steps:- Building First ASP.NET Core App ***`(Symbol,Price)`*** <br>

1. Install .Net Core Sdk <br> (Link: https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install)

2. Create folder ***`MyMVC`*** folder in D: drive or any other drive

3. Open command prompt and perform following operations ***`to create mvc project`***

    ```bash
    dotnet new mvc --auth none
    ```

    <img src="https://user-images.githubusercontent.com/88243315/227009164-ee454ba5-76c0-414d-a87a-ad883b5cb768.png" width="600px"   alt ="MA_prac2_1">

4. Go to controllers folder and modify HomeController.cs file to match following:

    ```csharp
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.Extensions.Logging;
    using MyMVC.Models;
    namespace MyMVC.Controllers
    {
        public class HomeController: Controller
        {
            public String Index()
            {
                return "Hello World";
            }
        }
    }
    ```

5. Run the project `dotnet run` and then go to browser and type ***`localhost:5192`***

    <img src="https://user-images.githubusercontent.com/88243315/227009174-565c7c2f-13de-455f-9a15-55ad9f073db7.png" width="500px"  alt ="MA_prac2_2">
    <img src="https://user-images.githubusercontent.com/88243315/227009179-e7a86f5f-e5cb-4570-886a-a3203eebd8d7.png" width="300px"  alt ="MA_prac2_3">

6. Now go back to command prompt and stop running project using `CTRL+C`

7. Go to `models folder` and add new file ***`StockQuote.cs`*** to it with following content

    ```csharp
    using System;
    namespace MyMVC.Models
    {
        public class StockQuote
        {
            public string Symbol
            {
                get;
                set;
            }
            public int Price
            {
                get;
                set;
            }
        }
    }
    ```

8. Now Add View to folder then home folder in it and modify `index.cshtml` file to match following

    ```html
    @{
    ViewData["Title"] = "Home Page";
    }
    <div>
    Symbol: @Model.Symbol <br/>
    Price: $@Model.Price <br/>
    </div>
    ```

9. Now modify ***`HomeController.cs`*** file to match following:

    ```csharp
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.Extensions.Logging;
    using MyMVC.Models;
    namespace MyMVC.Controllers
    {
        public class HomeController: Controller
        {
            public async Task < IActionResult > Index()
            {
                var model = new StockQuote
                {
                    Symbol = "HLLO", Price = 3200
                };
                return View(model);
            }
        }
    }
    ```

10. Now run the project using
***`dotnet run`***

11. Now go back to browser and refresh to get modified view response

    <img src="https://user-images.githubusercontent.com/88243315/227009183-0042e7d3-8b4a-4618-ac81-c7dde9987e35.png" width="500px"   alt ="MA_prac2_4">

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/227009183-0042e7d3-8b4a-4618-ac81-c7dde9987e35.png" width="500px"   alt ="MA_prac2_4">


</details>

<br>

<br>


## Building First ASP.NET Core App ***`(Name,RollNo)`*** `(TakeHomeTask)`

<details>
<summary>STEPS</summary>


B. Building First ASP.NET Core App ***`(Name,RollNo)`*** (TakeHomeTask) <br>

1. Install .Net Core Sdk <br> (Link: https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install)

2. Create folder ***`<anyName>`*** folder in D: drive or any other drive

3. Open command prompt and perform following operations ***`to create mvc project`***

    ```bash
    dotnet new mvc --auth none
    ```

    <img src="https://user-images.githubusercontent.com/88243315/227023206-50902c51-f837-42b1-ab4d-ed1e0916d794.png" width="600px"   alt ="MA_prac2_5">

4. Go to `models folder` and add new file ***`StockQuote.cs`*** to it with following content

    ```csharp
    using System;
    namespace NameRollNoMVC.Models
    {
        public class StockQuote
        {
            public string Name
            {
                get;
                set;
            }
            public string RollNo
            {
                get;
                set;
            }
        }
    }
    ```

5. Now modify ***`HomeController.cs`*** file to match following:

    ```csharp
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.Extensions.Logging;
    using NameRollNoMVC.Models;
    namespace NameRollNoMVC.Controllers
    {
        public class HomeController: Controller
        {
            public async Task < IActionResult > Index()
            {
                var model = new StockQuote
                {
                    Name = "Ninad", RollNo = "22306A1012"
                };
                return View(model);
            }
        }
    }
    ```

6. Now Add View to folder then home folder in it and modify `index.cshtml` file to match following

    ```html
    @{
    ViewData["Title"] = "Home Page";
    }
    <div>
        Name: @Model.Name <br/>
        RollNo: @Model.RollNo <br/>
    </div>
    ```

7. Now run the project using ***`dotnet run`***

    <img src="https://user-images.githubusercontent.com/88243315/227023225-c39b3cfb-3de8-4e38-a3f8-ebe42ba044c2.png" width="500px"   alt ="MA_prac2_6">

8. Now go back to browser and refresh to get modified view response

    <img src="https://user-images.githubusercontent.com/88243315/227023233-28e0a01c-c4e2-47e6-972c-3f1bc92cc9b1.png" width="400px"   alt ="MA_prac2_7">
    

</details>



<details>
<summary>OUTPUT</summary>

<img src="https://user-images.githubusercontent.com/88243315/227023233-28e0a01c-c4e2-47e6-972c-3f1bc92cc9b1.png" width="400px"   alt ="MA_prac2_7">


</details>

<br>

<br>

------------------------------------------------------------------

## Prac3A

# Aim: Working with Docker
3 a) Method 1: To pull and push images using docker

<details>
<summary>STEPS</summary>



***.Net SDK Download Link:***
<br>
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

Steps:

1.	Create Docker Hub account (sign up)
2.	login to https://labs.play-with-docker.com/
3.	Add new instance

    <img src="https://user-images.githubusercontent.com/88243315/232332330-cb776a84-48bb-4157-ad6b-42b861b9a2b6.png" width="300px" alt ="MA_prac3A_1">

<br>

4.	perform following in **CMD**

- Version check 
    - Command
        ```bash
        docker --version
        ```

        <img src="https://user-images.githubusercontent.com/88243315/232332332-7603e408-2be7-4413-a4bb-6e273bfb1c28.png" width="600px" alt ="MA_prac3A_2">


<br>

- To pull readymade image
    - Command
        ```bash
        docker pull rocker/verse
        ```

        <img src="https://user-images.githubusercontent.com/88243315/232332334-19a36eab-bea4-4432-aa3d-fa0fa15b9b95.png" width="600px" alt ="MA_prac3A_3">


<br>

- To check images in docker
    - Command
        ```bash
        docker images
        ```

        <img src="https://user-images.githubusercontent.com/88243315/232332336-3177283f-c36f-4c59-afc4-76fd314ad779.png" width="600px" alt ="MA_prac3A_4">

<br>

5. Now Login to docker hub and create repository

    <img src="https://user-images.githubusercontent.com/88243315/232333590-95e92151-9840-456d-83a8-a6cf19236775.png" width="600px" alt ="MA_prac3A_5">

<br>

6. Click on Create button -> Now check repository created

    <img src="https://user-images.githubusercontent.com/88243315/232333591-ce5c2784-7df3-4fd1-94fd-3ebcbdf777a4.png" width="600px" alt ="MA_prac3A_6">

<br>

7.	perform following in CMD
- To login to your docker account
    - Command
        ```bash
        docker login --username=ninadstudy
        password: 
        ```

        - Insert **password of docker login** in place of password.

        <img src="https://user-images.githubusercontent.com/88243315/232332341-9d7656d5-db11-4924-bd6e-45935e5581d5.png" width="600px" alt ="MA_prac3A_7">

<br>

- To tag image
    - Command
        ```bash
        docker tag 7291950d643e ninadstudy/repo1:firsttry
        ```

        - Insert **Image ID** obtained from `docker images` command.

        <img src="https://user-images.githubusercontent.com/88243315/232332343-076e1212-1205-4430-bf71-25e8ebc83a79.png" width="600px" alt ="MA_prac3A_8">

<br>

- To push image to docker hub account
    - Command
        ```bash
        docker push ninadstudy/repo1:firsttry
        ```

        - Insert **Image ID** obtained from `docker images` command.

        <img src="https://user-images.githubusercontent.com/88243315/232332344-903f87b3-465c-4c4d-8171-e0f0b5e0a598.png" width="600px" alt ="MA_prac3A_9">

<br>

8. Check it in docker hub now

    <img src="https://user-images.githubusercontent.com/88243315/232332346-681e9226-0309-4fac-9d77-311c1c3933b1.png" width="600px" alt ="MA_prac3A_10">

<br>

9. Check it in docker hub now

    <img src="https://user-images.githubusercontent.com/88243315/232332347-2a6975c4-a073-4adf-a796-ac435473c607.png" width="600px" alt ="MA_prac3A_11">

<br>



</details>

<br>


---------------------------

## Prac3B

3 b) **Method 2:** Build an image then push it to docker and run it

***.Net SDK Download Link:***
<br>
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

***Docker desktop Download Link:***
<br>
https://www.docker.com/products/docker-desktop/

<br>


<details>
<summary>STEPS</summary>


Steps:

***.Net SDK Download Link:***
<br>
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

Steps:

1. To create docker file
    - Command
        ```bash
        cat > Dockerfile << EOF
        FROM busybox
        CMD echo "Hello Ninad."
        EOF
        ```

        <img src="https://user-images.githubusercontent.com/88243315/232332350-9d36bc5d-d55b-49c1-8d94-9d7a14d510ef.png" width="400px" alt ="MA_prac3B_1">

<br>

2. To build image from docker file
    - Command
        ```bash
        dokcer build –t ninadstudy/repo2
        ```

        <img src="https://user-images.githubusercontent.com/88243315/232332351-6db8d2b5-cbc3-482a-bbe8-fde36e1f4f66.png" width="400px" alt ="MA_prac3B_2">

<br>

3. To check docker images
    - Command
        ```bash
        docker images
        ```

        <img src="https://user-images.githubusercontent.com/88243315/232332353-5f2246d6-f066-427d-9bbc-c31b480f1872.png" width="400px" alt ="MA_prac3B_3">

<br>

4. To push and run image to docker hub
    - Command
        ```bash
        docker push ninadstudy/repo2
        docker run ninadstudy/repo2
        ```

        <img src="https://user-images.githubusercontent.com/88243315/232332354-521cf19a-dc7f-4da8-ac86-bc3460739fee.png" width="400px" alt ="MA_prac3B_4">

<br>

5. Now check it on docker hub

    <img src="https://user-images.githubusercontent.com/88243315/232332356-ca0b6886-d8ad-4161-a804-7fd899810859.png" width="400px" alt ="MA_prac3B_5">


<br>

[🔝](#index)


<br>



</details>

<br>


----------------------------------------------------





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
