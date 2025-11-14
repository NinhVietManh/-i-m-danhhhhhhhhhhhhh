from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QComboBox, QCalendarWidget,
                             QLineEdit, QDateEdit, QScrollArea, QGridLayout, QMessageBox)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from datetime import datetime

class AttendancePage(QWidget):
    def __init__(self, username='User', role='Admin'):
        super().__init__()
        self.username = username
        self.role = role
        self.init_ui()
        
    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Header
        header_layout = QHBoxLayout()
        
        # Breadcrumb
        breadcrumb = QLabel('Tổng quan / Học vụ / Điểm danh')
        breadcrumb.setFont(QFont('Times New Roman', 9))
        breadcrumb.setStyleSheet('color: #7f8c8d;')
        
        # User info
        user_info_layout = QHBoxLayout()
        user_info_layout.addStretch()
        
        notification_btn = QPushButton('🔔')
        notification_btn.setFixedSize(35, 35)
        notification_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: none;
                border-radius: 17px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        
        user_label = QLabel(f'<b>{self.username}</b>')
        user_label.setFont(QFont('Times New Roman', 10))
        user_label.setStyleSheet('color: #2c3e50; margin-left: 10px;')
        
        role_label = QLabel(self.role)
        role_label.setFont(QFont('Times New Roman', 9))
        role_label.setStyleSheet('color: #7f8c8d; margin-left: 5px;')
        
        # Logout button
        logout_btn = QPushButton('Đăng xuất')
        logout_btn.setFont(QFont('Times New Roman', 9))
        logout_btn.setCursor(Qt.PointingHandCursor)
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 8px 15px;
                border: none;
                border-radius: 5px;
                margin-left: 15px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        logout_btn.clicked.connect(self.handle_logout)
        
        user_info_layout.addWidget(notification_btn)
        user_info_layout.addWidget(user_label)
        user_info_layout.addWidget(role_label)
        user_info_layout.addWidget(logout_btn)
        
        header_layout.addWidget(breadcrumb)
        header_layout.addLayout(user_info_layout)
        
        # Title section
        title_layout = QVBoxLayout()
        title_layout.setSpacing(5)
        
        title_label = QLabel('<b>Quản lý Điểm danh</b>')
        title_label.setFont(QFont('Times New Roman', 24))
        title_label.setStyleSheet('color: #2c3e50;')
        
        subtitle_label = QLabel('Quản lý điểm danh sinh viên')
        subtitle_label.setFont(QFont('Times New Roman', 11))
        subtitle_label.setStyleSheet('color: #7f8c8d;')
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(subtitle_label)
        
        # Tabs
        tabs_layout = QHBoxLayout()
        tabs_layout.setSpacing(0)
        
        record_tab = QPushButton('<b>Ghi nhận điểm danh</b>')
        record_tab.setFont(QFont('Times New Roman', 10))
        record_tab.setStyleSheet("""
            QPushButton {
                background-color: #5dade2;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px 5px 0 0;
            }
        """)
        
        course_tab = QPushButton('Tổng hợp khóa học')
        course_tab.setFont(QFont('Times New Roman', 10))
        course_tab.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #2c3e50;
                padding: 10px 20px;
                border: none;
                border-radius: 5px 5px 0 0;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        
        student_tab = QPushButton('Tổng hợp sinh viên')
        student_tab.setFont(QFont('Times New Roman', 10))
        student_tab.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #2c3e50;
                padding: 10px 20px;
                border: none;
                border-radius: 5px 5px 0 0;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        
        tabs_layout.addWidget(record_tab)
        tabs_layout.addWidget(course_tab)
        tabs_layout.addWidget(student_tab)
        tabs_layout.addStretch()
        
        # Content area
        content_frame = QFrame()
        content_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
            }
        """)
        
        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        # Left side - Calendar
        calendar_widget = self.create_calendar_section()
        
        # Right side - Quick Attendance
        quick_attendance = self.create_quick_attendance_section()
        
        content_layout.addWidget(calendar_widget, 1)
        content_layout.addWidget(quick_attendance, 1)
        
        content_frame.setLayout(content_layout)
        
        # Add all to main layout
        main_layout.addLayout(header_layout)
        main_layout.addLayout(title_layout)
        main_layout.addLayout(tabs_layout)
        main_layout.addWidget(content_frame)
        
        self.setLayout(main_layout)
        
    def create_calendar_section(self):
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Header
        header_layout = QHBoxLayout()
        
        # Month navigation
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton('◀'))
        
        month_label = QLabel('April 2025')
        month_label.setFont(QFont('Arial', 12, QFont.Bold))
        month_label.setStyleSheet('color: #2c3e50;')
        nav_layout.addWidget(month_label)
        
        nav_layout.addWidget(QPushButton('▶'))
        
        header_layout.addLayout(nav_layout)
        header_layout.addStretch()
        
        title_label = QLabel('<b>Lịch Điểm danh</b>')
        title_label.setFont(QFont('Times New Roman', 14))
        title_label.setStyleSheet('color: #2c3e50;')
        
        subtitle_label = QLabel('Chọn ngày để xem hoặc ghi nhận điểm danh')
        subtitle_label.setFont(QFont('Times New Roman', 9))
        subtitle_label.setStyleSheet('color: #7f8c8d;')
        
        # Calendar
        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: white;
            }
            QCalendarWidget QTableView {
                selection-background-color: #5dade2;
                font-size: 11px;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #f0f0f0;
            }
        """)
        calendar.setMinimumHeight(300)
        
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addLayout(header_layout)
        layout.addWidget(calendar)
        
        frame.setLayout(layout)
        return frame
        
    def create_quick_attendance_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: #f9f9f9;
                border-radius: 10px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        title_label = QLabel('<b>Điểm danh nhanh</b>')
        title_label.setFont(QFont('Times New Roman', 14))
        title_label.setStyleSheet('color: #2c3e50;')
        
        subtitle_label = QLabel('Ghi nhận điểm danh hoặc xem báo cáo')
        subtitle_label.setFont(QFont('Times New Roman', 9))
        subtitle_label.setStyleSheet('color: #7f8c8d; margin-bottom: 10px;')
        
        # Course field
        course_label = QLabel('<b>Khóa học</b>')
        course_label.setFont(QFont('Times New Roman', 10))
        course_label.setStyleSheet('color: #2c3e50;')
        
        course_combo = QComboBox()
        course_combo.addItems(['Chọn khóa học', 'Toán học', 'Vật lý', 'Hóa học', 'Sinh học'])
        course_combo.setStyleSheet("""
            QComboBox {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: white;
                font-size: 11px;
            }
        """)
        
        # Session field
        session_label = QLabel('<b>Học kỳ</b>')
        session_label.setFont(QFont('Times New Roman', 10))
        session_label.setStyleSheet('color: #2c3e50;')
        
        session_combo = QComboBox()
        session_combo.addItems(['2025', '2024', '2023'])
        session_combo.setStyleSheet("""
            QComboBox {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: white;
                font-size: 11px;
                font-family: 'Times New Roman';
            }
        """)
        
        # Date field
        date_label = QLabel('<b>Ngày</b>')
        date_label.setFont(QFont('Times New Roman', 10))
        date_label.setStyleSheet('color: #2c3e50;')
        
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDate(QDate.currentDate())
        date_edit.setDisplayFormat('dd/MM/yyyy')
        date_edit.setStyleSheet("""
            QDateEdit {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: white;
                font-size: 11px;
            }
        """)
        
        # Buttons
        buttons_layout = QHBoxLayout()
        
        record_btn = QPushButton('<b>Ghi nhận điểm danh</b>')
        record_btn.setFont(QFont('Times New Roman', 10))
        record_btn.setCursor(Qt.PointingHandCursor)
        record_btn.setStyleSheet("""
            QPushButton {
                background-color: #5dade2;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
        """)
        
        report_btn = QPushButton('Tạo báo cáo')
        report_btn.setFont(QFont('Times New Roman', 10))
        report_btn.setCursor(Qt.PointingHandCursor)
        report_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #2c3e50;
                padding: 12px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        
        buttons_layout.addWidget(record_btn)
        
        # Add widgets to layout
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addWidget(course_label)
        layout.addWidget(course_combo)
        layout.addWidget(session_label)
        layout.addWidget(session_combo)
        layout.addWidget(date_label)
        layout.addWidget(date_edit)
        layout.addWidget(record_btn)
        layout.addWidget(report_btn)
        layout.addStretch()
        
        frame.setLayout(layout)
        return frame
    
    def handle_logout(self):
        reply = QMessageBox.question(self, 'Đăng xuất', 
                                    'Bạn có chắc chắn muốn đăng xuất?',
                                    QMessageBox.Yes | QMessageBox.No, 
                                    QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # Close main window and show login
            from ui.login_window import LoginWindow
            self.login_window = LoginWindow()
            self.login_window.show()
            self.window().close()
