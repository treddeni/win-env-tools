import winreg
import sys

if len(sys.argv) == 2:
	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", 0, winreg.KEY_ALL_ACCESS)
	
	path = winreg.QueryValueEx(key, "Path")[0];
	
	path += ";" + sys.argv[1]
	
	winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, path)
else:
	print('Usage: python append-path.py [path to append]')
	print('Use "" around [path to append] if it contains whitespace')