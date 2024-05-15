## code to receive data and plot in real-time

import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import keyboard

stop_program = False


ser = serial.Serial('COMA0',9600)                        # COMA0 is your serial port(like COM3)

data = []                                               # List of data

def realTimePlot(frame):

    ## Stop the program without using crtl+c
    ## check if the 'Esc' key has been pressed
    if keyboard.is_pressed('esc')
        plt.close('all')
        ser.close()
        print('Program stopped')

        return


    Line = ser.readline().decode('utf-8').strip()      # Read a line of data from the serial port
    
    try:
        arduino_value = float(Line)                    # Convert to float
        data.append(arduino_value)                     # Add to the list of points to animate

    except valueError:                                                                           
        pass
    
    data = data [-150:]                                # Keep only the last 150 data 

    plt.clf()                                          # Clear the current plot

    plt.plot(data)                                     # Plot the data
    plt.set_ylim(0,1000)                               # Set up value ranges
    plt.set_title('Real-time Analog Data from Arduino') 
    plt.set_xlabel('Time')
    plt.set_ylabel('Analog value')


fig = plt.figure()                  #Set up the plot

ani = animation.FuncAnimation(fig, realTimePlot, frames=100, interval=100) #Animate the plot
plt.show()



