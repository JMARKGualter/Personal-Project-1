import tkinter as tk
from tkinter import messagebox
from database import create_database, add_user, authenticate_user
import terms  # Import terms.py to handle terms and conditions

# Create the database
create_database()

def fade_out(window, alpha=1.0):
    if alpha > 0:
        alpha -= 0.05  # Decrease alpha value
        window.attributes('-alpha', alpha)  # Set new alpha value
        window.after(50, fade_out, window, alpha)  # Call fade_out again after 50 ms
    else:
        window.destroy()  # Close the window when fully transparent

def login():
    username = username_entry.get()
    password = password_entry.get()

    if authenticate_user(username, password):
        root.withdraw()  # Hide the login window
        terms.create_terms_window(root)  # Show terms and conditions window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def login_as_guest():
    root.withdraw()
    terms.create_terms_window(root)

def sign_up():
    # Function to save the user
    def save_user():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showwarning("Sign Up Failed", "Please enter both username and password.")
            return

        if add_user(username, password):
            messagebox.showinfo("Sign Up Success", "Account created successfully!")
            fade_out(signup_window)  # Call fade_out instead of destroying directly
            root.deiconify()  # Show the login window again
        else:
            messagebox.showerror("Sign Up Failed", "Username already exists.")

    # Create the sign-up window
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("300x400")
    signup_window.configure(bg="black")

    # Remove title bar and buttons
    signup_window.overrideredirect(True)  
    # Center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - 300 / 2)
    center_y = int(screen_height / 2 - 400 / 2)
    signup_window.geometry(f"+{center_x}+{center_y}")

    # Make the window transparent
    signup_window.attributes('-alpha', 0.9)  # Set transparency level (0.0 to 1.0)

    # Happy face label
    happy_face_label = tk.Label(signup_window, text="😊", font=("Arial", 50), bg="black", fg="white")
    happy_face_label.pack(pady=10)

    # Username input
    tk.Label(signup_window, text="Username", bg="black", fg="white", font=("Arial", 12)).pack(pady=5)
    username_entry = tk.Entry(signup_window, bg="#333", fg="white", font=("Arial", 12), insertbackground="white")
    username_entry.pack(pady=5)

    # Password input
    tk.Label(signup_window, text="Password", bg="black", fg="white", font=("Arial", 12)).pack(pady=5)
    password_entry = tk.Entry(signup_window, show="*", bg="#333", fg="white", font=("Arial", 12), insertbackground="white")
    password_entry.pack(pady=5)

    # Buttons
    button_frame = tk.Frame(signup_window, bg="black")
    button_frame.pack(pady=20)

    # Sign-Up button
    tk.Button(button_frame, text="Sign Up", command=save_user, font=("Arial", 12, "bold"), bg="#4a90e2", fg="white").pack(side=tk.LEFT, padx=10)

    # Go Back button
    tk.Button(button_frame, text="Go Back", command=lambda: [fade_out(signup_window), root.deiconify()], font=("Arial", 12, "bold"), bg="#4a90e2", fg="white").pack(side=tk.LEFT, padx=10)
    
    # Mouse drag functionality
    def move_window(event):
        x = event.x_root - signup_window.winfo_width() // 2
        y = event.y_root - signup_window.winfo_height() // 2
        signup_window.geometry(f"+{x}+{y}")

    signup_window.bind("<B1-Motion >", move_window)

# Main window (Login)
root = tk.Tk()
root.title("CHILL ANALYST")
root.geometry("600x750")
root.configure(bg="#1a1a1a")

# Center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - 600 / 2)
center_y = int(screen_height / 2 - 750 / 2)
root.geometry(f"600x750+{center_x}+{center_y}")

# Make the window transparent
root.attributes('-alpha', 0.9)  # Set transparency level (0.0 to 1.0)

# Create a frame for the login content
content_frame = tk.Frame(root, bg="#1a1a1a", bd=10)
content_frame.pack(padx=20, pady=20)

# Welcome text
welcome_label = tk.Label(content_frame, text="Welcome to CHILL ANALYST", font=("Times New Roman", 30, "bold"), bg="#1a1a1a", fg="white")
welcome_label.pack(pady=10)

# Avatar
avatar_frame = tk.Frame(content_frame, bg="#1a1a1a")
avatar_frame.pack(pady=10)

# Load the image (ensure the path is correct)
image_path = r"C:images/chillguy.png"
avatar_image = tk.PhotoImage(file=image_path)
avatar_label = tk.Label(avatar_frame, image=avatar_image, bg="#1a1a1a")
avatar_label.pack()

# Input fields
username_label = tk.Label(content_frame, text="Username", font=("Arial", 12), bg="#1a1a1a", fg="white")
username_label.pack(pady=5)
username_entry = tk.Entry(content_frame, font=("Arial", 12), bg="#333", fg="white", insertbackground="white", width=30)
username_entry.pack(pady=5)

password_label = tk.Label(content_frame, text="Password", font=("Arial", 12), bg="#1a1a1a", fg="white")
password_label.pack(pady=5)
password_entry = tk.Entry(content_frame, show="*", font=("Arial", 12), bg="#333", fg="white", insertbackground="white", width=30)
password_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(content_frame, bg="#1a1a1a")
button_frame.pack(pady=20)

login_button = tk.Button(button_frame, text="Login", font=("Calibri", 12, "bold"), bg="#4a90e2", fg="white", command=login)
login_button.grid(row=0, column=0, padx=10)

signup_button = tk.Button(button_frame, text="Sign Up", font=("Calibri", 12, "bold"), bg="#4a90e2", fg="white", command=sign_up)
signup_button.grid(row=0, column=1, padx=10)

login_as_guest_button = tk.Button(button_frame, text="Login as Guest", command=login_as_guest, font=("Calibri", 12, "bold"), bg="#4a90e2", fg="white")
login_as_guest_button.grid(row=0, column=2, padx=10)

root.mainloop()