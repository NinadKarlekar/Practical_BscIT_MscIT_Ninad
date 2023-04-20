**Microservice Architecture** <br>
**Practical #7** <br>
**Working with TeamService**


***.Net SDK Download Link:***
<br>

- Latest Version:-
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

- Old Versions:-
    - **.Net SDK 1.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 3.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)


Steps:

1. We need to open ***3 command prompts***

2. On **command prompt `1`** start location service (go inside **locationservices** folder first)
- Command :
    ```console
    dotnet run --server.urls "http://*:5001"
    ```

- output:

    <img src="https://user-images.githubusercontent.com/88243315/233443050-a6c22766-c954-4cf8-8810-102d8b038ea7.png" alt="MA_prac7_1" width="800">

<br>

2. On **command prompt `2`** start location service (go inside **teamservices** folder first)
- Command :
    ```console
    dotnet run
    ```

- output:

    <img src="https://user-images.githubusercontent.com/88243315/233443058-5de00a2e-0e3f-4d08-ac97-ce9f9017a208.png" alt="MA_prac7_2" width="600">

<br>

3. On **command prompt `3`** run all following commands 

    1. **Command to Add new team**
        - Commands: To get all teams
            ```console
            curl -H "Content-Type:application/json" -X POST -d "{\"id\":\"e52baa63-d511-417e-9e54-7aab04286281\", \"name\":\"KC\"}" http://localhost:5000/teams

            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233443060-ef1cacbe-a076-4088-ab44-15006bfb6a0d.png" alt="" width="600">

    <br>

    2. **Command to add new member to team**
        - Commands: 
            ```console
            curl -H "Content-Type:application/json" -X POST -d "{\"id\":\"63e7acf8-8fae-42ce-9349-3c8593ac8292\",\"firstName\":\"Ninad\", \"lastName\":\"Karlekar\"}" http://localhost:5000/teams/e52baa63-d511-417e-9e54-7aab04286281/members
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233443061-09c66cfe-4d8d-45f0-b1d0-2e948544515c.png" alt="" width="600">

    <br>

    3. **Command to add new member to team**
        - Commands: 
            ```console
            curl -H "Content-Type:application/json" -X POST -d "{\"id\":\"64c3e69f-1580-4b2f-a9ff-2c5f3b8f0e1f\",\"latitude\":12.0,\"longitude\":12.0,\"altitude\":10.0,\"timestamp\":0,\"memberId\":\"63e7acf8-8fae-42ce-9349-3c8593ac8292\"}" http://localhost:5001/locations/63e7acf8-8fae-42ce-9349-3c8593ac8292

            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233443064-38974e7f-6a33-4a05-8f93-43a1eb354768.png" alt="" width="600">

    <br>

    4. **Command To confirm it is accessible from teams (that is from port 5000) it shows last location**
        - Commands: 
            ```console
            curl http://localhost:5000/teams/e52baa63-d511-417e-9e54-7aab04286281/members/63e7acf8-8fae-42ce-9349-3c8593ac8292
            ```

        - Output:

            <img src="https://user-images.githubusercontent.com/88243315/233443067-01a5fd32-79e9-4f58-89fc-5ea5b8561b9f.png" alt="" width="600">

    <br>

<br>

