# Practical 1

## STEPS

1. Open GNS3 and create a new project.

<br>

2. Drag and drop 3 routers as R1, R2, R3

    <img src="https://user-images.githubusercontent.com/88243315/224759418-33cba246-67a2-4579-8a04-c537fb51f886.png" alt="MN_prac1_1" width="350">

<br>

3. Right click on router -> configure -> select router name -> slots -> Select slot 1 as ***`NM-4T`***

    <img src="https://user-images.githubusercontent.com/88243315/224759422-58cbb542-870d-4931-ac12-e249de5593ce.png" alt="2" width="350">
    <img src="https://user-images.githubusercontent.com/88243315/224759426-b94601f2-497a-456c-ba04-770dd7e0beaf.png" alt="3" width="450">

<br>

4. Connect routers: 

    1. R1 and R2 ==> s1/0
    2. R1 and R3 ==> s1/1

    <img src="https://user-images.githubusercontent.com/88243315/224759429-25ae8050-75ee-46a8-afa9-db6090bbfe00.png" alt="4" width="550">

<br>

5. label topology with given labels below and click on run

    <img src="https://user-images.githubusercontent.com/88243315/224759433-f9fc7039-0c3e-416f-82a8-4169256cc023.png" alt="5" width="550">

<br>

6. After clicking on run -> right click on router -> console

    <img src="https://user-images.githubusercontent.com/88243315/224759436-2bff2be9-3048-4439-843d-2431f5de7d27.png" alt="6" width="300">

<br>

7. On `Router console` type following commands one by one.

    <details>
    <summary>R1 console</summary>
    <br>

    ```bash
    conf t


    int s1/0

    ip add 192.168.1.1 255.255.255.0

    no sh


    int s1/1

    ip add 172.24.1.1 255.255.255.0

    no sh

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759443-1f9f7863-6699-4595-b13b-d6027f012ee5.png" alt="8" width="550">

    </details>

    <br>

    <details>
    <summary>R2 console</summary>
    <br>

    ```bash
    conf t


    int s1/0

    ip add 192.168.1.2 255.255.255.0

    no sh

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759440-2569c2f4-a198-4bad-af9c-e9262af867b3.png" alt="7" width="550">


    </details>

    <br>

    <details>
    <summary>R3 console</summary>
    <br>

    ```bash
    conf t


    int s1/1

    ip add 172.24.1.3 255.255.255.0

    no sh

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759360-527b0970-679c-4fa0-baaf-730cb9e761ce.png" alt="9" width="550">


    </details>

<br>

8. To add ***`loopback address`*** ,On `Router console` type following commands one by one.

    <details>
    <summary>R1 console loopback</summary>
    <br>

    - continue after old console commands only.

    ```bash
    int lo0

    ip add 10.1.1.1 255.255.255.0

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759376-a8e83fc0-4740-4299-a16d-5e8ed7d7a407.png" alt="11" width="550">

    </details>

    <br>

    <details>
    <summary>R2 console loopback</summary>
    <br>

    - continue after old console commands only.

    ```bash
    int lo0

    ip add 10.2.2.2 255.255.255.0

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759378-ddf96dac-29c5-468f-ab76-7a540f02cd5a.png" alt="12" width="550">


    </details>

    <br>

    <details>
    <summary>R3 console loopback</summary>
    <br>

    - continue after old console commands only.

    ```bash
    int lo0

    ip add 10.3.3.3 255.255.255.0

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759373-5e0c0661-bb3a-4d91-9dc5-9827a9b5532d.png" alt="10" width="550">


    </details>

    <br>

9. to add ***`bgp protocol`***, On `Router console` type following commands one by one.

    <details>
    <summary>R1 console loopback</summary>
    <br>

    - continue after old console commands only.

    ```bash
    router bgp 100

    neighbor 192.168.1.2 remote-as 200

    neighbor 172.24.1.3 remote-as 300

    network 10.1.1.0 mask 255.255.255.0

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759391-a7754e7b-3787-4caa-b6a6-17c724a1e985.png" alt="14" width="550">

    </details>

    <br>

    <details>
    <summary>R2 console loopback</summary>
    <br>

    - continue after old console commands only.

    ```bash
    router bgp 200

    neighbor 192.168.1.1 remote-as 100

    network 10.2.2.0 mask 255.255.255.0

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759386-3a3b5266-f698-458c-89a7-188ca7925adf.png" alt="13" width="550">


    </details>

    <br>

    <details>
    <summary>R3 console loopback</summary>
    <br>

    - continue after old console commands only.

    ```bash
    router bgp 300

    neighbor 172.24.1.1 remote-as 100

    network 10.3.3.0 mask 255.255.255.0

    ```

    <img src="https://user-images.githubusercontent.com/88243315/224759394-c166aa50-bb4b-413f-b2f2-a6d2008b811d.png" alt="15" width="550">


    </details>

<br>

10. To `show ip route` type following command in each router console

    ```bash
    do sh ip route
    ```

    <details>
    <summary>Screenshot</summary>
    <br>
    <img src="https://user-images.githubusercontent.com/88243315/224759402-635f4451-0214-4ec2-83cb-8152aeee7631.png" alt="17" width="550">
    <img src="https://user-images.githubusercontent.com/88243315/224759404-10e1852f-0ab7-4e3d-8da2-e79b69eee903.png" alt="18" width="550">
    <img src="https://user-images.githubusercontent.com/88243315/224759399-fa588d23-0bc9-48bd-9d2d-0c30178bda4e.png" alt="16" width="550">
    
    </details>

    <br>


11. To verify output type following commands: ***(OUTPUT)***

    1. From ***`R2(COMPANY)`*** to ***`R3(CUSTOMER)`***

        ```bash
        do ping 10.3.3.3 source lo0
        ```

        - ***OUTPUT***

            <img src="https://user-images.githubusercontent.com/88243315/224759411-aee574c5-a8d6-4850-8f4c-634cc6f7ddba.png" alt="19" width="650">

            <br>

    2. From ***`R3(CUSTOMER)`*** to ***`R2(COMPANY)`***

        ```bash
        do ping 10.2.2.2 source lo0
        ```

        - ***OUTPUT***

            <img src="https://user-images.githubusercontent.com/88243315/224759415-0d722ead-89ff-49d8-8abc-a1e28d55278f.png" alt="20" width="650">