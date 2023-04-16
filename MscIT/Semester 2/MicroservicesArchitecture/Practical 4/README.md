# Aim: Working with Docker Desktop App

---------------------





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

1. Run hello-world on browser

    ```bash
    docker run -p 8080:8080 dotnetcoreservices/hello-world 
    ```

    <img src="https://user-images.githubusercontent.com/88243315/232334945-ee851886-839c-458e-9ab0-0ef0b692f088.png" width="600px" alt ="MA_prac4_1">

<br>

2. Run Localhost in browser

    <img src="https://user-images.githubusercontent.com/88243315/232334950-297bff2a-f0ba-4a5c-bcac-57ea4586ab38.png" width="600px" alt ="MA_prac4_2">

<br>

3. Lists **all the running Docker containers** on the host machine.

    ```bash
    docker ps
    ```

    <img src="https://user-images.githubusercontent.com/88243315/232334951-2d75ef72-8fb8-410c-bc17-a529733b4dd0.png" width="800px" alt ="MA_prac4_3">

<br>

4. Command

    ```bash
    curl http://localhost:8080/will/it/blend?
    ```

    <img src="https://user-images.githubusercontent.com/88243315/232335144-12ffea86-18dd-4584-a756-8afd4b7e616c.png" width="600px" alt ="MA_prac4_4">

<br>

5. Kill running process

    ```bash
    docker kill <PID> 
    ```

    - Insert ***`Container ID`*** in place of `<PID>` **(process id of application)**

    <img src="https://user-images.githubusercontent.com/88243315/232335145-88dabfd6-56e7-46ea-bd96-3653bc423254.png" width="600px" alt ="MA_prac4_5">

<br>

6. Process Id terminated

    <img src="https://user-images.githubusercontent.com/88243315/232335264-b9bf842f-cfa1-4538-838f-0d7349978991.png" width="600px" alt ="MA_prac4_6">

    <br>

    <img src="https://user-images.githubusercontent.com/88243315/232335267-acaa9117-7ea9-4500-9cb7-e47620a907d3.png" width="600px" alt ="MA_prac4_5">

</details>

**************