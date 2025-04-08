## Volatility Analysis
With **| findstr target** after the command in powershell it is possible to filter the result with lines containing only the target word.

### OS Profile (windows.info)
In the powershell I then used **volatility3**:
```sh
python3 C:\Users\jackz\Volatility\volatility3\vol.py -f .\JACK-20241025-090907.dmp windows.info
```
Result:
```sh
PS C:\Users\jackz\Desktop\test> python3 C:\Users\jackz\Volatility\volatility3\vol.py -f .\JACK-20241025-090907.dmp windows.info
Volatility 3 Framework 2.7.1
Progress:  100.00               PDB scanning finished
Variable        Value

Kernel Base     0xf80305800000
DTB     0x1af000
Symbols file:///C:/Users/jackz/Volatility/volatility3/volatility3/symbols/windows/ntkrnlmp.pdb/9074FC2B82ED2B7E1CB3366B64BE62F9-1.json.xz
Is64Bit True
IsPAE   False
layer_name      0 WindowsIntel32e
memory_layer    1 WindowsCrashDump64Layer
base_layer      2 FileLayer
KdVersionBlock  0xf803064099a0
Major/Minor     15.22621
MachineType     34404
KeNumberProcessors      12
SystemTime      2024-10-25 09:09:22
NtSystemRoot    C:\WINDOWS
NtProductType   NtProductWinNt
NtMajorVersion  10
NtMinorVersion  0
PE MajorOperatingSystemVersion  10
PE MinorOperatingSystemVersion  0
PE Machine      34404
PE TimeDateStamp        Fri Jul  2 05:18:00 1993
```
### Process List (windows.pslist.PsList)
Command:
```sh
PS C:\Users\jackz\Desktop\test> python3 C:\Users\jackz\Volatility\volatility3\vol.py -f .\JACK-20241025-090907.dmp windows.pslist.PsList
```
Result:
```sh
PS C:\Users\jackz\Desktop\test> python3 C:\Users\jackz\Volatility\volatility3\vol.py -f .\JACK-20241025-090907.dmp windows.pslist.PsList
Volatility 3 Framework 2.7.1
Progress:  100.00               PDB scanning finished
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime        File output

4       0       System  0xe30b558e5040  1176    -       N/A     False   2024-10-21 13:42:41.000000      N/A     Disabled
140     4       Secure System   0xe30b55ac9040  0       -       N/A     False   2024-10-21 13:42:37.000000      N/A     Disabled
204     4       Registry        0xe30b55df2040  4       -       N/A     False   2024-10-21 13:42:37.000000      N/A     Disabled
752     4       smss.exe        0xe30b7265d040  2       -       N/A     False   2024-10-21 13:42:41.000000      N/A     Disabled
1016    876     csrss.exe       0xe30b7b293140  18      -       0       False   2024-10-21 13:42:47.000000      N/A     Disabled
1032    876     wininit.exe     0xe30b7d1e6080  4       -       0       False   2024-10-21 13:42:48.000000      N/A     Disabled
1040    828     csrss.exe       0xe30b7d1e8140  0       -       1       False   2024-10-21 13:42:48.000000      2024-10-21 16:54:58.000000      Disabled
1104    1032    services.exe    0xe30b7d281080  9       -       0       False   2024-10-21 13:42:48.000000      N/A     Disabled
1124    1032    LsaIso.exe      0xe30b7d287080  2       -       0       False   2024-10-21 13:42:48.000000      N/A     Disabled
1140    1032    lsass.exe       0xe30b7d28b080  16      -       0       False   2024-10-21 13:42:48.000000      N/A     Disabled
1336    1104    svchost.exe     0xe30b7d331080  31      -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1372    1032    fontdrvhost.ex  0xe30b7d34b080  7       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1472    1104    svchost.exe     0xe30b7d3e30c0  15      -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1524    1104    svchost.exe     0xe30b7d460080  7       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1612    1104    svchost.exe     0xe30b7d4a6080  3       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1636    1104    svchost.exe     0xe30b7d4d8080  5       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1648    1104    svchost.exe     0xe30b7d4d7080  0       -       0       False   2024-10-21 13:42:49.000000      2024-10-21 14:10:14.000000      Disabled
1696    1104    svchost.exe     0xe30b7d51a080  5       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1704    1104    svchost.exe     0xe30b7d51b080  18      -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1776    1104    svchost.exe     0xe30b7d547080  4       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1812    1104    svchost.exe     0xe30b7d556080  27      -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1972    1104    svchost.exe     0xe30b7d669080  3       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
1100    1104    svchost.exe     0xe30b7d6c00c0  5       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
2084    1104    svchost.exe     0xe30b7d739080  11      -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
2120    1104    NVDisplay.Cont  0xe30b7d737080  32      -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
2180    1104    svchost.exe     0xe30b7d776080  6       -       0       False   2024-10-21 13:42:49.000000      N/A     Disabled
2248    1104    svchost.exe     0xe30b7d7ac0c0  22      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2304    1104    svchost.exe     0xe30b7d7b7080  7       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2316    1104    svchost.exe     0xe30b7d7b8080  9       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2368    1104    svchost.exe     0xe30b7d807080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2376    1104    svchost.exe     0xe30b7d80a080  6       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2392    1104    svchost.exe     0xe30b7d808080  6       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2516    1104    svchost.exe     0xe30b7d832080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2556    4       MemCompression  0xe30b7d8ad040  50      -       N/A     False   2024-10-21 13:42:50.000000      N/A     Disabled
2664    1104    svchost.exe     0xe30b7d9d7080  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2824    1104    svchost.exe     0xe30b7d9d8080  11      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2876    1104    igfxCUIService  0xe30b7da08080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2932    1104    svchost.exe     0xe30b7da6e080  8       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2960    1104    svchost.exe     0xe30b7da8b080  6       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2976    1104    svchost.exe     0xe30b7da90080  9       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2488    1104    svchost.exe     0xe30b7daef080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
2804    1104    svchost.exe     0xe30b7db240c0  7       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3144    1104    svchost.exe     0xe30b7daf2080  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3228    1104    svchost.exe     0xe30b7db2e080  13      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3252    1104    svchost.exe     0xe30b7db8b080  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3352    1104    svchost.exe     0xe30b7dc130c0  12      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3388    1104    svchost.exe     0xe30b7dc21080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3508    1104    svchost.exe     0xe30b7dd020c0  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3516    1104    svchost.exe     0xe30b7dc990c0  11      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3740    1104    svchost.exe     0xe30b7ddce080  17      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3792    1104    svchost.exe     0xe30b7de4c080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3816    1104    svchost.exe     0xe30b7de4d080  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3836    1104    svchost.exe     0xe30b7de51080  6       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
3908    2120    dbInstaller.ex  0xe30b7df22080  0       -       0       False   2024-10-21 13:42:50.000000      2024-10-21 13:42:50.000000      Disabled
4012    1104    spoolsv.exe     0xe30b7df570c0  9       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4128    1104    svchost.exe     0xe30b7f063080  6       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4244    1104    svchost.exe     0xe30b7f0b5080  11      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4252    1104    svchost.exe     0xe30b7f0b70c0  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4268    1104    svchost.exe     0xe30b7f0bc080  17      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4276    1104    svchost.exe     0xe30b7f0bd080  18      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4284    1104    svchost.exe     0xe30b7f0c0080  23      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4292    1104    svchost.exe     0xe30b7f0ba080  6       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4300    1104    svchost.exe     0xe30b7f0c3080  6       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4340    1104    IntelCpHDCPSvc  0xe30b7f0e90c0  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4368    1104    ControlServer.  0xe30b7f0f7080  10      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4384    1104    ACCSvc.exe      0xe30b7f10f080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4396    1104    mosquitto.exe   0xe30b7f114080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4428    1104    jhi_service.ex  0xe30b7f0f5080  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4508    1104    MpDefenderCore  0xe30b7f15d080  8       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4516    1104    NordUpdateServ  0xe30b7f166080  35      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4580    1104    nvcontainer.ex  0xe30b7f12d080  37      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4592    1104    OfficeClickToR  0xe30b7f130080  19      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4600    1104    CCDMonitorServ  0xe30b7f1a10c0  6       -       0       True    2024-10-21 13:42:50.000000      N/A     Disabled
4624    1104    LMS.exe 0xe30b7f1a5080  4       -       0       True    2024-10-21 13:42:50.000000      N/A     Disabled
4636    1104    svchost.exe     0xe30b7f15b080  5       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4676    1104    RtkAudUService  0xe30b7f1b5080  10      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4684    1104    RstMwService.e  0xe30b7f1b6080  8       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4696    1104    sshd.exe        0xe30b7f1b7080  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4716    1104    ssh-agent.exe   0xe30b7f1ba080  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4760    1104    svchost.exe     0xe30b7f1cd080  4       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4780    1104    svchost.exe     0xe30b7f1ce080  17      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4792    1104    vmnetdhcp.exe   0xe30b7f1d0080  3       -       0       True    2024-10-21 13:42:50.000000      N/A     Disabled
4800    1104    WavesSysSvc64.  0xe30b7f1d40c0  3       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4828    1104    vmnat.exe       0xe30b7f1e50c0  5       -       0       True    2024-10-21 13:42:50.000000      N/A     Disabled
4848    1104    svchost.exe     0xe30b7f1e3080  8       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4916    1104    svchost.exe     0xe30b7f229080  2       -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
4940    1104    MsMpEng.exe     0xe30b7f228080  64      -       0       False   2024-10-21 13:42:50.000000      N/A     Disabled
5172    1104    wslservice.exe  0xe30b7f2e60c0  12      -       0       False   2024-10-21 13:42:51.000000      N/A     Disabled
5188    1104    KillerNetworkS  0xe30b7f4aa080  13      -       0       False   2024-10-21 13:42:51.000000      N/A     Disabled
5208    1104    IntelCpHeciSvc  0xe30b7f4a8080  4       -       0       False   2024-10-21 13:42:51.000000      N/A     Disabled
5320    1104    vmware-authd.e  0xe30b7f3ad080  6       -       0       True    2024-10-21 13:42:51.000000      N/A     Disabled
5360    1104    vmware-usbarbi  0xe30b7f3b0080  5       -       0       False   2024-10-21 13:42:51.000000      N/A     Disabled
5536    1104    svchost.exe     0xe30b7f63a080  6       -       0       False   2024-10-21 13:42:51.000000      N/A     Disabled
5548    4252    dasHost.exe     0xe30b7f64b080  3       -       0       False   2024-10-21 13:42:51.000000      N/A     Disabled
5716    1104    xTendUtilitySe  0xe30b7f7020c0  7       -       0       False   2024-10-21 13:42:51.000000      N/A     Disabled
6404    1104    svchost.exe     0xe30b7f944080  8       -       0       False   2024-10-21 13:42:51.000000      N/A     Disabled
6788    4600    ccd.exe 0xe30b7fa81080  0       -       0       True    2024-10-21 13:42:51.000000      2024-10-21 13:42:53.000000      Disabled
6764    5716    xTendUtility.e  0xe30b7fc430c0  3       -       0       False   2024-10-21 13:42:52.000000      N/A     Disabled
4704    6764    conhost.exe     0xe30b7fc55080  4       -       0       False   2024-10-21 13:42:52.000000      N/A     Disabled
7348    4580    rundll32.exe    0xe30b7fe97080  0       -       1       False   2024-10-21 13:42:52.000000      2024-10-21 16:54:38.000000      Disabled
8080    1104    svchost.exe     0xe30b7fe83080  5       -       0       False   2024-10-21 13:42:54.000000      N/A     Disabled
7388    4276    AggregatorHost  0xe30b800b4080  4       -       0       False   2024-10-21 13:42:54.000000      N/A     Disabled
6892    1336    WmiPrvSE.exe    0xe30b80162080  6       -       0       False   2024-10-21 13:42:54.000000      N/A     Disabled
7364    1336    WmiPrvSE.exe    0xe30b801e90c0  10      -       0       False   2024-10-21 13:42:54.000000      N/A     Disabled
3108    1104    PresentationFo  0xe30b7d3a7080  7       -       0       False   2024-10-21 13:42:54.000000      N/A     Disabled
4504    1104    svchost.exe     0xe30b801db080  3       -       0       False   2024-10-21 13:42:54.000000      N/A     Disabled
2032    1104    svchost.exe     0xe30b80331080  7       -       0       False   2024-10-21 13:42:55.000000      N/A     Disabled
8652    1104    svchost.exe     0xe30b804f8080  10      -       0       False   2024-10-21 13:42:55.000000      N/A     Disabled
9192    1104    svchost.exe     0xe30b80605080  7       -       0       False   2024-10-21 13:42:56.000000      N/A     Disabled
9152    1104    svchost.exe     0xe30b8074e080  4       -       0       False   2024-10-21 13:42:56.000000      N/A     Disabled
9284    1104    svchost.exe     0xe30b807f7080  3       -       0       False   2024-10-21 13:42:56.000000      N/A     Disabled
9548    1104    PSSvc.exe       0xe30b593c5080  6       -       0       False   2024-10-21 13:42:58.000000      N/A     Disabled
10384   4580    nvcontainer.ex  0xe30b80cd0140  0       -       1       False   2024-10-21 13:43:00.000000      2024-10-21 16:54:38.000000      Disabled
12148   1104    svchost.exe     0xe30b81ad1080  13      -       0       False   2024-10-21 13:43:01.000000      N/A     Disabled
11760   1104    SearchIndexer.  0xe30b81ca3080  12      -       0       False   2024-10-21 13:43:02.000000      N/A     Disabled
11896   1104    svchost.exe     0xe30b81ccb0c0  16      -       0       False   2024-10-21 13:43:02.000000      N/A     Disabled
12764   9548    PSAdminAgent.e  0xe30b80905080  0       -       1       False   2024-10-21 13:43:03.000000      2024-10-21 16:54:38.000000      Disabled
13164   1104    NisSrv.exe      0xe30b8218a080  10      -       0       False   2024-10-21 13:43:06.000000      N/A     Disabled
12344   4580    rundll32.exe    0xe30b7f64e0c0  0       -       1       False   2024-10-21 13:43:08.000000      2024-10-21 13:43:12.000000      Disabled
13408   4580    rundll32.exe    0xe30b700840c0  0       -       1       False   2024-10-21 13:43:11.000000      2024-10-21 13:43:11.000000      Disabled
13952   1104    svchost.exe     0xe30b826c50c0  4       -       0       False   2024-10-21 13:43:13.000000      N/A     Disabled
14632   1104    SecurityHealth  0xe30b8290e080  10      -       0       False   2024-10-21 13:43:17.000000      N/A     Disabled
15220   8696    RtkAudUService  0xe30b827a9080  0       -       1       False   2024-10-21 13:43:20.000000      2024-10-21 16:54:44.000000      Disabled
14344   8696    WavesSvc64.exe  0xe30b82d5a0c0  0       -       1       False   2024-10-21 13:43:20.000000      2024-10-21 16:54:38.000000      Disabled
5712    1104    QASvc.exe       0xe30b80ec6080  3       -       0       False   2024-10-21 13:43:25.000000      N/A     Disabled
7008    5712    QAAgent.exe     0xe30b829d60c0  0       -       1       False   2024-10-21 13:43:26.000000      2024-10-21 16:54:38.000000      Disabled
6732    5712    QAAdminAgent.e  0xe30b82ed80c0  0       -       1       False   2024-10-21 13:43:27.000000      2024-10-21 16:54:38.000000      Disabled
2972    5712    QAAdminAgent.e  0xe30b82ef0080  0       -       1       False   2024-10-21 13:43:28.000000      2024-10-21 13:43:28.000000      Disabled
3660    9548    UpgradeTool.ex  0xe30b82fd4080  0       -       1       False   2024-10-21 13:43:28.000000      2024-10-21 13:43:34.000000      Disabled
15456   5712    QAAdminAgent.e  0xe30b831ac080  0       -       1       False   2024-10-21 13:43:29.000000      2024-10-21 13:43:29.000000      Disabled
16016   5712    QAAdminAgent.e  0xe30b832020c0  0       -       1       False   2024-10-21 13:43:30.000000      2024-10-21 13:43:30.000000      Disabled
16220   5712    QAAdminAgent.e  0xe30b833df0c0  0       -       1       False   2024-10-21 13:43:31.000000      2024-10-21 13:43:31.000000      Disabled
17140   4600    ccd.exe 0xe30b83e78080  14      -       0       True    2024-10-21 13:43:37.000000      N/A     Disabled
17152   17140   conhost.exe     0xe30b83c61080  4       -       0       False   2024-10-21 13:43:37.000000      N/A     Disabled
6108    17728   msedgewebview2  0xe30b7a6720c0  0       -       1       False   2024-10-21 13:43:49.000000      2024-10-21 16:54:38.000000      Disabled
7148    17728   msedgewebview2  0xe30b847a30c0  0       -       1       False   2024-10-21 13:43:49.000000      2024-10-21 16:54:38.000000      Disabled
7188    17728   msedgewebview2  0xe30b846530c0  0       -       1       False   2024-10-21 13:43:50.000000      2024-10-21 16:54:38.000000      Disabled
1656    17728   msedgewebview2  0xe30b84b41180  0       -       1       False   2024-10-21 13:43:50.000000      2024-10-21 16:54:38.000000      Disabled
18808   5712    UpgradeTool.ex  0xe30b848b80c0  0       -       1       False   2024-10-21 13:43:55.000000      2024-10-21 13:43:56.000000      Disabled
14468   4992    opera.exe       0xe30b84658080  0       -       1       False   2024-10-21 13:44:07.000000      2024-10-21 16:51:00.000000      Disabled
17976   1104    IAStorDataMgrS  0xe30b854e30c0  10      -       0       False   2024-10-21 13:44:54.000000      N/A     Disabled
11648   1104    svchost.exe     0xe30b846e90c0  5       -       0       False   2024-10-21 13:44:55.000000      N/A     Disabled
17876   1104    svchost.exe     0xe30b84e660c0  13      -       0       False   2024-10-21 13:44:55.000000      N/A     Disabled
20244   17876   MoUsoCoreWorke  0xe30b84ce60c0  7       -       0       False   2024-10-21 13:44:55.000000      N/A     Disabled
20240   1104    svchost.exe     0xe30b840630c0  4       -       0       False   2024-10-21 13:44:55.000000      N/A     Disabled
16956   1104    svchost.exe     0xe30b814cd080  7       -       0       False   2024-10-21 13:44:56.000000      N/A     Disabled
1736    20244   MoNotification  0xe30b79dda080  0       -       1       False   2024-10-21 13:44:56.000000      2024-10-21 13:44:57.000000      Disabled
17624   4384    ACCFixpackFold  0xe30b84bf0100  0       -       1       False   2024-10-21 13:45:56.000000      2024-10-21 13:45:56.000000      Disabled
11668   1104    svchost.exe     0xe30b8617c0c0  1       -       0       False   2024-10-21 13:47:11.000000      N/A     Disabled
2892    1104    svchost.exe     0xe30b8629f080  4       -       0       False   2024-10-21 13:47:11.000000      N/A     Disabled
19656   1104    svchost.exe     0xe30b5b0b2080  14      -       0       False   2024-10-21 13:47:12.000000      N/A     Disabled
10920   2084    taskhostw.exe   0xe30b8628f080  0       -       0       False   2024-10-21 13:48:25.000000      2024-10-21 13:50:14.000000      Disabled
19172   1104    svchost.exe     0xe30b864ed080  6       -       0       False   2024-10-21 13:48:25.000000      N/A     Disabled
3848    1104    svchost.exe     0xe30b8944c080  5       -       0       False   2024-10-21 13:48:26.000000      N/A     Disabled
6900    1104    svchost.exe     0xe30b85eb1080  4       -       0       False   2024-10-21 14:10:15.000000      N/A     Disabled
11176   22396   com.docker.bac  0xe30b862d9080  0       -       1       False   2024-10-21 14:18:09.000000      2024-10-21 16:54:43.000000      Disabled
22336   1104    vmcompute.exe   0xe30b85ef3080  3       -       0       False   2024-10-21 14:18:12.000000      N/A     Disabled
19676   22336   vmwp.exe        0xe30b842df080  0       -       0       False   2024-10-21 14:18:12.000000      2024-10-21 16:54:52.000000      Disabled
20084   12080   wsl.exe 0xe30b7f625080  0       -       1       False   2024-10-21 14:18:22.000000      2024-10-21 16:54:43.000000      Disabled
14380   14416   Code.exe        0xe30b8ba2d0c0  0       -       1       False   2024-10-21 14:21:43.000000      2024-10-21 16:54:18.000000      Disabled
16680   14416   python.exe      0xe30b8c3aa0c0  0       -       1       False   2024-10-21 14:21:48.000000      2024-10-21 16:54:18.000000      Disabled
2568    1104    svchost.exe     0xe30b87d870c0  13      -       0       False   2024-10-21 15:23:10.000000      N/A     Disabled
10040   1104    svchost.exe     0xe30b8c70a080  5       -       0       False   2024-10-21 15:24:38.000000      N/A     Disabled
4476    21632   Code.exe        0xe30b8efbd0c0  0       -       1       False   2024-10-21 16:54:18.000000      2024-10-21 16:54:18.000000      Disabled
23540   20244   MoNotification  0xe30b7a0630c0  0       -       2       False   2024-10-22 07:01:30.000000      2024-10-22 07:01:30.000000      Disabled
16748   4580    nvcontainer.ex  0xe30b8db350c0  0       -       2       False   2024-10-22 07:01:30.000000      2024-10-22 17:35:53.000000      Disabled
20860   9548    PSAdminAgent.e  0xe30b8dcdd0c0  0       -       2       False   2024-10-22 07:01:38.000000      2024-10-22 17:35:52.000000      Disabled
15332   15720   RtkAudUService  0xe30b80ec20c0  0       -       2       False   2024-10-22 07:01:46.000000      2024-10-22 17:35:54.000000      Disabled
9644    15720   WavesSvc64.exe  0xe30b808e00c0  0       -       2       False   2024-10-22 07:01:50.000000      2024-10-22 17:35:52.000000      Disabled
17480   4580    rundll32.exe    0xe30b85dc60c0  0       -       2       False   2024-10-22 07:01:52.000000      2024-10-22 07:01:52.000000      Disabled
3548    5712    QAAgent.exe     0xe30b8d8320c0  0       -       2       False   2024-10-22 07:02:01.000000      2024-10-22 17:35:53.000000      Disabled
5952    5712    QAAdminAgent.e  0xe30b851430c0  0       -       2       False   2024-10-22 07:02:02.000000      2024-10-22 17:35:52.000000      Disabled
19336   5712    QAAdminAgent.e  0xe30b7d3aa080  0       -       2       False   2024-10-22 07:02:03.000000      2024-10-22 07:02:03.000000      Disabled
19712   5712    QAAdminAgent.e  0xe30b82051080  0       -       2       False   2024-10-22 07:02:04.000000      2024-10-22 07:02:04.000000      Disabled
22992   5712    QAAdminAgent.e  0xe30b8bd0b080  0       -       2       False   2024-10-22 07:02:05.000000      2024-10-22 07:02:05.000000      Disabled
1840    5712    QAAdminAgent.e  0xe30b864f1080  0       -       2       False   2024-10-22 07:02:06.000000      2024-10-22 07:02:06.000000      Disabled
3880    5268    msedgewebview2  0xe30b8c5bd0c0  0       -       2       False   2024-10-22 07:02:21.000000      2024-10-22 17:35:53.000000      Disabled
5656    5268    msedgewebview2  0xe30b8339e080  0       -       2       False   2024-10-22 07:02:21.000000      2024-10-22 17:35:53.000000      Disabled
20704   1104    svchost.exe     0xe30b87d51080  6       -       0       False   2024-10-22 07:03:03.000000      N/A     Disabled
3808    4384    ACCFixpackFold  0xe30b81fea0c0  0       -       2       False   2024-10-22 07:04:33.000000      2024-10-22 07:04:33.000000      Disabled
16036   1576    wsl.exe 0xe30b86aba080  0       -       2       False   2024-10-22 07:04:39.000000      2024-10-22 17:35:53.000000      Disabled
17040   8316    wsl.exe 0xe30b8dbc0080  0       -       2       False   2024-10-22 07:04:44.000000      2024-10-22 17:35:53.000000      Disabled
7720    15108   wsl.exe 0xe30b7a0a8080  0       -       2       False   2024-10-22 07:04:46.000000      2024-10-22 17:35:53.000000      Disabled
23092   10208   Code.exe        0xe30b8ee65080  0       -       2       False   2024-10-22 07:06:18.000000      2024-10-22 15:10:38.000000      Disabled
16640   10208   python.exe      0xe30b842dd080  0       -       2       False   2024-10-22 07:06:23.000000      2024-10-22 15:10:38.000000      Disabled
20660   15720   opera.exe       0xe30b890db180  0       -       2       False   2024-10-22 07:29:12.000000      2024-10-22 17:35:46.000000      Disabled
23296   20660   opera.exe       0xe30b8dd300c0  0       -       2       False   2024-10-22 07:29:14.000000      2024-10-22 17:35:46.000000      Disabled
11292   3740    wlanext.exe     0xe30b7dd2e080  3       -       0       False   2024-10-22 08:22:20.000000      N/A     Disabled
21168   11292   conhost.exe     0xe30b8699c080  3       -       0       False   2024-10-22 08:22:20.000000      N/A     Disabled
4472    24836   Code.exe        0xe30b9a4c00c0  0       -       2       False   2024-10-22 14:56:10.000000      2024-10-22 14:56:49.000000      Disabled
10756   24836   Code.exe        0xe30b977700c0  0       -       2       False   2024-10-22 14:56:10.000000      2024-10-22 14:56:49.000000      Disabled
26412   27492   Code.exe        0xe30b6fe13080  0       -       2       False   2024-10-22 14:56:55.000000      2024-10-22 15:00:16.000000      Disabled
8540    27492   python.exe      0xe30b8f14a080  0       -       2       False   2024-10-22 14:56:57.000000      2024-10-22 15:00:16.000000      Disabled
23380   14892   Code.exe        0xe30b7df4f0c0  0       -       2       False   2024-10-22 15:00:24.000000      2024-10-22 15:05:07.000000      Disabled
9004    14892   python.exe      0xe30b84e980c0  0       -       2       False   2024-10-22 15:00:26.000000      2024-10-22 15:05:07.000000      Disabled
26144   1732    Code.exe        0xe30b8906b180  0       -       2       False   2024-10-22 15:10:44.000000      2024-10-22 15:32:18.000000      Disabled
9732    2364    Code.exe        0xe30b9559d080  0       -       2       False   2024-10-22 15:12:46.000000      2024-10-22 15:13:04.000000      Disabled
27244   2364    Code.exe        0xe30b8ea8f080  0       -       2       False   2024-10-22 15:12:46.000000      2024-10-22 15:13:04.000000      Disabled
15996   25464   Code.exe        0xe30b8d27f0c0  0       -       2       False   2024-10-22 15:13:07.000000      2024-10-22 15:32:04.000000      Disabled
25092   25464   Code.exe        0xe30b8e7710c0  0       -       2       False   2024-10-22 15:13:09.000000      2024-10-22 15:32:04.000000      Disabled
24684   25464   Code.exe        0xe30b87d7c080  0       -       2       False   2024-10-22 15:13:14.000000      2024-10-22 15:32:04.000000      Disabled
19672   1732    python.exe      0xe30b8d9a5080  0       -       2       False   2024-10-22 15:13:51.000000      2024-10-22 15:32:18.000000      Disabled
21304   21648   Code.exe        0xe30b98807080  0       -       2       False   2024-10-22 15:32:08.000000      2024-10-22 16:30:44.000000      Disabled
20248   21648   Code.exe        0xe30b98a160c0  0       -       2       False   2024-10-22 15:32:09.000000      2024-10-22 16:30:44.000000      Disabled
23920   26040   Code.exe        0xe30b981b91c0  0       -       2       False   2024-10-22 15:32:22.000000      2024-10-22 16:30:28.000000      Disabled
10980   26040   python.exe      0xe30b8bfd1080  0       -       2       False   2024-10-22 15:33:03.000000      2024-10-22 16:30:28.000000      Disabled
15452   20660   opera.exe       0xe30b8be5e0c0  0       -       2       False   2024-10-22 16:30:25.000000      2024-10-22 16:30:31.000000      Disabled
15140   20244   MoNotification  0xe30b8752e0c0  0       -       3       False   2024-10-23 07:07:15.000000      2024-10-23 07:07:16.000000      Disabled
9856    4580    nvcontainer.ex  0xe30b8eeac0c0  0       -       3       False   2024-10-23 07:07:16.000000      2024-10-23 16:36:08.000000      Disabled
23604   9548    PSAdminAgent.e  0xe30b9b9a30c0  0       -       3       False   2024-10-23 07:07:23.000000      2024-10-23 16:36:07.000000      Disabled
6596    24208   RtkAudUService  0xe30b98dec0c0  0       -       3       False   2024-10-23 07:07:33.000000      2024-10-23 16:36:11.000000      Disabled
16660   24208   WavesSvc64.exe  0xe30b860b60c0  0       -       3       False   2024-10-23 07:07:33.000000      2024-10-23 16:36:07.000000      Disabled
2800    4580    rundll32.exe    0xe30b98a5f0c0  0       -       3       False   2024-10-23 07:07:38.000000      2024-10-23 07:07:38.000000      Disabled
4868    5712    QAAgent.exe     0xe30b88f020c0  0       -       3       False   2024-10-23 07:07:47.000000      2024-10-23 16:36:07.000000      Disabled
8128    5712    QAAdminAgent.e  0xe30b81c430c0  0       -       3       False   2024-10-23 07:07:48.000000      2024-10-23 16:36:07.000000      Disabled
15932   5712    QAAdminAgent.e  0xe30b7a2420c0  0       -       3       False   2024-10-23 07:07:49.000000      2024-10-23 07:07:49.000000      Disabled
27620   5712    QAAdminAgent.e  0xe30b8e1870c0  0       -       3       False   2024-10-23 07:07:50.000000      2024-10-23 07:07:50.000000      Disabled
23308   5712    QAAdminAgent.e  0xe30b593c20c0  0       -       3       False   2024-10-23 07:07:51.000000      2024-10-23 07:07:51.000000      Disabled
16804   5712    QAAdminAgent.e  0xe30b8c4950c0  0       -       3       False   2024-10-23 07:07:52.000000      2024-10-23 07:07:52.000000      Disabled
15620   10464   msedgewebview2  0xe30b8287f080  0       -       3       False   2024-10-23 07:08:05.000000      2024-10-23 16:36:08.000000      Disabled
21112   4384    ACCFixpackFold  0xe30b891cb080  0       -       3       False   2024-10-23 07:10:18.000000      2024-10-23 07:10:18.000000      Disabled
14512   21664   Docker Desktop  0xe30b7fbd1080  0       -       3       False   2024-10-23 07:13:47.000000      2024-10-23 16:36:09.000000      Disabled
22520   19880   Code.exe        0xe30b8d84f080  0       -       3       False   2024-10-23 07:23:40.000000      2024-10-23 07:24:29.000000      Disabled
25756   19880   Code.exe        0xe30b809ec080  0       -       3       False   2024-10-23 07:23:41.000000      2024-10-23 07:24:29.000000      Disabled
12856   24468   Code.exe        0xe30b7d8b6080  0       -       3       False   2024-10-23 07:24:33.000000      2024-10-23 13:59:49.000000      Disabled
24984   24468   python.exe      0xe30b72bf5080  0       -       3       False   2024-10-23 07:24:42.000000      2024-10-23 13:59:49.000000      Disabled
13472   20244   MoNotification  0xe30b83c5e080  0       -       3       False   2024-10-23 07:37:49.000000      2024-10-23 07:37:50.000000      Disabled
20348   20244   MoNotification  0xe30b8900c080  0       -       3       False   2024-10-23 07:38:29.000000      2024-10-23 07:38:30.000000      Disabled
13712   20136   Code.exe        0xe30b79ac7080  0       -       3       False   2024-10-23 07:57:29.000000      2024-10-23 07:58:01.000000      Disabled
13200   20136   Code.exe        0xe30b8c641080  0       -       3       False   2024-10-23 07:57:29.000000      2024-10-23 07:58:01.000000      Disabled
13740   3056    Code.exe        0xe30b8926f0c0  0       -       3       False   2024-10-23 07:58:05.000000      2024-10-23 07:58:12.000000      Disabled
15820   3056    Code.exe        0xe30b8007e080  0       -       3       False   2024-10-23 07:58:05.000000      2024-10-23 07:58:12.000000      Disabled
21156   3056    Code.exe        0xe30b8322a080  0       -       3       False   2024-10-23 07:58:11.000000      2024-10-23 07:58:12.000000      Disabled
11108   8612    Code.exe        0xe30b8bfab080  0       -       3       False   2024-10-23 07:58:15.000000      2024-10-23 08:33:31.000000      Disabled
12664   8612    Code.exe        0xe30b765350c0  0       -       3       False   2024-10-23 07:58:16.000000      2024-10-23 08:33:31.000000      Disabled
21656   8612    Code.exe        0xe30b85159080  0       -       3       False   2024-10-23 07:58:23.000000      2024-10-23 08:33:31.000000      Disabled
20992   8612    Code.exe        0xe30b8ef93080  0       -       3       False   2024-10-23 07:58:23.000000      2024-10-23 08:33:31.000000      Disabled
3124    14044   Code.exe        0xe30b8de6a080  0       -       3       False   2024-10-23 08:33:32.000000      2024-10-23 12:58:32.000000      Disabled
4264    14044   python.exe      0xe30b599cb080  0       -       3       False   2024-10-23 08:34:32.000000      2024-10-23 12:58:32.000000      Disabled
20352   17376   Code.exe        0xe30b88f32180  0       -       3       False   2024-10-23 12:58:38.000000      2024-10-23 13:47:17.000000      Disabled
26824   17376   Code.exe        0xe30b984840c0  0       -       3       False   2024-10-23 12:58:40.000000      2024-10-23 13:47:17.000000      Disabled
27680   17376   Code.exe        0xe30b92bbd0c0  0       -       3       False   2024-10-23 12:58:40.000000      2024-10-23 13:47:17.000000      Disabled
20096   17376   Code.exe        0xe30b8da230c0  0       -       3       False   2024-10-23 12:58:47.000000      2024-10-23 13:47:17.000000      Disabled
16828   6780    Code.exe        0xe30b75eb30c0  0       -       3       False   2024-10-23 13:47:21.000000      2024-10-23 15:33:51.000000      Disabled
29308   6780    python.exe      0xe30b8b8f2080  0       -       3       False   2024-10-23 13:47:30.000000      2024-10-23 15:33:51.000000      Disabled
24952   19348   Code.exe        0xe30b8ef3e080  0       -       3       False   2024-10-23 13:59:55.000000      2024-10-23 14:07:08.000000      Disabled
18256   19348   python.exe      0xe30b8edaf080  0       -       3       False   2024-10-23 14:01:53.000000      2024-10-23 14:07:08.000000      Disabled
14172   8168    Code.exe        0xe30b84bea080  0       -       3       False   2024-10-23 14:07:13.000000      2024-10-23 14:20:03.000000      Disabled
23276   10836   Code.exe        0xe30b8cfdc0c0  0       -       3       False   2024-10-23 14:20:06.000000      2024-10-23 15:08:40.000000      Disabled
26552   10836   python.exe      0xe30b5b3c10c0  0       -       3       False   2024-10-23 14:20:22.000000      2024-10-23 15:08:40.000000      Disabled
9584    13304   opera.exe       0xe30b8c4640c0  0       -       3       False   2024-10-23 15:28:53.000000      2024-10-23 16:33:31.000000      Disabled
28800   20276   Code.exe        0xe30b985180c0  0       -       3       False   2024-10-23 15:33:53.000000      2024-10-23 16:04:45.000000      Disabled
14976   20276   python.exe      0xe30b5a2c20c0  0       -       3       False   2024-10-23 15:35:59.000000      2024-10-23 16:04:45.000000      Disabled
13328   20276   docker.exe      0xe30b804ea080  0       -       3       False   2024-10-23 16:01:57.000000      2024-10-23 16:04:45.000000      Disabled
29612   20276   docker.exe      0xe30b92ae70c0  0       -       3       False   2024-10-23 16:03:04.000000      2024-10-23 16:04:45.000000      Disabled
26052   20276   docker.exe      0xe30b810c20c0  0       -       3       False   2024-10-23 16:03:04.000000      2024-10-23 16:04:45.000000      Disabled
1892    20276   cmd.exe 0xe30b9a5c50c0  0       -       3       False   2024-10-23 16:04:45.000000      2024-10-23 16:04:45.000000      Disabled
16824   17728   Code.exe        0xe30b9bb0f0c0  0       -       3       False   2024-10-23 16:04:48.000000      2024-10-23 16:05:13.000000      Disabled
14368   17728   Code.exe        0xe30b853c50c0  0       -       3       False   2024-10-23 16:04:48.000000      2024-10-23 16:05:13.000000      Disabled
7976    17728   Code.exe        0xe30b9b0d80c0  0       -       3       False   2024-10-23 16:04:53.000000      2024-10-23 16:05:13.000000      Disabled
27204   17728   Code.exe        0xe30b700950c0  0       -       3       False   2024-10-23 16:04:56.000000      2024-10-23 16:05:13.000000      Disabled
7772    14244   Code.exe        0xe30b821cb080  0       -       3       False   2024-10-23 16:05:16.000000      2024-10-23 16:05:51.000000      Disabled
17900   14244   Code.exe        0xe30b97a270c0  0       -       3       False   2024-10-23 16:05:16.000000      2024-10-23 16:05:51.000000      Disabled
14544   14244   Code.exe        0xe30b9bb020c0  0       -       3       False   2024-10-23 16:05:24.000000      2024-10-23 16:05:51.000000      Disabled
21416   14244   Code.exe        0xe30b926340c0  0       -       3       False   2024-10-23 16:05:40.000000      2024-10-23 16:05:51.000000      Disabled
9052    15476   Code.exe        0xe30b8d83f080  0       -       3       False   2024-10-23 16:05:54.000000      2024-10-23 16:33:32.000000      Disabled
29252   15476   Code.exe        0xe30b97a2f080  0       -       3       False   2024-10-23 16:05:54.000000      2024-10-23 16:33:32.000000      Disabled
12380   15476   Code.exe        0xe30b7582b080  0       -       3       False   2024-10-23 16:05:58.000000      2024-10-23 16:33:32.000000      Disabled
24544   15476   Code.exe        0xe30b812d3080  0       -       3       False   2024-10-23 16:06:03.000000      2024-10-23 16:33:32.000000      Disabled
28072   20244   MoNotification  0xe30b8d2bc0c0  0       -       4       False   2024-10-24 07:00:48.000000      2024-10-24 07:00:49.000000      Disabled
21700   4580    nvcontainer.ex  0xe30b8ddb80c0  0       -       4       False   2024-10-24 07:00:49.000000      2024-10-24 15:50:54.000000      Disabled
9608    9548    PSAdminAgent.e  0xe30b989180c0  0       -       4       False   2024-10-24 07:00:54.000000      2024-10-24 15:50:54.000000      Disabled
17296   4580    rundll32.exe    0xe30b8d6e20c0  0       -       4       False   2024-10-24 07:01:15.000000      2024-10-24 07:01:15.000000      Disabled
2196    5712    QAAgent.exe     0xe30b891350c0  0       -       4       False   2024-10-24 07:01:20.000000      2024-10-24 15:50:54.000000      Disabled
4100    19784   RtkAudUService  0xe30b94ca70c0  0       -       4       False   2024-10-24 07:01:20.000000      2024-10-24 15:50:56.000000      Disabled
15384   5712    QAAdminAgent.e  0xe30b821430c0  0       -       4       False   2024-10-24 07:01:21.000000      2024-10-24 15:50:54.000000      Disabled
20256   19784   WavesSvc64.exe  0xe30b8c59b0c0  0       -       4       False   2024-10-24 07:01:22.000000      2024-10-24 15:50:54.000000      Disabled
14892   5712    QAAdminAgent.e  0xe30b8dda70c0  0       -       4       False   2024-10-24 07:01:22.000000      2024-10-24 07:01:22.000000      Disabled
8604    5712    QAAdminAgent.e  0xe30b82ce50c0  0       -       4       False   2024-10-24 07:01:23.000000      2024-10-24 07:01:23.000000      Disabled
8572    5712    QAAdminAgent.e  0xe30b832240c0  0       -       4       False   2024-10-24 07:01:24.000000      2024-10-24 07:01:24.000000      Disabled
20276   5712    QAAdminAgent.e  0xe30b7a2020c0  0       -       4       False   2024-10-24 07:01:25.000000      2024-10-24 07:01:25.000000      Disabled
27800   4384    ACCFixpackFold  0xe30b94d42080  0       -       4       False   2024-10-24 07:03:51.000000      2024-10-24 07:03:51.000000      Disabled
5964    14556   Code.exe        0xe30b7a409080  0       -       4       False   2024-10-24 07:14:48.000000      2024-10-24 07:18:40.000000      Disabled
22896   14556   Code.exe        0xe30b88b48080  0       -       4       False   2024-10-24 07:14:48.000000      2024-10-24 07:18:40.000000      Disabled
12640   18384   Docker Desktop  0xe30b8ebe5080  0       -       4       False   2024-10-24 07:14:52.000000      2024-10-24 15:50:55.000000      Disabled
11336   24620   wsl.exe 0xe30b81c73080  0       -       4       False   2024-10-24 07:14:55.000000      2024-10-24 15:50:55.000000      Disabled
28832   10452   wsl.exe 0xe30b8d34c080  0       -       4       False   2024-10-24 07:15:02.000000      2024-10-24 15:50:55.000000      Disabled
8856    14688   wsl.exe 0xe30b8dc5b080  0       -       4       False   2024-10-24 07:15:03.000000      2024-10-24 15:50:55.000000      Disabled
3164    9008    wsl.exe 0xe30b8dd1c080  0       -       4       False   2024-10-24 07:15:06.000000      2024-10-24 15:50:55.000000      Disabled
8104    1936    opera.exe       0xe30b8c4b70c0  0       -       4       False   2024-10-24 07:44:46.000000      2024-10-24 15:50:33.000000      Disabled
1428    9372    python.exe      0xe30b76150080  0       -       4       False   2024-10-24 08:02:54.000000      2024-10-24 14:29:12.000000      Disabled
30556   27484   Code.exe        0xe30b79c230c0  0       -       4       False   2024-10-24 14:27:32.000000      2024-10-24 14:28:10.000000      Disabled
28540   27484   Code.exe        0xe30b8dbef0c0  0       -       4       False   2024-10-24 14:27:33.000000      2024-10-24 14:28:10.000000      Disabled
24128   10108   Code.exe        0xe30b88b5e080  0       -       4       False   2024-10-24 14:29:42.000000      2024-10-24 14:49:29.000000      Disabled
24344   10108   Code.exe        0xe30b8865f140  0       -       4       False   2024-10-24 14:29:42.000000      2024-10-24 14:49:29.000000      Disabled
7644    10108   python.exe      0xe30b7a1620c0  0       -       4       False   2024-10-24 14:29:47.000000      2024-10-24 14:49:29.000000      Disabled
14456   16512   Code.exe        0xe30b74a220c0  0       -       4       False   2024-10-24 14:29:53.000000      2024-10-24 14:30:04.000000      Disabled
27280   16512   Code.exe        0xe30b86aa9080  0       -       4       False   2024-10-24 14:29:53.000000      2024-10-24 14:30:04.000000      Disabled
20164   16512   Code.exe        0xe30ba44a30c0  0       -       4       False   2024-10-24 14:30:03.000000      2024-10-24 14:30:04.000000      Disabled
15912   26256   Code.exe        0xe30b7a7c50c0  0       -       4       False   2024-10-24 14:30:08.000000      2024-10-24 14:40:03.000000      Disabled
9852    26256   python.exe      0xe30b74a1f0c0  0       -       4       False   2024-10-24 14:30:30.000000      2024-10-24 14:40:03.000000      Disabled
7768    22148   Code.exe        0xe30b9c3620c0  0       -       4       False   2024-10-24 14:40:05.000000      2024-10-24 14:40:14.000000      Disabled
26456   22148   Code.exe        0xe30b86a9a0c0  0       -       4       False   2024-10-24 14:40:05.000000      2024-10-24 14:40:14.000000      Disabled
15388   22148   Code.exe        0xe30b9baef0c0  0       -       4       False   2024-10-24 14:40:10.000000      2024-10-24 14:40:14.000000      Disabled
29272   23532   Code.exe        0xe30b8dedf0c0  0       -       4       False   2024-10-24 14:40:16.000000      2024-10-24 14:57:48.000000      Disabled
13552   23532   python.exe      0xe30b74a1a0c0  0       -       4       False   2024-10-24 14:40:45.000000      2024-10-24 14:57:48.000000      Disabled
22008   30396   Code.exe        0xe30b830e70c0  0       -       4       False   2024-10-24 14:49:31.000000      2024-10-24 14:49:42.000000      Disabled
5268    30396   Code.exe        0xe30ba4b560c0  0       -       4       False   2024-10-24 14:49:31.000000      2024-10-24 14:49:42.000000      Disabled
30360   30396   Code.exe        0xe30ba450b0c0  0       -       4       False   2024-10-24 14:49:36.000000      2024-10-24 14:49:42.000000      Disabled
25856   28472   Code.exe        0xe30b94d44140  0       -       4       False   2024-10-24 14:49:44.000000      2024-10-24 14:55:40.000000      Disabled
28480   28472   python.exe      0xe30b90e240c0  0       -       4       False   2024-10-24 14:50:12.000000      2024-10-24 14:55:40.000000      Disabled
24940   14868   Code.exe        0xe30b88e91100  0       -       4       False   2024-10-24 14:55:42.000000      2024-10-24 15:27:15.000000      Disabled
20296   22244   Code.exe        0xe30b99025080  0       -       4       False   2024-10-24 14:57:51.000000      2024-10-24 15:28:19.000000      Disabled
7860    22244   python.exe      0xe30b930960c0  0       -       4       False   2024-10-24 14:57:58.000000      2024-10-24 15:28:19.000000      Disabled
11876   14868   python.exe      0xe30b9d8350c0  0       -       4       False   2024-10-24 15:24:51.000000      2024-10-24 15:27:15.000000      Disabled
19960   26116   Code.exe        0xe30b91eca0c0  0       -       4       False   2024-10-24 15:27:17.000000      2024-10-24 15:33:02.000000      Disabled
27580   26116   python.exe      0xe30b80fea1c0  0       -       4       False   2024-10-24 15:27:40.000000      2024-10-24 15:33:02.000000      Disabled
10496   29400   Code.exe        0xe30b95278080  0       -       4       False   2024-10-24 15:28:23.000000      2024-10-24 15:28:39.000000      Disabled
16672   29400   python.exe      0xe30b8ef7d080  0       -       4       False   2024-10-24 15:28:24.000000      2024-10-24 15:28:39.000000      Disabled
18156   6804    python.exe      0xe30b869d20c0  0       -       4       False   2024-10-24 15:28:43.000000      2024-10-24 15:45:48.000000      Disabled
13608   6804    Code.exe        0xe30b88259080  0       -       4       False   2024-10-24 15:28:43.000000      2024-10-24 15:45:48.000000      Disabled
7676    14068   Code.exe        0xe30b8db38100  0       -       4       False   2024-10-24 15:33:04.000000      2024-10-24 15:50:45.000000      Disabled
22932   14068   python.exe      0xe30b826e1080  0       -       4       False   2024-10-24 15:33:19.000000      2024-10-24 15:50:45.000000      Disabled
11868   21192   csrss.exe       0xe30b88f3c180  18      -       5       False   2024-10-24 15:50:53.000000      N/A     Disabled
14896   21192   winlogon.exe    0xe30b94952140  6       -       5       False   2024-10-24 15:50:53.000000      N/A     Disabled
3472    14896   fontdrvhost.ex  0xe30b8c584180  7       -       5       False   2024-10-24 15:50:53.000000      N/A     Disabled
3552    14896   LogonUI.exe     0xe30b892840c0  0       -       5       False   2024-10-24 15:50:53.000000      2024-10-25 07:08:16.000000      Disabled
29928   14896   dwm.exe 0xe30b8219f0c0  35      -       5       False   2024-10-24 15:50:53.000000      N/A     Disabled
23972   2120    NVDisplay.Cont  0xe30b7df750c0  35      -       5       False   2024-10-24 15:50:59.000000      N/A     Disabled
25516   20244   MoNotification  0xe30b8c62c140  0       -       5       False   2024-10-25 07:08:00.000000      2024-10-25 07:08:01.000000      Disabled
2780    2304    sihost.exe      0xe30b86b340c0  14      -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
22764   4580    nvcontainer.ex  0xe30b8c0790c0  19      -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
11072   1104    svchost.exe     0xe30b56fb30c0  11      -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
8720    2876    igfxEM.exe      0xe30b806450c0  6       -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
27912   4580    nvcontainer.ex  0xe30b98bee0c0  34      -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
14856   1104    svchost.exe     0xe30b727690c0  2       -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
19628   1104    svchost.exe     0xe30b8eedf0c0  7       -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
24348   2084    taskhostw.exe   0xe30b840440c0  9       -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
20804   14896   userinit.exe    0xe30b8e1650c0  0       -       5       False   2024-10-25 07:08:01.000000      2024-10-25 07:08:24.000000      Disabled
12956   20804   explorer.exe    0xe30b828620c0  186     -       5       False   2024-10-25 07:08:01.000000      N/A     Disabled
10180   1104    svchost.exe     0xe30b987e90c0  1       -       0       False   2024-10-25 07:08:02.000000      N/A     Disabled
4956    1104    svchost.exe     0xe30b91c910c0  12      -       5       False   2024-10-25 07:08:02.000000      N/A     Disabled
1424    1336    Widgets.exe     0xe30b8ed360c0  12      -       5       False   2024-10-25 07:08:04.000000      N/A     Disabled
4544    1336    SearchHost.exe  0xe30b840020c0  51      -       5       False   2024-10-25 07:08:04.000000      N/A     Disabled
5512    1336    StartMenuExper  0xe30b8b8970c0  12      -       5       False   2024-10-25 07:08:04.000000      N/A     Disabled
29636   1336    RuntimeBroker.  0xe30b8daa50c0  5       -       5       False   2024-10-25 07:08:04.000000      N/A     Disabled
29844   1336    RuntimeBroker.  0xe30b81ac70c0  22      -       5       False   2024-10-25 07:08:04.000000      N/A     Disabled
12996   1104    svchost.exe     0xe30b88a6b0c0  3       -       5       False   2024-10-25 07:08:04.000000      N/A     Disabled
5664    1336    dllhost.exe     0xe30b8f0570c0  9       -       5       False   2024-10-25 07:08:06.000000      N/A     Disabled
23104   7252    PSAgent.exe     0xe30b849a70c0  5       -       5       False   2024-10-25 07:08:06.000000      N/A     Disabled
24008   21920   NVIDIA Web Hel  0xe30b80fd30c0  92      -       5       True    2024-10-25 07:08:07.000000      N/A     Disabled
12636   24008   conhost.exe     0xe30b8e7af0c0  3       -       5       False   2024-10-25 07:08:07.000000      N/A     Disabled
4404    3388    ctfmon.exe      0xe30b8c4240c0  15      -       5       False   2024-10-25 07:08:07.000000      N/A     Disabled
22252   1336    LockApp.exe     0xe30b833240c0  15      -       5       False   2024-10-25 07:08:07.000000      N/A     Disabled
19800   1336    RuntimeBroker.  0xe30b8edaa0c0  58      -       5       False   2024-10-25 07:08:08.000000      N/A     Disabled
18632   9548    PSAdminAgent.e  0xe30b825880c0  4       -       5       False   2024-10-25 07:08:08.000000      N/A     Disabled
15336   1336    unsecapp.exe    0xe30b91cb50c0  3       -       5       False   2024-10-25 07:08:09.000000      N/A     Disabled
3656    2084    LocationNotifi  0xe30b883020c0  4       -       5       False   2024-10-25 07:08:09.000000      N/A     Disabled
21372   1104    svchost.exe     0xe30b7b16b0c0  5       -       5       False   2024-10-25 07:08:09.000000      N/A     Disabled
27528   1336    TextInputHost.  0xe30b822900c0  26      -       5       False   2024-10-25 07:08:13.000000      N/A     Disabled
20356   12956   SecurityHealth  0xe30b892910c0  3       -       5       False   2024-10-25 07:08:20.000000      N/A     Disabled
9272    12956   TiltWheelMouse  0xe30b82d750c0  3       -       5       True    2024-10-25 07:08:20.000000      N/A     Disabled
23336   12956   RtkAudUService  0xe30b82c230c0  12      -       5       False   2024-10-25 07:08:22.000000      N/A     Disabled
13444   12956   WavesSvc64.exe  0xe30b8c3660c0  7       -       5       False   2024-10-25 07:08:24.000000      N/A     Disabled
11528   4580    rundll32.exe    0xe30b88f21180  0       -       5       False   2024-10-25 07:08:24.000000      2024-10-25 07:08:25.000000      Disabled
27040   4580    nvsphelper64.e  0xe30b79ce20c0  8       -       5       False   2024-10-25 07:08:25.000000      N/A     Disabled
21488   22764   NVIDIA Share.e  0xe30b7d3a30c0  37      -       5       False   2024-10-25 07:08:25.000000      N/A     Disabled
10464   21488   NVIDIA Share.e  0xe30b8059d0c0  11      -       5       False   2024-10-25 07:08:26.000000      N/A     Disabled
912     21488   NVIDIA Share.e  0xe30b8efdf0c0  19      -       5       False   2024-10-25 07:08:27.000000      N/A     Disabled
21272   12956   Focusrite Noti  0xe30b8c5ce0c0  6       -       5       False   2024-10-25 07:08:31.000000      N/A     Disabled
19600   5712    QAAgent.exe     0xe30b8e1540c0  5       -       5       False   2024-10-25 07:08:32.000000      N/A     Disabled
28228   5712    QAAdminAgent.e  0xe30b9ae020c0  3       -       5       False   2024-10-25 07:08:33.000000      N/A     Disabled
2764    1336    igfxext.exe     0xe30b98e510c0  5       -       5       False   2024-10-25 07:08:33.000000      N/A     Disabled
19080   5712    QAAdminAgent.e  0xe30b84de60c0  0       -       5       False   2024-10-25 07:08:34.000000      2024-10-25 07:08:34.000000      Disabled
25044   12956   GoogleDriveFS.  0xe30b98ee60c0  4       -       5       False   2024-10-25 07:08:35.000000      N/A     Disabled
25888   5712    QAAdminAgent.e  0xe30b893450c0  0       -       5       False   2024-10-25 07:08:35.000000      2024-10-25 07:08:35.000000      Disabled
15328   25044   crashpad_handl  0xe30b977260c0  8       -       5       False   2024-10-25 07:08:35.000000      N/A     Disabled
10604   25044   GoogleDriveFS.  0xe30b8ee570c0  200     -       5       False   2024-10-25 07:08:35.000000      N/A     Disabled
25996   5712    QAAdminAgent.e  0xe30b8eb990c0  0       -       5       False   2024-10-25 07:08:36.000000      2024-10-25 07:08:36.000000      Disabled
9472    10604   GoogleDriveFS.  0xe30b8d9e30c0  18      -       5       False   2024-10-25 07:08:36.000000      N/A     Disabled
15368   10604   conhost.exe     0xe30b761370c0  6       -       5       False   2024-10-25 07:08:36.000000      N/A     Disabled
6056    5712    QAAdminAgent.e  0xe30b85d330c0  0       -       5       False   2024-10-25 07:08:37.000000      2024-10-25 07:08:37.000000      Disabled
28104   10604   GoogleDriveFS.  0xe30b93cef0c0  10      -       5       False   2024-10-25 07:08:37.000000      N/A     Disabled
26720   10604   GoogleDriveFS.  0xe30b8f09b0c0  20      -       5       False   2024-10-25 07:08:37.000000      N/A     Disabled
21936   10604   GoogleDriveFS.  0xe30b8d6be0c0  13      -       5       False   2024-10-25 07:08:37.000000      N/A     Disabled
21516   10604   GoogleDriveFS.  0xe30b5a7c20c0  24      -       5       False   2024-10-25 07:08:37.000000      N/A     Disabled
22496   12956   browser_assist  0xe30b8fc250c0  10      -       5       True    2024-10-25 07:08:41.000000      N/A     Disabled
20220   2084    AcerDriveTray.  0xe30b843330c0  5       -       5       True    2024-10-25 07:08:41.000000      N/A     Disabled
16908   22496   browser_assist  0xe30b8df9b0c0  7       -       5       True    2024-10-25 07:08:42.000000      N/A     Disabled
26788   1336    unsecapp.exe    0xe30b82e020c0  3       -       5       False   2024-10-25 07:08:42.000000      N/A     Disabled
25136   20220   AcerDriveProxy  0xe30b973b40c0  5       -       5       True    2024-10-25 07:08:43.000000      N/A     Disabled
4928    20220   AcerDriveUI.ex  0xe30b8d1b40c0  10      -       5       False   2024-10-25 07:08:43.000000      N/A     Disabled
13436   12956   NordVPN.exe     0xe30b82b640c0  86      -       5       False   2024-10-25 07:08:47.000000      N/A     Disabled
9376    12956   CCXProcess.exe  0xe30b9bbdf0c0  3       -       5       True    2024-10-25 07:08:48.000000      N/A     Disabled
15652   9376    node.exe        0xe30b82b530c0  19      -       5       True    2024-10-25 07:08:48.000000      N/A     Disabled
352     15652   conhost.exe     0xe30b8bb760c0  4       -       5       False   2024-10-25 07:08:48.000000      N/A     Disabled
20880   15652   AdobeIPCBroker  0xe30b88f2b180  7       -       5       True    2024-10-25 07:08:50.000000      N/A     Disabled
8364    12956   msedge.exe      0xe30b851e40c0  0       -       5       False   2024-10-25 07:08:50.000000      2024-10-25 08:08:52.000000      Disabled
28836   2780    IGCCTray.exe    0xe30b831eb0c0  11      -       5       False   2024-10-25 07:08:56.000000      N/A     Disabled
26452   4232    OneDrive.exe    0xe30b82da80c0  32      -       5       False   2024-10-25 07:08:58.000000      N/A     Disabled
22828   1336    IGCC.exe        0xe30ba4a8a0c0  10      -       5       False   2024-10-25 07:09:00.000000      N/A     Disabled
23632   1336    RuntimeBroker.  0xe30b7f94b0c0  3       -       5       False   2024-10-25 07:09:01.000000      N/A     Disabled
26016   2780    msteams_autost  0xe30b860ed080  0       -       5       False   2024-10-25 07:09:03.000000      2024-10-25 07:09:04.000000      Disabled
14716   26016   ms-teams.exe    0xe30b7ffed080  46      -       5       False   2024-10-25 07:09:04.000000      N/A     Disabled
16280   1336    RuntimeBroker.  0xe30ba438a0c0  4       -       5       False   2024-10-25 07:09:05.000000      N/A     Disabled
29524   14716   msedgewebview2  0xe30b5b0840c0  52      -       5       False   2024-10-25 07:09:06.000000      N/A     Disabled
12892   29524   msedgewebview2  0xe30b8baac0c0  7       -       5       False   2024-10-25 07:09:06.000000      N/A     Disabled
28848   29524   msedgewebview2  0xe30b8bce1080  20      -       5       False   2024-10-25 07:09:06.000000      N/A     Disabled
18900   29524   msedgewebview2  0xe30b84167080  26      -       5       False   2024-10-25 07:09:06.000000      N/A     Disabled
24752   29524   msedgewebview2  0xe30b7dcc4080  11      -       5       False   2024-10-25 07:09:06.000000      N/A     Disabled
11344   29524   msedgewebview2  0xe30b8d456080  28      -       5       False   2024-10-25 07:09:07.000000      N/A     Disabled
18572   2780    CrossDeviceSer  0xe30b88f09180  16      -       5       False   2024-10-25 07:09:10.000000      N/A     Disabled
12272   12956   AbletonPushCpl  0xe30b8c4ea0c0  3       -       5       False   2024-10-25 07:09:12.000000      N/A     Disabled
18132   1336    RuntimeBroker.  0xe30b813e5080  1       -       5       False   2024-10-25 07:09:14.000000      N/A     Disabled
14584   14248   IAStorIcon.exe  0xe30b91f1d0c0  6       -       5       False   2024-10-25 07:09:26.000000      N/A     Disabled
24724   1104    nordvpn-servic  0xe30b9b0020c0  79      -       0       False   2024-10-25 07:09:29.000000      N/A     Disabled
11540   1104    svchost.exe     0xe30b8bf570c0  5       -       5       False   2024-10-25 07:10:01.000000      N/A     Disabled
24944   2084    BackgroundAgen  0xe30b8ec460c0  3       -       5       True    2024-10-25 07:10:01.000000      N/A     Disabled
24120   1104    nordsec-threat  0xe30b8dc790c0  185     -       0       False   2024-10-25 07:10:04.000000      N/A     Disabled
29836   24120   conhost.exe     0xe30b8d16c180  5       -       0       False   2024-10-25 07:10:15.000000      N/A     Disabled
26020   1336    SpotifyWidgetP  0xe30b849960c0  15      -       5       False   2024-10-25 07:10:23.000000      N/A     Disabled
24552   2084    ACCStd.exe      0xe30b812e30c0  26      -       5       False   2024-10-25 07:11:01.000000      N/A     Disabled
7324    2084    ePowerButton_N  0xe30b891eb080  6       -       5       False   2024-10-25 07:11:01.000000      N/A     Disabled
7272    4384    ACCFixpackFold  0xe30b8e47f080  0       -       5       False   2024-10-25 07:11:02.000000      2024-10-25 07:11:03.000000      Disabled
29400   12956   opera.exe       0xe30b8f40c080  48      -       5       False   2024-10-25 07:11:08.000000      N/A     Disabled
28128   29400   opera_crashrep  0xe30b88b33080  9       -       5       False   2024-10-25 07:11:08.000000      N/A     Disabled
30600   29400   opera.exe       0xe30b72715080  17      -       5       False   2024-10-25 07:11:08.000000      N/A     Disabled
29992   29400   opera.exe       0xe30b80887080  24      -       5       False   2024-10-25 07:11:08.000000      N/A     Disabled
860     29400   opera.exe       0xe30b8bba7080  11      -       5       False   2024-10-25 07:11:09.000000      N/A     Disabled
14412   29400   opera.exe       0xe30b82d84080  23      -       5       False   2024-10-25 07:11:10.000000      N/A     Disabled
16452   29400   opera.exe       0xe30b7ff71080  16      -       5       False   2024-10-25 07:11:11.000000      N/A     Disabled
26936   29400   opera.exe       0xe30b81af7080  10      -       5       False   2024-10-25 07:11:11.000000      N/A     Disabled
14248   29400   opera.exe       0xe30b79e5f080  24      -       5       False   2024-10-25 07:11:11.000000      N/A     Disabled
19404   29400   opera.exe       0xe30b84295080  25      -       5       False   2024-10-25 07:11:11.000000      N/A     Disabled
14768   29400   opera.exe       0xe30b8be9d080  15      -       5       False   2024-10-25 07:11:11.000000      N/A     Disabled
10636   29400   opera.exe       0xe30b7f28b080  23      -       5       False   2024-10-25 07:11:12.000000      N/A     Disabled
10668   29400   opera.exe       0xe30b8e572080  25      -       5       False   2024-10-25 07:11:12.000000      N/A     Disabled
9932    29400   opera.exe       0xe30b7a221080  27      -       5       False   2024-10-25 07:11:12.000000      N/A     Disabled
10936   29400   opera.exe       0xe30b81c93080  24      -       5       False   2024-10-25 07:11:14.000000      N/A     Disabled
6776    10632   com.docker.bac  0xe30b9b5a70c0  18      -       5       False   2024-10-25 07:12:23.000000      N/A     Disabled
11324   6776    conhost.exe     0xe30b8bec90c0  4       -       5       False   2024-10-25 07:12:23.000000      N/A     Disabled
13744   6776    com.docker.bac  0xe30ba43e2080  52      -       5       False   2024-10-25 07:12:24.000000      N/A     Disabled
26560   13744   com.docker.dev  0xe30ba43e3080  9       -       5       False   2024-10-25 07:12:24.000000      N/A     Disabled
8968    13744   com.docker.bui  0xe30b7a3e4080  22      -       5       False   2024-10-25 07:12:24.000000      N/A     Disabled
22348   13744   Docker Desktop  0xe30b7a3e3080  50      -       5       False   2024-10-25 07:12:26.000000      N/A     Disabled
14900   22336   vmwp.exe        0xe30b8f3f2080  76      -       0       False   2024-10-25 07:12:27.000000      N/A     Disabled
26684   14900   vmmemWSL        0xe30b8f3f1080  40      -       0       False   2024-10-25 07:12:27.000000      N/A     Disabled
20252   1336    dllhost.exe     0xe30b9a420080  5       -       5       False   2024-10-25 07:12:28.000000      N/A     Disabled
22772   22348   Docker Desktop  0xe30b8dd87080  18      -       5       False   2024-10-25 07:12:28.000000      N/A     Disabled
23344   22348   Docker Desktop  0xe30b9a421080  21      -       5       False   2024-10-25 07:12:28.000000      N/A     Disabled
22236   1336    dllhost.exe     0xe30b97a10080  20      -       5       False   2024-10-25 07:12:29.000000      N/A     Disabled
4188    5172    wslrelay.exe    0xe30b8c711080  9       -       5       False   2024-10-25 07:12:30.000000      N/A     Disabled
17532   22348   Docker Desktop  0xe30b89199080  23      -       5       False   2024-10-25 07:12:31.000000      N/A     Disabled
24500   5172    wslhost.exe     0xe30b9ad3b080  6       -       5       False   2024-10-25 07:12:32.000000      N/A     Disabled
17576   24500   conhost.exe     0xe30b8fc34080  6       -       5       False   2024-10-25 07:12:32.000000      N/A     Disabled
4752    5172    wslhost.exe     0xe30b89198080  3       -       5       False   2024-10-25 07:12:32.000000      N/A     Disabled
20844   4752    conhost.exe     0xe30b835f5080  6       -       5       False   2024-10-25 07:12:32.000000      N/A     Disabled
23464   13744   wsl.exe 0xe30ba43ee080  3       -       5       False   2024-10-25 07:12:32.000000      N/A     Disabled
23312   23464   wsl.exe 0xe30b9b942080  5       -       5       False   2024-10-25 07:12:32.000000      N/A     Disabled
15800   24500   msrdc.exe       0xe30b940cb080  16      -       5       False   2024-10-25 07:12:32.000000      N/A     Disabled
24872   5172    wslhost.exe     0xe30b8d052080  6       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
14332   24872   conhost.exe     0xe30b7a06c1c0  5       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
25908   5172    wslhost.exe     0xe30b81e1c1c0  2       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
18340   23312   wslhost.exe     0xe30b98ef5080  3       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
3700    25908   conhost.exe     0xe30b89166080  4       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
5380    13744   wsl.exe 0xe30b992c4080  3       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
30312   18340   conhost.exe     0xe30b814eb080  3       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
16476   24872   msrdc.exe       0xe30b81e07080  17      -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
4992    5380    wsl.exe 0xe30b7a315080  4       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
1916    4992    wslhost.exe     0xe30b8d996080  3       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
15688   1916    conhost.exe     0xe30b79e1c080  5       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
15768   13744   wsl.exe 0xe30b857cb080  2       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
14224   15768   wsl.exe 0xe30b842e0080  5       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
14124   14224   wslhost.exe     0xe30b89369080  3       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
5940    14124   conhost.exe     0xe30b9b005080  4       -       5       False   2024-10-25 07:12:37.000000      N/A     Disabled
16808   5172    wslhost.exe     0xe30b8698d080  5       -       5       False   2024-10-25 07:12:38.000000      N/A     Disabled
7540    16808   conhost.exe     0xe30b72b43080  3       -       5       False   2024-10-25 07:12:38.000000      N/A     Disabled
26996   16808   msrdc.exe       0xe30b86a91080  17      -       5       False   2024-10-25 07:12:38.000000      N/A     Disabled
21520   5172    wslhost.exe     0xe30b8c152080  2       -       5       False   2024-10-25 07:12:38.000000      N/A     Disabled
18760   21520   conhost.exe     0xe30b8bb95080  6       -       5       False   2024-10-25 07:12:38.000000      N/A     Disabled
15188   13744   wsl.exe 0xe30b8d3410c0  2       -       5       False   2024-10-25 07:12:39.000000      N/A     Disabled
29540   22256   wsl.exe 0xe30b8c4b40c0  0       -       5       False   2024-10-25 07:12:39.000000      2024-10-25 07:12:39.000000      Disabled
21540   15188   wsl.exe 0xe30b84f1f080  6       -       5       False   2024-10-25 07:12:39.000000      N/A     Disabled
28424   21540   wslhost.exe     0xe30b893f4080  3       -       5       False   2024-10-25 07:12:39.000000      N/A     Disabled
20960   28424   conhost.exe     0xe30b8779d080  4       -       5       False   2024-10-25 07:12:39.000000      N/A     Disabled
26076   13744   wsl.exe 0xe30b7a2bc0c0  2       -       5       False   2024-10-25 07:12:44.000000      N/A     Disabled
25900   26076   wsl.exe 0xe30b8ebf6080  4       -       5       False   2024-10-25 07:12:44.000000      N/A     Disabled
12656   25900   wslhost.exe     0xe30b8208a080  2       -       5       False   2024-10-25 07:12:44.000000      N/A     Disabled
18480   12656   conhost.exe     0xe30b853cc080  5       -       5       False   2024-10-25 07:12:44.000000      N/A     Disabled
12416   13744   wsl.exe 0xe30b7a306080  0       -       5       False   2024-10-25 07:12:44.000000      2024-10-25 07:12:50.000000      Disabled
30232   1336    ShellExperienc  0xe30b8de740c0  21      -       5       False   2024-10-25 07:13:06.000000      N/A     Disabled
23188   1336    RuntimeBroker.  0xe30b5b0880c0  5       -       5       False   2024-10-25 07:13:07.000000      N/A     Disabled
28680   12956   Code.exe        0xe30b8c46b0c0  61      -       5       False   2024-10-25 07:14:05.000000      N/A     Disabled
16252   28680   Code.exe        0xe30b91f21080  8       -       5       False   2024-10-25 07:14:06.000000      N/A     Disabled
10212   28680   Code.exe        0xe30b86c0e080  16      -       5       False   2024-10-25 07:14:06.000000      N/A     Disabled
5612    28680   Code.exe        0xe30b7a6ef080  20      -       5       False   2024-10-25 07:14:06.000000      N/A     Disabled
23376   28680   Code.exe        0xe30b8d40f080  26      -       5       False   2024-10-25 07:14:07.000000      N/A     Disabled
17752   28680   Code.exe        0xe30b9ae15080  20      -       5       False   2024-10-25 07:14:10.000000      N/A     Disabled
19248   25732   Code.exe        0xe30b87b6c0c0  0       -       5       False   2024-10-25 07:14:14.000000      2024-10-25 07:14:36.000000      Disabled
25184   28680   Code.exe        0xe30b80bd0080  24      -       5       False   2024-10-25 07:14:14.000000      N/A     Disabled
14932   25184   conhost.exe     0xe30b7a7ec080  0       -       5       False   2024-10-25 07:14:15.000000      2024-10-25 07:14:36.000000      Disabled
27928   25184   powershell.exe  0xe30b7a169080  0       -       5       False   2024-10-25 07:14:15.000000      2024-10-25 07:14:36.000000      Disabled
16584   25732   python.exe      0xe30b8ddb3080  0       -       5       False   2024-10-25 07:14:17.000000      2024-10-25 07:14:36.000000      Disabled
12800   28680   Code.exe        0xe30b7fbdf1c0  20      -       5       False   2024-10-25 07:14:36.000000      N/A     Disabled
14168   28680   Code.exe        0xe30b8e7151c0  19      -       5       False   2024-10-25 07:14:37.000000      N/A     Disabled
20824   14168   Code.exe        0xe30b988c0080  14      -       5       False   2024-10-25 07:14:39.000000      N/A     Disabled
24316   14168   Code.exe        0xe30b96dc6080  10      -       5       False   2024-10-25 07:14:39.000000      N/A     Disabled
9816    14168   Code.exe        0xe30b812cb080  10      -       5       False   2024-10-25 07:14:45.000000      N/A     Disabled
19472   12956   powershell.exe  0xe30b5a6c71c0  12      -       5       False   2024-10-25 07:14:52.000000      N/A     Disabled
11452   19472   conhost.exe     0xe30b81f630c0  3       -       5       False   2024-10-25 07:14:52.000000      N/A     Disabled
8816    1336    OpenConsole.ex  0xe30b853ce080  11      -       5       False   2024-10-25 07:14:52.000000      N/A     Disabled
16060   1336    WindowsTermina  0xe30b59aca080  40      -       5       False   2024-10-25 07:14:52.000000      N/A     Disabled
3488    1336    RuntimeBroker.  0xe30b942ac080  2       -       5       False   2024-10-25 07:14:53.000000      N/A     Disabled
21368   1336    ApplicationFra  0xe30b91f25080  7       -       5       False   2024-10-25 07:15:13.000000      N/A     Disabled
7360    1336    SystemSettings  0xe30b8429a080  48      -       5       False   2024-10-25 07:15:13.000000      N/A     Disabled
1660    1104    svchost.exe     0xe30b8b8a5080  3       -       5       False   2024-10-25 07:15:16.000000      N/A     Disabled
4936    1336    UserOOBEBroker  0xe30b7ffe6080  2       -       5       False   2024-10-25 07:15:16.000000      N/A     Disabled
1768    16060   OpenConsole.ex  0xe30b82405080  6       -       5       False   2024-10-25 07:15:21.000000      N/A     Disabled
21592   16060   powershell.exe  0xe30b594c4080  12      -       5       False   2024-10-25 07:15:21.000000      N/A     Disabled
22172   16060   OpenConsole.ex  0xe30b804de0c0  5       -       5       False   2024-10-25 07:15:33.000000      N/A     Disabled
15136   16060   powershell.exe  0xe30b88309080  9       -       5       False   2024-10-25 07:15:33.000000      N/A     Disabled
1264    16060   OpenConsole.ex  0xe30b82eac080  7       -       5       False   2024-10-25 07:15:46.000000      N/A     Disabled
3024    16060   powershell.exe  0xe30b8bf64080  12      -       5       False   2024-10-25 07:15:46.000000      N/A     Disabled
30100   16060   OpenConsole.ex  0xe30b88eb4080  6       -       5       False   2024-10-25 07:15:56.000000      N/A     Disabled
18220   16060   powershell.exe  0xe30b84fdf080  11      -       5       False   2024-10-25 07:15:56.000000      N/A     Disabled
15476   16060   OpenConsole.ex  0xe30b98e32080  6       -       5       False   2024-10-25 07:16:06.000000      N/A     Disabled
1592    16060   powershell.exe  0xe30b8209a080  11      -       5       False   2024-10-25 07:16:06.000000      N/A     Disabled
19168   16060   OpenConsole.ex  0xe30b7fe96080  6       -       5       False   2024-10-25 07:16:19.000000      N/A     Disabled
14764   16060   powershell.exe  0xe30b8072b080  11      -       5       False   2024-10-25 07:16:19.000000      N/A     Disabled
23868   14168   Code.exe        0xe30b79bb20c0  10      -       5       False   2024-10-25 07:16:59.000000      N/A     Disabled
7996    14168   Code.exe        0xe30b891790c0  10      -       5       False   2024-10-25 07:16:59.000000      N/A     Disabled
10004   14168   pet.exe 0xe30b91581100  3       -       5       False   2024-10-25 07:17:19.000000      N/A     Disabled
14188   10004   conhost.exe     0xe30b890ca180  3       -       5       False   2024-10-25 07:17:19.000000      N/A     Disabled
7940    25184   conhost.exe     0xe30b9ae93080  6       -       5       False   2024-10-25 07:17:19.000000      N/A     Disabled
25568   25184   powershell.exe  0xe30b8df9c080  10      -       5       False   2024-10-25 07:17:19.000000      N/A     Disabled
19388   14168   python.exe      0xe30b88868080  8       -       5       False   2024-10-25 07:17:20.000000      N/A     Disabled
18172   19388   conhost.exe     0xe30b860cd080  3       -       5       False   2024-10-25 07:17:20.000000      N/A     Disabled
24276   14168   Code.exe        0xe30b7a207080  17      -       5       False   2024-10-25 07:17:20.000000      N/A     Disabled
17492   16060   OpenConsole.ex  0xe30b833801c0  6       -       5       False   2024-10-25 07:19:29.000000      N/A     Disabled
16716   16060   powershell.exe  0xe30b75ec51c0  11      -       5       False   2024-10-25 07:19:29.000000      N/A     Disabled
8280    1336    DataExchangeHo  0xe30b806f31c0  2       -       5       False   2024-10-25 07:19:30.000000      N/A     Disabled
23656   16060   OpenConsole.ex  0xe30b8bd07080  7       -       5       False   2024-10-25 07:20:03.000000      N/A     Disabled
10548   16060   powershell.exe  0xe30b8d680080  9       -       5       False   2024-10-25 07:20:03.000000      N/A     Disabled
19548   2780    AcerRegistrati  0xe30b86195080  6       -       5       True    2024-10-25 07:23:46.000000      N/A     Disabled
11492   1336    backgroundTask  0xe30b849020c0  12      -       5       False   2024-10-25 07:26:40.000000      N/A     Disabled
13676   1336    PhoneExperienc  0xe30ba44be080  16      -       5       False   2024-10-25 07:26:41.000000      N/A     Disabled
28440   19472   docker-compose  0xe30b97b26080  46      -       5       False   2024-10-25 07:54:19.000000      N/A     Disabled
3052    15136   docker.exe      0xe30b88f1a180  5       -       5       False   2024-10-25 07:59:35.000000      N/A     Disabled
7432    3052    docker.exe      0xe30b88f75180  16      -       5       False   2024-10-25 07:59:35.000000      N/A     Disabled
29140   29400   opera.exe       0xe30b8d95b0c0  27      -       5       False   2024-10-25 08:00:18.000000      N/A     Disabled
28384   8364    msedge.exe      0xe30b8631f0c0  52      -       5       False   2024-10-25 08:08:52.000000      N/A     Disabled
25296   28384   msedge.exe      0xe30b8d5bc0c0  8       -       5       False   2024-10-25 08:08:52.000000      N/A     Disabled
9536    28384   msedge.exe      0xe30b81c540c0  14      -       5       False   2024-10-25 08:08:53.000000      N/A     Disabled
2676    28384   msedge.exe      0xe30b832130c0  24      -       5       False   2024-10-25 08:08:53.000000      N/A     Disabled
18176   28384   msedge.exe      0xe30b757520c0  11      -       5       False   2024-10-25 08:08:53.000000      N/A     Disabled
20112   1336    dllhost.exe     0xe30b8eaa1080  4       -       5       False   2024-10-25 08:10:21.000000      N/A     Disabled
10288   1336    SDXHelper.exe   0xe30b7aa0b080  14      -       5       False   2024-10-25 08:10:22.000000      N/A     Disabled
26408   1104    WUDFHost.exe    0xe30b9ae1d0c0  6       -       0       False   2024-10-25 08:31:29.000000      N/A     Disabled
21588   22348   docker.exe      0xe30b88b17100  0       -       5       False   2024-10-25 08:31:30.000000      2024-10-25 08:31:49.000000      Disabled
25772   21588   conhost.exe     0xe30b8c51b080  4       -       5       False   2024-10-25 08:31:30.000000      N/A     Disabled
4144    21588   docker-compose  0xe30b891f2080  18      -       5       False   2024-10-25 08:31:30.000000      N/A     Disabled
22560   22348   docker.exe      0xe30b88ed4080  0       -       5       False   2024-10-25 08:32:19.000000      2024-10-25 08:32:24.000000      Disabled
26636   22560   conhost.exe     0xe30b8c06b080  3       -       5       False   2024-10-25 08:32:19.000000      N/A     Disabled
15812   22560   docker-compose  0xe30b8d5590c0  18      -       5       False   2024-10-25 08:32:20.000000      N/A     Disabled
12676   22348   docker.exe      0xe30b7a5520c0  0       -       5       False   2024-10-25 08:33:18.000000      2024-10-25 08:33:20.000000      Disabled
18436   12676   conhost.exe     0xe30b89037080  4       -       5       False   2024-10-25 08:33:18.000000      N/A     Disabled
29668   12676   docker-compose  0xe30b9b949180  17      -       5       False   2024-10-25 08:33:18.000000      N/A     Disabled
25124   22348   docker.exe      0xe30b8db070c0  0       -       5       False   2024-10-25 08:33:49.000000      2024-10-25 08:33:52.000000      Disabled
24980   25124   conhost.exe     0xe30b8db410c0  4       -       5       False   2024-10-25 08:33:49.000000      N/A     Disabled
28388   25124   docker-compose  0xe30ba450f1c0  18      -       5       False   2024-10-25 08:33:49.000000      N/A     Disabled
11612   1336    Video.UI.exe    0xe30b986b00c0  13      -       5       False   2024-10-25 08:40:51.000000      N/A     Disabled
12808   1336    backgroundTask  0xe30b8beaa180  12      -       5       False   2024-10-25 08:40:51.000000      N/A     Disabled
11532   1336    RuntimeBroker.  0xe30b9044a0c0  4       -       5       False   2024-10-25 08:40:53.000000      N/A     Disabled
29148   1336    dllhost.exe     0xe30b6ff130c0  4       -       5       False   2024-10-25 08:44:48.000000      N/A     Disabled
25484   12956   autopsy64.exe   0xe30b9b4430c0  148     -       5       False   2024-10-25 08:44:59.000000      N/A     Disabled
16176   25484   cmd.exe 0xe30b882020c0  0       -       5       False   2024-10-25 08:45:06.000000      2024-10-25 08:45:15.000000      Disabled
11848   16176   conhost.exe     0xe30b9e0a10c0  4       -       5       False   2024-10-25 08:45:06.000000      N/A     Disabled
29632   16176   java.exe        0xe30b9c8d90c0  59      -       5       False   2024-10-25 08:45:07.000000      N/A     Disabled
21184   29400   opera.exe       0xe30ba4342100  21      -       5       False   2024-10-25 08:45:16.000000      N/A     Disabled
5020    28680   Code.exe        0xe30ba4185080  26      -       5       False   2024-10-25 08:46:43.000000      N/A     Disabled
28504   28256   Code.exe        0xe30b81993080  0       -       5       False   2024-10-25 08:46:46.000000      2024-10-25 08:47:24.000000      Disabled
6068    28256   Code.exe        0xe30b7a2e4080  0       -       5       False   2024-10-25 08:46:46.000000      2024-10-25 08:47:24.000000      Disabled
13932   17768   Code.exe        0xe30b8089a080  0       -       5       False   2024-10-25 08:47:27.000000      2024-10-25 08:47:35.000000      Disabled
5160    17768   Code.exe        0xe30b9cee6080  0       -       5       False   2024-10-25 08:47:27.000000      2024-10-25 08:47:35.000000      Disabled
24372   17768   Code.exe        0xe30b94cb0080  0       -       5       False   2024-10-25 08:47:32.000000      2024-10-25 08:47:35.000000      Disabled
6236    28680   Code.exe        0xe30b5a2c4080  21      -       5       False   2024-10-25 08:47:35.000000      N/A     Disabled
23076   28680   Code.exe        0xe30b8de1f080  21      -       5       False   2024-10-25 08:47:35.000000      N/A     Disabled
28784   6236    Code.exe        0xe30b86a96080  13      -       5       False   2024-10-25 08:47:38.000000      N/A     Disabled
24844   6236    Code.exe        0xe30b83e40080  9       -       5       False   2024-10-25 08:47:39.000000      N/A     Disabled
27780   6236    Code.exe        0xe30b8dca5080  9       -       5       False   2024-10-25 08:47:41.000000      N/A     Disabled
17412   6236    Code.exe        0xe30b82d4d080  9       -       5       False   2024-10-25 08:47:41.000000      N/A     Disabled
25116   6236    Code.exe        0xe30b89443080  11      -       5       False   2024-10-25 08:47:43.000000      N/A     Disabled
23232   6236    pet.exe 0xe30b9bc2a0c0  3       -       5       False   2024-10-25 08:50:39.000000      N/A     Disabled
7732    23232   conhost.exe     0xe30b981320c0  4       -       5       False   2024-10-25 08:50:39.000000      N/A     Disabled
28676   25184   conhost.exe     0xe30b79c630c0  7       -       5       False   2024-10-25 08:50:40.000000      N/A     Disabled
6844    25184   powershell.exe  0xe30b935840c0  11      -       5       False   2024-10-25 08:50:40.000000      N/A     Disabled
17828   6236    python.exe      0xe30b7a2840c0  8       -       5       False   2024-10-25 08:50:41.000000      N/A     Disabled
30340   17828   conhost.exe     0xe30b72bec080  2       -       5       False   2024-10-25 08:50:41.000000      N/A     Disabled
6828    6236    Code.exe        0xe30b8c46d080  15      -       5       False   2024-10-25 08:50:41.000000      N/A     Disabled
17504   29400   opera.exe       0xe30b9accc0c0  25      -       5       False   2024-10-25 08:57:54.000000      N/A     Disabled
12740   29400   opera.exe       0xe30b9d3051c0  26      -       5       False   2024-10-25 09:04:46.000000      N/A     Disabled
7900    1104    svchost.exe     0xe30b9e8120c0  4       -       0       False   2024-10-25 09:06:40.000000      N/A     Disabled
27760   29400   opera.exe       0xe30b9f8570c0  15      -       5       False   2024-10-25 09:08:05.000000      N/A     Disabled
15600   1336    FileCoAuth.exe  0xe30ba00ce0c0  5       -       5       False   2024-10-25 09:08:06.000000      N/A     Disabled
29504   1336    backgroundTask  0xe30b9f89b0c0  9       -       5       False   2024-10-25 09:08:41.000000      N/A     Disabled
32616   16060   OpenConsole.ex  0xe30b9e89f0c0  6       -       5       False   2024-10-25 09:08:42.000000      N/A     Disabled
32624   16060   powershell.exe  0xe30b8e0460c0  13      -       5       False   2024-10-25 09:08:42.000000      N/A     Disabled
33132   1104    svchost.exe     0xe30b791db0c0  12      -       0       False   2024-10-25 09:08:53.000000      N/A     Disabled
33404   1104    svchost.exe     0xe30b898350c0  5       -       0       False   2024-10-25 09:08:54.000000      N/A     Disabled
33736   1336    smartscreen.ex  0xe30b897240c0  11      -       5       False   2024-10-25 09:09:03.000000      N/A     Disabled
32640   3352    audiodg.exe     0xe30b9ea130c0  8       -       0       False   2024-10-25 09:09:04.000000      N/A     Disabled
24824   32624   DumpIt.exe      0xe30b89c350c0  8       -       5       False   2024-10-25 09:09:06.000000      N/A     Disabled
32920   24824   conhost.exe     0xe30b89c790c0  5       -       5       False   2024-10-25 09:09:06.000000      N/A     Disabled
33772   29400   opera.exe       0xe30b9d9510c0  21      -       5       False   2024-10-25 09:09:20.000000      N/A     Disabled
3244    1104    svchost.exe     0xe30b9ff350c0  11      -       0       False   2024-10-25 09:10:12.000000      N/A     Disabled
15076   1336    RuntimeBroker.  0xe30b968570c0  8       -       5       False   2024-10-25 09:10:12.000000      N/A     Disabled
0       0               0xe30b8e3581c0  0       -       N/A     False   N/A     N/A     Disabled
```

```sh
```

```sh
```

```sh
```

```sh
```
