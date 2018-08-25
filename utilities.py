import os

def onConfigNameChanged(parent):
	print(parent)
	if parent.nameLE.text():
		configNameUnderscored = parent.nameLE.text().replace(' ','_')
		configPath = os.path.expanduser('~/linuxcnc/configs') + '/' + configNameUnderscored
		parent.configPathLB.setText(configPath)
	else:
		parent.configPathLB.setText('')

