#!/usr/bin/python

import Tkinter as tk
import pandas as pd 
import matplotlib 
import os
import shutil
import calculationall as ca

from datetime import datetime
from Tkinter import *

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#===========
# CONSTANTS
#===========
height = 600
width = 800
option_button_height = 2
option_button_width = 2

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def updateroot(root):
   root.update()
   
def donothing():
   pass

class WindowNew(Frame):

	def __init__(self, conf, master=None):
		Frame.__init__(self, master)
		self.conf 			= conf
		self.top 			= None
		self.whp			= None 
		self.mr				= None 
		self.ent			= None 
		self.pwf			= None
		self.tableheight 	= 1
		self.tablewidth 	= 4
		self.entries 		= []

	def create(self):
		self.top 	= Toplevel(master=None, cnf = self.conf)
		self.grid()
		self.create_window_one()

	def show_entry_fields(self):
		print(self.whp.get())
		print(self.mr.get())
		print(self.ent.get())
		print(self.pwf.get())
		
		tabledata = []
		for x in self.entries:
			print('pepeg')
			column = []
			for y in x:
				column.append(y.get())
			tabledata.append(column)
			print(column)
		print(tabledata)

	def enter_entry_fields(self):
		tabledata = []
		for x in self.entries:
			print('pepeg')
			column = []
			for y in x:
				column.append(y.get())
			tabledata.append(column)
			print(column)
		
		subTableinput = []
		
		for x in tabledata:
			elemListSubinput = ca.OneInput(float(x[0]), float(x[1]), float(x[2]), float(x[3]))
			subTableinput.append(elemListSubinput)
		
		currentTableInput = ca.inputTable(float(self.whp.get()), float(self.mr.get()), float(self.ent.get()), float(self.pwf.get()))

		currentTableInput.subTable = subTableinput

		ca.automatedinput(currentTableInput)

		self.top.destroy()

		restart_program()
		

	def appendgrid(self):
		curheight = self.tableheight + 5
		width = self.tablewidth + 1
		print(curheight, width)
		cols = []
		for j in range(1, width):
			e = Entry(self.top)
			e.grid(row=curheight, column=j, sticky=NSEW)
			# e.insert(END, '%d.%d' % (curheight, j))
			cols.append(e)
		self.entries.append(cols)

		self.tableheight += 1

	def create_window_one(self):
		
		self.top.title('Dataframe Input')

		tk.Label(self.top, text="WHP (bar)  ",background="#CBCBCB").grid(row=0)
		tk.Label(self.top, text="Massrate (Kg/s)  ",background="#CBCBCB").grid(row=1)
		tk.Label(self.top, text="Enthalpy (KJ/kg)  ",background="#CBCBCB").grid(row=2)
		tk.Label(self.top, text="PWF (bar)  ",background="#CBCBCB").grid(row=3)

		self.whp = tk.Entry(self.top)
		self.mr = tk.Entry(self.top)
		self.ent = tk.Entry(self.top)
		self.pwf = tk.Entry(self.top)

		self.whp.grid(row=0, column=1)
		self.mr.grid(row=1, column=1)
		self.ent.grid(row=2, column=1)
		self.pwf.grid(row=3, column=1)

		tbwidth = self.tablewidth
		tbheight = self.tableheight

		tk.Label(self.top, text="MD(meter)",background="#CBCBCB").grid(row=4, column=1)
		tk.Label(self.top, text="Angle",background="#CBCBCB").grid(row=4, column=2)
		tk.Label(self.top, text="Diameter(m)",background="#CBCBCB").grid(row=4, column=3)
		tk.Label(self.top, text="Roughness(m)",background="#CBCBCB").grid(row=4, column=4)
		for i in range(5 , 5 + tbheight):
			cols = []
			for j in range(1, 1 + tbwidth):
				e = Entry(self.top)
				e.grid(row=i, column=j, sticky=NSEW)
				# e.insert(END, '%d.%d' % (i, j))
				cols.append(e)
			self.entries.append(cols)
		
		tk.Button(self.top, 
			text='Insert Row', command=lambda : self.appendgrid()).grid(row=20, 
														column=4, 
														sticky=tk.W, 
														pady=4)

		tk.Button(self.top, 
			text='Enter Data', command=self.enter_entry_fields).grid(row=20, 
														column=1, 
														sticky=tk.W, 
														pady=4)

	
