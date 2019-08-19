# SimpleTk

#### A package to create simple Tkinter-GUIs using a seperate textfile

##### Description
SimpleTk is a Class wich interprets a text file with fitting syntax
to a tkinter GUI (just like Kivy). 

##### Implementation

###### Import
```python
from tkinter import * 
from SimpleTk import SimpleTk
```

###### Initialisation        
```python
root = Tk()
stk = SimpleTk(root, "project/testGUI.stk") # "gui.stk" is the standard value 
root.mainloop()
```

###### Changing Widget Properties
```python
stk.buttonName1["text"] = "I'm a button"
stk.frameName1.bind("<Button-1>", lambda e: print("Click Event"))
```

##### File Syntax
In the additional text file you have to take care of the specific syntax.
The current version is still sensitive to errors.

Important points:
- use `tab` to indent child-widgets
- No `tabs` at the end or middle of a line
- `command` can't be added to the widget properties (must be added afterwards in the program code)
- Use `{3}` to declare a maximum number of Columns for a parent-Widget (grid-geometry manager will be used inside that widget)
    - Lines without these brackets will use the pack-geometry manager to place child widgets		
- Use `..` to type spaces in string arguments _(a better solution is in work)_
- With `>` you can use this line to tyoe pure python code (e.g. to call methods on a widget)
- Use `#` to comment out the line from this point

Example:
- General:
    - `Widget-Class: WidgetName(Properties){Columns}`
- Example:
    - `Label: label1(text="This is a label", bg="lightblue"){3}`

To define a Childwidget just indent this line a line under the parent widget.


###### Style
You can predefine paremters for specific Widgets:

Example:
- General:
    - `Style: WidgetName(Properties)`
- Example:
    - `Style: Label(bg="lightgreen", fg="gold")`


##### Motivation
SimpleTk is a opportunity to outsource your fundamental GUI-implementation in an external file
with clearer and more structured syntax. Especially when you have a huge design or you just want to test
something.

###### Comparison

Tkinter:
```python
frame1 = Frame(root, bg = "white")     
frame1.pack(padx = 5, pady = 5, expand = True, fill = BOTH)   

lf1 = LabelFrame(frame1, text = "Header", bg = "gold")  
lf1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = N+S+E+W)

label1 = Label(lf1, text = "My first GUI", bg = "lightblue")   
label1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = N+S+E+W)

button1 = Button(lf1, text = "This is a Button")   
button1.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = N+S+E+W)

entry1 = Entry(lf1, bg = "white")  
entry1.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = N+S+E+W)

lf2 = LabelFrame(frame1, text = "Footer", bg = "gold")  
lf2.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = N+S+E+W)

label2 = Label(lf2, text = "Footer", bg = "lightblue")    
label2.pack(padx = 5, pady = 5, expand = True, fill = BOTH)

cb1 = ttk.Combobox(lf2)
cb1.pack(padx = 5, pady = 5, expand = True, fill = BOTH)
cb1.set("Selection")
```

SimpleTk:
```
Style: Label(bg = "lightblue")    
Style: LabelFrame(bg = "gold")

Frame: frame1 (bg = "white") {1}      
    LabelFrame: lf1 (text = "Header") {2}    
        Label: label1 (text = "My..first..GUI")     
        Button: button1 (text = "Thi..i..a..Button")  
        Entry: entry1 (bg = "white")        
    LabelFrame: lf2 (text = "Footer")    
        Label: label2 (text = "Footer")
        ttk.Combobox: cb1 ()

> cb1.set("Selection")
```