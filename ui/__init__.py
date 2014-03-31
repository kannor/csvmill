from Tkinter import *

import tkFileDialog

class CSVMillUi(Frame):
	"""
	"""
	def __init__(self):
		Frame.__init__(self, bg="")
		self.master.title = "csv mill"
		self.grid()

		self.banner()
		self.input_field_label()
		self.input_field()
		self.browsw_btn()

	def banner(self):
		opt = {
			"text": "CSV Mill",
			"width": 0,
			"height": 0
		}
		grid_opt = {
			"padx": 0,
			"pady": 0
		}

		self.label = Label(self, **opt).grid(**grid_opt)


	def input_field_label(self):
		opt = {
			"text": "Input File"
		}
		grid_opt = {
			"row": 2,
			"column": 0,
			"padx": 20,
			"pady": 50
		}

		self.input_field_label = Label(self, **opt).grid(**grid_opt)

	def input_field(self):
		input_opt = {
			"width": 20,
			"height": 20
		}
		grid_opt = {
			"row": 2,
			"column": 1,
			"padx": 20,
			"pady": 50
		}

		self.input_field = Entry(self).grid(**grid_opt)


	def browsw_btn(self):
		opt = {
			"text": "browse"
		}
		grid_opt = {
			"row": 2,
			"column": 3,
			"padx": 20,
			"pady": 50
		}

		self.btn = Button(self, **opt).grid(**grid_opt)

	def select(self):
		pass



