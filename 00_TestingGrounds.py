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

    def to_play(self, num_rounds):
        if num_rounds == 3:  # Custom button pressed
            self.open_custom_rounds_dialog()
        else:
            # Hide current frame and open the Play window with predefined rounds
            self.intro_frame.grid_forget()
            Play(num_rounds, self.master)

    def open_custom_rounds_dialog(self):
        self.custom_rounds_window = Toplevel(self.master)
        self.custom_rounds_window.title("Enter Custom Rounds")

        Label(self.custom_rounds_window, text="Enter number of rounds (1-99):").pack(pady=10)

        self.rounds_entry = Entry(self.custom_rounds_window, width=10)
        self.rounds_entry.pack(pady=5)
        self.rounds_entry.focus()

        Button(self.custom_rounds_window, text="OK", command=self.confirm_custom_rounds).pack(pady=10)

    def confirm_custom_rounds(self):
        try:
            num_rounds = int(self.rounds_entry.get())
            if 1 <= num_rounds <= 99:
                self.custom_rounds_window.destroy()
                self.intro_frame.grid_forget()
                Play(num_rounds, self.master)
            else:
                self.show_error("Please enter a number between 1 and 99.")
        except ValueError:
            self.show_error("Please enter a valid number.")

    def show_error(self, message):
        error_window = Toplevel(self.master)
        error_window.title("Error")
        Label(error_window, text=message, padx=20, pady=20).pack()
        Button(error_window, text="OK", command=error_window.destroy).pack(pady=10)

class Play:
    def __init__(self, how_many, master):
        self.master = master
        self.play_box = Toplevel(master)
        self.play_box.title("God Questionnaire")  # Updated window title

        print("You Chose {} rounds".format(how_many))

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        self.start_over_button = Button(self.control_frame, text="Start Over",
                                        command=self.start_over)
        self.start_over_button.grid(row=0, column=2)

        self.exit_button = Button(self.control_frame, text="Back to Main Menu",
                                  command=self.return_to_main)
        self.exit_button.grid(row=0, column=3)

    def start_over(self):
        self.play_box.destroy()
        ChooseRounds(self.master)

    def return_to_main(self):
        self.play_box.destroy()
        ChooseRounds(self.master)

if __name__ == "__main__":
    root = Tk()
    root.title("God Questionnaire")  # Updated main window title
    ChooseRounds(root)  # Start with the God Questionnaire GUI
    root.mainloop()
