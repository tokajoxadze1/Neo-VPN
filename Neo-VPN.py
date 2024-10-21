import os
import subprocess
import tkinter as tk
from tkinter import scrolledtext

# Program description and author info
program_description = """
NEO-VPN - A Hacker-Style Tor VPN Manager 🌐💻

Version: V 1.0
Author: 🥷 Tornike Jokhadze 🥷

This program allows you to control the Tor VPN, start and stop the service, 
and check your IP address to ensure your privacy is protected.

🛡️ Designed for educational purposes only.
"""

# Function to display network information on startup
def show_network_info():
    log_message("Displaying network information... 🌐")
    try:
        # Display network info (Linux)
        result = subprocess.check_output(['ifconfig'])
        network_info = result.decode('utf-8')
        log_message(f"Network Info:\n{network_info}")
    except subprocess.CalledProcessError:
        log_message("Unable to fetch network info. Please ensure you are on a Linux system. ❌")
    except Exception as e:
        log_message(f"Error fetching network info: {e} ❌")

# NEO start function
def start_neo():
    log_message("Starting NEO VPN... 🚀")
    os.system("sudo systemctl start tor")
    log_message("NEO VPN is now active. Your real IP should be hidden. 🔒")

# NEO stop function
def stop_neo():
    log_message("Stopping NEO VPN... 🛑")
    os.system("sudo systemctl stop tor")
    log_message("NEO VPN is now stopped. Your real IP is exposed. ⚠️")

# NEO restart function
def restart_neo():
    log_message("Restarting NEO VPN... 🔄")
    os.system("sudo systemctl restart tor")
    log_message("NEO VPN has been restarted. Your real IP should now be hidden. 🔒")

# Log messages
def log_message(message):
    log_box.insert(tk.END, message + '\n')
    log_box.see(tk.END)

# Check IP function
def check_ip():
    log_message("Checking current IP address... 🔍")
    try:
        # Using a different IP check service
        result = subprocess.check_output(['curl', 'https://checkip.amazonaws.com'])
        ip_address = result.decode('utf-8').strip()  # strip to remove newline characters
        log_message(f"Current IP: {ip_address} 🌍")
    except Exception as e:
        log_message(f"Error fetching IP: {e} ❌")

# GUI design
def create_gui():
    global log_box  # Make log_box global so it's accessible in other functions

    window = tk.Tk()
    window.title("NEO-VPN - Tor VPN Manager")
    window.configure(bg='black')
    window.geometry("800x800")  # Adjust the window size to be bigger

    # Title Label (Larger Font Size)
    title_label = tk.Label(window, text="💻🌐 NEO-VPN - A Hacker-Style Tor VPN Manager 🌐💻", 
                           fg='lightgreen', bg='black', font=("Courier", 18, 'bold'))
    title_label.grid(column=0, row=0, columnspan=3, padx=20, pady=10)

    # Display program description and author info
    description_label = tk.Label(window, text=program_description, fg='lightblue', bg='black', font=("Courier", 12))
    description_label.grid(column=0, row=1, columnspan=3, padx=20, pady=10)

    # Author info with green color and bigger size
    author_label = tk.Label(window, text="Author: 🥷 Tornike Jokhadze 🥷", fg='lightgreen', bg='black', font=("Courier", 14, 'bold'))
    author_label.grid(column=0, row=2, columnspan=3, padx=20, pady=10)

    # Log messages area
    log_box = scrolledtext.ScrolledText(window, width=80, height=20, bg='black', fg='lightgreen', font=("Courier", 10))
    log_box.grid(column=0, row=3, columnspan=3, padx=20, pady=10)

    # Create buttons in 3 columns
    button_frame = tk.Frame(window, bg='black')
    button_frame.grid(column=0, row=4, columnspan=3, pady=10)

    start_button = tk.Button(button_frame, text="Start NEO VPN", command=start_neo, width=20, bg='green', fg='black', font=("Courier", 12, 'bold'))
    start_button.grid(row=0, column=0, padx=10, pady=5)

    stop_button = tk.Button(button_frame, text="Stop NEO VPN", command=stop_neo, width=20, bg='red', fg='black', font=("Courier", 12, 'bold'))
    stop_button.grid(row=0, column=1, padx=10, pady=5)

    restart_button = tk.Button(button_frame, text="Restart NEO VPN", command=restart_neo, width=20, bg='#FFA500', fg='black', font=("Courier", 12, 'bold'))  # Orange color
    restart_button.grid(row=0, column=2, padx=10, pady=5)

    check_ip_button = tk.Button(button_frame, text="Check IP", command=check_ip, width=20, bg='skyblue', fg='black', font=("Courier", 12, 'bold'))  # Sky blue color
    check_ip_button.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

    # Run the network info function when the program starts
    show_network_info()

    # Run the GUI
    window.mainloop()

# Main program
if __name__ == "__main__":
    create_gui()
