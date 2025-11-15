from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QTableWidget, QTableWidgetItem,
                             QComboBox, QLineEdit, QFrame, QMessageBox, QTabWidget,
                             QCheckBox, QTextEdit, QGroupBox, QGridLayout, QDialog,
                             QProgressBar, QSpinBox, QTimeEdit, QDateTimeEdit)
from PyQt5.QtCore import Qt, QTimer, QDateTime, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QPainter, QPen
import qrcode
from io import BytesIO
import random
import string

class WGVDiemDanh(QMainWindow):
    """Cửa sổ Điểm danh trực tiếp của Giảng viên"""
    
    def __init__(self, lhp_code):
        super().__init__()
        self.lhp_code = lhp_code
        self.attendance_code = ""
        self.qr_code = ""
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle(f'Điểm danh - {self.lhp_code}')
        self.setGeometry(100, 100, 1200, 800)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Header info
        header = self.create_header()
        layout.addWidget(header)
        
        # Tab widget for different attendance methods
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #ddd;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #f8f9fa;
                padding: 12px 20px;
                margin: 2px;
                min-width: 120px;
            }
            QTabBar::tab:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        
        # Tab 1: Điểm danh thủ công
        self.manual_tab = self.create_manual_tab()
        self.tabs.addTab(self.manual_tab, "✋ Điểm danh Thủ công")
        
        # Tab 2: Điểm danh khuôn mặt
        self.face_tab = self.create_face_tab()
        self.tabs.addTab(self.face_tab, "👤 Điểm danh Khuôn mặt")
        
        # Tab 3: Mã điểm danh
        self.code_tab = self.create_code_tab()
        self.tabs.addTab(self.code_tab, "🔢 Mã điểm danh")
        
        # Tab 4: Mã QR
        self.qr_tab = self.create_qr_tab()
        self.tabs.addTab(self.qr_tab, "📱 Mã QR")
        
        # Tab 5: Theo dõi
        self.monitor_tab = self.create_monitor_tab()
        self.tabs.addTab(self.monitor_tab, "👀 Theo dõi")
        
        layout.addWidget(self.tabs)
        
        # Bottom controls
        bottom_layout = QHBoxLayout()
        
        save_btn = QPushButton("💾 Lưu điểm danh")
        save_btn.setFixedHeight(40)
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        save_btn.clicked.connect(self.save_attendance)
        
        export_btn = QPushButton("📤 Xuất danh sách")
        export_btn.setFixedHeight(40)
        export_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #5dade2;
            }
        """)
        
        close_btn = QPushButton("❌ Đóng")
        close_btn.setFixedHeight(40)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        close_btn.clicked.connect(self.close)
        
        bottom_layout.addWidget(save_btn)
        bottom_layout.addWidget(export_btn)
        bottom_layout.addStretch()
        bottom_layout.addWidget(close_btn)
        
        layout.addLayout(bottom_layout)
        main_widget.setLayout(layout)
        
    def create_header(self):
        """Tạo header thông tin buổi học"""
        header = QFrame()
        header.setStyleSheet("""
            QFrame {
                background-color: #34495e;
                color: white;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        
        layout = QHBoxLayout()
        
        # Class info
        info_layout = QVBoxLayout()
        
        class_label = QLabel(f"Lớp học phần: {self.lhp_code} - Lập trình căn bản A1")
        class_label.setFont(QFont('Arial', 14, QFont.Bold))
        
        time_label = QLabel(f"Thời gian: {QDateTime.currentDateTime().toString('dd/MM/yyyy hh:mm')}")
        time_label.setFont(QFont('Arial', 11))
        
        room_label = QLabel("Phòng học: 101 - Tòa nhà A")
        room_label.setFont(QFont('Arial', 11))
        
        info_layout.addWidget(class_label)
        info_layout.addWidget(time_label)
        info_layout.addWidget(room_label)
        
        # Quick stats
        stats_layout = QVBoxLayout()
        
        total_label = QLabel("Tổng SV: 45")
        total_label.setFont(QFont('Arial', 12, QFont.Bold))
        total_label.setAlignment(Qt.AlignCenter)
        
        present_label = QLabel("Có mặt: 0")
        present_label.setFont(QFont('Arial', 11))
        present_label.setAlignment(Qt.AlignCenter)
        present_label.setStyleSheet("color: #2ecc71;")
        
        absent_label = QLabel("Vắng: 45")
        absent_label.setFont(QFont('Arial', 11))
        absent_label.setAlignment(Qt.AlignCenter)
        absent_label.setStyleSheet("color: #e74c3c;")
        
        stats_layout.addWidget(total_label)
        stats_layout.addWidget(present_label)
        stats_layout.addWidget(absent_label)
        
        layout.addLayout(info_layout)
        layout.addStretch()
        layout.addLayout(stats_layout)
        
        header.setLayout(layout)
        return header
        
    def create_manual_tab(self):
        """Tạo tab điểm danh thủ công"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Instructions
        instruction = QLabel("✋ Điểm danh thủ công: Tick chọn trạng thái cho từng sinh viên")
        instruction.setFont(QFont('Arial', 12, QFont.Bold))
        instruction.setStyleSheet("color: #2c3e50; margin: 10px 0;")
        layout.addWidget(instruction)
        
        # Search and filter
        search_layout = QHBoxLayout()
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("Tìm kiếm sinh viên...")
        search_input.setFixedHeight(35)
        
        filter_combo = QComboBox()
        filter_combo.addItems(["Tất cả", "Có mặt", "Vắng có phép", "Vắng không phép"])
        filter_combo.setFixedHeight(35)
        
        search_layout.addWidget(QLabel("Tìm kiếm:"))
        search_layout.addWidget(search_input)
        search_layout.addWidget(QLabel("Lọc:"))
        search_layout.addWidget(filter_combo)
        search_layout.addStretch()
        
        # Bulk actions
        bulk_layout = QHBoxLayout()
        
        select_all_btn = QPushButton("☑️ Chọn tất cả có mặt")
        select_all_btn.setFixedHeight(35)
        select_all_btn.clicked.connect(self.select_all_present)
        
        clear_all_btn = QPushButton("❌ Xóa chọn tất cả")
        clear_all_btn.setFixedHeight(35)
        clear_all_btn.clicked.connect(self.clear_all_selection)
        
        bulk_layout.addWidget(select_all_btn)
        bulk_layout.addWidget(clear_all_btn)
        bulk_layout.addStretch()
        
        # Student table
        self.manual_table = QTableWidget()
        self.manual_table.setColumnCount(6)
        self.manual_table.setHorizontalHeaderLabels([
            "MSV", "Họ tên", "Có mặt", "Vắng có phép", "Vắng không phép", "Ghi chú"
        ])
        self.manual_table.setAlternatingRowColors(True)
        
        # Sample student data
        students = [
            ["2021001", "Nguyễn Văn A"],
            ["2021002", "Trần Thị B"],
            ["2021003", "Lê Văn C"],
            ["2021004", "Phạm Thị D"],
            ["2021005", "Hoàng Văn E"]
        ]
        
        self.manual_table.setRowCount(len(students))
        for i, (msv, name) in enumerate(students):
            self.manual_table.setItem(i, 0, QTableWidgetItem(msv))
            self.manual_table.setItem(i, 1, QTableWidgetItem(name))
            
            # Radio button group for attendance status
            present_cb = QCheckBox()
            absent_p_cb = QCheckBox()  # Vắng có phép
            absent_np_cb = QCheckBox() # Vắng không phép
            
            # Group checkboxes so only one can be selected
            present_cb.toggled.connect(lambda checked, row=i: self.toggle_attendance(row, 0, checked))
            absent_p_cb.toggled.connect(lambda checked, row=i: self.toggle_attendance(row, 1, checked))
            absent_np_cb.toggled.connect(lambda checked, row=i: self.toggle_attendance(row, 2, checked))
            
            self.manual_table.setCellWidget(i, 2, present_cb)
            self.manual_table.setCellWidget(i, 3, absent_p_cb)
            self.manual_table.setCellWidget(i, 4, absent_np_cb)
            self.manual_table.setItem(i, 5, QTableWidgetItem(""))
            
        layout.addLayout(search_layout)
        layout.addLayout(bulk_layout)
        layout.addWidget(self.manual_table)
        widget.setLayout(layout)
        return widget
        
    def create_face_tab(self):
        """Tạo tab điểm danh khuôn mặt"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Instructions
        instruction = QLabel("👤 Điểm danh bằng Khuôn mặt: Sử dụng camera để nhận diện sinh viên")
        instruction.setFont(QFont('Arial', 12, QFont.Bold))
        instruction.setStyleSheet("color: #2c3e50; margin: 10px 0;")
        layout.addWidget(instruction)
        
        # Camera section
        camera_layout = QHBoxLayout()
        
        # Camera preview (placeholder)
        camera_frame = QFrame()
        camera_frame.setFixedSize(400, 300)
        camera_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #3498db;
                border-radius: 8px;
                background-color: #ecf0f1;
            }
        """)
        
        camera_label = QLabel("📷 Camera Preview\n(Chức năng đang phát triển)")
        camera_label.setAlignment(Qt.AlignCenter)
        camera_label.setFont(QFont('Arial', 12))
        camera_label.setStyleSheet("color: #7f8c8d;")
        
        camera_layout_inner = QVBoxLayout()
        camera_layout_inner.addWidget(camera_label)
        camera_frame.setLayout(camera_layout_inner)
        
        # Control panel
        control_frame = QFrame()
        control_frame.setFixedWidth(350)
        control_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #ddd;
                border-radius: 8px;
                background-color: white;
                padding: 20px;
            }
        """)
        
        control_layout = QVBoxLayout()
        
        # Camera controls
        start_camera_btn = QPushButton("📹 Bật Camera")
        start_camera_btn.setFixedHeight(40)
        start_camera_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
        """)
        
        stop_camera_btn = QPushButton("⏹️ Tắt Camera")
        stop_camera_btn.setFixedHeight(40)
        stop_camera_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
        """)
        
        # Recognition results
        result_label = QLabel("Kết quả nhận diện:")
        result_label.setFont(QFont('Arial', 11, QFont.Bold))
        
        self.recognition_text = QTextEdit()
        self.recognition_text.setFixedHeight(150)
        self.recognition_text.setPlaceholderText("Kết quả nhận diện sẽ hiển thị tại đây...")
        
        control_layout.addWidget(start_camera_btn)
        control_layout.addWidget(stop_camera_btn)
        control_layout.addWidget(QLabel(""))  # Spacer
        control_layout.addWidget(result_label)
        control_layout.addWidget(self.recognition_text)
        control_layout.addStretch()
        
        control_frame.setLayout(control_layout)
        
        camera_layout.addWidget(camera_frame)
        camera_layout.addWidget(control_frame)
        
        # Recognition log table
        log_label = QLabel("Nhật ký nhận diện:")
        log_label.setFont(QFont('Arial', 12, QFont.Bold))
        log_label.setStyleSheet("color: #2c3e50; margin: 20px 0 10px 0;")
        
        self.face_log_table = QTableWidget()
        self.face_log_table.setColumnCount(4)
        self.face_log_table.setHorizontalHeaderLabels([
            "Thời gian", "MSV", "Họ tên", "Độ tin cậy"
        ])
        self.face_log_table.setAlternatingRowColors(True)
        
        layout.addLayout(camera_layout)
        layout.addWidget(log_label)
        layout.addWidget(self.face_log_table)
        widget.setLayout(layout)
        return widget
        
    def create_code_tab(self):
        """Tạo tab mã điểm danh"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Instructions
        instruction = QLabel("🔢 Mã điểm danh: Tạo mã để sinh viên nhập vào ứng dụng")
        instruction.setFont(QFont('Arial', 12, QFont.Bold))
        instruction.setStyleSheet("color: #2c3e50; margin: 10px 0;")
        layout.addWidget(instruction)
        
        # Code creation section
        code_section = QFrame()
        code_section.setStyleSheet("""
            QFrame {
                border: 1px solid #ddd;
                border-radius: 8px;
                background-color: white;
                padding: 25px;
                margin: 10px 0;
            }
        """)
        
        code_layout = QVBoxLayout()
        
        # Manual code input
        manual_layout = QHBoxLayout()
        
        code_label = QLabel("Nhập mã điểm danh:")
        code_label.setFont(QFont('Arial', 12, QFont.Bold))
        
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("VD: LOP123, CLASS456...")
        self.code_input.setFixedHeight(40)
        self.code_input.setFont(QFont('Arial', 12))
        
        create_code_btn = QPushButton("✅ Tạo mã")
        create_code_btn.setFixedHeight(40)
        create_code_btn.setFixedWidth(100)
        create_code_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5dade2;
            }
        """)
        create_code_btn.clicked.connect(self.create_attendance_code)
        
        manual_layout.addWidget(code_label)
        manual_layout.addWidget(self.code_input)
        manual_layout.addWidget(create_code_btn)
        
        # Auto generate
        auto_layout = QHBoxLayout()
        
        auto_btn = QPushButton("🎲 Tạo mã tự động")
        auto_btn.setFixedHeight(40)
        auto_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        auto_btn.clicked.connect(self.generate_random_code)
        
        auto_layout.addWidget(auto_btn)
        auto_layout.addStretch()
        
        # Current code display
        self.current_code_label = QLabel("Mã hiện tại: Chưa tạo")
        self.current_code_label.setFont(QFont('Arial', 14, QFont.Bold))
        self.current_code_label.setStyleSheet("color: #27ae60; margin: 15px 0;")
        
        # Code settings
        settings_layout = QGridLayout()
        
        settings_layout.addWidget(QLabel("Thời gian hết hạn:"), 0, 0)
        self.expire_time = QSpinBox()
        self.expire_time.setRange(5, 120)
        self.expire_time.setValue(30)
        self.expire_time.setSuffix(" phút")
        settings_layout.addWidget(self.expire_time, 0, 1)
        
        settings_layout.addWidget(QLabel("Cho phép điểm danh muộn:"), 1, 0)
        self.allow_late = QCheckBox("Có")
        settings_layout.addWidget(self.allow_late, 1, 1)
        
        code_layout.addLayout(manual_layout)
        code_layout.addLayout(auto_layout)
        code_layout.addWidget(self.current_code_label)
        code_layout.addLayout(settings_layout)
        
        code_section.setLayout(code_layout)
        layout.addWidget(code_section)
        
        # Code usage log
        log_label = QLabel("Lịch sử sử dụng mã:")
        log_label.setFont(QFont('Arial', 12, QFont.Bold))
        log_label.setStyleSheet("color: #2c3e50;")
        
        self.code_log_table = QTableWidget()
        self.code_log_table.setColumnCount(4)
        self.code_log_table.setHorizontalHeaderLabels([
            "Thời gian", "MSV", "Họ tên", "IP Address"
        ])
        self.code_log_table.setAlternatingRowColors(True)
        
        layout.addWidget(log_label)
        layout.addWidget(self.code_log_table)
        widget.setLayout(layout)
        return widget
        
    def create_qr_tab(self):
        """Tạo tab mã QR"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Instructions
        instruction = QLabel("📱 Mã QR: Tạo mã QR cho sinh viên quét bằng điện thoại")
        instruction.setFont(QFont('Arial', 12, QFont.Bold))
        instruction.setStyleSheet("color: #2c3e50; margin: 10px 0;")
        layout.addWidget(instruction)
        
        # QR generation section
        qr_layout = QHBoxLayout()
        
        # QR display
        self.qr_frame = QFrame()
        self.qr_frame.setFixedSize(300, 300)
        self.qr_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #3498db;
                border-radius: 8px;
                background-color: white;
            }
        """)
        
        self.qr_label = QLabel("📱 Mã QR sẽ hiển thị tại đây")
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setFont(QFont('Arial', 12))
        self.qr_label.setStyleSheet("color: #7f8c8d;")
        
        qr_layout_inner = QVBoxLayout()
        qr_layout_inner.addWidget(self.qr_label)
        self.qr_frame.setLayout(qr_layout_inner)
        
        # QR controls
        control_frame = QFrame()
        control_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #ddd;
                border-radius: 8px;
                background-color: white;
                padding: 20px;
            }
        """)
        
        control_layout = QVBoxLayout()
        
        generate_qr_btn = QPushButton("🔄 Tạo mã QR")
        generate_qr_btn.setFixedHeight(50)
        generate_qr_btn.setStyleSheet("""
            QPushButton {
                background-color: #9b59b6;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #8e44ad;
            }
        """)
        generate_qr_btn.clicked.connect(self.generate_qr_code)
        
        refresh_qr_btn = QPushButton("🔄 Làm mới QR")
        refresh_qr_btn.setFixedHeight(40)
        refresh_qr_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
        """)
        
        # QR settings
        settings_label = QLabel("Cài đặt mã QR:")
        settings_label.setFont(QFont('Arial', 12, QFont.Bold))
        
        self.qr_url_input = QLineEdit()
        self.qr_url_input.setPlaceholderText("Link web điểm danh (tự động tạo)")
        self.qr_url_input.setReadOnly(True)
        
        self.qr_expire = QSpinBox()
        self.qr_expire.setRange(5, 60)
        self.qr_expire.setValue(15)
        self.qr_expire.setSuffix(" phút")
        
        control_layout.addWidget(generate_qr_btn)
        control_layout.addWidget(refresh_qr_btn)
        control_layout.addWidget(QLabel(""))  # Spacer
        control_layout.addWidget(settings_label)
        control_layout.addWidget(QLabel("Thời gian hết hạn:"))
        control_layout.addWidget(self.qr_expire)
        control_layout.addWidget(QLabel("Link web:"))
        control_layout.addWidget(self.qr_url_input)
        control_layout.addStretch()
        
        control_frame.setLayout(control_layout)
        
        qr_layout.addWidget(self.qr_frame)
        qr_layout.addWidget(control_frame)
        
        # QR usage log
        log_label = QLabel("Lịch sử sử dụng QR:")
        log_label.setFont(QFont('Arial', 12, QFont.Bold))
        log_label.setStyleSheet("color: #2c3e50; margin: 20px 0 10px 0;")
        
        self.qr_log_table = QTableWidget()
        self.qr_log_table.setColumnCount(5)
        self.qr_log_table.setHorizontalHeaderLabels([
            "Thời gian", "MSV", "Họ tên", "Thiết bị", "IP Address"
        ])
        self.qr_log_table.setAlternatingRowColors(True)
        
        layout.addLayout(qr_layout)
        layout.addWidget(log_label)
        layout.addWidget(self.qr_log_table)
        widget.setLayout(layout)
        return widget
        
    def create_monitor_tab(self):
        """Tạo tab theo dõi điểm danh"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Instructions
        instruction = QLabel("👀 Theo dõi điểm danh: Xem IP và thời gian điểm danh của sinh viên")
        instruction.setFont(QFont('Arial', 12, QFont.Bold))
        instruction.setStyleSheet("color: #2c3e50; margin: 10px 0;")
        layout.addWidget(instruction)
        
        # Real-time stats
        stats_frame = QFrame()
        stats_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #ddd;
                border-radius: 8px;
                background-color: white;
                padding: 20px;
                margin: 10px 0;
            }
        """)
        
        stats_layout = QHBoxLayout()
        
        # Create stat cards
        total_card = self.create_monitor_stat_card("Tổng SV", "45", "#3498db")
        attended_card = self.create_monitor_stat_card("Đã điểm danh", "12", "#27ae60")
        pending_card = self.create_monitor_stat_card("Chưa điểm danh", "33", "#e74c3c")
        rate_card = self.create_monitor_stat_card("Tỷ lệ", "26.7%", "#f39c12")
        
        stats_layout.addWidget(total_card)
        stats_layout.addWidget(attended_card)
        stats_layout.addWidget(pending_card)
        stats_layout.addWidget(rate_card)
        
        stats_frame.setLayout(stats_layout)
        layout.addWidget(stats_frame)
        
        # Filter and refresh
        control_layout = QHBoxLayout()
        
        filter_combo = QComboBox()
        filter_combo.addItems(["Tất cả", "Đã điểm danh", "Chưa điểm danh", "Vừa điểm danh"])
        filter_combo.setFixedHeight(35)
        
        refresh_btn = QPushButton("🔄 Làm mới")
        refresh_btn.setFixedHeight(35)
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        refresh_btn.clicked.connect(self.refresh_monitor)
        
        auto_refresh = QCheckBox("Tự động làm mới (30s)")
        auto_refresh.setChecked(True)
        
        control_layout.addWidget(QLabel("Lọc:"))
        control_layout.addWidget(filter_combo)
        control_layout.addWidget(refresh_btn)
        control_layout.addWidget(auto_refresh)
        control_layout.addStretch()
        
        # Monitor table
        self.monitor_table = QTableWidget()
        self.monitor_table.setColumnCount(7)
        self.monitor_table.setHorizontalHeaderLabels([
            "MSV", "Họ tên", "Trạng thái", "Thời gian", "Phương thức", "IP Address", "Thiết bị"
        ])
        self.monitor_table.setAlternatingRowColors(True)
        
        # Sample monitoring data
        monitor_data = [
            ["2021001", "Nguyễn Văn A", "Có mặt", "08:15:30", "Mã QR", "192.168.1.15", "iPhone 12"],
            ["2021003", "Lê Văn C", "Có mặt", "08:16:45", "Mã code", "192.168.1.23", "Android"],
            ["2021007", "Hoàng Thị F", "Có mặt", "08:17:12", "Khuôn mặt", "192.168.1.8", "Camera GV"],
            ["2021002", "Trần Thị B", "Chưa điểm danh", "-", "-", "-", "-"],
            ["2021004", "Phạm Thị D", "Chưa điểm danh", "-", "-", "-", "-"]
        ]
        
        self.monitor_table.setRowCount(len(monitor_data))
        for i, row in enumerate(monitor_data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                
                # Color coding for status
                if j == 2 and value == "Có mặt":
                    item.setStyleSheet("color: #27ae60; font-weight: bold;")
                elif j == 2 and value == "Chưa điểm danh":
                    item.setStyleSheet("color: #e74c3c; font-weight: bold;")
                    
                self.monitor_table.setItem(i, j, item)
        
        layout.addLayout(control_layout)
        layout.addWidget(self.monitor_table)
        
        # Setup auto refresh timer
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.refresh_monitor)
        if auto_refresh.isChecked():
            self.refresh_timer.start(30000)  # 30 seconds
        
        auto_refresh.toggled.connect(self.toggle_auto_refresh)
        
        widget.setLayout(layout)
        return widget
        
    def create_monitor_stat_card(self, title, value, color):
        """Tạo thẻ thống kê cho monitor"""
        card = QFrame()
        card.setFixedHeight(80)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                border-left: 4px solid {color};
            }}
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 10, 15, 10)
        
        title_label = QLabel(title)
        title_label.setFont(QFont('Arial', 10))
        title_label.setStyleSheet("color: #7f8c8d;")
        
        value_label = QLabel(value)
        value_label.setFont(QFont('Arial', 18, QFont.Bold))
        value_label.setStyleSheet(f"color: {color};")
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        card.setLayout(layout)
        
        return card
        
    # Event handlers
    def toggle_attendance(self, row, status_type, checked):
        """Toggle attendance status (0=present, 1=absent_permitted, 2=absent_not_permitted)"""
        if checked:
            # Uncheck other status checkboxes in the same row
            for col in range(2, 5):  # Columns 2, 3, 4
                if col != status_type + 2:
                    checkbox = self.manual_table.cellWidget(row, col)
                    if checkbox:
                        checkbox.setChecked(False)
                        
    def select_all_present(self):
        """Select all students as present"""
        for row in range(self.manual_table.rowCount()):
            present_cb = self.manual_table.cellWidget(row, 2)
            if present_cb:
                present_cb.setChecked(True)
                
    def clear_all_selection(self):
        """Clear all attendance selections"""
        for row in range(self.manual_table.rowCount()):
            for col in range(2, 5):
                checkbox = self.manual_table.cellWidget(row, col)
                if checkbox:
                    checkbox.setChecked(False)
                    
    def create_attendance_code(self):
        """Create attendance code"""
        code = self.code_input.text().strip().upper()
        if code:
            self.attendance_code = code
            self.current_code_label.setText(f"Mã hiện tại: {code}")
            self.current_code_label.setStyleSheet("color: #27ae60; margin: 15px 0; font-weight: bold;")
            QMessageBox.information(self, "Thành công", f"Đã tạo mã điểm danh: {code}")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập mã điểm danh!")
            
    def generate_random_code(self):
        """Generate random attendance code"""
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.code_input.setText(code)
        self.create_attendance_code()
        
    def generate_qr_code(self):
        """Generate QR code"""
        if not self.attendance_code:
            self.generate_random_code()
            
        # Create web URL for QR
        web_url = f"https://attendance.edu.vn/check-in?code={self.attendance_code}&class={self.lhp_code}"
        self.qr_url_input.setText(web_url)
        
        # Generate QR code image
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(web_url)
            qr.make(fit=True)
            
            qr_img = qr.make_image(fill_color="black", back_color="white")
            
            # Convert to QPixmap and display
            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            qr_pixmap = QPixmap()
            qr_pixmap.loadFromData(buffer.getvalue())
            
            # Scale to fit frame
            scaled_pixmap = qr_pixmap.scaled(280, 280, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            self.qr_label.setPixmap(scaled_pixmap)
            self.qr_label.setText("")
            
            QMessageBox.information(self, "Thành công", "Đã tạo mã QR thành công!")
            
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể tạo mã QR: {str(e)}")
            
    def refresh_monitor(self):
        """Refresh monitoring data"""
        # In real application, this would fetch data from server
        QMessageBox.information(self, "Thông báo", "Đã làm mới dữ liệu theo dõi!")
        
    def toggle_auto_refresh(self, checked):
        """Toggle auto refresh timer"""
        if checked:
            self.refresh_timer.start(30000)
        else:
            self.refresh_timer.stop()
            
    def save_attendance(self):
        """Save attendance data"""
        QMessageBox.information(self, "Thành công", "Đã lưu dữ liệu điểm danh!")
        
    def closeEvent(self, event):
        """Handle window close event"""
        reply = QMessageBox.question(self, 'Xác nhận', 
                                   'Bạn có chắc chắn muốn đóng cửa sổ điểm danh?\n'
                                   'Dữ liệu chưa lưu sẽ bị mất!',
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
