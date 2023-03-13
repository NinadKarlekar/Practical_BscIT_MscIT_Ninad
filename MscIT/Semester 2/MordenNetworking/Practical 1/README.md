# Practical 1

## STEPS

1. Open GNS3 and create a new project.
2. Drag and drop 3 routers as R1, R2, R3

    <img src="" alt="1" width="550">

3. Right click on router -> configure -> select router name -> slots -> Select slot 1 as ***`NM-4T`***

    <img src="" alt="2" width="550">
    <img src="" alt="3" width="550">

4. Connect routers: 

    1. R1 and R2 ==> s1/0
    2. R1 and R3 ==> s1/1

    <img src="" alt="4" width="550">

5. Lable topology with given lables below and click on run

    <img src="" alt="5" width="550">

6. After clicking on run -> right click on router -> console

    <img src="" alt="6" width="550">

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

    <img src="" alt="8" width="550">

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

    <img src="" alt="7" width="550">


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

    <img src="" alt="9" width="550">


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

    <img src="" alt="11" width="550">

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

    <img src="" alt="12" width="550">


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

    <img src="" alt="10" width="550">


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

    <img src="" alt="14" width="550">

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

    <img src="" alt="13" width="550">


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

    <img src="" alt="15" width="550">


    </details>

<br>

10. To `show ip route` type following command in each router console

    ```bash
    do sh ip route
    ```

    <details>
    <summary>Screenshot</summary>
    <br>
    <img src="" alt="17" width="550">
    <img src="" alt="18" width="550">
    <img src="" alt="16" width="550">
    
    </details>



11. To verify output type following commands: ***(OUTPUT)***

    1. From ***`R2(COMPANY)`*** to ***`R3(CUSTOMER)`***

        ```bash
        do ping 10.3.3.3 source lo0
        ```

        - OUTPUT

            <img src="" alt="18" width="550">

            <br>

    2. From ***`R3(CUSTOMER)`*** to ***`R2(COMPANY)`***

        ```bash
        do ping 10.2.2.2 source lo0
        ```

        - OUTPUT

            <img src="" alt="13" width="550">