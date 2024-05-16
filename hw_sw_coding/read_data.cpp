// Reading analog data from an Arduino pin(P0)

int analogPin = P0;                         // Define the analog pin 
int sensorValue = 0;                        // Sesnsor value           

void setup() {
 
    serial.begin(9600);                     // Initialize serial communication at 9600 bps
}

void loop() {

    sensorValue = analogRead(analogPin)     // Read the analog input

    serial.printIn(sensorValue);          // send the value to the serial port

}

