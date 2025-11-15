from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QFrame, QMessageBox, QStackedWidget)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

class BaseMainWindow(QMainWindow):
    """Base class for all main windows"""
    logout_requested = pyqtSignal()
    
    def __init__(self, full_name, role):
        super().__init__()
        self.full_name = full_name
        self.role = role
        self.init_base_ui()
        
    def init_base_ui(self):
        self.setWindowTitle(f'Hệ thống điểm danh - {self.role}')
        self.setGeometry(100, 100, 1400, 900)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create sidebar
        self.sidebar = self.create_sidebar()
        main_layout.addWidget(self.sidebar)
        
        # Create content area
        self.content_area = QStackedWidget()
        self.content_area.setStyleSheet("""
            QStackedWidget {
                background-color: #f8f9fa;
            }
        """)
        main_layout.addWidget(self.content_area)
        
        main_widget.setLayout(main_layout)
        
    def create_sidebar(self):
        """Create sidebar with navigation menu"""
        sidebar = QFrame()
        sidebar.setFixedWidth(280)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border-right: 1px solid #34495e;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        header = QFrame()
        header.setFixedHeight(80)
        header.setStyleSheet("background-color: #34495e;")
        
        header_layout = QVBoxLayout()
        header_layout.setContentsMargins(20, 10, 20, 10)
        
        # User info
        user_label = QLabel(f"{self.full_name}")
        user_label.setFont(QFont('Arial', 12, QFont.Bold))
        user_label.setStyleSheet("color: white;")
        
        role_label = QLabel(f"{self.role}")
        role_label.setFont(QFont('Arial', 10))
        role_label.setStyleSheet("color: #bdc3c7;")
        
        header_layout.addWidget(user_label)
        header_layout.addWidget(role_label)
        header.setLayout(header_layout)
        
        layout.addWidget(header)
        
        # Navigation menu
        self.nav_layout = QVBoxLayout()
        nav_widget = QWidget()
        nav_widget.setLayout(self.nav_layout)
        layout.addWidget(nav_widget)
        
        # Spacer
        layout.addStretch()
        
        # Logout button
        logout_btn = QPushButton("🚪 Đăng xuất")
        logout_btn.setFixedHeight(50)
        logout_btn.setFont(QFont('Arial', 11))
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                text-align: left;
                padding: 15px 20px;
                margin: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        logout_btn.clicked.connect(self.handle_logout)
        layout.addWidget(logout_btn)
        
        sidebar.setLayout(layout)
        return sidebar
        
    def add_nav_button(self, text, icon_text="📋"):
        """Add a navigation button to the sidebar"""
        btn = QPushButton(f"{icon_text} {text}")
        btn.setFixedHeight(50)
        btn.setFont(QFont('Arial', 11))
        btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #ecf0f1;
                border: none;
                text-align: left;
                padding: 15px 20px;
                margin: 2px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #3498db;
            }
        """)
        self.nav_layout.addWidget(btn)
        return btn
        
    def handle_logout(self):
        reply = QMessageBox.question(self, 'Xác nhận', 
                                   'Bạn có chắc chắn muốn đăng xuất?',
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.close()
            # Import here to avoid circular import
            from ui.login_window import LoginWindow
            self.login_window = LoginWindow()
            self.login_window.show()
