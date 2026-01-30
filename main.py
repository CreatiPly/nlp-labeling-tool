# GUI basics practice

from tkinter import *

nlp_text_labeling_tool = Tk()
nlp_text_labeling_tool.geometry("1280x720")
nlp_text_labeling_tool.title("NLP Text Labeling Tool by Haseeb Khan 539657")
nlp_text_labeling_tool.configure(background="#2d2d2d")

nlp_text_labeling_tool.columnconfigure(0, weight=1)
nlp_text_labeling_tool.columnconfigure(1, weight=3)
nlp_text_labeling_tool.columnconfigure(2, weight=2)

nlp_text_labeling_tool.rowconfigure(0, weight=1)
nlp_text_labeling_tool.rowconfigure(1, weight=1)

# LEFT SIDE BAR

frame_left = LabelFrame(
    nlp_text_labeling_tool,
    text="  Files   ",
    fg="#ffffff",
    background="#2d2d2d",
    padx=10,
    pady=10,
)
frame_left.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=5, pady=5)

frame_left.columnconfigure(0, weight=1)
frame_left.rowconfigure(0, weight=1)
frame_left.rowconfigure(1, weight=0)

select_file = Button(frame_left, text="Select File")
select_file.grid(row=1, column=0, sticky="ew")

# MIDDLE SECTION

frame_mid = LabelFrame(
    nlp_text_labeling_tool,
    text="  Text Display  ",
    fg="#ffffff",
    background="#2d2d2d",
    padx=10,
    pady=10,
)
frame_mid.grid(row=0, column=1, sticky="nsew", rowspan=2, padx=5, pady=5)

frame_mid.columnconfigure(0, weight=1)
frame_mid.rowconfigure(0, weight=1)
frame_mid.rowconfigure(1, weight=0)

button_frame = Frame(frame_mid, background="#2d2d2d")
button_frame.grid(row=1, column=0, sticky="ew")

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

add_label = Button(button_frame, text="Add Label")
add_label.grid(row=0, column=0, sticky="ew", padx=5)
edit_label = Button(button_frame, text="Edit Label")
edit_label.grid(row=0, column=1, sticky="ew", padx=5)
delete_label = Button(button_frame, text="Delete Label")
delete_label.grid(row=0, column=2, sticky="ew", padx=5)

# RIGHT SIDE BAR : UP

frame_right_up = LabelFrame(
    nlp_text_labeling_tool,
    text="  Annotations  ",
    fg="#ffffff",
    background="#2d2d2d",
    padx=10,
    pady=10,
)
frame_right_up.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

# RIGHT SIDE BAR : DOWN

frame_right_down = LabelFrame(
    nlp_text_labeling_tool,
    text="  Stats  ",
    fg="#ffffff",
    background="#2d2d2d",
    padx=10,
    pady=10,
)
frame_right_down.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

frame_right_down.columnconfigure(0, weight=1)
frame_right_down.rowconfigure(0, weight=1)
frame_right_down.rowconfigure(1, weight=0)


save_labels = Button(frame_right_down, text="Save Labels")
save_labels.grid(row=1, column=0, sticky="ew")

nlp_text_labeling_tool.mainloop()
