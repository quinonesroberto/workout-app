import time
import os
from tkinter import *

# Instantiate the window here. 
window = Tk()
window.title("Workout Timer")
variable_sec=StringVar()
variable_cycle=StringVar()


# Entry Widgets.
Ecycles_input=Entry(window)
Esec_ex_input=Entry(window)
Esec_res_input=Entry(window)

#Label Widgets
Lcycles_input=Label(text="How many workouts will you do?")
Lsec_ex_input=Label(text="How many seconds in each exercise?")
Lsec_rest_input=Label(text="How many seconds in each rest?")
Lcycles_out=Label(textvariable=variable_cycle)
Ltimer_out=Label(textvariable=variable_sec)



# sound function 
def call_sound():
    return os.system('afplay /System/Library/Sounds/Glass.aiff')


#Label Update Functions
def update_label():
    for n in range(5, -1, -1):
        variable_sec.set("Workout starts in " + str(n))
        time.sleep(1)
        window.update()
    else:
        variable_sec.set("Lets Rock!")
        time.sleep(1)
        window.update()
    call_sound()
    
    num_cycles = int(Ecycles_input.get())
    sec_x = int(Esec_ex_input.get())
    sec_rest = int(Esec_res_input.get())
    
    
    for cycle in range(num_cycles):
        for n in range(sec_x, -1, -1):
            time.sleep(1)
            variable_sec.set("Workout for " + str(n))
            variable_cycle.set("Cycle: " + str(cycle+1))
            window.update()
        # This will need to be adapted for general use. 
        # Also this directory should have a Sounds subdirectory with the sound you want. 
        call_sound()

        if cycle + 1 == num_cycles:
            variable_sec.set("YOU DID IT!")
            variable_cycle.set("")
            window.update() 
            break
        else: 
            for n in range(sec_rest, -1, -1):
                time.sleep(1)
                variable_sec.set("Rest for " + str(n)) 
                window.update() 
            
                
        call_sound()
   


    

#button config.
startButton = Button(window, text='START', command=update_label)
pauseButton = Button(window, text='PAUSE')

#positioning
Lcycles_input.grid(row=0, column=1)
Lsec_ex_input.grid(row=1, column=1)
Lsec_rest_input.grid(row=2, column=1)
Ecycles_input.grid(row=0, column=2)
Esec_ex_input.grid(row=1, column=2)
Esec_res_input.grid(row=2, column=2)
startButton.grid(row=3, column=0)
pauseButton.grid(row=3, column=4)
Lcycles_out.grid(row=4, column=1)
Ltimer_out.grid(row=6, column=1)




#grid row/column config.
Grid.rowconfigure(window, 0, weight=1)
Grid.rowconfigure(window, 1, weight=1)
Grid.rowconfigure(window, 2, weight=1)
Grid.rowconfigure(window, 3, weight=1)
Grid.rowconfigure(window, 4, weight=1)
Grid.rowconfigure(window, 5, weight=1)
Grid.rowconfigure(window, 6, weight=1)
Grid.rowconfigure(window, 7, weight=1)
Grid.columnconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 1, weight=1)
Grid.columnconfigure(window, 2, weight=1)
Grid.columnconfigure(window, 3, weight=1)
Grid.columnconfigure(window, 4, weight=1)
Grid.columnconfigure(window, 5, weight=1)



    



window.mainloop()



 