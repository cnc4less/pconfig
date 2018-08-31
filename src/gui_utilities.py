import os, subprocess

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

	# gui combo
	parent.gui_cb.addItem('Select a GUI', False)
	parent.gui_cb.addItem('Axis', 'axis')
	parent.gui_cb.addItem('Touchy', 'touchy')
	parent.gui_cb.addItem('Gmoccapy', 'gmoccapy')
	parent.gui_cb.addItem('Gscreen', 'gscreen')
	parent.gui_cb.addItem(' Mini', ' mini')
	parent.gui_cb.addItem('tkLinuxCNC', 'tklinuxcnc')

	# position offset combo position_offset_cb
	parent.position_offset_cb.addItem('Relative', 'RELATIVE')
	parent.position_offset_cb.addItem('Machine', 'MACHINE')

	# position feedback combo
	parent.position_feedback_cb.addItem('Commanded', 'COMMANDED')
	parent.position_feedback_cb.addItem('Actual', 'ACTUAL')

	# parallel port type
	parent.port_0_type_cb.addItem('None', False)
	parent.port_0_type_cb.addItem('Out', 'out')
	parent.port_0_type_cb.addItem('In', 'in')
	parent.port_0_type_cb.addItem('EPP', 'epp')
	parent.port_0_type_cb.addItem('X', 'x')

"""
parent..addItem('', '')
parent..addItem('', ['', ''])

"""
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

def port_0_setup(parent):
	port_0_type = parent.port_0_type_cb.currentData()
	blank = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	dir_in = ['out', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in',
		'in', 'in', 'in', 'in', 'in','out', 'out']
	dir_out = ['out', 'out', 'out', 'out', 'out', 'out', 'out', 'out', 'out',
		'in', 'in', 'in', 'in', 'out', 'in', 'out', 'out']
	dir_x = ['in', 'out', 'out', 'out', 'out', 'out', 'out', 'out', 'out',
		'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in']
	pin_list = ''
	if not port_0_type:
		parent.port_0_gb.setEnabled(False)
		pin_list = blank
	elif port_0_type == 'out':
		parent.port_0_gb.setEnabled(True)
		pin_list = dir_out
	elif port_0_type == 'in':
		parent.port_0_gb.setEnabled(True)
		pin_list = dir_in
	elif port_0_type == 'epp':
		parent.port_0_gb.setEnabled(True)
		pin_list = dir_out
	elif port_0_type == 'x':
		parent.port_0_gb.setEnabled(True)
		pin_list = dir_x
	for index, item in enumerate(pin_list):
		getattr(parent, 'dir_lb_' + str(index + 1)).setText(item)
		# build the pin combos based on the pin_list


def latency_test():
	subprocess.call('latency-test')

def minperiod(parent, steptime=None, stepspace=None, latency=None):
	if parent.step_time_le.text() and parent.step_space_le.text():
		if steptime is None: steptime = int(parent.step_time_le.text())
		if stepspace is None: stepspace = int(parent.step_space_le.text())
		if latency is None: latency = int(parent.latency_le.text())
		if steptime <= 5000: # doublestep
			min_period = max(latency + steptime + stepspace + 5000, 4*steptime)
			max_hz = 1e9 / min_period
		else:
			min_period = latency + max(steptime, stepspace)
			max_hz = 1e9 / min_period
		parent.min_period_lb.setText('{} ns'.format(min_period))
		parent.max_step_rate_lb.setText('{0:.0f} Hz'.format(max_hz))



