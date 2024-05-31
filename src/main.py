# Import necessary modules
import multiprocessing
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

# Define the main function
def main():
    # Freeze support for multiprocessing
    multiprocessing.freeze_support()
    # Create a new application
    app = QApplication([])
    # Create a new main window
    widget = MainWindow()
    # Show the main window
    widget.show()
    # Execute the application
    app.exec_()

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()
