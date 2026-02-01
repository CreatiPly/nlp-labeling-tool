# GUI basics practice

from tkinter import *
from tkinter import filedialog, simpledialog, colorchooser
import os
import json


class nlp_text_labeling_tool(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.minsize(960, 540)
        self.title("NLP Text Labeling Tool by Haseeb Khan 539657")
        self.configure(background="#2d2d2d")

        self.all_labels = []
        self.current_folder = ""
        self.current_file = ""

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

        self.file_selector.bind("<<ListboxSelect>>", self.display_selected_file)

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

        self.text_display_area = Text(
            self.frame_mid,
            width=40,
            height=10,
            background="#2d2d2d",
            foreground="white",
            font=("Consolas", 12),
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )

        self.text_display_area.grid(row=0, column=0, sticky="nsew", pady=(0, 10))

        self.button_frame = Frame(self.frame_mid, background="#2d2d2d")
        self.button_frame.grid(row=1, column=0, sticky="ew")

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)

        self.add_label_button = Button(
            self.button_frame, text="Add Label", command=self.add_label
        )
        self.add_label_button.grid(row=0, column=0, sticky="ew", padx=5)
        self.edit_label_button = Button(
            self.button_frame, text="Edit Label", command=self.edit_label
        )
        self.edit_label_button.grid(row=0, column=1, sticky="ew", padx=5)
        self.delete_label_button = Button(
            self.button_frame, text="Delete Label", command=self.delete_label
        )
        self.delete_label_button.grid(row=0, column=2, sticky="ew", padx=5)

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

        self.frame_right_up.columnconfigure(0, weight=1)
        self.frame_right_up.rowconfigure(0, weight=1)

        self.label_list = Listbox(
            self.frame_right_up,
            background="#2d2d2d",
            foreground="white",
            font=("Consolas", 12),
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        self.label_list.grid(row=0, column=0, sticky="nsew")

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

        self.stats_list = Listbox(
            self.frame_right_down,
            background="#2d2d2d",
            foreground="white",
            font=("Consolas", 12),
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        self.stats_list.grid(row=0, column=0, sticky="nsew")

        self.save_labels_button = Button(
            self.frame_right_down, text="Save Labels", command=self.save_labels
        )
        self.save_labels_button.grid(row=1, column=0, sticky="ew")

    def select_folder(self):
        selected_folder_path = filedialog.askdirectory()
        if selected_folder_path:
            self.current_folder = selected_folder_path
            self.file_selector.delete(0, END)
            for file_name in os.listdir(selected_folder_path):
                if file_name.endswith(".txt"):
                    self.file_selector.insert(END, file_name)

    def display_selected_file(self, event):
        selection = self.file_selector.curselection()
        if selection:
            self.all_labels = []
            self.label_list.delete(0, END)

            file_name = self.file_selector.get(selection[0])
            self.current_file = file_name
            full_path_to_file = os.path.join(self.current_folder, file_name)

            with open(full_path_to_file, "r", encoding="utf-8") as file:
                file_content = file.read()

            self.text_display_area.delete("1.0", END)
            self.text_display_area.insert("1.0", file_content)

            json_file_path = file_name.replace(".txt", ".json")
            full_json_path = os.path.join(self.current_folder, json_file_path)

            if os.path.exists(full_json_path):
                with open(full_json_path, "r", encoding="utf-8") as f:
                    saved_data = json.load(f)
                    self.all_labels = saved_data.get("labels", [])

                for item in self.all_labels:
                    name = item["label_name"]

                    start_index = f"1.0+{item['start_index']}c"
                    end_index = f"1.0+{item['end_index']}c"

                    label_id = f"{name}_{start_index}"
                    self.text_display_area.tag_add(label_id, start_index, end_index)
                    self.text_display_area.tag_config(
                        label_id, background=item["color"], foreground="black"
                    )

                    display_label = f"{name}: '{item['selected_text']}' ({item['start_index']} to {item['end_index']})"
                    self.label_list.insert(END, display_label)

                self.update_stats()

    def add_label(self):
        try:
            start = self.text_display_area.index("sel.first")
            end = self.text_display_area.index("sel.last")
            selected_text = self.text_display_area.get(start, end)

            char_start = len(self.text_display_area.get("1.0", start))
            char_end = char_start + len(selected_text)

            Label_name = simpledialog.askstring(
                "Input", "Enter label name:", parent=self
            )

            if Label_name:
                color = colorchooser.askcolor(title="Choose label color", parent=self)
                chosen_color = color[1] if color[1] else "#ffff00"

                start_index = f"1.0+{char_start}c"
                label_id = f"{Label_name.upper()}_{start_index}"
                self.text_display_area.tag_add(label_id, start, end)
                self.text_display_area.tag_config(
                    label_id, background=chosen_color, foreground="black"
                )

                label_data = {
                    "label_name": Label_name.upper(),
                    "start_index": char_start,
                    "end_index": char_end,
                    "selected_text": selected_text,
                    "color": chosen_color,
                }
                self.all_labels.append(label_data)

                display_label = f"{Label_name.upper()}: '{selected_text}' ({char_start} to {char_end})"
                self.label_list.insert(END, display_label)

                self.update_stats()
        except TclError:
            print("No text selected to label.")

    def save_labels(self):
        if not self.current_file or not self.current_folder:
            return

        json_file_path = self.current_file.replace(".txt", ".json")
        save_path = os.path.join(self.current_folder, json_file_path)

        output_data = {
            "text": self.text_display_area.get("1.0", "end-1c"),
            "labels": self.all_labels,
        }

        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=4)

        print(f"Labels saved to {save_path}")

    def update_stats(self):
        self.stats_list.delete(0, END)
        counts = {}
        for item in self.all_labels:
            name = item["label_name"]
            counts[name] = counts.get(name, 0) + 1

        for name, count in counts.items():
            self.stats_list.insert(END, f"{name}: {count}")

    def delete_label(self):
        selected = self.label_list.curselection()

        if not selected:
            return

        index = selected[0]
        label_to_delete = self.all_labels[index]

        start_index = f"1.0+{label_to_delete['start_index']}c"
        end_index = f"1.0+{label_to_delete['end_index']}c"
        label_id = f"{label_to_delete['label_name']}_{start_index}"

        self.text_display_area.tag_remove(label_id, start_index, end_index)

        self.all_labels.pop(index)
        self.label_list.delete(index)

        self.update_stats()

    def edit_label(self):
        selected = self.label_list.curselection()
        if not selected:
            return

        index = selected[0]
        label = self.all_labels[index]

        new_name = simpledialog.askstring(
            "Edit Label",
            "Enter new label name:",
            initialvalue=label["label_name"],
            parent=self,
        )
        if not new_name:
            return

        color = colorchooser.askcolor(
            title="Choose new color", color=label["color"], parent=self
        )
        new_color = color[1] if color[1] else label["color"]

        start_index = f"1.0+{label['start_index']}c"
        end_index = f"1.0+{label['end_index']}c"
        old_tag_id = f"{label['label_name']}_{start_index}"
        self.text_display_area.tag_remove(old_tag_id, start_index, end_index)

        new_tag_id = f"{new_name.upper()}_{start_index}"
        self.text_display_area.tag_add(new_tag_id, start_index, end_index)
        self.text_display_area.tag_config(
            new_tag_id, background=new_color, foreground="black"
        )

        label["label_name"] = new_name.upper()
        label["color"] = new_color

        self.label_list.delete(index)
        display_label = f"{label['label_name']}: '{label['selected_text']}' ({label['start_index']} to {label['end_index']})"
        self.label_list.insert(index, display_label)

        self.update_stats()


if __name__ == "__main__":
    app = nlp_text_labeling_tool()
    app.mainloop()
