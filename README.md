# VMBot v4.0
-
- **The bot now works almost without pictures, in coordinates.**
- **The code was significantly compressed and transferred to a single file.**
- **Files differ only in the resolution of the screen on which the bot works.**
- **Added logs.**

# VMBot v2.0
-
The bot that is automating the process of creating the virtial machines and downloading the browser through it.

Generally, the majority of the work the bot do is moving the cursor, clicking, scrolling and waiting for the appearence of the picture on the screen, on which it relies when working. These actions are available to be used by the PyAutoGUI framework.
Most of the logical code is written in main.py. The "big" functions or frequently used functions are written in the other files (like functions.py or VPN_start.py). I tried to keep the structure of the code by formatting it like that.
