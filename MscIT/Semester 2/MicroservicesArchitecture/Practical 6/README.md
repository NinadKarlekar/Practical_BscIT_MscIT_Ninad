**Microservice Architecture** <br>
**Practical #6** <br>
**Working with TeamService**


***.Net SDK Download Link:***
<br>

- Latest Version:-
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

- Old Versions:-
    - **.Net SDK 1.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 3.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 5.0** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)

- [Download **TeamService** Folder here](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EjtwfgKaFQhCtELPXRgueFsBYRp82m8pANgd7GgAHVepgw?e=r53Yv2)

Steps:

1. Create new project:
- Command :
    ```console
    dotnet new webapi -o TeamService
    ```

- output:

    <img src="https://user-images.githubusercontent.com/88243315/233396627-13b3d7f6-b36f-4a88-8614-b4e3d946afb7.png" alt="" width="600">

<br>

2. Remove existing `weatherforecast` files both model and controller files.

<br>

3. Add **`Member.cs`** to **`"D:\TeamService\Models"`** folder and add following code.

    <details>
    <summary>CODE</summary>

    ```csharp
    using System;
    namespace TeamService.Models
    {
        public class Member 
        {
            public Guid ID { get; set; }
            public string FirstName { get; set; }
            public string LastName { get; set; }
            
            public Member() { }
            
            public Member(Guid id) : this()
            {
                this.ID = id;
            }
            
            public Member(string firstName, string lastName, Guid id) : this(id)
            {
                this.FirstName = firstName;
                this.LastName = lastName;
            }
            
            public override string ToString() 
            {
                return this.LastName;
            }
        }
    }
    ```
    </details>

<br>

4. Add **`Team.cs`** to **`"D:\TeamService\Models"`** folder and add following code.

    <details>
    <summary>CODE(Team.cs)</summary>

    ```csharp
    using System;
    using System.Collections.Generic;

    namespace TeamService.Models
    {
        public class Team 
        {
            public string Name { get; set; }
            public Guid ID { get; set; }
            public ICollection<Member> Members { get; set; }

            public Team()
            {
                this.Members = new List<Member>();
            }

            public Team(string name) : this()
            {
                this.Name = name;
            }

            public Team(string name, Guid id)  : this(name) 
            {
                this.ID = id;
            }

            public override string ToString() 
            {
                return this.Name;
            }
        }
    }

    ```
    </details>

<br>

5. Add **`TeamsController.cs`** to **`"D:\TeamService\Controllers"`** folder and add following code.

    <details>
    <summary>CODE(TeamsController.cs)</summary>

    ```csharp
    using System;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Mvc;
    using System.Collections.Generic;
    using System.Linq;
    using TeamService.Models;
    using System.Threading.Tasks;
    using TeamService.Persistence;

    namespace TeamService
    {
        [Route("[controller]")]
        public class TeamsController : Controller
        {
            ITeamRepository repository;

            public TeamsController(ITeamRepository repo)
            {
                repository = repo;
            }

            [HttpGet]
            public virtual IActionResult GetAllTeams()
            {
                return this.Ok(repository.List());
            }

            [HttpGet("{id}")]
            public IActionResult GetTeam(Guid id)
            {
                Team team = repository.Get(id);

                if (team != null)
                {
                    return this.Ok(team);
                }
                else {
                    return this.NotFound();
                }
            }

            [HttpPost]
            public virtual IActionResult CreateTeam([FromBody]Team newTeam)
            {
                repository.Add(newTeam);
                return this.Created($"/teams/{newTeam.ID}", newTeam);
            }

            [HttpPut("{id}")]
            public virtual IActionResult UpdateTeam([FromBody]Team team, Guid id)
            {
                team.ID = id;

                if(repository.Update(team) == null)
                {
                    return this.NotFound();
                }
                else
                {
                    return this.Ok(team);
                }
            }

            [HttpDelete("{id}")]
            public virtual IActionResult DeleteTeam(Guid id)
            {
                Team team = repository.Delete(id);

                if (team == null)
                {
                    return this.NotFound();
                }
                else {
                    return this.Ok(team.ID);
                }
            }
        }
    }


    ```
    </details>

<br>

