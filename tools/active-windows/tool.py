# tools/tool_hello/tool.py
import tkinter as tk

def run(root):
    # Tạo một cửa sổ Toplevel mới
    tool_window = tk.Toplevel(root)
    tool_window.title("Active Windows")
    
    # Căn giữa cửa sổ con so với cửa sổ cha
    window_width = 800
    window_height = 600
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    
    center_x = int(root_x + (root_width / 2) - (window_width / 2))
    center_y = int(root_y + (root_height / 2) - (window_height / 2))
    
    tool_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    