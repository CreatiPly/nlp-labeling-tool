# GUI basics practice

from tkinter import *
from tkinter import filedialog
import os


class nlp_text_labeling_tool(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.minsize(960, 540)
        self.title("NLP Text Labeling Tool by Haseeb Khan 539657")
        self.configure(background="#2d2d2d")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.left_side_bar()
        self.middle_section()
        self.right_side_bar_up()
        self.right_side_bar_down()

    def left_side_bar(self):
        self.frame_left = LabelFrame(
            self,
            text="  Files   ",
            fg="#ffffff",
            background="#2d2d2d",
            padx=10,
            pady=10,
        )
        self.frame_left.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=5, pady=5)
        self.frame_left.columnconfigure(0, weight=1)
        self.frame_left.rowconfigure(0, weight=1)
        self.frame_left.rowconfigure(1, weight=0)

        self.file_selector = Listbox(
            self.frame_left,
            background="#2d2d2d",
            foreground="white",
            font=("Consolas", 12),
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        self.file_selector.grid(row=0, column=0, sticky="nsew", pady=(0, 10))

        self.select_folder_button = Button(
            self.frame_left, text="Select Folder", command=self.select_folder
        )
        self.select_folder_button.grid(row=1, column=0, sticky="ew")

    def middle_section(self):
        # MIDDLE SECTION

        self.frame_mid = LabelFrame(
            self,
            text="  Text Display  ",
            fg="#ffffff",
            background="#2d2d2d",
            padx=10,
            pady=10,
        )
        self.frame_mid.grid(row=0, column=1, sticky="nsew", rowspan=2, padx=5, pady=5)

        self.frame_mid.columnconfigure(0, weight=1)
        self.frame_mid.rowconfigure(0, weight=1)
        self.frame_mid.rowconfigure(1, weight=0)

        self.button_frame = Frame(self.frame_mid, background="#2d2d2d")
        self.button_frame.grid(row=1, column=0, sticky="ew")

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)

        self.add_label = Button(self.button_frame, text="Add Label")
        self.add_label.grid(row=0, column=0, sticky="ew", padx=5)
        self.edit_label = Button(self.button_frame, text="Edit Label")
        self.edit_label.grid(row=0, column=1, sticky="ew", padx=5)
        self.delete_label = Button(self.button_frame, text="Delete Label")
        self.delete_label.grid(row=0, column=2, sticky="ew", padx=5)

    def right_side_bar_up(self):
        # RIGHT SIDE BAR : UP

        self.frame_right_up = LabelFrame(
            self,
            text="  Annotations  ",
            fg="#ffffff",
            background="#2d2d2d",
            padx=10,
            pady=10,
        )

        self.frame_right_up.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

    def right_side_bar_down(self):
        # RIGHT SIDE BAR : down

        self.frame_right_down = LabelFrame(
            self,
            text="  Stats  ",
            fg="#ffffff",
            background="#2d2d2d",
            padx=10,
            pady=10,
        )

        self.frame_right_down.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.frame_right_down.columnconfigure(0, weight=1)
        self.frame_right_down.rowconfigure(0, weight=1)
        self.frame_right_down.rowconfigure(1, weight=0)

        self.save_labels = Button(self.frame_right_down, text="Save Labels")
        self.save_labels.grid(row=1, column=0, sticky="ew")

    def select_folder(self):
        selected_folder_path = filedialog.askdirectory()
        if selected_folder_path:
            self.file_selector.delete(0, END)
            os.listdir(selected_folder_path)
            for file_name in os.listdir(selected_folder_path):
                if file_name.endswith(".txt"):
                    self.file_selector.insert(END, file_name)


if __name__ == "__main__":
    app = nlp_text_labeling_tool()
    app.mainloop()
