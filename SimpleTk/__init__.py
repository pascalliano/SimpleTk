from tkinter import *
from tkinter import ttk
import os.path

class SimpleTk:
    def __init__(self, root, file="gui.stk"):

        with open(file, "r") as f:
            self.data = [["".join(_.split(" ")).split("#")[0]] for _ in f.read().strip().split("\n") if _.split("#")[0].strip() != ""]

        self.parents = {}
        self.columns = {}
        self.indents = {}
        self.properties = {}
        self.widgets = {}
        self.styles = {}
        self.commands = []

        for i in self.data:
            i = i[0]
            if i.split(":")[0] != "Style" and i.strip()[0] != ">":
                self.parents[i.split(":")[-1].split("(")[0]] = i.split("\t")[-1].split(":")[0]
                self.indents[i.split(":")[-1].split("(")[0]] = i.count("\t")
                self.properties[i.split(":")[-1].split("(")[0]] = i.split("(")[-1].split(")")[0]
                self.columns[i.split(":")[-1].split("(")[0]] = int(i.split("{")[-1].split("}")[0]) if "{" in i else 0
            elif i.split(":")[0] == "Style" and i.strip()[0] != ">":
                self.styles[i.split(":")[-1].split("(")[0]] = i.split("(")[-1].split(")")[0]
            elif ">" in i:
                self.commands.append(i.split(">")[-1].strip())


        indent_keys = list(self.indents.keys())
        indent_keys.reverse()
        for i in indent_keys:
            tab_count = self.indents[i]
            for j in indent_keys[indent_keys.index(i):]:
                if self.indents[j] < tab_count:
                    self.properties[i] += f",parent={j}"
                    break

        self.parents_used = {_: -1 for _ in self.parents}
        for i in self.properties:
            parent = self.properties[i].split("parent=")[-1] if "parent=" in self.properties[i] else root
            parent_cols = self.columns[parent] if parent != root else 0
            if parent != root:
                self.parents_used[parent] += 1
            if parent != root:
                exec(f"{i} = {self.parents[i]}({parent})")
            else:
                exec(f"{i} = {self.parents[i]}(root)")

            if self.parents[i] in list(self.styles.keys()):
                exec(f'{i}.config({" ".join(self.styles[self.parents[i]].split(".."))})')

            exec(f'{i}.config({" ".join(self.properties[i].split(",parent")[0].split(".."))})')

            try:
                if parent_cols == 0:
                    exec(f"{i}.pack(padx = 5, pady = 5, expand = True, fill = BOTH)")
                else:
                    r, c = self.parents_used[parent] // parent_cols, self.parents_used[parent] % parent_cols
                    exec(f"{i}.grid(row={r}, column={c}, padx=5, pady=5, sticky=N+S+E+W)")
                    self.widgets[parent].grid_rowconfigure(r, weight=1)
                    self.widgets[parent].grid_columnconfigure(c, weight=1)
                self.widgets[i] = eval(i)
            except Exception as e:
                print("Fehler", e)

            exec(f"self.{i} = {i}")
            root.update()

        for i in self.commands:
            exec(i)

if not os.path.isfile("gui.stk"):
    with open("gui.stk", "w") as f:
        f.write("""# SimpleTk GUI-File
# Take a look at https://pypi.org/project/simpleTk/ to learn about the syntax

Frame: fr1(bg = "white")
\tLabelFrame: lf1(text = "SimpleTk")
\t\tLabel: l1(text = "My..first..SimpleTk..GUI", bg = "white")

\tLabelFrame: lf2(text = "This..is..a..LabelFrame"){2}
\t\tButton: b1(text = "This..is..a..Button", bg = "gold")
\t\tEntry: e1()
\t\tttk.Combobox: cb1(state = "readonly", values = ["This", "is", "a", "ComboBox"])
\t\tLabel: l2(text = "ttk..is..also..supported", fg = "red")""")