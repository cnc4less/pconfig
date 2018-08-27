import os

def build_combos(parent):
	# units combo
	parent.units_cb.addItem('Imperial', 'inch')
	parent.units_cb.addItem('Metric', 'metric')

	# drive timing combo
	parent.drive_timing_cb.addItem('None', False)
	parent.drive_timing_cb.addItem('Gecko 201', ['500', '4000', '20000', '1000'])
	parent.drive_timing_cb.addItem('Gecko 202', ['500', '4500', '20000', '1000'])
	parent.drive_timing_cb.addItem('Gecko 203v', ['1000', '2000', '200', '200'])
	parent.drive_timing_cb.addItem('Gecko 210', ['500', '4000', '20000', '1000'])
	parent.drive_timing_cb.addItem('Gecko 212', ['500', '4000', '20000', '1000'])
	parent.drive_timing_cb.addItem('Gecko 320', ['3500', '500', '200', '200'])
	parent.drive_timing_cb.addItem('Gecko 540', ['1000', '2000', '200', '200'])
	parent.drive_timing_cb.addItem('L297', ['500', '4000', '4000', '1000'])
	parent.drive_timing_cb.addItem('PMDX 150', ['1000', '2000', '1000', '1000'])
	parent.drive_timing_cb.addItem('Sherline', ['22000', '22000', '100000', '100000'])
	parent.drive_timing_cb.addItem('Xylotex BS-3', ['2000', '1000', '200', '200'])
	parent.drive_timing_cb.addItem('Parker 750', ['1000', '1000', '1000', '200000'])
	parent.drive_timing_cb.addItem('JVL SMD41/42', ['500', '500', '2500', '2500'])
	parent.drive_timing_cb.addItem('Hobbycnc', ['2000', '2000', '2000', '2000'])
	parent.drive_timing_cb.addItem('Keling 4030', ['5000', '5000', '20000', '20000'])



def configPath(text):
	if not text:
		return ''
	configNameUnderscored = text.replace(' ','_')
	return os.path.join(os.path.expanduser('~/linuxcnc/configs'), configNameUnderscored)

def set_drive_timing(parent):
	data = parent.drive_timing_cb.itemData(parent.drive_timing_cb.currentIndex())
	parent.step_time_le.setText(data[0])
	parent.step_space_le.setText(data[1])
	parent.dir_setup_le.setText(data[2])
	parent.dir_hold_le.setText(data[3])


"""

'None', False
'Gecko 201', ['500', '4000', '20000', '1000']
'Gecko 202', ['500', '4500', '20000', '1000']
'Gecko 203v', ['1000', '2000', '200', '200']
'Gecko 210', ['500', '4000', '20000', '1000']
'Gecko 212', ['500', '4000', '20000', '1000']
'Gecko 320', ['3500', '500', '200', '200']
'Gecko 540', ['1000', '2000', '200', '200']
'L297', ['500', '4000', '4000', '1000']
'PMDX 150', ['1000', '2000', '1000', '1000']
'Sherline', ['22000', '22000', '100000', '100000']
'Xylotex BS-3', ['2000', '1000', '200', '200']
'Parker 750', ['1000', '1000', '1000', '200000']
'JVL SMD41/42', ['500', '500', '2500', '2500']
'Hobbycnc', ['2000', '2000', '2000', '2000']
'Keling 4030', ['5000', '5000', '20000', '20000']

def set_connections(parent):
	parent.nameLE.textChanged.connect(config_name_changed)


def config_name_changed():


	def build_gui():
		gui_utilities.build_combos(self)
		gui_utilities.set_connections(self)

	def setup(self):
		self.nameLE.textChanged.connect(self.config_name_changed)
"""
