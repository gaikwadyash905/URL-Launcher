import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import shutil

def browse_file():
    """Open a file dialog to select a text file containing URLs."""
    global urls
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                urls = [line.strip() for line in file if line.strip()]
                messagebox.showinfo("File Loaded", f"Successfully loaded {len(urls)} URLs.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read the file: {e}")

def get_installed_browsers():
    """Retrieve a list of installed browsers."""
    browsers = []
    try:
        # Detecting the default browser
        default_browser_name = webbrowser.get().name.title()
        browsers.append((f"Default ({default_browser_name})", None))

        # Check for specific browsers
        for name, command in [
            ("Google Chrome", "google-chrome"),
            ("Mozilla Firefox", "firefox"),
            ("Microsoft Edge", "msedge"),
            ("Safari", "safari")
        ]:
            if shutil.which(command):
                browsers.append((name, command))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to detect installed browsers: {e}")
    return browsers

def open_urls():
    """Open the URLs in the selected browser."""
    if not urls:
        messagebox.showerror("Error", "No URLs loaded. Please select a file first.")
        return

    selected_browser = browser_var.get()

    if selected_browser == "None":
        selected_browser = None  # Use system default browser

    try:
        browser_instance = webbrowser.get(selected_browser)
        for url in urls:
            browser_instance.open_new_tab(url)
        messagebox.showinfo("Success", "All URLs have been opened successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open URLs: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Open URLs in Browser")

urls = []

# Instructions Label
tk.Label(root, text="Step 1: Select a text file containing URLs (one URL per line)", font=("Arial", 10)).pack(pady=10)

# File browse button
tk.Button(root, text="Browse File", command=browse_file, font=("Arial", 10)).pack(pady=5)

# Separator
tk.Label(root, text="Step 2: Select a browser", font=("Arial", 10)).pack(pady=10)

# Radio buttons for browser selection
browser_var = tk.StringVar(value="None")

installed_browsers = get_installed_browsers()
for text, value in installed_browsers:
    tk.Radiobutton(root, text=text, variable=browser_var, value=value if value else "None", font=("Arial", 10)).pack(anchor=tk.W, padx=20)

# Open URLs button
tk.Button(root, text="Open URLs", command=open_urls, font=("Arial", 10)).pack(pady=10)

# Run the application
root.mainloop()
