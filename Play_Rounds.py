from tkinter import *


class ChooseRounds:
    def __init__(self, master):
        self.master = master
        self.intro_frame = Frame(master, padx=10, pady=10)
        self.intro_frame.grid()

        # Main GUI and instructions
        self.intro_heading_label = Label(self.intro_frame, text="Greek God Questionnaire",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = "In each round you will be given 4 Different options " \
                                  "of Greek Gods to choose. Pick A god and see if you" \
                                  "are correct!\n\n" \
                                  "To begin choose how many rounds you wish to " \
                                  "play..."
        self.choose_instructions_label = Label(self.intro_frame,
                                               text=choose_instructions_txt,
                                               wraplength=300, justify="left")
        self.choose_instructions_label.grid(row=1)

        # Button for rounds to work
        self.how_many_frame = Frame(self.intro_frame)
        self.how_many_frame.grid(row=2)

        button_back = ["#6C9484", "#E4A484"]

        self.rounds_button = []
        for item in range(2):
            button_text = "Play" if item == 0 else "Help"
            btn = Button(self.how_many_frame,
                         fg="#FFF", bg=button_back[item],
                         text=button_text,
                         font=("Arial", "13", "bold"), width=10,
                         command=lambda i=item: self.to_play(i))
            btn.grid(row=0, column=item, padx=5, pady=5)
            self.rounds_button.append(btn)

    def to_play(self, num_rounds):
        if num_rounds == 0:
            self.open_play_rounds_dialog()
        else:
            # remove original frame and open new window
            self.intro_frame.grid_forget()
            self.open_help_window()

    def open_play_rounds_dialog(self):
        self.Play_rounds_window = Toplevel(self.master)
        self.Play_rounds_window.title("God Questionnaire")

        # Instructions
        Label(self.Play_rounds_window, text="Enter the number of rounds you wish to play").pack(pady=10)

        # choose number of rounds
        self.rounds_entry = Entry(self.Play_rounds_window, width=10)
        self.rounds_entry.pack(pady=5)
        self.rounds_entry.focus()

        # Produce Error label
        self.error_label = Label(self.Play_rounds_window, text="", fg="red")
        self.error_label.pack(pady=5)

        # Ok button
        Button(self.Play_rounds_window, text="OK", command=self.confirm_play_rounds).pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    root.title("God Questionnaire")
    ChooseRounds(root)
    root.mainloop()
