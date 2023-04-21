**Microservice Architecture** <br>
**Practical #5** <br>
**Building ASP.Net core REST API**

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

- [Download **`Glossary`** Folder here](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/Et0OoRtikihKia6ug4YpcsMBcm2bWq7P3aeaWvNRzC2vKg?e=JEncMW)



<br>

**Steps**:

1. On **`Command prompt 1`**
    - Command :
        ```console
        dotnet new webapi -o Glossary
        ```

    - Output:

        <img src="https://user-images.githubusercontent.com/88243315/233608498-45581549-16d8-4bcf-8934-be302c429540.png" alt="MA_prac5_1" width="600">

    <br>

    - Command :
        ```console
        cd Glossary

        dotnet run
        ```

    - Output:

        <img src="https://user-images.githubusercontent.com/88243315/233608506-ad70bcda-27d2-4e9b-8c8e-a721ae668966.png" alt="MA_prac5_2" width="600">

    <br>



2. On **`Command prompt 2`**
    - Command :
        ```console
        curl --insecure http://localhost:5160/weatherforecast
        ```

    - Output:

        <img src="https://user-images.githubusercontent.com/88243315/233608516-5d6c89b9-69cd-4dfc-8aa7-0ac6c88ea9cc.png" alt="MA_prac5_3" width="600">

    <br>

3. Now Change the content:
    1. To get started, remove the **`WeatherForecast.cs`** file from the **`root of the project`** and the **`WeatherForecastController.cs`** file from the **`Controllers folder`**.

    2. Add **`GlossaryItem.cs`** to **`".\Glossary\GlossaryItem.cs "`** folder and add following code.

        <details>
        <summary>CODE</summary>

        ```csharp
        // GlossaryItem.cs

        namespace Glossary
        {
            public class GlossaryItem
            {
                public string Term { get; set; }
                public string Definition { get; set; }
            }
        }
        ```
        </details>

    <br>

    3. Add **`GlossaryController.cs`** to **`".\Glossary\Controllers\GlossaryController.cs "`** folder and add following code.

        <details>
        <summary>CODE</summary>

        ```csharp
        //Controllers/GlossaryController.cs
        using System;
        using System.Collections.Generic;
        using Microsoft.AspNetCore.Mvc;
        using System.IO;

        namespace Glossary.Controllers
        {
            [ApiController]
            [Route("api/[controller]")]
            public class GlossaryController : ControllerBase
            {
                private static List<GlossaryItem> Glossary = new List<GlossaryItem> {
                    new GlossaryItem
                    {
                        Term = "HTML",
                        Definition = "Hypertext Markup Language"
                    },
                    new GlossaryItem
                    {
                        Term = "MVC",
                        Definition = "Model View Controller"
                    },
                    new GlossaryItem
                    {
                        Term = "OpenID",
                        Definition = "An open standard for authentication"
                    }
                };

                [HttpGet]
                public ActionResult<List<GlossaryItem>> Get()
                {
                    return Ok(Glossary);
                }

                [HttpGet]
                [Route("{term}")]
                public ActionResult<GlossaryItem> Get(string term)
                {
                    var glossaryItem = Glossary.Find(item =>
                    item.Term.Equals(term, StringComparison.InvariantCultureIgnoreCase));

                    if (glossaryItem == null)
                    {
                        return NotFound();
                    }
                    else
                    {
                        return Ok(glossaryItem);
                    }
                }

                [HttpPost]
                public ActionResult Post(GlossaryItem glossaryItem)
                {
                    var existingGlossaryItem = Glossary.Find(item =>
                    item.Term.Equals(glossaryItem.Term, StringComparison.InvariantCultureIgnoreCase));

                    if (existingGlossaryItem != null)
                    {
                        return Conflict("Cannot create the term because it already exists.");
                    }
                    else
                    {
                        Glossary.Add(glossaryItem);
                        var resourceUrl = Path.Combine(Request.Path.ToString(), Uri.EscapeUriString(glossaryItem.Term));
                        return Created(resourceUrl, glossaryItem);
                    }
                }

                [HttpPut]
                public ActionResult Put(GlossaryItem glossaryItem)
                {
                    var existingGlossaryItem = Glossary.Find(item =>
                    item.Term.Equals(glossaryItem.Term, StringComparison.InvariantCultureIgnoreCase));

                    if (existingGlossaryItem == null)
                    {
                        return BadRequest("Cannot update a nont existing term.");
                    }
                    else
                    {
                        existingGlossaryItem.Definition = glossaryItem.Definition;
                        return Ok();
                    }
                }

                [HttpDelete]
                [Route("{term}")]
                public ActionResult Delete(string term)
                {
                    var glossaryItem = Glossary.Find(item =>
                    item.Term.Equals(term, StringComparison.InvariantCultureIgnoreCase));

                    if (glossaryItem == null)
                    {
                        return NotFound();
                    }
                    else
                    {
                        Glossary.Remove(glossaryItem);
                        return NoContent();
                    }
                }
            }
        }
        ```
        </details>


    - Output:

        <img src="https://user-images.githubusercontent.com/88243315/233608519-f8420c20-4f54-4081-af51-7a3a3edaea82.png" alt="MA_prac5_4" width="600">
        <img src="https://user-images.githubusercontent.com/88243315/233608522-bc262773-13d2-43b1-9e54-a07b6ba4fd2c.png" alt="MA_prac5_5" width="600">

    <br>



4. Now stop running previous dotnet run on **`command prompt 1`** using **`Ctrl+C`**. and Run it again for new code.

- On **`Command prompt 1`**
    - Command :
        ```console
        dotnet run
        ```

    - Output:

        <img src="https://user-images.githubusercontent.com/88243315/233608524-e9bd1b25-80f1-4774-a010-7f351dab0c2c.png" alt="MA_prac5_6" width="400">

    <br>

- On **`Command prompt 2`**

    1. **Getting a list of items:**
        - Commands: 
            ```console
            curl --insecure https://localhost:5160/api/glossary
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233608526-82529339-9902-48cf-acc6-419405b75538.png" alt="MA_prac5_7" width="800">

    <br>

    2. **Getting a single item:**
        - Commands: 
            ```console
            curl --insecure https://localhost:5001/api/glossary/MVC
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233608529-6db95c25-f934-4e44-ae97-447a26c8461f.png" alt="MA_prac5_8" width="800">

    <br>

    3. **Creating an item:**
        - Commands: 
            ```console
            curl --insecure -X POST -d "{\"term\": \"MFA\", \"definition\":\"An authentication process.\"}" -H "Content-Type:application/json" https://localhost:5001/api/glossary

            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233608532-86ea026c-5876-423f-93e7-d2ba57fe8991.png" alt="MA_prac5_9" width="800">

    <br>

    4. **Update Item:**
        - Commands: 
            ```console
            curl --insecure -X PUT -d "{\"term\": \"MVC\", \"definition\":\"Modified record of Model View Controller.\"}" -H "Content-Type:application/json" https://localhost:5001/api/glossary
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233608536-113bb16c-b1ac-420d-9e84-bf5f9bc143b7.png" alt="MA_prac5_10" width="800">

            <br>
        - Checking
            <br>

            <img src="https://user-images.githubusercontent.com/88243315/233608539-afd3717c-fbd1-4d05-a2f2-810bb42a5393.png" alt="MA_prac5_11" width="800">

    <br>

    5. **Delete Item:**
        - Commands: 
            ```console
            curl --insecure --request DELETE --url https://localhost:5001/api/glossary/openid
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233608540-8e0d92da-0f5b-401f-adf4-1ea70d32e8d4.png" alt="MA_prac5_12" width="800">

    <br>