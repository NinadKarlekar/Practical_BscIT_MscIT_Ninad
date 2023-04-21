**Microservice Architecture** <br>
**Practical #9** <br>
**Building an ASP.NET Core Web Application & Invoking REST APIs from JavaScript**

----------------------------
***.Net SDK Download Link:***
<br>

- Latest Version:-
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

- Old Versions:-
    - **.Net SDK 1.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 3.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 5.0** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)



--------------------
## Create your web API
## Open two command prompts

- Download [StatlerWaldorfCorp.WebApp](https://NinadKarlekar.github.io/Practical_BscIT_MscIT_Ninad/tree/main/MscIT/Semester%202/MicroservicesArchitecture/Practical%205/Glossary) folder.

Steps:

1. Change code of **`ApiController.cs`** from **`".\StatlerWaldorfCorp.WebApp\Controllers"`** 

    <details>
    <summary>CODE</summary>

    ```csharp
    using Microsoft.AspNetCore.Mvc;
    using StatlerWaldorfCorp.WebApp.Models;

    namespace StatlerWaldorfCorp.WebApp.Controllers
    {
        [Route("api/test")]
        public class ApiController : Controller
        {
            [HttpGet]
            public IActionResult GetTest()
            {
                return this.Ok(new StockQuote { Symbol = "API", Price = 9999 });
            }
        }
    }
    ```
    </details>

<br>

2. Change code of **`HomeController.cs`** from **`".\StatlerWaldorfCorp.WebApp\Controllers"`** 

    <details>
    <summary>CODE</summary>

    ```csharp
    using Microsoft.AspNetCore.Mvc;
    using System.Threading.Tasks;
    using StatlerWaldorfCorp.WebApp.Models;

    namespace StatlerWaldorfCorp.WebApp.Controllers
    {
        public class HomeController : Controller
        {
            public IActionResult Index()
            {
                var model = new StockQuote { Symbol = "HLLO", Price = 3200 };

                return View(model);            
            }
        }
    }
    ```
    </details>

<br>

3. Change code of **`StockQuote.cs`** from **`".\StatlerWaldorfCorp.WebApp\Models"`** 

    <details>
    <summary>CODE</summary>

    ```csharp
    namespace StatlerWaldorfCorp.WebApp.Models
    {
        public class StockQuote
        {
            public string Symbol { get; set; }
            public int Price { get; set; }
        }
    }
    ```
    </details>

<br>

4. Change code of **`Index.cshtml`** from **`".\StatlerWaldorfCorp.WebApp\Views\Home\Index.cshtml"`** 

    <details>
    <summary>CODE</summary>

    ```html
    <html>
    <head>
        <title>Hello world</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script src="/Scripts/hello.js"></script>
    </head>
    <body>
        <h1>Hello World</h1>
        <div>
            <h2>Stock Quote</h2>
            <div>
                Symbol: @Model.Symbol<br/>
                Price: $@Model.Price<br/>
            </div>
        </div>
        <br/>
        <div>
            <p class="quote-symbol">The Symbol is </p>
            <p class="quote-price">The price is $</p>
        </div>
    </body>
    </html>
    ```
    </details>

<br>

5. Change code of **`hello.js`** from **`".\StatlerWaldorfCorp.WebApp\wwwroot\Scripts"`** 

    <details>
    <summary>CODE</summary>

    ```javascript
    $(document).ready(function () {
        $.ajax({
            url: "/api/test"
        }).then(function (data) {
            $('.quote-symbol').append(data.symbol);
            $('.quote-price').append(data.price);
        });
    });
    ```
    </details>

<br>

6. Change code of **`Program.cs`** from **`".\StatlerWaldorfCorp.WebApp"`** 

    <details>
    <summary>CODE</summary>

    ```csharp
    using System;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.Extensions.Configuration;
    using System.IO;

    namespace StatlerWaldorfCorp.WebApp
    {
        public class Program
        {
            public static void Main(string[] args)
            {
                var config = new ConfigurationBuilder()
                    .AddCommandLine(args)
                    .Build();

                var host = new WebHostBuilder()
                    .UseContentRoot(Directory.GetCurrentDirectory())
                    .UseKestrel()
                    .UseStartup<Startup>()
                    .UseConfiguration(config)
                    .Build();

                host.Run();
            }
        }
    }
    ```
    </details>

<br>

7. Change code of **`Startup.cs`** from **`".\StatlerWaldorfCorp.WebApp"`** 

    <details>
    <summary>CODE</summary>

    ```csharp
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.Extensions.Logging;
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.Extensions.Configuration;

    namespace StatlerWaldorfCorp.WebApp
    {
        public class Startup
        {
            public Startup(IHostingEnvironment env)
            {
                var builder = new ConfigurationBuilder()
                    .SetBasePath(env.ContentRootPath)
                    .AddEnvironmentVariables();

                Configuration = builder.Build();
            }

            public IConfiguration Configuration { get; set; }

            public void ConfigureServices(IServiceCollection services) {            
                services.AddMvc();
            }

            public void Configure(IApplicationBuilder app, IHostingEnvironment env, ILoggerFactory loggerFactory)
            {     
            loggerFactory.AddConsole();
            loggerFactory.AddDebug();       
            
            app.UseDeveloperExceptionPage();
            app.UseMvc(routes =>
            {
                routes.MapRoute("default",
                    template: "{controller=Home}/{action=Index}/{id?}");
            });
            app.UseStaticFiles();
            }
        }
    }

    ```
    </details>

<br>


7. Change code of **`StatlerWaldorfCorp.WebApp.csproj`** from **`".\StatlerWaldorfCorp.WebApp"`** 

    <details>
    <summary>CODE</summary>

    ```xml
    <Project Sdk="Microsoft.NET.Sdk.Web">

    <PropertyGroup>
        <TargetFramework>netcoreapp1.1</TargetFramework>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="Microsoft.AspNetCore" Version="1.1.1" />
        <PackageReference Include="Microsoft.AspNetCore.Mvc" Version="1.1.2" />
        <PackageReference Include="Microsoft.AspNetCore.StaticFiles" Version="1.1.1" />
        <PackageReference Include="Microsoft.Extensions.Logging.Debug" Version="1.1.1" />
        <PackageReference Include="Microsoft.VisualStudio.Web.BrowserLink" Version="1.1.0" />
        <PackageReference Include="Microsoft.Extensions.Configuration" Version="1.1.1"/>
        <PackageReference Include="Microsoft.Extensions.Options.ConfigurationExtensions" Version="1.1.1"/>
        <PackageReference Include="Microsoft.Extensions.Configuration.Json" Version="1.1.1"/>
        <PackageReference Include="Microsoft.Extensions.Configuration.CommandLine" Version="1.1.1"/>      
    </ItemGroup>

    </Project>
    ```
    </details>

<br>

8. Open command prompt and enter following commmand

    ```console
    dotnet run
    ```

    <img src="https://user-images.githubusercontent.com/88243315/233698981-657b3655-df99-4b72-a930-9dd15115da0c.png" alt="MA_prac9_1" width="400">

<br>

9. Open browser and go to http://localhost:5000/

    <img src="https://user-images.githubusercontent.com/88243315/233698989-914d7d91-37e5-46ed-bf07-8b06c05caa17.png" alt="MA_prac9_2" width="400">