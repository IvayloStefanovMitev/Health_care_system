from canvas import root
from gui_health_system.authentication import render_entry

# This allows the program to be executable by itself.
if __name__ == '__main__':
    # visualizing the login and the register button on the screen
    render_entry()
    root.mainloop()