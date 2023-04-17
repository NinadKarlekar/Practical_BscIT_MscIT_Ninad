# Practical 6 : Hadoop Installation:  
## Aim: Install, run Hadoop and HDFS and explore HDFS on Windows

- Steps to Install Hadoop

1. [Java JDK 1.8](#1-install-java)
2. [Download Hadoop and extract and place under C drive](#2-download-hadoop)
3. [Path in Environment Variables](#3-set-path-for-environment-variables)
4. [Change files under Hadoop directory](#4-change-files-under-hadoop-directory)
5. [Create folder datanode and namenode under data directory](#5-create-folder-datanode-and-namenode-under-data-directory)
6. [Change HDFS and YARN files](#6-change-hdfs-and-yarn-files)
7. [Java Home environment in Hadoop environment](#7-java-home-environment-in-hadoop-environment)
8. [Download “redistributable” package](#)
9. [Hadoop Configurations]()
10. [Format the NameNode]()
11. [Complete Test by executing start-all.cmd]()

------------------------------------

<br>

### 1.	Install Java

- Java JDK Link to download (https://www.oracle.com/java/technologies/javase-jdk8-downloads.html) | [Drive Link](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EldIHnqoojZAuQAXCkc9omABST-5MPkCY7gVZ00037d7vA?e=vURHYu)
- Extract and install Java in C:\Java
- open cmd and type -> 

    ```console
    javac -version
    ```

    <img src="https://user-images.githubusercontent.com/88243315/232517670-5c100186-bc1c-4a35-918c-0a520aafac78.png" alt="BDA_prac6_1" width="300px">

<br>

### 2.	Download Hadoop

- Download hadoop-3.3.0.tar.gz [Drive link](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EldIHnqoojZAuQAXCkc9omABST-5MPkCY7gVZ00037d7vA?e=vURHYu) |
https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz

- right click .rar.gz file -> show more options -> 7-zip->and extract to **`C:\Hadoop-3.3.0\`**

    <img src="https://user-images.githubusercontent.com/88243315/232517681-ee55678e-9899-425f-8894-8ac6ef5914a1.png" alt="BDA_prac6_2" width="600px">

<br>

### 3. Set path for Environment Variables

- Set the path **JAVA_HOME** Environment variable

    <img src="https://user-images.githubusercontent.com/88243315/232517687-865c61ac-5c66-4440-bbfb-d21211902674.png" alt="BDA_prac6_3" width="600px">

- Set the path **HADOOP_HOME** Environment variable

    <img src="https://user-images.githubusercontent.com/88243315/232517691-921837cb-cc37-4970-8389-2a0fecf56f24.png" alt="BDA_prac6_4" width="600px">

- Add this variables to both **user variables** and **system variables**. -> Click on user variable -> path -> edit-> add path for Hadoop and java upto ‘bin’


- Click **OK**.

<br>

### 4. Change files under Hadoop directory

1. Edit file `C:/Hadoop-3.3.0/etc/hadoop/core-site.xml`
    - paste the below xml code in folder and save
    ```xml
    <configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
    </configuration>
    ```

<br>

2. Rename **`mapred-site.xml.template`** to **`mapred-site.xml`** **(IF EXIST)** and edit this file **`C:/Hadoop-3.3.0/etc/hadoop/mapred-site.xml`**, paste xml code and save this file.
    ```xml
    <configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    </configuration>
    ```

<br>

### 5. Create folder ***datanode*** and ***namenode*** under ***data directory***

1. Create folder `data` under `C:\Hadoop-3.3.0`
2. Create folder `datanode` under `C:\Hadoop-3.3.0\data`
3. Create folder `namenode` under `C:\Hadoop-3.3.0\data`

<br>

### 6. Change HDFS and YARN files

1. Edit file **`C:\Hadoop-3.3.0\etc\hadoop\hdfs-site.xml`**
    - paste the below xml code in folder and save
    ```xml
    <configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>

    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/hadoop-3.3.0/data/namenode</value>
    </property>

    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/hadoop-3.3.0/data/datanode</value>
    </property>

    </configuration>
    ```

<br>

2. Edit file **`C:\Hadoop-3.3.0\etc\hadoop\yarn-site.xml`**
    - paste the below xml code in folder and save
    ```xml
    <configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <property>
        <name>yarn.nodemanager.auxservices.mapreduce.shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>

    <property>
        <name>yarn.resourcemanager.address</name>
        <value>127.0.0.1:8032</value>
    </property>

    <property>
        <name>yarn.resourcemanager.scheduler.address</name>
        <value>127.0.0.1:8030</value>
    </property>

    <property>
        <name>yarn.resourcemanager.resource-tracker.address</name>
        <value>127.0.0.1:8031</value>
    </property>

    </configuration>
    ```

<br>

### 7. ***Java Home environment*** in Hadoop environment

- Edit file ***`C:/Hadoop-3.3.0/etc/hadoop/hadoop-env.cmd`***
    - Find **JAVA_HOME=%JAVA_HOME%** and replace it as
    set **JAVA_HOME="C:\Java\jdk1.8.0_361"**


<br>

### 8. Download **`"redistributable"`** package

- Download and run **`VC_redist.x64.exe`**
- Download:- [Drive Link](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EldIHnqoojZAuQAXCkc9omABST-5MPkCY7gVZ00037d7vA?e=vURHYu) | [Github link](https://github.com/s911415/apache-hadoop-3.1.0-winutils)

<br>

### 9. Hadoop Configurations

- Download **bin** folder from [Drive Link](https://vsitedu-my.sharepoint.com/:f:/g/personal/ninad_karlekar_vsit_edu_in/EldIHnqoojZAuQAXCkc9omABST-5MPkCY7gVZ00037d7vA?e=vURHYu) | [Github link](https://github.com/s911415/apache-hadoop-3.1.0-winutils)

- Copy the **bin** folder to c:\hadoop-3.3.0. Replace the existing **bin** folder.

- Copy ***`"hadoop-yarn-server-timelineservice-3.0.3.jar"`*** from ***`~\hadoop-3.0.3\share\hadoop\yarn\timelineservice`*** to ***`~\hadoop-3.0.3\share\hadoop\yarn folder`***.  

<br>

### 10. Format the NameNode
- Open cmd ‘Run as Administrator’ and type command
    ```console
    hdfs namenode –format
    ```

    <img src="https://user-images.githubusercontent.com/88243315/232517694-9fb6dccf-c81a-4b93-a100-8771bba3f940.png" alt="BDA_prac6_5" width="600px">

<br>

### 11. Testing

1. Open cmd **`‘Run as Administrator’`** and change directory to **`C:\Hadoop-3.3.0\sbin`**
2. type ***`start-all.cmd`***
3. You will get 4 more running threads for `Datanode`, `namenode`, `resouce manager` and `node manager`

    <img src="https://user-images.githubusercontent.com/88243315/232517702-054c2c02-95ce-4eec-8c20-48eda4436293.png" alt="BDA_prac6_6" width="900px">

4. Type `JPS` command to `start-all.cmd` command prompt, you will get following output.

    <img src="https://user-images.githubusercontent.com/88243315/232517714-c0fa0f6a-9330-4da7-8565-b44e0d60852e.png" alt="BDA_prac6_7" width="400px">

5. Run http://localhost:9870/ from any browser

    <img src="https://user-images.githubusercontent.com/88243315/232517717-67061cdb-5527-4705-af6c-258e7d58cc65.png" alt="BDA_prac6_7" width="800px">

    <img src="https://user-images.githubusercontent.com/88243315/232535827-379b77ab-c3b5-461f-b0ee-c2102b31cc93.png" alt="BDA_prac6_7" width="800px">

--------------------