6. Add **`MembersController.cs`** to **`"D:\TeamService\Controllers"`** folder and add following code.

    <details>
    <summary>CODE(MembersController.cs)</summary>

    ```csharp
    using System;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Mvc;
    using System.Collections.Generic;
    using System.Linq;
    using TeamService.Models;
    using System.Threading.Tasks;
    using TeamService.Persistence;

    namespace TeamService
    {
        [Route("/teams/{teamId}/[controller]")]
        public class MembersController : Controller
        {
            ITeamRepository repository;

            public MembersController(ITeamRepository repo)
            {
                repository = repo;
            }

            [HttpGet]
            public virtual IActionResult GetMembers(Guid teamID)
            {
                Team team = repository.Get(teamID);
                if (team == null)
                {
                    return this.NotFound();
                }
                else
                {
                    return this.Ok(team.Members);
                }
            }

            [HttpGet]
            [Route("/teams/{teamId}/[controller]/{memberId}")]
            public virtual IActionResult GetMember(Guid teamID, Guid memberId)
            {
                Team team = repository.Get(teamID);
                if (team == null)
                {
                    return this.NotFound();
                }
                else
                {
                    var q = team.Members.Where(m => m.ID == memberId);
                    if (q.Count() < 1)
                    {
                        return this.NotFound();
                    }
                    else
                    {
                        return this.Ok(q.First());
                    }
                }
            }

            [HttpPut]
            [Route("/teams/{teamId}/[controller]/{memberId}")]
            public virtual IActionResult UpdateMember([FromBody]Member updatedMember, Guid teamID, Guid memberId)
            {
                Team team = repository.Get(teamID);
                if (team == null)
                {
                    return this.NotFound();
                }
                else
                {
                    var q = team.Members.Where(m => m.ID == memberId);
                    if (q.Count() < 1)
                    {
                        return this.NotFound();
                    }
                    else
                    {
                        team.Members.Remove(q.First());
                        team.Members.Add(updatedMember);
                        return this.Ok();
                    }
                }
            }

            [HttpPost]
            public virtual IActionResult CreateMember([FromBody]Member newMember, Guid teamID)
            {
                Team team = repository.Get(teamID);
                if (team == null)
                {
                    return this.NotFound();
                }
                else
                {
                    team.Members.Add(newMember);
                    var teamMember = new { TeamID = team.ID, MemberID = newMember.ID };
                    return this.Created($"/teams/{teamMember.TeamID}/[controller]/{teamMember.MemberID}", teamMember);
                }
            }

            [HttpGet]
            [Route("/members/{memberId}/team")]
            public IActionResult GetTeamForMember(Guid memberId)
            {
                var teamId = GetTeamIdForMember(memberId);
                if (teamId != Guid.Empty)
                {
                    return this.Ok(new { TeamID = teamId });
                }
                else
                {
                    return this.NotFound();
                }
            }

            private Guid GetTeamIdForMember(Guid memberId)
            {
                foreach (var team in repository.List())
                {
                    var member = team.Members.FirstOrDefault(m => m.ID == memberId);
                    if (member != null)
                    {
                        return team.ID;
                    }
                }
                return Guid.Empty;
            }
        }
    }

    ```
    </details>

<br>

7. Create folder **`"D:\TeamService\Persistence"`**:

<br>

8. Add **`ITeamReposiroty.cs`** to **`"D:\TeamService\Persistence"`** folder and add following code.

    <details>
    <summary>CODE(ITeamReposiroty.cs)</summary>

    ```csharp
    using System;
    using System.Collections.Generic;
    using TeamService.Models;

    namespace TeamService.Persistence
    {
        public interface ITeamRepository
        {
            IEnumerable<Team> List();
            Team Get(Guid id);
            Team Add(Team team);
            Team Update(Team team);
            Team Delete(Guid id);
        }
    }

    ```
    </details>

<br>

