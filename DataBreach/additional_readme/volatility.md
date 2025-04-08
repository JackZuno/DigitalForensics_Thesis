## Volatility (Failed, I Hate volatility)
I want to analyze the RAM of one of my docker containers. The problem is that extracting a RAM image directly from a Docker container image is not straightforward because Docker images do not contain memory snapshots; they consist of filesystem layers (code, libraries, configuration files, etc.) rather than live process memory.\
However, it is possible to perform memory analysis on a Docker container environment, but it involves a different approach.\
Since Docker containers share the host kernel and are isolated processes running on the host, you would need to capture the RAM of the entire host system. Once you have this RAM dump, you can then try to isolate memory segments related to Docker containers or processes.

### Extract the RAM Image
To save the image of the host RAM I used **DumpIt.exe**.\
After the program is downloaded and the folder is extracted, I run *DumpIt.exe* and then saved the image.\
On the target container I installed **avml**:
```bash
wget https://github.com/microsoft/avml/releases/download/v0.14.0/avml

chmod 755 avml

avml memory.dmp
```

### OS Profile
The first part is used to extract info about the OS running, which in this case the host of the OS (a windows computer where I am running docker).\
To see more about it go here: **[windows.info](volatility/volatility.md#os-profile-windowsinfo)**.

### Process List
This command is used to retrieve the list of all processes running on the device. From this list it is possible to look for container processes that are running.\
To see more about it go here: **[windows.pslist.PsList](volatility/volatility.md#process-list-windowspslistpslist)**.

```sh
```

```sh
```

```sh
```

```sh
```
