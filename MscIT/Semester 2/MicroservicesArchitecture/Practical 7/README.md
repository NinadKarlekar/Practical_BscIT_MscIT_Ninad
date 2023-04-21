**Microservice Architecture** <br>
**Practical #7** <br>
**Working with TeamService**

| Name | README |
| --- | --- |
| Practical #7A. Running Location Service Locally using .Net core. | [Practical #7A](#practical-7a) |
| Practical #7B. Running Location Service in Docker. | [Practical #7B](#practical-7b) |

<br>

---------------------------------

***.Net SDK Download Link:***
<br>

- Latest Version:-
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

- Old Versions:-
    - **.Net SDK 1.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 3.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 5.0** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)


## **Practical #7A** 
[.Net SDK 3.1](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)

<br>

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

    3. **Command to add new location to member**
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

------------------------------------------------
--------------------------------------------------

## **Practical #7B** <br>

[.Net SDK 3.1](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)

## Running Location Service in Docker
Steps:

1. Create docker hub login first to use it in play with docker [Click Here to login](https://hub.docker.com/)

<br>

2. Now login in to Play-With-Docker  [Click Here to login](https://labs.play-with-docker.com/)

<br>

3. Click on **Start** -> Click on **Add New Instance**

    <img src="https://user-images.githubusercontent.com/88243315/233550542-7d6931b5-39f5-403b-ad8c-a61dbe3b3a89.png" alt="MA_prac7B_1" width="600">

<br>

4. Start typing following commands on play with docker

    1. **Command To run teamservice**
        - Commands: 
            ```console
            docker run -d -p 5000:5000 -e PORT=5000 \

            -e LOCATION__URL=http://localhost:5001 \

            dotnetcoreservices/teamservice:location

            ```

        - Output (you can observe that it has started port 5000 on top):

            <img src="https://user-images.githubusercontent.com/88243315/233550546-85fb478a-b6e5-4af2-9812-e99c4691fe6d.png" alt="MA_prac7B_2" width="800">

    <br>

    2. **Command to run location service**
        - **Commands**: 
            ```console
            docker run -d -p 5001:5001 -e PORT=5001 \

            dotnetcoreservices/locationservice:nodb
            ```

        - **Output** (now it has started one more port that is 5001 for location service):

            <img src="https://user-images.githubusercontent.com/88243315/233550547-48ca33c8-54dd-40f7-9adf-786666952f5c.png" alt="MA_prac7B_3" width="800">

    <br>

    3. **Command to check running images in docker**
        - **Commands**: 
            ```console
            docker images
            ```

        - **Output**:

            <img src="https://user-images.githubusercontent.com/88243315/233550552-e56e5267-67b5-4d6e-b95e-8d7372836f5e.png" alt="MA_prac7B_4" width="800">

    <br>

    4. **Command to create new team**
        - **Commands**: 
            ```console
            curl -H "Content-Type:application/json" -X POST -d '{"id":"e52baa63-d511-417e-9e54-7aab04286281", "name":"KC"}' http://localhost:5000/teams
            ```

        - **Output**:

            <img src="https://user-images.githubusercontent.com/88243315/233550555-edc87b38-8d8f-4f2b-881e-781681cd77f5.png" alt="MA_prac7B_5" width="900">

    <br>

    5. **Command To confirm that team is added**
        - **Commands**: 
            ```console
            curl http://localhost:5000/teams/e52baa63-d511-417e-9e54-7aab04286281
            ```

        - **Output**:

            <img src="https://user-images.githubusercontent.com/88243315/233550558-3a77b9dd-22ec-41be-a85d-40e1c2815c6d.png" alt="MA_prac7B_6" width="800">

    <br>

    6. **Command to add new member to team**
        - **Commands**: 
            ```console
            curl -H "Content-Type: application/json" -X POST -d '{"id":"63e7acf8-8fae-42ce-9349-3c8593ac8292", "firstName":"Ninad", "lastName":"Karlekar"}' http://localhost:5000/teams/e52baa63-d511-417e-9e54-7aab04286281/members

            ```

        - **Output**:

            <img src="https://user-images.githubusercontent.com/88243315/233550564-ae61fc6b-e220-478e-9691-510986a41327.png" alt="MA_prac7B_7" width="800">

    <br>

    7. **Command To confirm member added**
        - **Commands**: 
            ```console
            curl http://localhost:5000/teams/e52baa63-d511-417e-9e54-7aab04286281
            ```

        - **Output**:

            <img src="https://user-images.githubusercontent.com/88243315/233550567-0449bf0a-33a8-4aca-80af-da3826859daf.png" alt="MA_prac7B_8" width="800">

    <br>

    8. **Command To add location for member**
        - **Commands**: 
            ```console
            curl -H "Content-Type:application/json" -X POST -d \

            '{"id":"64c3e69f-1580-4b2f-a9ff-2c5f3b8f0e1f","latitude":12.0,"longitude":12.0,"altitude":10.0, "timestamp":0,"memberId":"63e7acf8-8fae-42ce-9349-3c8593ac8292"}' http://localhost:5001/locations/63e7acf8-8fae-42ce-9349-3c8593ac8292
            ```

        - **Output**:

            <img src="https://user-images.githubusercontent.com/88243315/233550572-3d832b0d-aa85-4d27-821f-2ec0f454d8df.png" alt="MA_prac7B_9" width="800">

    <br>

    9. **Command To confirm location is added in member**
        - **Commands**: 
            ```console
            curl http://localhost:5001/locations/63e7acf8-8fae-42ce-9349-3c8593ac8292
            ```

        - **Output**:

            <img src="https://user-images.githubusercontent.com/88243315/233550576-ea9aaec4-92f5-49a8-a782-1fe75d8e0321.png" alt="MA_prac7B_10" width="800">

    <br>