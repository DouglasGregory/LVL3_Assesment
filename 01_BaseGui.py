from tkinter import *

class ChooseRounds:
    def __init__(self, master):
        self.master = master
        self.intro_frame = Frame(master, padx=10, pady=10)
        self.intro_frame.grid()

        # Heading and brief instructions
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

        # Rounds buttons...
        self.how_many_frame = Frame(self.intro_frame)
        self.how_many_frame.grid(row=2)

        button_back = ["#6C9484", "#E4A484"]

        for item in range(1, 3):
            if item == 1:
                button_text = "Play"
            elif item == 2:
                button_text = "Help"

            self.rounds_button = Button(self.how_many_frame,
                                        fg="#FFF", bg=button_back[item - 1],
                                        text=button_text,
                                        font=("Arial", "13", "bold"), width=10,
                                        command=lambda i=item: self.to_play(i))
            self.rounds_button.grid(row=0, column=item - 1,
                                    padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()
    root.title("God Questionnaire")  # Updated main window title
    ChooseRounds(root)  # Start with the God Questionnaire GUI
    root.mainloop()
