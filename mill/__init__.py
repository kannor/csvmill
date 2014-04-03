import csv

class Mill(object):

	def __init__(self, input_csv, output_csv):
		self.input_csv = input_csv
		self.output_csv = output_csv

		if self.input_csv == self.output_csv:
			raise ValueError

	def process(self, filename=None):
		"""
		Open, Process and Save csv file.
		"""
		if not filename:
			filename = self.input_csv

		if filename.endswith('.csv'):

			with open(filename) as _file:
				reader = csv.reader(_file)
				data = list(reader)

			self.save(self.format(self.purify(data)))
			return

		raise TypeError(
				"Excepting csv filetype got %s filetype instead." % (filename.split('.', 1)[1])
			)

	def save(self, data):
		"""
		Save a written csv file.
		"""
		self.write(data)

	def purify(self, csv_list):
		"""
		Revome the unwanted jiberish on top of the csv files
		"""
		for row in csv_list:
			if row[0] == "hole ID":
				return csv_list[csv_list.index(row) + 1:]
		return csv_list

	def format(self, csv_list):
		"""
		Core of the class...
		Format the csv.
		csv_list should be puried before formatting.
		"""
		new_csv = []
		for row in csv_list:

			new_row = list()
			new_row.extend(row[:3] + [1888.99, row[4], 0, 1178.99])
			
			new_csv.append(new_row)
		return new_csv

	def write(self, data, filename=None):
		"""
		Write a new csv file.
		"""
		if not filename:
			filename = self.output_csv

		with open(filename, "w") as _file:
			writer = csv.writer(_file)
			
			writer.writerow(list(_ for _ in self.header()))
			writer.writerows(data)	

	def header(self, format=None):
		"""
		Returns the csv header base on the format.
		"""
		return 	["hole ID", "East", "North", "Plan", "depth", "dip", "Target depth"]

	def close(self, _file):
		"""
		Close and opnned csv file.
		"""
		if isinstance(file, _file):
			_file.close()
		else:
			raise TypeError(
					"Excepting a FileType not %s " % (type(_file))
				)
