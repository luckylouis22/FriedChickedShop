from tkinter import *
import tkinter.font as tkFont


class MainScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Fried Chicken Shop")
        self.root.geometry("1000x800")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Max and Min value of orders for each item.
        self.MAX_QTY = 99
        self.MIN_QTY = 1
        # Price of each item (float/int).
        self.BURGER_PRICE = 0.99
        self.TENDERS_PRICE = 0.99
        self.FIRES_PRICE = 0.99
        self.MASHPOTATOS_PRICE = 0.99
        self.ONE_PIECE_PRICE = 0.99
        self.POPCORN_CHICKEN_PRICE = 0.99
        self.THREE_PIECE_PRICE = 0.99
        self.TWO_PIECE_PRICE = 0.99

        # Defined and asigned all photos to a variable.
        self.burger_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Assessment\91906LouisYang\imgs\burger.png"
        )
        self.tenders_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Assessment\91906LouisYang\imgs\tenders.png"
        )
        self.fries_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Assessment\91906LouisYang\imgs\fries.png"
        )
        self.mashpotatos_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Assessment\91906LouisYang\imgs\mashpotatos.png"
        )
        self.one_piece_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Assessment\91906LouisYang\imgs\one_piece.png"
        )
        self.popcorn_chicken_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Assessment\91906LouisYang\imgs\popcorn_chicken.png"
        )
        self.three_piece_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Assessment\91906LouisYang\imgs\three_piece.png"
        )
        self.two_piece_img = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Assessment\91906LouisYang\imgs\two_piece.png"
        )

        # Dictonary to handle change made to spinbox.
        self.qty_vars = {}
        # Dictonary of every item and how many user has selected.
        self.cart_counts = {}
        # Dictonary for all ofmenu items.
        self.food_items = {
            "Burger": [
                self.BURGER_PRICE,
                self.burger_img,
            ],
            "Tenders": [
                self.TENDERS_PRICE,
                self.tenders_img,
            ],
            "Fries": [
                self.FIRES_PRICE,
                self.fries_img,
            ],
            "Mashpotatos": [
                self.MASHPOTATOS_PRICE,
                self.mashpotatos_img,
            ],
            "One Piece": [
                self.ONE_PIECE_PRICE,
                self.one_piece_img,
            ],
            "Popcorn Chicken": [
                self.POPCORN_CHICKEN_PRICE,
                self.popcorn_chicken_img,
            ],
            "Three Piece": [
                self.THREE_PIECE_PRICE,
                self.three_piece_img,
            ],
            "Two piece": [
                self.TWO_PIECE_PRICE,
                self.two_piece_img,
            ],
        }

        # All fonts used in the programme.
        self.cart_items_font = tkFont.Font(
            family="Verdana",
            size=10,
        )
        self.title_font = tkFont.Font(
            family="Verdana",
            size=40,
        )
        self.subtitle_font = tkFont.Font(
            family="Verdana",
            size=20,
        )
        self.checkout_item_font = tkFont.Font(
            family="Verdana",
            size=11,
        )
        self.cart_title_font = tkFont.Font(
            family="Verdana",
            size=20,
        )

        self.container = Frame(self.root)
        self.frames = {}
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        # Creating frames
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["CheckoutFrame"] = self.create_checkout_frame()
        self.container.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainFrame")

    def create_main_frame(self):
        """
        This function creates the main frame containing the menu and the cart.

        Returns:
            Frame: Returns the main frame.
        """
        # Set row where menu items start to build, to aviod laying on top of title.
        item_start_row = 1
        item_start_col = 0

        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        # This block of code make the scroll bar
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
            font=self.title_font,
        )
        self.title.grid(
            row=0,
            column=0,
            columnspan=2,
        )
        # For loop to creat menu items based on all items in the food_items dict.
        for i in self.food_items:
            price, img = self.food_items[i]
            food_frame = Frame(
                self.content_frame,
                bd=2,
                relief=RAISED,
                padx=10,
                pady=10,
            )
            food_frame.grid(
                row=item_start_row,
                column=item_start_col,
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
            self.food_frame_price = Label(food_frame, text=f"${price}")
            self.food_frame_price.grid(row=2, column=0)
            self.food_frame = Button(
                food_frame,
                text="Add to cart",
                command=lambda name=i: self.add_to_cart(name),
            )
            self.food_frame.grid(row=3, column=0)

            if item_start_col == 0:
                item_start_col = 1
            else:
                item_start_col = 0
                item_start_row += 1

        # This block of code makes the cart the displays in main frame.
        self.cart_frame = Frame(self.content_frame, bd=2, relief=RAISED)
        self.cart_frame.grid(
            row=1,
            column=2,
            rowspan=3,
        )
        self.cart_frame_label = Label(
            self.cart_frame, text="cart", font=self.cart_title_font
        )
        self.cart_frame_label.grid(row=0, column=0)
        self.cart_frame_listbox = Listbox(self.cart_frame, font=self.cart_items_font)
        self.cart_frame_listbox.grid(row=1, column=0, ipadx=50, ipady=100)
        self.qty_note = Label(
            self.cart_frame,
            text="Note that quantity is changed in checkout.",
            font=self.cart_items_font,
        )
        self.qty_note.grid(row=2, column=0, ipady=10)

        self.checkout_button = Button(
            self.cart_frame,
            bg="red",
            text="Checkout",
            width=25,
            command=lambda: self.show_frame("CheckoutFrame"),
        )

        self.checkout_button.grid(
            row=3,
            column=0,
            ipadx=10,
            ipady=10,
        )

        return frame

    def create_checkout_frame(self):
        """
        This function create the checkout frame which is accessed when pressing checkout in main frame.

        Returns:
            Frame: Returns the checkout frame.
        """
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

        Label(frame, text="CHECKOUT", font=self.title_font).grid(
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
        self.checkout_items_frame = Frame(panel)
        self.checkout_items_frame.grid(
            row=0,
            column=0,
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

    def render_checkout(self):
        """
        This funtion creates all items the user has selected in the checkout frame, as well as the price of each item and a total price.
        users are also able to change the quanty of each item from the spinbox generated here.
        """

        row = 1
        total = 0.0
        self.qty_vars.clear()
        # First I cleared all previous widget to update all item user has properly .
        for widget in self.checkout_items_frame.winfo_children():
            widget.destroy()
        # Thid if,else statement checks if there is anything in cart. If there isnt anything, then it will tell the user in the checkout frame that there isnt anyting in cart.
        if not self.cart_counts:
            empty_checkout = Label(
                self.checkout_items_frame,
                text="Your cart is empty.",
                font=self.subtitle_font,
                fg="red",
            )
            empty_checkout.grid(row=0, column=0, padx=20, pady=20)
        else:
            # Makes the titles of each column.
            self.checkout_item_label = Label(
                self.checkout_items_frame,
                text="Item",
                font=self.subtitle_font,
            )
            self.checkout_item_label.grid(
                row=0,
                column=1,
                padx=20,
                pady=10,
            )
            self.qty_label = Label(
                self.checkout_items_frame,
                text="Qty",
                font=self.subtitle_font,
            )
            self.qty_label.grid(
                row=0,
                column=2,
                padx=20,
                pady=10,
            )
            self.price_label = Label(
                self.checkout_items_frame, text="Price", font=self.subtitle_font
            )
            self.price_label.grid(
                row=0,
                column=3,
                padx=20,
                pady=10,
            )
            self.item_total_label = Label(
                self.checkout_items_frame, text="Item Total", font=self.subtitle_font
            )
            self.item_total_label.grid(
                row=0,
                column=4,
                padx=20,
                pady=10,
            )
            # Prices each item and qty user has selected.
            for name in self.cart_counts:
                qty = self.cart_counts[name]
                price = self.food_items[name][0]
                subtotal = price * qty
                total += subtotal

                slot = Frame(self.checkout_items_frame)
                slot.grid(row=row, column=1, padx=8)

                remove_button = Button(
                    self.checkout_items_frame,
                    text="X",
                    font=self.checkout_item_font,
                    command=lambda n=name: self.remove_item(n),
                )
                remove_button.grid(
                    row=row,
                    column=0,
                    padx=8,
                    ipadx=6,
                    ipady=3,
                )

                self.slot_name = Label(slot, text=name, font=self.checkout_item_font)
                self.slot_name.grid(row=row, column=1)

                value = StringVar(value=qty)
                self.qty_vars[name] = value
                spinbox = Spinbox(
                    self.checkout_items_frame,
                    from_=self.MIN_QTY,
                    to=self.MAX_QTY,
                    width=4,
                    textvariable=value,
                    font=self.checkout_item_font,
                )
                # Calles qty function if number in spinbox is changed.
                spinbox.config(command=lambda n=name: self.qty_change(n))
                spinbox.bind("<Return>", lambda e, n=name: self.qty_change(n))
                spinbox.grid(
                    row=row,
                    column=2,
                    padx=8,
                    ipadx=20,
                    ipady=5,
                )
                price = Label(
                    self.checkout_items_frame,
                    text=f"${price:.2f}",
                    font=self.checkout_item_font,
                )
                price.grid(row=row, column=3, padx=8)
                subtotal = Label(
                    self.checkout_items_frame,
                    text=f"${subtotal:.2f}",
                    font=self.checkout_item_font,
                )
                subtotal.grid(row=row, column=4, padx=8)
                row += 1
            total = Label(
                self.checkout_items_frame, text=f"${total:.2f}", font=self.subtitle_font
            )
            total.grid(row=row, column=5)

    def add_to_cart(self, item_name):
        """
        Inserts items that are not duplicated to the listbox.

        Args:
            item_name (String): The name of the selected/given item name to add to the listbox.
        """
        if item_name not in self.cart_counts:
            self.cart_counts[item_name] = 1
            self.cart_frame_listbox.insert("end", item_name)

    def show_frame(self, name):
        """
        Raises different frames to the top and when checkout frame is raised it will call render checkout function.

        Args:
            name (String): The name of the frame.
        """
        frame = self.frames[name]
        frame.tkraise()
        if name == "CheckoutFrame":
            self.render_checkout()

    def qty_change(self, name):
        """
        This function changes the number of item selected in the spinbox of checkout frames and saves to cart_counts. As well asm vaildating input in spinbox.

        Args:
            name (String): Name of the items
        """
        try:
            new_qty = int(self.qty_vars[name].get())
        except ValueError:
            new_qty = 1
        new_qty = max(self.MIN_QTY, min(self.MAX_QTY, new_qty))
        self.cart_counts[name] = new_qty
        self.render_checkout()

    def remove_item(self, name):
        """
        This function removes item from the lsitbox. This was done by removing unwanted item in cart_counts dict. Then removing everthing in listbox and then add to listbox based on cart_counts dict.

        Args:
            name (String): Name of the item wanted to be deleted.
        """
        if name in self.cart_counts:
            del self.cart_counts[name]
        self.cart_frame_listbox.delete(0, END)
        for i in self.cart_counts.keys():
            self.cart_frame_listbox.insert(END, i)
        self.render_checkout()

    def run(self):
        self.root.mainloop()


# runs the whole programme
if __name__ == "__main__":
    app = MainScreen()
    app.run()
