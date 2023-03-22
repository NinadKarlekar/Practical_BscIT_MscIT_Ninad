**Microservice Architecture** <br>
**Practical #2** <br>
**Building First Console App**


***.Net SDK Download Link:***
<br>
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install


-------------------------------

A. Building First ASP.NET Core App ***`(Symbol,Price)`*** <br>
B. Building First ASP.NET Core App ***`(Name,RollNo)`*** <br>


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
    <img src="https://user-images.githubusercontent.com/88243315/227009179-e7a86f5f-e5cb-4570-886a-a3203eebd8d7.png" width="200px"  alt ="MA_prac2_3">

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


------------------------------

B. Building First ASP.NET Core App ***`(Name,RollNo)`*** (TakeHomeTask) <br>

1. Install .Net Core Sdk <br> (Link: https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install)

2. Create folder ***`<anyName>`*** folder in D: drive or any other drive

3. Open command prompt and perform following operations ***`to create mvc project`***

    ```bash
    dotnet new mvc --auth none
    ```

    <img src="https://user-images.githubusercontent.com/88243315/227009189-31f3aef4-4c5b-49b6-bc9c-11f905d4b94c.png" width="600px"   alt ="MA_prac2_5">

4. Go to `models folder` and add new file ***`StockQuote.cs`*** to it with following content

    ```csharp
    using System;
    namespace MyMVC.Models
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
    using MyMVC.Models;
    namespace MyMVC.Controllers
    {
        public class HomeController: Controller
        {
            public async Task < IActionResult > Index()
            {
                var model = new StockQuote
                {
                    Name = "Ninad", RollNo = 1012
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
    RollNo: $@Model.RollNo <br/>
    </div>
    ```

7. Now run the project using ***`dotnet run`***

    <img src="https://user-images.githubusercontent.com/88243315/227009196-d67df093-1aad-4555-b40c-6ee873902d3c.png" width="500px"   alt ="MA_prac2_6">

8. Now go back to browser and refresh to get modified view response

    <img src="https://user-images.githubusercontent.com/88243315/227009201-0de65f69-065a-424c-bf28-3db93957a9c4.png" width="400px"   alt ="MA_prac2_7">

