from tkinter import *

item_num = 8 
class MainScreen:
    def __init__(self):
        self.root = Tk()    
        self.root.title("Fried Chicken Shop")
        self.root.geometry("800x700")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        
        self.container = Frame(self.root)
        self.frames = {}

        
        self.frames["MainFrame"] = self.create_main_frame()
        self.container.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainFrame")
        
    def create_main_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
            

        
        self.canvas = Canvas(frame)
        self.scrollbar = Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        content_frame = Frame(self.canvas)
        content_frame.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.img1 = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\burger.png"
        )
        
        self.img2 = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\tenders.png"
        )
        self.img3 = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\fries.png"
        )
        
        self.img4 = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\mashpotatos.png"
        )
        self.img5 = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\one_piece.png"
        )
        
        self.img6 = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\popcorn_chicken.png"
        )
        self.img7 = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\three_piece.png"
        )
        
        self.img8 = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\two_piece.png"
        )
        self.image_label1 =Label(content_frame, image=self.img1)
        self.image_label1.grid(row=0, column=0)
        self.image_label1 =Label(content_frame, image=self.img2)
        self.image_label1.grid(row=0, column=1)
        self.image_label1 =Label(content_frame, image=self.img3)
        self.image_label1.grid(row=1, column=0)
        self.image_label1 =Label(content_frame, image=self.img4)
        self.image_label1.grid(row=1, column=1)
        self.image_label1 =Label(content_frame, image=self.img5)
        self.image_label1.grid(row=2, column=0)
        self.image_label1 =Label(content_frame, image=self.img6)
        self.image_label1.grid(row=2, column=1)
        self.image_label1 =Label(content_frame, image=self.img7)
        self.image_label1.grid(row=3, column=0)
        self.image_label1 =Label(content_frame, image=self.img8)
        self.image_label1.grid(row=3, column=1)
        
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0,weight=1)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        
        
        self.canvas.create_window((0, 0), window=content_frame, anchor="nw")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns") 
        def _on_mousewheel(event): self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel) 
        return frame  
            
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
        
    def run(self):
        self.root.mainloop()

# runs the whole programme
if __name__ == "__main__":
    app = MainScreen()
    app.run()   