import os
import time
import tkinter as tk
from distutils.dir_util import copy_tree, remove_tree
import psutil

profiles_storage = r"{}\discord_profiles".format(os.path.expanduser('~'))
local_dir = r"{basepath}\Discord".format(basepath=os.path.expandvars('%LOCALAPPDATA%'))
roaming_dir = r"{basepath}\discord".format(basepath=os.path.expandvars('%APPDATA%'))


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn_main_profile = tk.Button(self)
        self.btn_main_profile["text"] = "Main Profile\n(Free-MeN4)"
        self.btn_main_profile["command"] = self.switch_to_main_profile
        self.btn_main_profile.pack(side="top", pady=5)

        self.btn_main_profile = tk.Button(self)
        self.btn_main_profile["text"] = "Alternative Profile"
        self.btn_main_profile["command"] = self.switch_to_alternative_profile
        self.btn_main_profile.pack(side="top")

        self.btn_main_profile = tk.Button(self)
        self.btn_main_profile["text"] = "Clear Discord State"
        self.btn_main_profile["command"] = self.clear_state
        self.btn_main_profile.pack(side="top", pady=25)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def clear_state(self):
        self.kill_discord()

        if roaming_dir and roaming_dir.endswith('discord') and not roaming_dir.endswith('Roaming'):
            try:
                remove_tree(roaming_dir)
            except FileNotFoundError:
                pass

    def switch_to_main_profile(self):
        self.clear_state()
        copy_tree(r"{}\{}\Local\Discord".format(profiles_storage, 'main_profile'), "{}".format(local_dir))
        copy_tree(r"{}\{}\Roaming\discord".format(profiles_storage, 'main_profile'), "{}".format(roaming_dir))
        self.launch_discord()

    def switch_to_alternative_profile(self):
        self.clear_state()
        copy_tree(r"{}\{}\Local\Discord".format(profiles_storage, 'alt_profile'), "{}".format(local_dir))
        copy_tree(r"{}\{}\Roaming\discord".format(profiles_storage, 'alt_profile'), "{}".format(roaming_dir))
        self.launch_discord()

    def launch_discord(self):
        os.startfile(r"{}\Desktop\Discord.lnk".format(os.path.expanduser('~')))

    def kill_discord(self):
        # kill existing Discord process
        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                try:
                    parent = psutil.Process(proc.ppid())
                    parent.kill()
                    break
                except psutil.NoSuchProcess:
                    pass
        time.sleep(2)


def center_window(root, width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


root = tk.Tk()
root.iconbitmap(r'{}\app.ico'.format(local_dir))
root.resizable(width=False, height=False)
root.title('DiscordZ')
center_window(root, 250, 200)
app = Application(master=root)
app.mainloop()
