**Microservice Architecture** <br>
**Practical #10** <br>
**Working with Docker Volumes and Networks**


***.Net SDK Download Link:***
<br>

- Latest Version:-
https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install

- Old Versions:-
    - **.Net SDK 1.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 3.1** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)
    - **.Net SDK 5.0** :- [DriveLink](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ)



## Steps [.Net SDK 3.1](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EnUooqMLj91Bke5reTl6ui8BnxsQ4YDBTpifjMJLD_3Pwg?e=xVskIQ):

1. Create docker hub login first to use it in play with docker [Click Here to login](https://hub.docker.com/)

<br>

2. Now login in to **Play-With-Docker** ->Click on **Start** -> Click on **Add New Instance**  [Click Here to login](https://labs.play-with-docker.com/)

3. Perform Following steps Inside **Play-With-Docker**

    1. Pull ***nginx image*** into docker

        - Command :
            ```console
            docker pull nginx
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560327-1d1753ac-aea2-4814-a6be-40c157ffd360.png" alt="MA_prac10_1" width="800">

        <br>

    2. Now run the pulled image in Conatiner named **`"webApp"`**

        - Command :
            ```console
            docker run -it --name=webApp -d -p 80:80 nginx
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560332-a60ad369-205d-4422-8cae-2e8d8ca9f987.png" alt="MA_prac10_2" width="800">

        <br>

    3. Click on port 80 to check output (it shows welcome page)

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560336-df8f84b4-e85a-4a1f-9ae7-9804f4cb8dd2.png" alt="MA_prac10_3" width="500">

        <br>

    4. We make changes into **` “index.html”`** file inside `/usr/share/nginx/html` folder

        - Command :
            ```console
            docker exec -it webApp bash

            cd /usr/share/nginx/html

            echo "Hello NK" > index.html
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560337-2bb829de-cbd1-4252-9a0e-47315502b47d.png" alt="MA_prac10_4" width="600">

        <br>

    5. Type exit to return to docker prompt and check process status using **`ps`** option

        - Command :
            ```console
            Exit

            docker ps
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560339-fd3b776e-d2d5-45c1-8c8f-0ff6a4bc9da2.png" alt="MA_prac10_5" width="800">

        <br>

    6. Now refresh on **`port 80`** to see output (you should get modified output)

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560341-28773ac8-df79-438b-bb67-6f6cd4cf250a.png" alt="MA_prac10_6" width="500">

        <br>

    7. Now stop running container named **`“webApp”`**.

        - Command :
            ```console
            docker stop webApp
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560343-11cdbdbe-e217-4140-a0c5-975220762fb5.png" alt="MA_prac10_7" width="500">

        <br>

    8. Start nginx in new container named as **`“webApp1”`**.

        - Command :
            ```console
            docker run -it --name=webApp1 -d -p 80:80 nginx
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560346-953569cf-2227-4c8c-8a23-35269aad8cf1.png" alt="MA_prac10_8" width="800">

        <br>

    9. Now Click on **`port 80`** (you will see the welcome page again)

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560350-b602da51-a3cf-43ae-a8f2-d2633a0ff9d5.png" alt="MA_prac10_9" width="600">

        <br>

- ### To solve this issue **we create new volume**.

    <br>

    10. Create **another instance in play with docker**

    11. create **new volume**

        - Command :
            ```console
            docker volume create MyVolume
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560354-966e88c7-57c7-4304-ac8e-ab5cd8f3ce5d.png" alt="MA_prac10_10" width="500">

        <br>

    12. Check **volume is created**

        - Command :
            ```console
            docker volume ls
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560357-81e4dd62-4f12-4de8-8ce7-ea2621761828.png" alt="MA_prac10_11" width="500">

        <br>

    13. Check **details of volume**

        - Command :
            ```console
            docker volume inspect MyVolume
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560359-5701b5fc-62f4-4edd-803d-845dfa56fb77.png" alt="MA_prac10_12" width="800">

        <br>

    14. Mount this volume to nginx new container named **`“webApp12”`**

        - Command :
            ```console
            docker run -d --name=webApp12 --mount source=MyVolume,destination=/usr/share/nginx/html -p 80:80 nginx
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560361-9f2501a8-190c-4ae1-9650-cc9d7bab0826.png" alt="MA_prac10_13" width="800">

        <br>

    15. Now keep on doing **`"ls"`** and **`"cd"`** to go inside **`_data`** folder of our volume **`“MyVolume”`**

        - Command :
            ```console
            ls /
            
            cd /var/lib/docker
            
            ls
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560365-f320ffef-75b0-4f7b-abfd-1d55336357c1.png" alt="MA_prac10_14" width="800">

        <br>

    16. change directory to **`volumes`** and then **`MyVolumes`**

        - Command :
            ```console
            cd volumes
            
            ls
            
            cd MyVolume
            
            ls
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560366-a3ba3d16-a362-4104-8a7a-4523d878d9bd.png" alt="MA_prac10_15" width="800">

        <br>

    17. change directory to **`_data`** 

        - Command :
            ```console
            cd _data
            
            ls
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560368-bcb24869-2739-46b2-8efa-65cb923c58f1.png" alt="MA_prac10_16" width="500">

        <br>

    18. Modify contents of **`index.html`** file with **`“from MyVolume hello KB”`**

        - Command :
            ```console
            echo "from MyVolume Ninad 22306A1012" > index.html
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560368-bcb24869-2739-46b2-8efa-65cb923c58f1.png" alt="MA_prac10_17" width="500">

        <br>

    19. Now refersh **`port 80`** (to get modified output)

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560379-6d9f1d36-a97a-4ee5-a3b5-f105d01b3329.png" alt="MA_prac10" width="800">

        <br>

    20. Now stop this running container named **`“webApp12”`**

        - Command :
            ```console
            docker stop webApp12
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560374-4750a565-5d49-45d1-b2a4-7e7d4a7bbbc5.png" alt="MA_prac10_" width="300">

        <br>

    21. Now run nginx in new container named **`“webApp13”`**

        - Command :
            ```console
            docker run -d --name=webApp13 --mount source=MyVolume,destination=/usr/share/nginx/html -p 80:80 nginx
            ```

        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560377-c147edc0-d473-440a-a127-c454e96218b0.png" alt="MA_prac10_18" width="800">

        <br>

    22. Click on **`port 80`** and refresh the page you should get edited file as output.


        - output:

            <img src="https://user-images.githubusercontent.com/88243315/233560379-6d9f1d36-a97a-4ee5-a3b5-f105d01b3329.png" alt="MA_prac10_18" width="800">

        <br>