#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import os
import importlib.util
from PIL import Image, ImageTk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Hacking System")

        # Căn giữa cửa sổ
        window_width = 1200
        window_height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Khung chứa các công cụ
        self.tools_frame = tk.Frame(self)
        self.tools_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        self.load_tools()

    def load_tools(self):
        tools_path = "tools"
        if not os.path.exists(tools_path):
            os.makedirs(tools_path)

        # Lấy danh sách các module công cụ
        tool_modules = []
        for tool_name in os.listdir(tools_path):
            tool_dir = os.path.join(tools_path, tool_name)
            if os.path.isdir(tool_dir):
                init_file = os.path.join(tool_dir, '__init__.py')
                if os.path.exists(init_file):
                    try:
                        spec = importlib.util.spec_from_file_location(tool_name, init_file)
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        tool_modules.append(module.TOOL_INFO)
                    except Exception as e:
                        print(f"Lỗi khi tải module {tool_name}: {e}")

        # Sắp xếp các công cụ theo index
        tool_modules.sort(key=lambda x: x.get('index', 0))

        # Hiển thị các công cụ lên giao diện
        for tool_info in tool_modules:
            self.add_tool_button(tool_info)

    def add_tool_button(self, tool_info):
        tool_id = tool_info.get("id")
        tool_name = tool_info.get("name", "N/A")
        icon_path = tool_info.get("icon")

        # Tải icon
        try:
            full_icon_path = os.path.join("tools", tool_id, icon_path)
            img = Image.open(full_icon_path)
            img = img.resize((48, 48), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Không thể tải icon cho {tool_name}: {e}")
            # Sử dụng icon mặc định nếu có lỗi
            try:
                img = Image.open("icons/default_icon.png")
                img = img.resize((48, 48), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
            except:
                photo = None
        
        button = tk.Button(self.tools_frame, text=tool_name, image=photo, compound=tk.TOP, 
                           command=lambda t=tool_id: self.launch_tool(t))
        if photo:
            button.image = photo # Giữ tham chiếu đến ảnh để không bị garbage collector xóa
        button.pack(side=tk.LEFT, padx=10, pady=10)

    def launch_tool(self, tool_id):
        try:
            tool_module_path = f"tools.{tool_id}.tool"
            tool_module = importlib.import_module(tool_module_path)
            # Giả sử mỗi module có một hàm `run` để khởi chạy
            tool_module.run(self)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể khởi chạy công cụ {tool_id}: {e}")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()