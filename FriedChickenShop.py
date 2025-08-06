from tkinter import *
import tkinter.font as tkFont


class MainScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Fried Chicken Shop")
        self.root.geometry("900x1000")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.container = Frame(self.root)
        self.frames = {}
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["CheckoutFrame"] = self.create_checkout_frame()
        self.container.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainFrame")

    def create_main_frame(self):
        item_start_row = 1
        col = 0
        cart_title_font = tkFont.Font(
            family="Verdana",
            size=20,
        )
        cart_items_font = tkFont.Font(
            family="Verdana",
            size=10,
        )
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
        self.content_frame = Frame(self.canvas)
        self.content_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.title = Label(
            self.content_frame,
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

        for i in food_items:
            price, img = food_items[i]
            food_frame = Frame(
                self.content_frame,
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
            self.food_frame = Button(
                food_frame,
                text="Add to cart",
                command=lambda name=i: self.add_to_cart(name),
            )
            self.food_frame.grid(row=3, column=0)

            if col == 0:
                col = 1
            else:
                col = 0
                item_start_row += 1

        self.cart_frame = Frame(self.content_frame, bd=2, relief=RAISED)
        self.cart_frame.grid(
            row=1,
            column=2,
            rowspan=3,
        )
        self.cart_frame_label = Label(
            self.cart_frame, text="cart", font=cart_title_font
        )
        self.cart_frame_label.grid(row=0, column=0)
        self.cart_frame_listbox = Listbox(self.cart_frame, font=cart_items_font)
        self.cart_frame_listbox.grid(row=1, column=0, ipadx=60, ipady=300)
        self.checkout_button = Button(
            self.cart_frame,
            bg="red",
            text="Checkout",
            width=25,
            command=lambda: self.show_frame("CheckoutFrame"),
        )

        self.checkout_button.grid(
            row=2,
            column=0,
            ipadx=10,
            ipady=10,
        )

        return frame

    def create_checkout_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

        title_font = tkFont.Font(
            family="Verdana",
            size=32,
        )
        self.item_font = tkFont.Font(
            family="Verdana",
            size=12,
        )

        Label(frame, text="CHECKOUT", font=title_font).grid(
            row=0,
            column=0,
            pady=20,
        )

        panel = Frame(
            frame,
            bd=2,
            relief=GROOVE,
            padx=20,
            pady=20,
        )
        panel.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10,
        )
        panel.columnconfigure(
            0,
            weight=1,
        )

        bottom = Frame(frame)
        bottom.grid(row=2, column=0, pady=10)
        Button(
            bottom, text="Back to Menu", command=lambda: self.show_frame("MainFrame")
        ).grid(
            row=0,
            column=0,
            padx=10,
            ipadx=10,
            ipady=10,
        )
        Button(bottom, text="Place Order", bg="red", fg="white").grid(
            row=0,
            column=1,
            padx=10,
            ipadx=10,
            ipady=10,
        )

        return frame

    def add_to_cart(self, item_name):
        self.cart_frame_listbox.insert("end", item_name)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def run(self):
        self.root.mainloop()


# runs the whole programme
if __name__ == "__main__":
    app = MainScreen()
    app.run()
