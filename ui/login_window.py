from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QFrame, QMessageBox, QApplication, QDesktopWidget)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon, QFontDatabase
from ui.main_window import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.init_ui()
        
    def center_window(self):
        """Center the window on the screen"""
        desktop = QDesktopWidget()
        screen_geometry = desktop.availableGeometry()
        window_geometry = self.frameGeometry()
        
        # Calculate center position
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        
        # Move window to center
        self.move(window_geometry.topLeft())
        
    def init_ui(self):
        self.setWindowTitle('Hệ thống điểm danh')
        self.setFixedSize(1600, 900)
        
        # Center the window on screen
        self.center_window()
        
        # Main horizontal layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Left sidebar - Logo area
        left_sidebar = QFrame()
        left_sidebar.setFixedWidth(420)
        left_sidebar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
            }
        """)
        
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignCenter)
        
        # Logo frame with white background
        logo_container = QFrame()
        logo_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        logo_container.setFixedSize(340, 280)
        
        logo_layout = QVBoxLayout()
        logo_layout.setContentsMargins(25, 40, 25, 40)
        logo_layout.setSpacing(10)
        
        logo_title = QLabel('<b>Phần<br>mềm</b>')
        logo_title.setFont(QFont('Times New Roman', 24, QFont.Bold))
        logo_title.setStyleSheet('color: #2c3e50; line-height: 1.2;')
        logo_title.setAlignment(Qt.AlignCenter)
        logo_title.setWordWrap(True)
        
        logo_layout.addWidget(logo_title)
        logo_container.setLayout(logo_layout)
        
        left_layout.addWidget(logo_container)
        left_sidebar.setLayout(left_layout)
        
        # Right side - Login form
        right_side = QFrame()
        right_side.setStyleSheet("""
            QFrame {
                background-color: white;
            }
        """)
        
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(80, 60, 80, 60)
        form_layout.setSpacing(20)
        form_layout.setAlignment(Qt.AlignTop)
        
        # Sign In title
        title_label = QLabel('<b>Đăng Nhập</b>')
        title_label.setFont(QFont('Times New Roman', 34))
        title_label.setMinimumHeight(60)
        title_label.setStyleSheet('color: #2c3e50; margin-bottom: 30px; padding: 10px 0;')
        title_label.setAlignment(Qt.AlignLeft)
        
        # Email field
        email_label = QLabel('<b>Tên đăng nhập</b>')
        email_label.setFont(QFont('Times New Roman', 12))
        email_label.setStyleSheet('color: #2c3e50; margin-top: 10px;')
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Nhập tên đăng nhập')
        self.username_input.setFont(QFont('Times New Roman', 12))
        self.username_input.setFixedHeight(60)
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 12px 15px;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                background-color: #f8f9fa;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border: 1px solid #5dade2;
                background-color: white;
            }
        """)
        
        # Password field
        password_label = QLabel('<b>Mật khẩu</b>')
        password_label.setFont(QFont('Times New Roman', 12))
        password_label.setStyleSheet('color: #2c3e50; margin-top: 15px;')
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Nhập mật khẩu')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFont(QFont('Times New Roman', 12))
        self.password_input.setFixedHeight(60)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 12px 15px;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                background-color: #f8f9fa;
                color: #2c3e50;
            }
            QLineEdit:focus {
                border: 1px solid #5dade2;
                background-color: white;
            }
        """)
        self.password_input.returnPressed.connect(self.handle_login)
        
        # Remember me and Forgot password
        options_layout = QHBoxLayout()
        options_layout.setContentsMargins(0, 10, 0, 10)
        
        forgot_btn = QPushButton('Quên mật khẩu?')
        forgot_btn.setFont(QFont('Times New Roman', 10))
        forgot_btn.setStyleSheet("""
            QPushButton {
                color: #5dade2;
                border: none;
                background: transparent;
                text-align: right;
            }
            QPushButton:hover {
                color: #3498db;
            }
        """)
        forgot_btn.setCursor(Qt.PointingHandCursor)
        
        options_layout.addStretch()
        options_layout.addWidget(forgot_btn)
        
        # Sign In button
        login_btn = QPushButton('Đăng nhập')
        login_btn.setFont(QFont('Times New Roman', 10))
        login_btn.setFixedHeight(60)
        login_btn.setCursor(Qt.PointingHandCursor)
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #5dade2;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 8px;
                margin-top: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
            QPushButton:pressed {
                background-color: #2980b9;
            }
        """)
        login_btn.clicked.connect(self.handle_login)
        
        # Demo accounts info
        demo_label = QLabel('<i>Tài khoản demo: admin/admin123 | teacher/teacher123 | student/student123</i>')
        demo_label.setAlignment(Qt.AlignCenter)
        demo_label.setFont(QFont('Times New Roman', 9))
        demo_label.setStyleSheet('color: #95a5a6; margin-top: 25px;')
        demo_label.setWordWrap(True)
        
        # Add widgets to form layout
        form_layout.addWidget(title_label)
        form_layout.addWidget(email_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addLayout(options_layout)
        form_layout.addWidget(login_btn)
        form_layout.addWidget(demo_label)
        form_layout.addStretch()
        
        right_side.setLayout(form_layout)
        
        # Add both sides to main layout
        main_layout.addWidget(left_sidebar)
        main_layout.addWidget(right_side)
        
        self.setLayout(main_layout)
        
    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        # Mock user database
        users = {
            'admin': {
                'password': 'admin123',
                'role': 'Super Admin',
                'full_name': 'Administrator'
            },
            'teacher': {
                'password': 'teacher123',
                'role': 'Teacher',
                'full_name': 'John Smith'
            },
            'student': {
                'password': 'student123',
                'role': 'Student',
                'full_name': 'Jane Doe'
            },
            'manager': {
                'password': 'manager123',
                'role': 'Manager',
                'full_name': 'Michael Johnson'
            }
        }
        
        # Validate credentials
        if username in users and users[username]['password'] == password:
            user_info = users[username]
            self.open_main_window(user_info['full_name'], user_info['role'])
        else:
            # Show error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Login Failed')
            msg.setText('Invalid username or password!')
            msg.setInformativeText('Please check your credentials and try again.')
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                }
                QLabel {
                    color: #2c3e50;
                    font-size: 12px;
                }
            """)
            msg.exec_()
            self.password_input.clear()
            
    def open_main_window(self, full_name, role):
        self.main_window = MainWindow(full_name, role)
        self.main_window.show()
        self.close()