class Window(Frame):

	# Define settings upon initialization. Here you can specify
	def __init__(self, master=None):
		
		# parameters that you want to send through the Frame class. 
		Frame.__init__(self, master)   

		#reference to the master widget, which is the tk window				 
		self.master = master

		#with that, we want to then run init_window, which doesn't yet exist
		self.init_window()

	def init_window(self):

		conf = {
			"height"	: height,
			"width"		: width,
			"bg"		: "#CBCBCB"
		}

		creationwindow = WindowNew(conf)

		menubar = Menu(self.master)

		filemenu = Menu(menubar, tearoff=0)

		filemenu.add_command(label="New", command=creationwindow.create)

		# filemenu.add_command(label="Open", command=donothing)

		# filemenu.add_command(label="Save", command=donothing)

		filemenu.add_separator()

		filemenu.add_command(label="Exit", command=root.quit)

		menubar.add_cascade(label="File", menu=filemenu)

		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Help Index", command=donothing)
		helpmenu.add_command(label="About...", command=donothing)
		menubar.add_cascade(label="Help", menu=helpmenu)

		root.config(menu=menubar)

		
	def client_exit(self):
		exit()

# options = [
# 	'P',
# 	'T',
# 	'V',
# 	'PI'
# ]


#===========
#GLOBAL VAR
#===========
# besaran pada sumbu
x_val = "X"
y_val = "Y"

#==================
# DUMMY DATA FRAME
#==================
try:
	dummy = pd.read_csv("output.csv")
	options = list(dummy)
	datacount = dummy.MDmeter.count()
	ps = dummy['Pressure']
	finalp = ps[datacount - 1]
	initp = ps[0]
except Exception as e:
	options = ['empty']
	finalp = 0
	initp = 0
	print(e)


#================
# event handler
#================

# fungsi yang dipanggil saat tombol export csv ditekan
# menerima nama file yang akan diekpor dan menulis ke file system
def exportCSV(filename):
	now = datetime.now()
	dt_string = now.strftime("%d-%m-%Y-%H%M%S")
	print(dt_string)
	newfilename = 'dataframecomplete'+ dt_string +'.csv'
	shutil.copyfile('output.csv', 'savedata/'+newfilename)
	print("CSV file saved in savedata/{} file".format(newfilename))

# fungsi yang dipanggil ketika tombol export report ditekan
# menerima nama file yang akan diekspor dan menulis ke file system
def exportReport(filename):
	now = datetime.now()
	dt_string = now.strftime("%d-%m-%Y-%H%M%S")
	print(dt_string)
	newfilename = 'dataframereport'+ dt_string +'.csv'
	
	print("CSV file saved in savedata/{} file".format(newfilename))

# fungsi yang akan dipanggil ketika option diganti
# menerima 2 parameter => sumbu (x || y) dan variabel sumbu (P, V, T)
def setPlot(axis, var):
	if (axis == 'x'):
		x_val = var
	else:
		y_val = var

	print("just changed {} axis var to {}".format(axis, var))


# plot result dengan sumbu x dan y yang telah dipilih oleh pengguna
# df merupakan data frame yang akan di plot
def doPlot(df, frame):
	print("will plot with x : {} and y : {}".format(varx.get(), vary.get()))

	# hapus plot lama, jika ada 
	try:
		# canvas.get_tk_widget.pack_forget()
		for child in frame.winfo_children():
			child.destroy()
	except :
		print("something seems a bit off")

	f = Figure(figsize=(5,5), dpi=100)
	a = f.add_subplot(111)
	a.plot(df[varx.get()].tolist(), df[vary.get()].tolist())
	a.grid(b=True, which='both', color='#666666', linestyle='--')

	# df.plot(x=varx.get(), y=vary.get())
	# plt.show()
	canvas = FigureCanvasTkAgg(f, frame)
	canvas.draw()
	canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

	# toolbar = NavigationToolbar2TkAgg(canvas, frame)
	# toolbar.update()
	# canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# =====================
