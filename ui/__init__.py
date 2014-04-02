from Tkinter import *

import tkFileDialog

from mill import Mill

class CSVMillUi(Frame):
	"""
	"""
	def __init__(self):

		self.input_csv = self.output_csv = ""

		Frame.__init__(self, bg="")
		self.master.title = "csv mill"
		self.grid()

		self._banner()
		self._input_field_label()
		self._input_field()
		self._browse_btn()
		self._format_btn()

	def _banner(self):
		opt = {
			"text": "CSV Mill",
			"width": 0,
			"height": 0
		}
		grid_opt = {
			"padx": 0,
			"pady": 0
		}

		self.label = Label(self, **opt)
		self.label.grid(**grid_opt)


	def _input_field_label(self):
		opt = {
			"text": "Input File"
		}
		grid_opt = {
			"row": 2,
			"column": 0,
			"padx": 20,
			"pady": 50
		}

		self.input_field_label = Label(self, **opt)
		self.input_field_label.grid(**grid_opt)

	def _input_field(self):
		opt = {
			"width": 40
		}
		grid_opt = {
			"row": 2,
			"column": 1,
			"padx": 0,
			"pady": 50
		}

		self.input_field = Entry(self, **opt)
		self.input_field.grid(**grid_opt)


	def _browse_btn(self):
		opt = {
			"text": "browse",
			"command": self.getfilename
		}
		grid_opt = {
			"row": 2,
			"column": 3,
			"padx": 0,
			"pady": 50
		}

		self.browse_btn = Button(self, **opt)
		self.browse_btn.grid(**grid_opt)

	def _format_btn(self):
		opt = {
			"text": "FORMAT",
			"command": self.savefilename
		}
		grid_opt = {
			"row": 2,
			"column": 4,
			"padx": 0,
			"pady": 50
		}

		self.format_btn = Button(self, **opt)
		self.format_btn.grid(**grid_opt)

	def _select(self):
		pass

	def clear(self):
		"""
		Clear the input field. 
		"""
		self.input_field.delete(0, END)

	def reset(self):
		"""
		Reset self.input_csv and self.output_csv
		"""

		self.input_csv = self.output_csv = ""

	def getfilename(self):
		opt = {
			"parent": self,
			"filetypes": [("csv files", ".csv")],
			"title": "Open cvs file"
		}

		#get filename
		filename = tkFileDialog.askopenfilename(**opt)

		if filename:
			self.clear()

			self.input_csv = filename
			self.input_field.insert(0, filename)

	def savefilename(self):
		opt = {
			"defaultextension": ".csv",
			"initialfile": "formated.csv",
			"parent": self,
			"filetypes": [("csv files", ".csv")],
			"title": "Open cvs file"
		}

		filename = tkFileDialog.asksaveasfilename(**opt)

		if filename:
			self.output_csv = filename

			Mill(self.input_csv, self.output_csv).process()
			
			self.clear()
			self.reset()		
			



