#!/usr/bin/python

import tkinter as tk
import pandas as pd 
import matplotlib 

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
options = [
	'P',
	'T',
	'V',
	'PI'
]


#===========
#GLOBAL VAR
#===========
# besaran pada sumbu
x_val = "X"
y_val = "Y"

#==================
# DUMMY DATA FRAME
#==================
dummy = pd.read_csv("~/sandbox/python/therwell.csv")



#================
# event handler
#================

# fungsi yang dipanggil saat tombol export csv ditekan
# menerima nama file yang akan diekpor dan menulis ke file system
def exportCSV(filename):
	print("export CSV here, may i help you with this {} file".format(filename))

# fungsi yang dipanggil ketika tombol export report ditekan
# menerima nama file yang akan diekspor dan menulis ke file system
def exportReport(filename):
	print("export report here, may i help you with this {} file".format(filename))

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
root.configure(background = "#CBCBCB");


#==========================================================
# pembagian window jadi beberapa frame dengan spesialisasi
#==========================================================

frame_options = tk.Frame(root, width=width, height=75, background="#CBCBCB")
frame_options.pack(fill=None, expand=False, side=tk.TOP)
frame_options.pack_propagate(False)

frame_plot = tk.Frame(root, width=width, height=425, background="#CBCBCB")
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

frame_x_var = tk.Frame(frame_option_buttons, width=80, height=45, background="#CBCBCB")
frame_x_var.pack(fill=None, expand=False, side=tk.LEFT)
frame_x_var.pack_propagate(0)

# frame_padding = tk.Frame(frame_option_buttons, width=50, height=45,background="#CBCBCB")
# frame_padding.pack(fill=None, expand=False, side=tk.LEFT)

# label_y_var = tk.Label(frame_option_buttons, wraplength=1, text="x : ", bg="#CBCBCB",font="none 11 bold")
# label_y_var.pack(fill=None)

frame_y_var = tk.Frame(frame_option_buttons, width=80, height=45, background="#CBCBCB")
frame_y_var.pack(fill=None, expand=False, side=tk.LEFT)
frame_y_var.pack_propagate(0)

frame_padding = tk.Frame(frame_option_buttons, width=50, height=45, background="#CBCBCB")
frame_padding.pack(fill=None, expand=False, side=tk.RIGHT)

frame_plot_button = tk.Frame(frame_option_buttons, width=50, height=45, background="#CBCBCB")
frame_plot_button.pack(fill=None, expand=False, side=tk.RIGHT)
frame_plot_button.pack_propagate(0)


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

dropdown_x_var = tk.OptionMenu(frame_x_var, varx, *options)
dropdown_x_var.pack(fill=None, expand=False, side=tk.LEFT)

vary = tk.StringVar(frame_y_var)
vary.set(options[0])

dropdown_y_var = tk.OptionMenu(frame_y_var, vary, *options)
dropdown_y_var.pack(fill=None, expand=False, side=tk.LEFT)

button_plot = tk.Button(frame_plot_button, width=option_button_width, height=option_button_height, text="Plot", command=lambda: doPlot(dummy, frame_plot))
button_plot.pack(fill=None, expand=None, side=tk.LEFT)


#====================================
# label untuk menaruh output dari csv
#====================================

frame_padding = tk.Frame(frame_label, width=400, height=20, background="#CBCBCB")
frame_padding.pack(fill=None, expand=False, side=tk.TOP)

frame_label_whp = tk.Frame(frame_label, width=400, height=40, background="#CBCBCB")
frame_label_whp.pack(fill="both", expand=False, side=tk.TOP)
frame_label_whp.pack_propagate(0)

frame_label_pwf = tk.Frame(frame_label, width=400, height=40, background="#CBCBCB")
frame_label_pwf.pack(fill="both", expand=False, side=tk.TOP)
frame_label_pwf.pack_propagate(0)

label_whp = tk.Label(frame_label_whp, text="WHP : ", bg="#CBCBCB", font="none 12 bold")
label_whp.pack(fill="x")

label_pwf = tk.Label(frame_label_pwf, text="PWF : ", bg="#CBCBCB", font="none 12 bold")
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

button_export_report = tk.Button(frame_export_report, width=15, height=1, text="Export Report" , bg="white" , command=lambda: exportReport("my ass.txt"))
button_export_report.pack(fill=None)

button_export_csv = tk.Button(frame_export_csv, width=15, height=1, text="Export CSV" , bg="white" , command=lambda:exportCSV("my ass.csv"))
button_export_csv.pack(fill=None)




#=============
# MAIN
#=============

root.mainloop()
