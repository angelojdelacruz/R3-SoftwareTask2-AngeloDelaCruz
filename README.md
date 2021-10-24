# R3-SoftwareTask2-AngeloDelaCruz
 A simulation of controlling a four-wheeled rover with input from a keyboard

 The input.py file establishes a server for the output.py file to connect to.
Once a connection between the two are established, input.py starts recording keyboard inputs, but has specific responses when the arrow keys, or any of the f keys from f1 to f6.
The arrow keys determine which way each the rover's motors are rotating, which determines if the rover is moving forwards, backwards, turning left, or turning right. The f keys set the specific speed at which the motors turn the wheels in intervals of 51, from 0 to 255. Input.py also determines once a key is not being pressed, and displays the motors as not moving as such (This applies to any key not being pressed, so if a non-functional key is pressed and released, the program will still display the message that the rover is not moving.)
Holding down a key causes the direction the rover is moving in to be printed repeatedly until the key is released. 

This program is more of a simulation than an actual implementation of controls for a 4-wheeled rover. I've never had experience working with python sockets, establishing and connecting a server and client, so I wasn't entirely sure how to send/receive inputs over them. On top of other assignments and midterms this previous week, it was hard finding the time to learn more about the processes used in this program, and I would have absolutely attempted to make an actual implementation if I had the time.
