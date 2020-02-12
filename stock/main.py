from win32api import GetMonitorInfo, MonitorFromPoint
from tkinter import *
from tkinter.ttk import *
import sys

WIDTH_WINDOW = None
HEIGHT_WINDOW = None

class Window(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
 
		self.master = master
		self.master.title("Finance information")
		self.master.overrideredirect(True)
		self.pack(fill = BOTH, expand = True)
 
		frame_test = Frame(self)
		frame_test.pack(fill = X)
 
		label_test = Label(frame_test, text="Test", width = 10)
		label_test.pack(side = LEFT, padx = 10, pady = 10)

		# 아래 코드 순서 변경하지 말기
		self.master.update()
		self.master.geometry("+%d+%d" % ( (WIDTH_WINDOW - self.master.winfo_width()) / 2, (HEIGHT_WINDOW - self.master.winfo_height()) / 2))
		# 위 코드 순서 변경하지 말기
 
		# 초기에는 비 활성화
		self.master.withdraw()
	
		window_controller = Toplevel()
		window_controller.attributes("-topmost", True)
		window_controller.overrideredirect(True)

		"""
		몰래 보기
		"""
		self.window_peek = Toplevel()
		self.window_peek.attributes("-topmost", True)
		self.window_peek.overrideredirect(True)
		self.window_peek.withdraw()
		self.bool_peek = False
		def peekPrice():
			if self.bool_peek:
				self.bool_peek = False
				self.window_peek.withdraw()
			else:
				self.bool_peek = True
				self.window_peek.update()
				self.window_peek.deiconify()
		button_peek = Button(window_controller, text = "/", width = 5, command = peekPrice)
		button_peek.pack(side = LEFT)

		"""
		메인 활성화
		"""
		self.bool_activation = False
		def activateWindow():
			if self.bool_activation:
				self.bool_activation = False
				self.master.withdraw()
				button_activation.configure(text = "+")
			else:
				self.bool_activation = True
				self.master.update()
				self.master.deiconify()
				button_activation.configure(text = "-")
		button_activation = Button(window_controller, text = "+", width = 5, command = activateWindow)
		button_activation.pack(side = LEFT)

		"""
		종료
		"""
		def exitProgram():
			sys.exit()
		button_exit = Button(window_controller, text = "x", width = 5, command = exitProgram)
		button_exit.pack(side = LEFT)

		# 아래 코드 순서 변경하지 말기
		window_controller.update()
		window_controller.geometry("+%d+%d" % ( WIDTH_WINDOW - window_controller.winfo_width(), HEIGHT_WINDOW - window_controller.winfo_height()))
		# 위 코드 순서 변경하지 말기

def getWindowSize():
	global WIDTH_WINDOW, HEIGHT_WINDOW

	list_area = GetMonitorInfo(MonitorFromPoint((0,0))).get("Work")
	WIDTH_WINDOW = list_area[2]
	HEIGHT_WINDOW = list_area[3]

if __name__ == '__main__':

	getWindowSize()

	root = Tk()
	window = Window(root)
	root.mainloop()