9. Add **`MemoryTeamRepository.cs`** to **`"D:\TeamService\Persistence"`** folder and add following code.

    <details>
    <summary>CODE(MemoryTeamRepository.cs)</summary>

    ```csharp
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using TeamService;
    using TeamService.Models;

    namespace TeamService.Persistence
    {
        public class MemoryTeamRepository : ITeamRepository
        {
            protected static ICollection<Team> teams;

            public MemoryTeamRepository()
            {
                if (teams == null)
                {
                    teams = new List<Team>();
                }
            }

            public MemoryTeamRepository(ICollection<Team> teams)
            {
                MemoryTeamRepository.teams = teams;
            }

            public IEnumerable<Team> List()
            {
                return teams;
            }

            public Team Get(Guid id)
            {
                return teams.FirstOrDefault(t => t.ID == id);
            }

            public Team Update(Team t)
            {
                Team team = this.Delete(t.ID);
                if (team != null)
                {
                    team = this.Add(t);
                }
                return team;
            }

            public Team Add(Team team)
            {
                teams.Add(team);
                return team;
            }

            public Team Delete(Guid id)
            {
                var q = teams.Where(t => t.ID == id);
                Team team = null;
                if (q.Count() > 0)
                {
                    team = q.First();
                    teams.Remove(team);
                }
                return team;
            }
        }
    }


    ```
    </details>

<br>

10. Add following line to [**`Startup.cs`**]() in **`public void ConfigureServices(IServiceCollection services)`**
method.
    ```csharp
    services.AddScoped<ITeamRepository, MemoryTeamRepository>();
    ```

<br>

11. Now open **two command prompts** to run this project

    <br>

12. On **Command prompt 1**: (go inside folder **teamservice** first)

- Commands:
    ```console
    dotnet run
    ```

- Output:

    <img src="https://user-images.githubusercontent.com/88243315/233396639-fa60f809-755e-48b2-9ef0-43f99dd01b50.png" alt="" width="600">

    <br>

13. On command prompt 2
    1. **To get all teams**
        - Commands: To get all teams
            ```console
            curl --insecure https://localhost:5001/teams
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233396642-33e5ccf4-94ec-4273-a871-19f3b451466a.png" alt="" width="600">

    <br>

    2. **To create new team**
        - Commands: 
            ```console
            curl --insecure -H "Content-Type:application/json" –X POST –d "{\"id\":\"e52baa63-d511-417e-9e54-7aab04286281\", \"name\":\"KC\"}" https://localhost:5001/teams
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233396645-bf1d181d-1ff7-4590-b700-ae14cb75e253.png" alt="" width="600">

    <br>

    3. **To create one more new team**
        - Commands: 
            ```console
            curl --insecure -H "Content-Type:application/json" –X POST –d "{\"id\":\"e12baa63-d511-417e-9e54-7aab04286281\", \"name\":\"MSC Part1\"}" https://localhost:5001/teams
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233396651-fcd5a0e4-9d6e-4891-8308-1d2f03214b1c.png" alt="" width="600">

    <br>

    4. **To get all teams**
        - Commands: To get all teams
            ```console
            curl --insecure https://localhost:5001/teams
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233396653-0a409b89-8248-4b86-a925-087c3d3de318.png" alt="" width="600">

    <br>

    5. **to get single team with team-id as parameter**
        - Commands: 
            ```console
            curl --insecure https://localhost:5001/teams/e52baa63-d511-417e-9e54-7aab04286281
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233396658-4bd0a864-0704-4f0d-9207-9b91b8f0ca20.png" alt="" width="600">

    <br>

    6. **to update team details (change name of first team from "KC" to "KC IT DEPT")**
        - Commands: 
            ```console
            curl --insecure -H "Content-Type:application/json" –X PUT –d "{\"id\":\"e52baa63-d511-417e-9e54-7aab04286281\", \"name\":\"KC IT DEPT\"}" https://localhost:5001/teams/e52baa63-d511-417e-9e54-7aab04286281
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233396661-9e6346c8-e0d1-42bb-973e-cc0a43b9f2dd.png" alt="" width="600">

    <br>

    7. **To delete team**
        - Commands: 
            ```console
            curl --insecure -H "Content-Type:application/json" –X DELETE https://localhost:5001/teams/e52baa63-d511-417e-9e54-7aab04286281
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233396668-81a3a0ca-b4f0-4f1d-8ec3-4d9deccd192d.png" alt="" width="600">

    <br>

    8. **With get all teams now it shows only one team (first one is deleted)**
        - Commands: To get all teams
            ```console
            curl --insecure https://localhost:5001/teams
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233396671-9ce1808d-195e-4121-a038-dac3a47a955a.png" alt="" width="600">

----------------------------------

