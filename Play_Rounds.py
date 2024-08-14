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
        self.intro_heading_label = Label(self.intro_frame, text="Colour Quest",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = "In each round you will be given six different " \
                                  "colours to choose from.  Pick a colour and see if " \
                                  "you can beat the computer's score!\n\n" \
                                  "To begin, choose how many rounds you'd like to " \
                                  "play..."
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
                                        command=lambda i=item: self.to_play(i)
                                        )
            self.rounds_button.grid(row=0, column=item - 1,
                                    padx=5, pady=5)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # Hide root window (ie: hide rounds choice window).
        root.withdraw()


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        print("You Chose {} rounds".format(how_many))

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        self.start_over_button = Button(self.control_frame, text="Start Over",
                                        command=self.close_play)
        self.start_over_button.grid(row=0, column=2)

    def close_play(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()
