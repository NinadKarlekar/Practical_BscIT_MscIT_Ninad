# Practical 3

## STEPS

1. Open GNS3 and create a new project.

<br>

2. Drag and drop 3 routers as R1, R2, R3 and three switches and complete topology as follows

    <img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/164cf156-746d-4a51-900d-ff22b7cf0d83" alt="MN_prac3_1" width="800">

3. Right click on router -> configure -> select router name -> slots -> Select slot 1 as ***`NM-4T`***

    <img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/e48b6919-22a9-4810-8e44-f0846a033893" alt="MN_prac3_2" width="600">


<br>

4. Connect routers: 

    1. R1 and R2 ==> s1/0
    2. R1 and R3 ==> s1/1
    3. R2 and R3 ==> f0/0

    <br>

## Step 1: Configure IP addresses on the given routers


<details>
<summary>R1 console</summary>
<br>

```console
conf t
```

```console
int f0/1
```

```console
ip add 192.168.1.1 255.255.255.0
```

```console
no sh
```

```console

int s1/0
```

```console
ip add 172.16.1.1 255.255.255.0
```

```console
no sh
```

```console

int s1/1
```

```console
ip add 172.16.5.1 255.255.255.0
```

```console
no sh

```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/3675d35e-bdbe-400f-9c99-f8730ffaa7a6" alt="MN_prac3_3" width="550">

</details>

<br>

<details>
<summary>R2 console</summary>
<br>

```console
conf t
```

```console
int f0/0
```

```console
ip add 10.10.10.2 255.255.255.0
```

```console
no sh
```

```console
int f0/1
```

```console
ip add 192.168.2.2 255.255.255.0
```

```console
no sh
```

```console

int s1/0
```

```console
ip add 172.16.1.2 255.255.255.0
```

```console
no sh

```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/d2e737ef-9425-4c5d-b2a4-b9578f9e32f3" alt="MN_prac3_4" width="550">


</details>

<br>

<details>
<summary>R3 console</summary>
<br>

```console
conf t
```

```console
int f0/0
```

```console
ip add 10.10.10.3 255.255.255.0
```

```console
no sh
```

```console
int f0/1
```

```console
ip add 192.168.3.3 255.255.255.0
```

```console
no sh
```

```console
int s1/1
```

```console
ip add 172.16.5.3 255.255.255.0
```

```console
no sh
```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/8063cc93-f768-4d7d-b93f-44665ee7e1c9" alt="MN_prac3_5" width="550">


</details>

<br>

<details>
<summary>check connection On all routers:</summary>
<br>

```console
do sh ip int br | include up
```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/2de03085-3d40-463f-b2b1-424cc81f3145" alt="MN_prac3_6" width="550">
<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/761a2cf5-3a17-46f7-8148-a62b19ad2c9a" alt="MN_prac3_7" width="550">
<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/12e9892c-41bd-4a00-92f0-1c2c36c3ce4a" alt="MN_prac3_8" width="550">


</details>

<br>

## Step 2: Configure IRP in autonomous system 65200


<details>
<summary>R2 console</summary>
<br>

```console
router ospf 1
```

```console
network 10.10.10.0 0.0.0.255 area 0
```

```console
network 192.168.2.0 0.0.0.255 area 1
```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/81031ea9-0907-42cb-bf58-e5b8851049ee" alt="MN_prac3_9" width="550">

</details>

<br>

<details>
<summary>R3 console</summary>
<br>

```console
router ospf 1
network 10.10.10.0 0.0.0.255 area 0
network 192.168.3.0 0.0.0.255 area 2

```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/ac03798d-1856-40fb-bab0-d0ba696449b0" alt="MN_prac3_10" width="550">

</details>

<br>

<details>
<summary>Ping</summary>
<br>

```console
do ping 192.168.2.2
```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/e9076091-577f-473c-a40f-332edbbcfc42" alt="MN_prac3_11" width="550">

</details>

<br>

## Step 3: IBGP & EBGP configuration


<details>
<summary>R1 console</summary>
<br>

```console
router bgp 65100
```

```console
network 192.168.1.0
```

```console
network 172.16.1.0 mask 255.255.255.0
```

```console
network 172.16.5.0 mask 255.255.255.0
```

```console
neighbor 172.16.1.2 remote-as 65200
```

```console
neighbor 172.16.5.3 remote-as 65200
```

```console
do sh ip route


```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/081f0c61-a9fb-4135-a10e-0b331426984d" alt="MN_prac3_12" width="550">

</details>

<br>

<details>
<summary>R2 console</summary>
<br>

```console
router bgp 65200
```

```console
redistribute ospf 1
```

```console
network 172.16.1.0 mask 255.255.255.0
```

```console
neighbor 172.16.1.1 remote-as 65100
```

```console
neighbor 10.10.10.3 remote-as 65200
```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/3c856161-2b23-4b52-b4ef-e4f072e88abb" alt="MN_prac3_13" width="550">

</details>

<br>

<details>
<summary>R3 console</summary>
<br>

```console
router bgp 65200
```

```console
redistribute ospf 1
```

```console
network 172.16.5.0 mask 255.255.255.0
```

```console
neighbor 172.16.5.1 remote-as 65100
```

```console
neighbor 10.10.10.2 remote-as 65200
```

```console
do sh ip route

```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/1f940445-0a5d-4ad2-9a77-9994da3ad8b7" alt="MN_prac3_14" width="550">

</details>

<br>

## Step 4: PING

<details>
<summary>R1 console</summary>
<br>

```console
do ping 192.168.3.3
```

```console
do ping 192.168.2.2
```

<img src="https://github.com/NinadKarlekar/TestRepoNK/assets/88243315/24db677f-0b50-49ba-bbec-f9d3e3463277" alt="MN_prac3_15" width="550">

</details>