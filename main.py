import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def create_bootable_installer():
    volume = volume_entry.get()
    os_installer_path = os_entry.get()

    # Ensure the volume and OS installer path are provided
    if not volume or not os_installer_path:
        messagebox.showerror("Error", "Please provide both the volume and macOS installer path.")
        return

    # Construct the command based on the chosen installer
    command = f"sudo '{os_installer_path}/Contents/Resources/createinstallmedia' --volume /Volumes/{volume}"

    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success", "Bootable installer created successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to create bootable installer: {e}")


def select_volume():
    volume = filedialog.askdirectory()
    volume_entry.delete(0, tk.END)
    volume_entry.insert(0, volume.split("/")[-1])


def select_os_installer():
    os_installer_path = filedialog.askopenfilename(
        title="Select macOS Installer",
        filetypes=[("macOS Installer", "Install macOS*.app")]
    )
    os_entry.delete(0, tk.END)
    os_entry.insert(0, os_installer_path)


# Set up the GUI
root = tk.Tk()
root.title("macOS Bootable Installer Creator")

tk.Label(root, text="Select USB Volume:").grid(row=0, column=0, padx=10, pady=10)
volume_entry = tk.Entry(root, width=30)
volume_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_volume).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select macOS Installer:").grid(row=1, column=0, padx=10, pady=10)
os_entry = tk.Entry(root, width=30)
os_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_os_installer).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Create Installer", command=create_bootable_installer).grid(row=2, columnspan=3, pady=20)

root.mainloop()