# Tkinter window
# =====================

root = tk.Tk()
root.title("Therwell")
root.geometry('{}x{}'.format(width, height))
root.configure(background = "#CBCBCB")

app = Window(root)

#==========================================================
# pembagian window jadi beberapa frame dengan spesialisasi
#==========================================================

frame_options = tk.Frame(root, width=width, height=75, background="#CBCBCB")
frame_options.pack(fill=None, expand=False, side=tk.TOP)
frame_options.pack_propagate(False)

frame_plot = tk.Frame(root, width=width, height=425, background="#FFFFFF")
frame_plot.pack(fill=None, expand=False, side=tk.TOP)
frame_plot.pack_propagate(False)

frame_exports = tk.Frame(root, width=width, height=100, background="#CBCBCB")
frame_exports.pack(fill=None, expand=False, side=tk.TOP)

frame_label = tk.Frame(frame_exports, width=400, height=100, background="#CBCBCB")
frame_label.pack(fill=None, expand=False, side=tk.LEFT)
frame_label.pack_propagate(False)

frame_export_buttons = tk.Frame(frame_exports, width=400, height=100, background="#CBCBCB")
frame_export_buttons.pack(fill=None, expand=False, side=tk.RIGHT)
frame_export_buttons.pack_propagate(False)


#===============
# tombol option
#===============

frame_padding = tk.Frame(frame_options, width=width, height=15, background="#CBCBCB")
frame_padding.pack(fill=None, expand=False, side=tk.TOP)

frame_option_buttons = tk.Frame(frame_options, width=width, height=45, background="#CBCBCB")
frame_option_buttons.pack(fill=None, expand=False, side=tk.TOP)
frame_option_buttons.pack_propagate(0)

frame_padding = tk.Frame(frame_option_buttons, width=50, height=45,background="#CBCBCB")
frame_padding.pack(fill=None, expand=False, side=tk.LEFT)

# label_x_var = tk.Label(frame_option_buttons, wraplength=1, text="x : ", bg="#CBCBCB",font="none 11 bold")
# label_x_var.pack(fill=None)

frame_x_var = tk.Frame(frame_option_buttons, width=150, height=45, background="#CBCBCB")
frame_x_var.pack(fill=None, expand=False, side=tk.LEFT)
frame_x_var.pack_propagate(0)

frame_x_title = tk.Label(frame_x_var, text="X Axis: ", background="#CBCBCB")
frame_x_title.pack(fill=None, expand=False, side=tk.LEFT)

# frame_padding = tk.Frame(frame_option_buttons, width=50, height=45,background="#CBCBCB")
# frame_padding.pack(fill=None, expand=False, side=tk.LEFT)

# label_y_var = tk.Label(frame_option_buttons, wraplength=1, text="x : ", bg="#CBCBCB",font="none 11 bold")
# label_y_var.pack(fill=None)

frame_y_var = tk.Frame(frame_option_buttons, width=150, height=45, background="#CBCBCB")
frame_y_var.pack(fill=None, expand=False, side=tk.LEFT)
frame_y_var.pack_propagate(0)

frame_y_title = tk.Label(frame_y_var, text="Y Axis: ", background="#CBCBCB")
frame_y_title.pack(fill=None, expand=False, side=tk.LEFT)

frame_padding = tk.Frame(frame_option_buttons, width=50, height=45, background="#CBCBCB")
frame_padding.pack(fill=None, expand=False, side=tk.RIGHT)

frame_plot_button = tk.Frame(frame_option_buttons, width=50, height=45, background="#CBCBCB")
frame_plot_button.pack(fill=None, expand=False, side=tk.RIGHT)
frame_plot_button.pack_propagate(0)

frame_refresh_button = tk.Frame(frame_option_buttons, width=100, height=45, background="#CBCBCB")
frame_refresh_button.pack(fill=None, expand=False, side=tk.RIGHT)
frame_refresh_button.pack_propagate(0)


