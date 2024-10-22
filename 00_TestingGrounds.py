import csv
import random
from tkinter import *


class ChooseRounds:
    def __init__(self, master):
        self.master = master  # Set master to the Tk instance
        self.intro_frame = Frame(self.master, padx=10, pady=10)
        self.intro_frame.grid()

        # Initialize user score and rounds played
        self.user_score = 0
        self.rounds_played = 0

        # Define user choice label and round results label
        self.user_choice_label = Label(self.intro_frame, text="")
        self.user_choice_label.grid(row=3)  # Adjust row as necessary

        self.round_results_label = Label(self.intro_frame, text="")
        self.round_results_label.grid(row=4)  # Adjust row as necessary

        # Load all data from the CSV file
        self.all_data = self.get_all_data()

        # Main GUI and instructions
        self.intro_heading_label = Label(self.intro_frame, text="Greek God Questionnaire",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = ("In each round you will be given 2 Different options "
                                   "of Greek Gods to choose. Pick a god and see if you "
                                   "are correct!\n\n"
                                   "To begin, choose how many rounds you wish to "
                                   "play...")
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

        # Initialize the correct answer and god name
        self.correct_answer = ""
        self.god_name = ""

    def get_all_data(self):
        with open("gods.csv", "r") as file:
            var_all_data = list(csv.reader(file, delimiter=","))
        var_all_data.pop(0)  # Remove the header row from the data.
        return var_all_data

    def to_play(self, num_rounds):
        if num_rounds == 0:
            self.open_play_rounds_dialog()
        else:
            self.intro_frame.grid_forget()
            self.open_help_window()

    def check_answer(self, user_answer):
        if user_answer.lower() == self.correct_answer.lower():
            self.user_score += 1
            self.user_choice_label.config(text="Great work! \n"
                                               f"You've got it correct! \n"
                                               f"{self.god_name} is {self.correct_answer}.")
        else:
            self.user_choice_label.config(text="Unfortunate! \n"
                                               "That answer is not correct! "
                                               f"{self.god_name} is {self.correct_answer}.")

        self.round_results_label.config(
            text=f"Round {self.rounds_played + 1}: Current score: {self.user_score}"
        )

    def open_play_rounds_dialog(self):
        self.Play_rounds_window = Toplevel(self.master)
        self.Play_rounds_window.title("God Questionnaire")

        # Instructions
        Label(self.Play_rounds_window, text="Enter the number of rounds you wish to play").pack(pady=10)

        # Choose number of rounds
        self.rounds_entry = Entry(self.Play_rounds_window, width=10)
        self.rounds_entry.pack(pady=5)
        self.rounds_entry.focus()

        # Produce Error label
        self.error_label = Label(self.Play_rounds_window, text="", fg="red")
        self.error_label.pack(pady=5)

        # OK button
        Button(self.Play_rounds_window, text="OK", command=self.confirm_play_rounds).pack(pady=10)

    def confirm_play_rounds(self):
        try:
            num_rounds = int(self.rounds_entry.get())
            if 1 <= num_rounds <= 99:
                self.Play_rounds_window.destroy()
                self.intro_frame.grid_forget()
                self.Play(num_rounds, self)  # Pass self to Play
            else:
                self.show_error("Please enter a number between 1 and 99.")
        except ValueError:
            self.show_error("Please enter a valid number.")

    def show_error(self, message):
        self.error_label.config(text=message)

    def open_help_window(self):
        help_window = Toplevel(self.master)
        help_window.title("Help")

        help_text = (
            "This is a Questionnaire about Greek Gods.\n\n"
            "In this Questionnaire, you will be answering"
            "a selection of questions. \n\n"
            "Depending on your choices, this will affect"
            "the outcome. To play, you will \n\n"
            "answer the questions presented to you.\n\n"
            "Answering these correctly will contribute to"
            "your final result. Choose carefully..."
        )

        Label(help_window, text=help_text, padx=20, pady=20, justify=LEFT).pack()
        Button(help_window, text="OK", command=help_window.destroy).pack(pady=10)

    class Play:
        def __init__(self, how_many, main_instance):
            self.main_instance = main_instance  # Store the main instance of ChooseRounds
            self.how_many = how_many
            self.current_round = 0

            self.play_box = Toplevel(self.main_instance.master)
            self.play_box.title("God Questionnaire")

            self.quest_frame = Frame(self.play_box, padx=10, pady=10)
            self.quest_frame.grid()
            self.control_frame = Frame(self.quest_frame)
            self.control_frame.grid(row=6)

            self.start_over_button = Button(self.control_frame, text="Start Over",
                                            command=self.start_over)
            self.start_over_button.grid(row=0, column=0, padx=5, pady=5)
            self.exit_button = Button(self.control_frame, text="Back to Main Menu",
                                      command=self.return_to_main)
            self.exit_button.grid(row=0, column=1, padx=5, pady=5)

            self.display_next_round()

        def display_next_round(self):
            if self.current_round < self.how_many:
                Label(self.quest_frame, text=f"Round {self.current_round + 1}").grid(row=0)
                self.user_answer_entry = Entry(self.quest_frame)  # Entry for user answer
                self.user_answer_entry.grid(row=1)
                Button(self.quest_frame, text="Submit", command=self.submit_answer).grid(row=2)
            else:
                self.finish_game()

        def submit_answer(self):
            user_answer = self.user_answer_entry.get()
            # Use the main instance to check the answer
            self.main_instance.check_answer(user_answer)
            self.current_round += 1  # Move to the next round
            self.display_next_round()  # Refresh the display for the next round

            # Select a random question for the new round.
            current_question = random.choice(self.main_instance.all_data)
            self.main_instance.all_data.remove(current_question)

            # Set the question details.
            self.main_instance.god_name = current_question[2]
            self.main_instance.correct_answer = current_question[0]

        def finish_game(self):
            Label(self.quest_frame, text="You've completed all rounds!").grid(row=0)
            Button(self.quest_frame, text="Finish", command=self.return_to_main).grid(row=1)

        def start_over(self):
            self.play_box.destroy()
            self.main_instance.master.destroy()
            root = Tk()
            root.title("God Questionnaire")
            ChooseRounds(root)
            root.mainloop()

        def return_to_main(self):
            self.play_box.destroy()
            self.main_instance.master.deiconify()



if __name__ == "__main__":
    root = Tk()
    root.title("God Questionnaire")
    ChooseRounds(root)  # Pass the root to ChooseRounds
    root.mainloop()
