from tkinter import *
from functools import partial  # To prevent unwanted windows


class ChooseRounds:

    def __init__(self):
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # heading and brief instructions
        self.intro_heading_label = Label(self.intro_frame, text="Gods Questionnaire ",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = "TXT GOES HERE"
        self.choose_instructions_label = Label(self.intro_frame,
                                               text=choose_instructions_txt,
                                               wraplength=300, justify="left")
        self.choose_instructions_label.grid(row=1)

        # Rounds buttons...
        self.how_many_frame = Frame(self.intro_frame)
        self.how_many_frame.grid(row=2)

        button_back = ["#CC0000", "#009900", "#000099"]

        for item in range(1, 4):
            self.rounds_button = Button(self.how_many_frame,
                                        fg=button_fg, bg=button_back[item - 1],
                                        text="{} Rounds".format(item),
                                        font=button_font, width=10,
                                        command=lambda: self.to_play(item)
                                        )
            self.rounds_button.grid(row=0, column=item - 1,
                                    padx=5, pady=5)

    def to_play(self, num_rounds):
        print("".format(num_rounds))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Gods Questionnaire ")
    ChooseRounds()
    root.mainloop()