# button_x_p = tk.Button(frame_x_var, width=option_button_width, height=option_button_height, text="P", command=lambda: setPlot('x', 'P'))
# button_x_p.pack(fill=None, expand=False, side=tk.LEFT)

# button_x_v = tk.Button(frame_x_var, width=option_button_width, height=option_button_height, text="V", command=lambda: setPlot('x', 'V'))
# button_x_v.pack(fill=None, expand=False, side=tk.LEFT)

# button_y_t = tk.Button(frame_y_var, width=option_button_width, height=option_button_height, text='T', command=lambda: setPlot('y', 'T'))
# button_y_t.pack(fill=None, expand=False, side=tk.LEFT)

# button_y_pi = tk.Button(frame_y_var, width=option_button_width, height=option_button_height, text='pi', command=lambda: setPlot('y', 'PI'))
# button_y_pi.pack(fill=None, expand=False, side=tk.LEFT)

varx = tk.StringVar(frame_x_var)
varx.set(options[0])

frame_x_title = tk.Frame(frame_x_var)

dropdown_x_var = tk.OptionMenu(frame_x_var, varx, *options)
dropdown_x_var.pack(fill=None, expand=False, side=tk.LEFT)

vary = tk.StringVar(frame_y_var)
vary.set(options[0])

dropdown_y_var = tk.OptionMenu(frame_y_var, vary, *options)
dropdown_y_var.pack(fill=None, expand=False, side=tk.LEFT)

button_plot = tk.Button(frame_plot_button, width=10, height=option_button_height, text="Plot", command=lambda: doPlot(dummy, frame_plot))
button_plot.pack(fill=None, expand=None, side=tk.LEFT)

button_refresh = tk.Button(frame_refresh_button, width=10, height=option_button_height, text="Refresh", command=restart_program)
button_refresh.pack(fill=None, expand=None, side=tk.LEFT)

#====================================
# label untuk menaruh output dari csv
#====================================


WHP = min(finalp, initp)
PWF = max(finalp, initp)

frame_padding = tk.Frame(frame_label, width=400, height=20, background="#CBCBCB")
frame_padding.pack(fill=None, expand=False, side=tk.TOP)

frame_label_whp = tk.Frame(frame_label, width=400, height=40, background="#CBCBCB")
frame_label_whp.pack(fill="both", expand=False, side=tk.TOP)
frame_label_whp.pack_propagate(0)

frame_label_pwf = tk.Frame(frame_label, width=400, height=40, background="#CBCBCB")
frame_label_pwf.pack(fill="both", expand=False, side=tk.TOP)
frame_label_pwf.pack_propagate(0)

label_whp = tk.Label(frame_label_whp, text="WHP : " + str(round(WHP, 3)), bg="#CBCBCB", font="none 12 bold")
label_whp.pack(fill="x")

label_pwf = tk.Label(frame_label_pwf, text="PWF : " + str(round(PWF, 3)), bg="#CBCBCB", font="none 12 bold")
label_pwf.pack(fill="x")


#===============
# tombol export
#===============

frame_padding = tk.Frame(frame_export_buttons, width=400, height=20, background="#CBCBCB")
frame_padding.pack(fill=None, expand=False, side=tk.TOP)


frame_export_report = tk.Frame(frame_export_buttons, width=300, height=30, background="#CBCBCB")
frame_export_report.pack(fill=None, expand=False, side=tk.TOP)
frame_export_report.pack_propagate(0)

frame_export_csv = tk.Frame(frame_export_buttons, width=300, height=30, background="#CBCBCB")
frame_export_csv.pack(fill=None, expand=False, side=tk.TOP)
frame_export_csv.pack_propagate(0)

button_export_report = tk.Button(frame_export_report, width=15, height=1, text="Export Report" , bg="white" , command=lambda: exportReport("report.txt"))
button_export_report.pack(fill=None)

button_export_csv = tk.Button(frame_export_csv, width=15, height=1, text="Export CSV" , bg="white" , command=lambda:exportCSV("output.csv"))
button_export_csv.pack(fill=None)




#=============
# MAIN
#=============

root.mainloop()
