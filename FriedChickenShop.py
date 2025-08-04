from tkinter import *
import tkinter.font as tkFont

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
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.frames["MainFrame"] = self.create_main_frame()
        self.container.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainFrame")

    def create_main_frame(self):

        title_font = tkFont.Font(
            family="Verdana",
            size=40,
        )

        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        self.canvas = Canvas(frame)
        self.scrollbar = Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        content_frame = Frame(self.canvas)
        content_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=content_frame, anchor="nw")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.title = Label(
            content_frame,
            text="Fried Chicken",
            font=title_font,
        )
        self.title.grid(
            row=0,
            column=0,
            columnspan=2,
        )
        self.burger_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\burger.png"
        )

        self.tenders_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\tenders.png"
        )
        self.fries_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\fries.png"
        )

        self.mashpotatos_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\mashpotatos.png"
        )
        self.one_piece_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\one_piece.png"
        )

        self.popcorn_chicken_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\popcorn_chicken.png"
        )
        self.three_piece_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\three_piece.png"
        )

        self.two_piece_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\91906LouisYang\imgs\two_piece.png"
        )

        food_items = {
            "Burger": [
                0.99,
                self.burger_img,
            ],
            "Tenders": [
                0.99,
                self.tenders_img,
            ],
            "Fries": [
                0.99,
                self.fries_img,
            ],
            "Mashpotatos": [
                0.99,
                self.mashpotatos_img,
            ],
            "One Piece": [
                0.99,
                self.one_piece_img,
            ],
            "Popcorn Chicken": [
                0.99,
                self.popcorn_chicken_img,
            ],
            "Three Piece": [
                0.99,
                self.three_piece_img,
            ],
            "Two piece": [
                0.99,
                self.two_piece_img,
            ],
        }
        item_start_row = 1
        col = 0
        for i in food_items:
            price, img = food_items[i]
            food_frame = Frame(
                content_frame,
                bd=2,
                relief=RAISED,
                padx=10,
                pady=10,
            )
            food_frame.grid(
                row=item_start_row,
                column=col,
                padx=10,
                pady=10,
            )
            self.food_frame_img = Label(
                food_frame,
                image=img,
            )
            self.food_frame_img.grid(
                row=0,
                column=0,
            )
            self.food_frame_text = Label(food_frame, text=i)
            self.food_frame_text.grid(row=1, column=0)
            self.food_frame_price = Label(food_frame, text=price)
            self.food_frame_price.grid(row=2, column=0)
            self.food_frame = Button(food_frame, text="Add to cart")
            self.food_frame.grid(row=3, column=0)

            if col == 0:
                col = 1
            else:
                col = 0
                item_start_row += 1
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
