# Aim: Working with Docker

## 3 a) Method 1: To pull and push images using docker

---------------------

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

[🔝](#index)

</details>

**************

## 3 b) **Method 2:** Build an image then push it to docker and run it

---------------------

<details>
<summary>STEPS</summary>



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

</details>

************************************************