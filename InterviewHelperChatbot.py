import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create GenerativeModel instance
model = genai.GenerativeModel('gemini-1.5-flash')


# Function to generate interview questions and answers
def generate_interview_qna(job_title):
    if not job_title:
        return "Please enter a valid job title."

    prompt = f"Generate technical interview questions with 2-3 line answers for a {job_title} position."
    response = model.generate_content(prompt)
    return response.text


# Function to handle 'Get Questions' button click
def get_questions():
    job_title = job_title_entry.get().strip()

    if job_title:
        result = generate_interview_qna(job_title)
        display_output(result)
    else:
        messagebox.showwarning("Input Error", "Please enter a job title.")


# Function to display the generated output in the chat window
def display_output(output):
    chat_window.config(state=tk.NORMAL)
    chat_window.delete(1.0, tk.END)  # Clear previous output
    chat_window.insert(tk.END, f"Technical Interview Questions:\n{output}\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)


# Create main window
root = tk.Tk()
root.title("Interview Helper Chatbot")
root.geometry("600x500")
root.config(bg="#e3f2fd")

# Title Label
title_label = tk.Label(root, text="Interview Helper", font=("Helvetica", 16, "bold"), bg="#2196f3", fg="white", pady=10)
title_label.pack(fill=tk.X)

# Instruction Label
instruction_label = tk.Label(root, text="Enter a job title to get technical interview questions with brief answers.",
                             font=("Arial", 12), bg="#e3f2fd")
instruction_label.pack(pady=10)

# Job Title Input
job_title_label = tk.Label(root, text="Job Title:", font=("Arial", 12), bg="#e3f2fd")
job_title_label.pack(pady=5)
job_title_entry = tk.Entry(root, font=("Arial", 12), width=40)
job_title_entry.pack(pady=5)

# Get Questions Button
get_questions_button = tk.Button(root, text="Get Questions", font=("Arial", 12), bg="#64b5f6", fg="white",
                                 command=get_questions)
get_questions_button.pack(pady=20)

# Output Window (ScrolledText)
chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, font=("Arial", 12), width=60, height=10,
                                        bg="#f1f8e9")
chat_window.pack(pady=10)


# Function to handle exit button
def exit_app():
    root.quit()


# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), bg="#f44336", fg="white", command=exit_app)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
