# GUI basics practice

from tkinter import *

nlp_text_labeling_tool = Tk()
nlp_text_labeling_tool.geometry("1200x600")
nlp_text_labeling_tool.title("NLP Text Labeling Tool by Haseeb Khan 539657")

nlp_text_labeling_tool.columnconfigure(0, weight=1)
nlp_text_labeling_tool.columnconfigure(1, weight=3)
nlp_text_labeling_tool.columnconfigure(2, weight=2)

nlp_text_labeling_tool.rowconfigure(0, weight=1)
nlp_text_labeling_tool.rowconfigure(1, weight=1)

#LEFT SIDE BAR

frame_left = Frame(nlp_text_labeling_tool, background="#2d2d2d", relief="groove", borderwidth=2)
frame_left.grid(row=0, column=0, rowspan=2, sticky="nsew")

frame_left.columnconfigure(0, weight=1)
frame_left.rowconfigure(0, weight=1)
frame_left.rowconfigure(1, weight=0)

select_file = Button(frame_left, text="Select File")
select_file.grid(row=1, column=0, sticky="ew", pady=10, padx=10)

# MIDDLE SECTION

frame_mid = Frame(nlp_text_labeling_tool, background="#2d2d2d")
frame_mid.grid(row=0, column=1, sticky="nsew", rowspan=2)

frame_mid.columnconfigure(0, weight=1)
frame_mid.rowconfigure(0, weight=1)
frame_mid.rowconfigure(1, weight=0)

button_frame = Frame(frame_mid,)
button_frame.grid(row=1, column=0, sticky="ew", pady=10, padx=10)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

add_label = Button(button_frame, text="Add Label")
add_label.grid(row=0, column=0, sticky="ew")
edit_label = Button(button_frame, text="Edit Label")
edit_label.grid(row=0, column=1, sticky="ew")
delete_label = Button(button_frame, text="Delete Label")
delete_label.grid(row=0, column=2, sticky="ew")

# RIGHT SIDE BAR : UP

frame_right_up = Frame(nlp_text_labeling_tool, background="#2d2d2d")
frame_right_up.grid(row=0, column=2, sticky="nsew")

# RIGHT SIDE BAR : DOWN

frame_right_down = Frame(nlp_text_labeling_tool, background="#2d2d2d")
frame_right_down.grid(row=1, column=2, sticky="nsew")

nlp_text_labeling_tool.mainloop()