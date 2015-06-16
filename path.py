import winreg

PARENT_KEY = "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment"

def getPath():
	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, PARENT_KEY)
	return winreg.QueryValueEx(key, "Path")[0];
	
def setPath(newPath):
	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, PARENT_KEY, 0, winreg.KEY_ALL_ACCESS)
	winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, newPath)
	
def appendToPath(appendPath):
	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, PARENT_KEY, 0, winreg.KEY_ALL_ACCESS)	
	path = winreg.QueryValueEx(key, "Path")[0];
	if path[len(path)-1] != ';':
		path += ';'
	path += appendPath
	winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, path)			