from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QLineEdit, QTextEdit, QFrame, 
                             QMessageBox, QTabWidget, QGroupBox, QFormLayout,
                             QComboBox, QDateEdit, QFileDialog, QProgressBar)
from PyQt5.QtCore import Qt, QDate, QTimer
from PyQt5.QtGui import QFont, QPixmap

class WAdminChiTietSV(QMainWindow):
    """Cửa sổ Chi tiết Sinh viên cho Admin"""
    
    def __init__(self, msv):
        super().__init__()
        self.msv = msv
        self.init_ui()
        self.load_student_data()
        
    def init_ui(self):
        self.setWindowTitle(f'Chi tiết sinh viên - {self.msv}')
        self.setGeometry(100, 100, 900, 700)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        header = self.create_header()
        layout.addWidget(header)
        
        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #ddd;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #f8f9fa;
                padding: 10px 20px;
                margin: 2px;
            }
            QTabBar::tab:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        
        # Tab 1: Thông tin cá nhân
        self.info_tab = self.create_info_tab()
        self.tabs.addTab(self.info_tab, "👤 Thông tin cá nhân")
        
        # Tab 2: Đăng ký khuôn mặt
        self.face_tab = self.create_face_tab()
        self.tabs.addTab(self.face_tab, "📷 Đăng ký Khuôn mặt")
        
        # Tab 3: Lịch sử điểm danh
        self.history_tab = self.create_history_tab()
        self.tabs.addTab(self.history_tab, "📊 Lịch sử điểm danh")
        
        layout.addWidget(self.tabs)
        
        # Bottom buttons
        bottom_layout = QHBoxLayout()
        
        save_btn = QPushButton("💾 Lưu thay đổi")
        save_btn.setFixedHeight(40)
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        save_btn.clicked.connect(self.save_changes)
        
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
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        close_btn.clicked.connect(self.close)
        
        bottom_layout.addWidget(save_btn)
        bottom_layout.addStretch()
        bottom_layout.addWidget(close_btn)
        
        layout.addLayout(bottom_layout)
        main_widget.setLayout(layout)
        
    def create_header(self):
        """Tạo header thông tin sinh viên"""
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
        
        # Student avatar (placeholder)
        avatar_frame = QFrame()
        avatar_frame.setFixedSize(80, 80)
        avatar_frame.setStyleSheet("""
            QFrame {
                background-color: #ecf0f1;
                border-radius: 40px;
                border: 2px solid white;
            }
        """)
        
        avatar_label = QLabel("📷")
        avatar_label.setAlignment(Qt.AlignCenter)
        avatar_label.setFont(QFont('Arial', 24))
        
        avatar_layout = QVBoxLayout()
        avatar_layout.addWidget(avatar_label)
        avatar_frame.setLayout(avatar_layout)
        
        # Student info
        info_layout = QVBoxLayout()
        
        self.student_name = QLabel(f"Đang tải...")
        self.student_name.setFont(QFont('Arial', 16, QFont.Bold))
        
        self.student_class = QLabel(f"MSV: {self.msv}")
        self.student_class.setFont(QFont('Arial', 12))
        
        self.student_status = QLabel("Trạng thái: Hoạt động")
        self.student_status.setFont(QFont('Arial', 11))
        self.student_status.setStyleSheet("color: #2ecc71;")
        
        info_layout.addWidget(self.student_name)
        info_layout.addWidget(self.student_class)
        info_layout.addWidget(self.student_status)
        
        layout.addWidget(avatar_frame)
        layout.addLayout(info_layout)
        layout.addStretch()
        
        header.setLayout(layout)
        return header
        
    def create_info_tab(self):
        """Tạo tab thông tin cá nhân"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Personal information form
        personal_group = QGroupBox("Thông tin cá nhân")
        personal_group.setFont(QFont('Arial', 12, QFont.Bold))
        personal_layout = QFormLayout()
        
        self.ho_input = QLineEdit()
        self.ten_input = QLineEdit()
        self.email_input = QLineEdit()
        self.sdt_input = QLineEdit()
        self.ngaysinh_input = QDateEdit()
        self.ngaysinh_input.setDate(QDate.currentDate().addYears(-20))
        
        personal_layout.addRow("Họ và tên đệm:", self.ho_input)
        personal_layout.addRow("Tên:", self.ten_input)
        personal_layout.addRow("Email:", self.email_input)
        personal_layout.addRow("Số điện thoại:", self.sdt_input)
        personal_layout.addRow("Ngày sinh:", self.ngaysinh_input)
        
        personal_group.setLayout(personal_layout)
        
        # Academic information
        academic_group = QGroupBox("Thông tin học tập")
        academic_group.setFont(QFont('Arial', 12, QFont.Bold))
        academic_layout = QFormLayout()
        
        self.lop_combo = QComboBox()
        self.lop_combo.addItems(["CNTT01", "CNTT02", "KT01", "QTKD01"])
        
        self.khoa_combo = QComboBox()
        self.khoa_combo.addItems(["Công nghệ Thông tin", "Kế toán", "Quản trị Kinh doanh"])
        
        self.nienkhoa_input = QLineEdit()
        self.trangthai_combo = QComboBox()
        self.trangthai_combo.addItems(["Hoạt động", "Tạm dừng", "Thôi học"])
        
        academic_layout.addRow("Lớp hành chính:", self.lop_combo)
        academic_layout.addRow("Khoa:", self.khoa_combo)
        academic_layout.addRow("Niên khóa:", self.nienkhoa_input)
        academic_layout.addRow("Trạng thái:", self.trangthai_combo)
        
        academic_group.setLayout(academic_layout)
        
        # Contact information
        contact_group = QGroupBox("Thông tin liên hệ")
        contact_group.setFont(QFont('Arial', 12, QFont.Bold))
        contact_layout = QFormLayout()
        
        self.diachi_input = QTextEdit()
        self.diachi_input.setFixedHeight(80)
        
        self.nguoi_lienhe_input = QLineEdit()
        self.sdt_lienhe_input = QLineEdit()
        
        contact_layout.addRow("Địa chỉ:", self.diachi_input)
        contact_layout.addRow("Người liên hệ khẩn cấp:", self.nguoi_lienhe_input)
        contact_layout.addRow("SĐT liên hệ khẩn cấp:", self.sdt_lienhe_input)
        
        contact_group.setLayout(contact_layout)
        
        layout.addWidget(personal_group)
        layout.addWidget(academic_group)
        layout.addWidget(contact_group)
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
        
    def create_face_tab(self):
        """Tạo tab đăng ký khuôn mặt"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Instructions
        instruction = QLabel("📷 Đăng ký khuôn mặt cho sinh viên để sử dụng chức năng điểm danh tự động")
        instruction.setFont(QFont('Arial', 12, QFont.Bold))
        instruction.setStyleSheet("color: #2c3e50; margin: 10px 0;")
        layout.addWidget(instruction)
        
        # Face registration section
        face_layout = QHBoxLayout()
        
        # Camera preview
        camera_frame = QFrame()
        camera_frame.setFixedSize(400, 300)
        camera_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #3498db;
                border-radius: 8px;
                background-color: #ecf0f1;
            }
        """)
        
        self.camera_label = QLabel("📷 Camera Preview\n(Chức năng đang phát triển)")
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.camera_label.setFont(QFont('Arial', 12))
        self.camera_label.setStyleSheet("color: #7f8c8d;")
        
        camera_layout = QVBoxLayout()
        camera_layout.addWidget(self.camera_label)
        camera_frame.setLayout(camera_layout)
        
        # Control panel
        control_frame = QFrame()
        control_frame.setFixedWidth(300)
        control_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #ddd;
                border-radius: 8px;
                background-color: white;
                padding: 20px;
            }
        """)
        
        control_layout = QVBoxLayout()
        
        # Face registration status
        status_label = QLabel("Trạng thái đăng ký:")
        status_label.setFont(QFont('Arial', 12, QFont.Bold))
        
        self.face_status = QLabel("❌ Chưa đăng ký")
        self.face_status.setFont(QFont('Arial', 11))
        self.face_status.setStyleSheet("color: #e74c3c;")
        
        # Progress bar
        self.face_progress = QProgressBar()
        self.face_progress.setVisible(False)
        
        # Control buttons
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
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        start_camera_btn.clicked.connect(self.start_face_registration)
        
        capture_btn = QPushButton("📸 Chụp ảnh")
        capture_btn.setFixedHeight(40)
        capture_btn.setStyleSheet("""
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
        capture_btn.clicked.connect(self.capture_face)
        
        record_btn = QPushButton("🎥 Quay video")
        record_btn.setFixedHeight(40)
        record_btn.setStyleSheet("""
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
        record_btn.clicked.connect(self.record_face_video)
        
        save_face_btn = QPushButton("💾 Lưu đăng ký")
        save_face_btn.setFixedHeight(40)
        save_face_btn.setStyleSheet("""
            QPushButton {
                background-color: #9b59b6;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #8e44ad;
            }
        """)
        save_face_btn.clicked.connect(self.save_face_registration)
        
        delete_face_btn = QPushButton("🗑️ Xóa đăng ký")
        delete_face_btn.setFixedHeight(40)
        delete_face_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        delete_face_btn.clicked.connect(self.delete_face_registration)
        
        control_layout.addWidget(status_label)
        control_layout.addWidget(self.face_status)
        control_layout.addWidget(self.face_progress)
        control_layout.addWidget(QLabel(""))  # Spacer
        control_layout.addWidget(start_camera_btn)
        control_layout.addWidget(capture_btn)
        control_layout.addWidget(record_btn)
        control_layout.addWidget(QLabel(""))  # Spacer
        control_layout.addWidget(save_face_btn)
        control_layout.addWidget(delete_face_btn)
        control_layout.addStretch()
        
        control_frame.setLayout(control_layout)
        
        face_layout.addWidget(camera_frame)
        face_layout.addWidget(control_frame)
        
        # Instructions
        instructions_text = QTextEdit()
        instructions_text.setFixedHeight(100)
        instructions_text.setPlainText(
            "Hướng dẫn đăng ký khuôn mặt:\n"
            "1. Bấm 'Bật Camera' để mở camera\n"
            "2. Chụp 5-10 ảnh ở các góc độ khác nhau\n"
            "3. Hoặc quay video 10-15 giây\n"
            "4. Bấm 'Lưu đăng ký' để hoàn tất"
        )
        instructions_text.setReadOnly(True)
        
        layout.addLayout(face_layout)
        layout.addWidget(QLabel("Hướng dẫn:"))
        layout.addWidget(instructions_text)
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
        
    def create_history_tab(self):
        """Tạo tab lịch sử điểm danh"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Statistics summary
        stats_frame = QFrame()
        stats_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #ddd;
                border-radius: 8px;
                background-color: white;
                padding: 20px;
                margin-bottom: 20px;
            }
        """)
        
        stats_layout = QHBoxLayout()
        
        # Create summary cards
        total_card = self.create_summary_card("Tổng buổi học", "47", "#3498db")
        present_card = self.create_summary_card("Có mặt", "41", "#27ae60")
        absent_p_card = self.create_summary_card("Vắng có phép", "2", "#f39c12")
        absent_np_card = self.create_summary_card("Vắng không phép", "4", "#e74c3c")
        rate_card = self.create_summary_card("Tỷ lệ chuyên cần", "87.2%", "#9b59b6")
        
        stats_layout.addWidget(total_card)
        stats_layout.addWidget(present_card)
        stats_layout.addWidget(absent_p_card)
        stats_layout.addWidget(absent_np_card)
        stats_layout.addWidget(rate_card)
        
        stats_frame.setLayout(stats_layout)
        layout.addWidget(stats_frame)
        
        # Placeholder for attendance history table
        history_label = QLabel("📊 Lịch sử điểm danh chi tiết (Đang phát triển)")
        history_label.setFont(QFont('Arial', 14))
        history_label.setAlignment(Qt.AlignCenter)
        history_label.setStyleSheet("color: #7f8c8d; padding: 50px;")
        
        layout.addWidget(history_label)
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
        
    def create_summary_card(self, title, value, color):
        """Tạo thẻ tóm tắt"""
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
        value_label.setFont(QFont('Arial', 16, QFont.Bold))
        value_label.setStyleSheet(f"color: {color};")
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        card.setLayout(layout)
        
        return card
        
    def load_student_data(self):
        """Tải dữ liệu sinh viên"""
        # Mock data - in real app, load from database
        student_data = {
            "2021001": {
                "ho": "Nguyễn Văn",
                "ten": "A",
                "email": "nva@student.edu",
                "sdt": "0901234567",
                "lop": "CNTT01",
                "khoa": "Công nghệ Thông tin",
                "nienkhoa": "2021-2025",
                "face_registered": True
            }
        }
        
        if self.msv in student_data:
            data = student_data[self.msv]
            
            # Update header
            self.student_name.setText(f"{data['ho']} {data['ten']}")
            self.student_class.setText(f"MSV: {self.msv} - Lớp: {data['lop']}")
            
            # Update form
            self.ho_input.setText(data['ho'])
            self.ten_input.setText(data['ten'])
            self.email_input.setText(data['email'])
            self.sdt_input.setText(data['sdt'])
            self.lop_combo.setCurrentText(data['lop'])
            self.khoa_combo.setCurrentText(data['khoa'])
            self.nienkhoa_input.setText(data['nienkhoa'])
            
            # Update face registration status
            if data['face_registered']:
                self.face_status.setText("✅ Đã đăng ký")
                self.face_status.setStyleSheet("color: #27ae60;")
        
    # Event handlers
    def start_face_registration(self):
        QMessageBox.information(self, "Thông báo", "Chức năng bật camera đang được phát triển!")
        
    def capture_face(self):
        QMessageBox.information(self, "Thông báo", "Chức năng chụp ảnh đang được phát triển!")
        
    def record_face_video(self):
        QMessageBox.information(self, "Thông báo", "Chức năng quay video đang được phát triển!")
        
    def save_face_registration(self):
        QMessageBox.information(self, "Thành công", "Đã lưu đăng ký khuôn mặt thành công!")
        self.face_status.setText("✅ Đã đăng ký")
        self.face_status.setStyleSheet("color: #27ae60;")
        
    def delete_face_registration(self):
        reply = QMessageBox.question(self, 'Xác nhận', 
                                   'Bạn có chắc chắn muốn xóa đăng ký khuôn mặt?',
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Thành công", "Đã xóa đăng ký khuôn mặt!")
            self.face_status.setText("❌ Chưa đăng ký")
            self.face_status.setStyleSheet("color: #e74c3c;")
        
    def save_changes(self):
        QMessageBox.information(self, "Thành công", "Đã lưu thay đổi thông tin sinh viên!")
        
    def closeEvent(self, event):
        event.accept()
