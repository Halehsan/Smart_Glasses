import time
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import keyboard

data = []  # List to store data

def realTimePlot(frame):
    ## Stop the program without using crtl+c
    ## Check if the 'Esc' key has been pressed
    #keyboard = Controller()
    
    if keyboard.is_pressed('esc'):
        plt.close('all')
        print('Program stopped')
        return

    # Generate a random value between 0 and 1023 to simulate Arduino input
    arduino_value = random.uniform(0, 1000)
    data.append(arduino_value)  # Add to the list of points to animate

    #data = data[-150:]  # Keep only the last 150 data points

    plt.clf()  # Clear the current plot

    plt.plot(data)  # Plot the data
    plt.ylim(0, 1000)  # Set up value ranges
    plt.title('Real-time Analog Data (Simulated)')
    plt.xlabel('Time')
    plt.ylabel('Analog value')

fig = plt.figure()  # Set up the plot

ani = animation.FuncAnimation(fig, realTimePlot, frames=100, interval=100)  # Animate the plot
plt.show()


