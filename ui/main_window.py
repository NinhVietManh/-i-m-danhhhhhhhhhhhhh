from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QStackedWidget, QFrame, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from ui.attendance_page import AttendancePage

class MainWindow(QMainWindow):
    def __init__(self, username, role='Super Admin'):
        super().__init__()
        self.username = username
        self.role = role
        self.current_page = 'attendance'
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Hệ thống Quản lý Điểm danh')
        self.setGeometry(100, 100, 1200, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #e8e0dd;
            }
        """)
        
        # Central widget
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        sidebar = self.create_sidebar()
        
        # Content area
        self.content_area = QStackedWidget()
        self.content_area.setStyleSheet("""
            QStackedWidget {
                background-color: #e8e0dd;
            }
        """)
        
        # Add pages
        self.attendance_page = AttendancePage(self.username, self.role)
        self.content_area.addWidget(self.attendance_page)
        
        # Add to main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.content_area)
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Logo area
        logo_frame = QFrame()
        logo_frame.setStyleSheet("""
            QFrame {
                background-color: #34495e;
                padding: 20px;
            }
        """)
        logo_layout = QVBoxLayout()
        
        logo_label = QLabel('<b>Quản lý<br>Điểm danh</b>')
        logo_label.setFont(QFont('Times New Roman', 16))
        logo_label.setStyleSheet('color: white; padding: 10px;')
        logo_label.setAlignment(Qt.AlignLeft)
        
        logo_layout.addWidget(logo_label)
        logo_frame.setLayout(logo_layout)
        
        # Menu items
        menu_frame = QFrame()
        menu_layout = QVBoxLayout()
        menu_layout.setContentsMargins(0, 20, 0, 0)
        menu_layout.setSpacing(0)
        
        # Dashboard button
        dashboard_btn = self.create_menu_button('☰  Tổng quan', 'dashboard')
        menu_layout.addWidget(dashboard_btn)
        
        # User Management button
        user_btn = self.create_menu_button('👥  Quản lý người dùng', 'users')
        menu_layout.addWidget(user_btn)
        
        # Academic section label
        academic_label = QLabel('  HỌC VỤ')
        academic_label.setFont(QFont('Times New Roman', 9, QFont.Bold))
        academic_label.setStyleSheet('color: #7f8c8d; padding: 15px 20px 10px 20px;')
        menu_layout.addWidget(academic_label)
        
        # Attendance button (active)
        attendance_btn = self.create_menu_button('▶  Điểm danh', 'attendance', active=True)
        menu_layout.addWidget(attendance_btn)
        
        # Other menu items
        learning_btn = self.create_menu_button('▶  Lớp học phần', 'learning')
        menu_layout.addWidget(learning_btn)
        
        session_btn = self.create_menu_button('▶  Buổi học', 'session')
        menu_layout.addWidget(session_btn)
        
        grade_btn = self.create_menu_button('▶  Điểm số', 'grade')
        menu_layout.addWidget(grade_btn)
        
        certificate_btn = self.create_menu_button('▶  Báo cáo', 'certificate')
        menu_layout.addWidget(certificate_btn)
        
        menu_layout.addStretch()
        
        # Settings button at bottom
        settings_btn = self.create_menu_button('⚙  Cài đặt', 'settings')
        menu_layout.addWidget(settings_btn)
        
        menu_frame.setLayout(menu_layout)
        
        # User info at bottom
        user_frame = QFrame()
        user_frame.setStyleSheet("""
            QFrame {
                background-color: #34495e;
                padding: 15px;
            }
        """)
        user_layout = QVBoxLayout()
        
        user_label = QLabel(f'{self.username}')
        user_label.setFont(QFont('Arial', 11, QFont.Bold))
        user_label.setStyleSheet('color: white;')
        
        role_label = QLabel(self.role)
        role_label.setFont(QFont('Arial', 9))
        role_label.setStyleSheet('color: #bdc3c7;')
        
        user_layout.addWidget(user_label)
        user_layout.addWidget(role_label)
        user_frame.setLayout(user_layout)
        
        # Add all to sidebar
        layout.addWidget(logo_frame)
        layout.addWidget(menu_frame)
        layout.addWidget(user_frame)
        
        sidebar.setLayout(layout)
        return sidebar
        
    def create_menu_button(self, text, page_id, active=False):
        btn = QPushButton(text)
        btn.setFont(QFont('Times New Roman', 11))
        btn.setCursor(Qt.PointingHandCursor)
        
        if active:
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 15px 20px;
                    border: none;
                    background-color: #4a6278;
                    color: white;
                    border-left: 4px solid #5dade2;
                }
            """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 15px 20px;
                    border: none;
                    background-color: transparent;
                    color: #bdc3c7;
                }
                QPushButton:hover {
                    background-color: #34495e;
                    color: white;
                }
            """)
        
        btn.clicked.connect(lambda: self.switch_page(page_id))
        return btn
        
    def switch_page(self, page_id):
        if page_id == 'attendance':
            self.content_area.setCurrentWidget(self.attendance_page)
        # Add other pages here
