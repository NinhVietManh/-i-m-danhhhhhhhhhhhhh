import sys
from PyQt5.QtWidgets import QApplication
from ui.login_window import LoginWindow

def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Show login window
    login = LoginWindow()
    login.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
