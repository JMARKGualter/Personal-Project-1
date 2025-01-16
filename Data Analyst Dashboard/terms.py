import tkinter as tk
from tkinter import messagebox
import subprocess


def create_terms_window(root):
    #DISPLAY TERMS AND CONDITION

    terms_text = """By using my Data Visualization app, you agree to the following terms and conditions. 
        The app is designed to help data analysts and professionals visualize data, explore relationships, 
        and dive deeper into machine learning and big data analysis. As a user, you acknowledge that the app is 
        for educational and analytical purposes only and should not be used to facilitate unlawful activities, 
        including but not limited to cybercrimes, fraud, or any malicious acts. The app should not be used in a manner 
        that violates any applicable laws or regulations.

        Users are encouraged to share feedback to improve the app's functionality, but all feedback and suggestions 
        must be appropriate and respectful. Any form of harassment, offensive language, or illegal activity related to 
        the app will result in immediate action. Additionally, users must not share or post any content from the app 
        in public forums, blogs, or on social media unless they have obtained explicit permission from the owner. Any misuse 
        of the app for the purpose of spreading inappropriate content or violating privacy rights will result in suspension 
        of access and potential legal action.

        I also takes the issue of plagiarism seriously. If any instances of plagiarism are detected, the owner ensures 
        that such content will not be made public or published in any form. The responsibility for ensuring the originality 
        and authenticity of any analysis, research, or work produced using the app lies with the user. By using the app, you 
        agree to adhere to these guidelines and understand that any violation may lead to the suspension of access and further 
        legal actions."""

    # Create a new top-level window for terms
    terms_window = tk.Toplevel(root)
    terms_window.title("Terms and Conditions")
    terms_window.geometry("400x600")  # Default dimensions of the terms window
    terms_window.configure(bg="black")

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the terms window
    window_width = 400  # Desired width of the terms window
    window_height = 600  # Desired height of the terms window
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # Apply the geometry to the terms window
    terms_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    terms_window.attributes('-alpha', 0.9)  # Set transparency level (0.0 to 1.0)

    # Create a scrollbar for the terms text area
    scrollbar = tk.Scrollbar(terms_window)
    scrollbar.pack(side="right", fill="y")

    # Create a text widget to display the terms and conditions
    text_widget = tk.Text(terms_window, wrap="word", height=30, width=50, bg="#333", fg="white", font=("Calibri", 10))
    text_widget.insert("1.0", terms_text)
    text_widget.config(state="disabled")  # Make the text widget read-only
    text_widget.pack(pady=10, padx=10)

    scrollbar.config(command=text_widget.yview)

    # Checkbox for user to agree to terms
    agree_var = tk.BooleanVar()
    agree_checkbox = tk.Checkbutton(terms_window, text="I accept the Terms and Conditions", variable=agree_var,
                                    bg="black", fg="green", font=("Arial", 12), anchor="w")
    agree_checkbox.pack(pady=10)

    # Function to handle when the user clicks the "Accept" button
    def accept_terms():
        if agree_var.get():
            messagebox.showinfo("Accepted", "You have accepted the terms and conditions.")
            terms_window.destroy()  # Close the terms window
            run_main_app()  # Call the function to run main.py after terms are accepted
        else:
            messagebox.showwarning("Terms Not Accepted", "You must accept the terms and conditions to proceed.")

    # Accept button
    accept_button = tk.Button(terms_window, text="Accept", command=accept_terms, font=("Arial", 12, "bold"),
                              bg="#4a90e2", fg="white")
    accept_button.pack(pady=20)

    # Make the terms window modal (grab the input focus)
    terms_window.grab_set()
    terms_window.transient()  # This keeps the terms window above the main window
    terms_window.wait_window()  # Wait until the terms window is closed before continuing


def run_main_app():
    subprocess.Popen(["python", "main.py"])
