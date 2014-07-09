pr2_listens
===========

Interface for PR2 to listen to speech and audio commands, and be able to physically move and respond to those commands with appropriate action.

This project was developed as part of a research project at Carnegie Mellon University.

Dependencies:
- SoX - Sound eXchange - http://sox.sourceforge.net/
- PortAudio - For audio input collection and initial handling
- Google Speech API - (v1)
- ROS (Robot Operating System) on PR2

Audio editing techniques:
For audio editing, I utilized a library called SoX. It is effectively a command line interface to be able to resample and edit audio tracks.
For further documentation on the various techniques and commands used, please refer to: http://sox.sourceforge.net/Docs/Documentation


Architecture Design:
Various architechture designs were tried and tested. This was finally chosen as the optimal option.
We have one central server that is responsible for "Listening & Speech to text translation". The speech to text was further handled using the Google Speech API.
Each client could then ping the server, indicating that it wishes to now listen for commands. While "KEEP ALIVE" messages are sent to the server, it continues to listen. When no clients are active, the server stays alive, but temporarily stops listening and translating.


