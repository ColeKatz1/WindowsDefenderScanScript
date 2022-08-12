import os

def runScan(scanType):
    os.system('cmd /c ""%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType "' + scanType )


runScan("1") #this runs a quick scan
#runScan("2") #this runs a full scan
