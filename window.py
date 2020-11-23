import tkinter as tk
from sql_interface import MusicDB,SQL_query 

connection = MusicDB()
query = SQL_query(connection)

class Window():
    def __init__(self, parent):
        self.root = parent
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True)
        self.scroll1Y = tk.Scrollbar(self.main_frame)
        self.trackList = tk.Listbox(self.main_frame, width=20, 
                                    yscrollcommand=self.scroll1Y.set)
        self.enter_but =  tk.Button(self.main_frame, 
                                    text = "OK", 
                                    command = self.list_tracks)
        self.scroll1Y.configure(command=self.trackList.yview)
        self.entry = tk.Entry(self.main_frame)
        self.show_widgets()
    def show_widgets(self):
        self.entry.grid(row=0, column =0,padx= 5, pady=5)
        self.trackList.grid(row=1, column=0, columnspan= 2)
        self.trackList.bind('<<ListboxSelect>>', self.callback_select)
        self.enter_but.grid(row=0, column =1, columnspan= 2, padx=10)
        self.scroll1Y.grid(row=1, column=2, padx=1, sticky="wns")

    def list_tracks(self):
        print (self.entry.get())
        result = query.get_track(self.entry.get())
        self.trackList.delete(0, tk.END)
        for track in result:
            self.trackList.insert(tk.END, track)
    def callback_select(self, event):
        lt = event.widget
        value = lt.get( int(lt.curselection()[0]))
        print (value)
        self.get_track_info(value)

    def get_track_info(self, track_name):
        result = query.get_info(track_name)
        print ("Album : ",result)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("350x300")
    root.configure(bg = "red")
    Window(root)
    root.mainloop()