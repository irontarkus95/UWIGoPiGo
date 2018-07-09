#### Space Disaster Tutorial

Space disaster is an experiment to create an engaging scenario for students to play around with image recognition using the Raspberry Pi and PiCamera. The scenario is that the players' ship has been damaged, including the ship's microphone so it's computer can no longer listen to commands. However, the ship's computer can still see them. The ship's manual has collection of predefined symbols which correspond to different repair instructions. The players must now draw these symbols to and show to the camera before the timer ends in order to fix the multiple errors. The malfunctions are randomly choosen from a list to make each run slightly different, and espeak is used for an audible countdown.

##### Note: 
We hope to improve the drawing recognition by using [Sketch-RNN](https://github.com/payalbajaj/sketch_rnn_classification) for proper classification.
