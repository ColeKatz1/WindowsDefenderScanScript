import os

def runWDScan(scanType):
    os.system('cmd /c ""%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType "' + scanType )


runWDScan("1") #this runs a quick scan
#runWDScan("2") #this runs a full scan
