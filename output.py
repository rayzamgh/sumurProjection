#!/usr/bin/python

import tkinter as tk

# CONSTANTS
height = 600
width = 800

# besaran pada sumbu
x_val = "X"
y_val = "Y"


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




















root = tk.Tk()
root.title("Therwell")
root.geometry('{}x{}'.format(width, height))
root.configure(background = "#CBCBCB");

# pembagian window jadi beberapa frame dengan spesialisasi

frame_options = tk.Frame(root, width=width, height=100, background="red")
frame_options.pack(fill=None, expand=False, side=tk.TOP)

frame_plot = tk.Frame(root, width=width, height=400, background="green")
frame_plot.pack(fill=None, expand=False, side=tk.TOP)

frame_exports = tk.Frame(root, width=width, height=100, background="yellow")
frame_exports.pack(fill=None, expand=False, side=tk.TOP)

frame_label = tk.Frame(frame_exports, width=400, height=100, background="#CBCBCB")
frame_label.pack(fill=None, expand=False, side=tk.LEFT)

frame_export_buttons = tk.Frame(frame_exports, width=400, height=100, background="black")
frame_export_buttons.pack(fill=None, expand=False, side=tk.RIGHT)


# label untuk menaruh ouput dari csv

frame_label_whp = tk.Frame(frame_label, width=400, height=40, background="blue")
frame_label_whp.pack(fill="both", expand=False, side=tk.TOP)

frame_label_pwf = tk.Frame(frame_label, width=400, height=40, background="purple")
frame_label_pwf.pack(fill="both", expand=False, side=tk.TOP)

label_whp = tk.Label(frame_label_whp, text="WHP : ", bg="white", font="none 12 bold")
label_whp.pack(fill=None)

label_pwf = tk.Label(frame_label_pwf, text="PWF : ", bg="white", font="none 12 bold")
label_pwf.pack(fill=None)

# tombol export

frame_export_report = tk.Frame(frame_export_buttons, width=400, height=50, background="red")
frame_export_report.pack(fill=None, expand=False, side=tk.TOP)

frame_export_csv = tk.Frame(frame_export_buttons, width=400, height=50, background="pink")
frame_export_csv.pack(fill=None, expand=False, side=tk.TOP)

button_export_report = tk.Button(frame_export_report, width=15, height=2, text="Export Report" , bg="white" , command=lambda: exportReport("my ass.txt"))
button_export_report.pack(fill="both")

button_export_csv = tk.Button(frame_export_csv, width=15, height=2, text="Export CSV" , bg="white" , command=lambda:exportCSV("my ass.csv"))
button_export_csv.pack(fill="both")





# buka window

root.mainloop()
