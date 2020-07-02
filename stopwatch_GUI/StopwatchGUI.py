try:
    import Tkinter
except:
    import tkinter as Tkinter

counter = 0
running = False
def counter_label(label):
    def count():
        if running:
            global counter
            if counter==0:
                display="Starting."
            else:
                display=str(counter)

            label['text']=display
            label.after(1000, count)    # Delays by 1000ms=1 seconds and call count again.
            counter += 1
    count()

def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

def Reset(label):
    global counter
    counter=0
    if running==False:      # If reset is pressed after pressing stop.
        reset['state']='disabled'
        label['text']='Welcome Again !'
    else:                          # If reset is pressed while the stopwatch is running.
        label['text']='Starting.'

root = Tkinter.Tk()
root.title("GUI Stopwatch using Tkinter and time")
root.minsize(width=500, height=100)
label = Tkinter.Label(root, text="Hey !", fg="black", font="Verdana 16 bold")
label.pack()
start=Tkinter.Button(root, text='Start', width=30, command=lambda:Start(label))
stop = Tkinter.Button(root, text='Stop', width=30, state='disabled', command=Stop)
reset = Tkinter.Button(root, text='Reset', width=30, state='disabled', command=lambda:Reset(label))
start.pack()
stop.pack()
reset.pack()
root.mainloop()
