from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QStackedWidget, QMessageBox,
                             QTableWidget, QTableWidgetItem, QLineEdit, QTabWidget,
                             QProgressBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ui.common.base_window import BaseMainWindow

class WSinhVienMain(BaseMainWindow):
    """Cửa sổ chính cho Sinh viên"""
    
    def __init__(self, full_name, role):
        super().__init__(full_name, role)
        self.setup_sinhvien_ui()
        
    def setup_sinhvien_ui(self):
        """Thiết lập giao diện Sinh viên"""
        self.setWindowTitle('Hệ thống điểm danh - Sinh viên')
        
        # Create warning banner
        self.create_warning_banner()
        
        # Create content pages
        self.create_content_pages()
        
        # Create navigation
        self.create_navigation()
        
        # Show default page
        self.show_diemdanh_tab()
        
    def create_warning_banner(self):
        """Tạo thanh cảnh báo chuyên cần"""
        # Calculate attendance rate (mock data)
        self.attendance_rate = 85.5  # Mock: 85.5%
        self.absent_rate = 14.5  # 100 - attendance_rate
        
        # Determine warning level
        if self.absent_rate >= 20:
            warning_color = "#e74c3c"  # Red
            warning_text = "🚨 CẢNH BÁO ĐỎ: Tỷ lệ vắng mặt quá cao!"
            warning_detail = f"Bạn đã vắng {self.absent_rate:.1f}% (≥20%). Có nguy cơ bị cấm thi!"
        elif self.absent_rate >= 10:
            warning_color = "#f39c12"  # Yellow/Orange
            warning_text = "⚠️ CẢNH BÁO VÀNG: Chú ý chuyên cần"
            warning_detail = f"Bạn đã vắng {self.absent_rate:.1f}% (10-20%). Cần cải thiện việc tham gia lớp."
        else:
            warning_color = "#27ae60"  # Green
            warning_text = "✅ CHUYÊN CẦN TỐT"
            warning_detail = f"Bạn đã vắng {self.absent_rate:.1f}% (<10%). Hãy duy trì!"
            
        # Insert warning banner at the top
        banner = QFrame()
        banner.setFixedHeight(60)
        banner.setStyleSheet(f"""
            QFrame {{
                background-color: {warning_color};
                border: none;
                margin: 0;
            }}
        """)
        
        banner_layout = QHBoxLayout()
        banner_layout.setContentsMargins(20, 10, 20, 10)
        
        warning_label = QLabel(warning_text)
        warning_label.setFont(QFont('Arial', 14, QFont.Bold))
        warning_label.setStyleSheet("color: white;")
        
        detail_label = QLabel(warning_detail)
        detail_label.setFont(QFont('Arial', 11))
        detail_label.setStyleSheet("color: white;")
        
        banner_layout.addWidget(warning_label)
        banner_layout.addWidget(detail_label)
        banner_layout.addStretch()
        
        banner.setLayout(banner_layout)
        
        # Add banner to the top of main widget
        main_widget = self.centralWidget()
        main_layout = main_widget.layout()
        main_layout.insertWidget(0, banner)
        
    def create_content_pages(self):
        """Tạo các trang nội dung"""
        # Tab Điểm danh
        self.diemdanh_tab = self.create_diemdanh_tab()
        self.content_area.addWidget(self.diemdanh_tab)
        
        # Tab Lịch học & Chuyên cần
        self.lichhoc_tab = self.create_lichhoc_tab()
        self.content_area.addWidget(self.lichhoc_tab)
        
    def create_diemdanh_tab(self):
        """Tạo tab điểm danh"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Điểm danh")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Current classes info
        current_classes_frame = QFrame()
        current_classes_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
            }
        """)
        
        classes_layout = QVBoxLayout()
        classes_title = QLabel("Lớp học phần hôm nay")
        classes_title.setFont(QFont('Arial', 16, QFont.Bold))
        classes_title.setStyleSheet("color: #2c3e50; margin-bottom: 15px;")
        classes_layout.addWidget(classes_title)
        
        # Today's classes
        today_classes = [
            "🕒 07:00-09:30: Lập trình căn bản A1 - Phòng 101",
            "🕒 13:30-16:00: Cấu trúc dữ liệu B1 - Phòng 205"
        ]
        
        for class_info in today_classes:
            class_label = QLabel(class_info)
            class_label.setFont(QFont('Arial', 11))
            class_label.setStyleSheet("color: #7f8c8d; padding: 5px 0;")
            classes_layout.addWidget(class_label)
            
        current_classes_frame.setLayout(classes_layout)
        layout.addWidget(current_classes_frame)
        
        # Code input section
        code_section = QFrame()
        code_section.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 30px;
            }
        """)
        
        code_layout = QVBoxLayout()
        
        code_title = QLabel("Nhập mã điểm danh")
        code_title.setFont(QFont('Arial', 18, QFont.Bold))
        code_title.setStyleSheet("color: #2c3e50; margin-bottom: 15px;")
        code_layout.addWidget(code_title)
        
        code_instruction = QLabel("Nhập mã điểm danh mà giảng viên cung cấp:")
        code_instruction.setFont(QFont('Arial', 12))
        code_instruction.setStyleSheet("color: #7f8c8d; margin-bottom: 20px;")
        code_layout.addWidget(code_instruction)
        
        # Code input
        input_layout = QHBoxLayout()
        
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Nhập mã điểm danh (VD: LOP123)")
        self.code_input.setFont(QFont('Arial', 14))
        self.code_input.setFixedHeight(50)
        self.code_input.setStyleSheet("""
            QLineEdit {
                padding: 10px 15px;
                border: 2px solid #ddd;
                border-radius: 8px;
                background-color: #f8f9fa;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #3498db;
                background-color: white;
            }
        """)
        self.code_input.returnPressed.connect(self.submit_attendance_code)
        
        submit_btn = QPushButton("✅ Điểm danh")
        submit_btn.setFixedSize(120, 50)
        submit_btn.setFont(QFont('Arial', 12, QFont.Bold))
        submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:pressed {
                background-color: #229954;
            }
        """)
        submit_btn.clicked.connect(self.submit_attendance_code)
        
        input_layout.addWidget(self.code_input)
        input_layout.addWidget(submit_btn)
        
        code_layout.addLayout(input_layout)
        
        # Recent attendance status
        status_label = QLabel("Trạng thái điểm danh gần đây:")
        status_label.setFont(QFont('Arial', 14, QFont.Bold))
        status_label.setStyleSheet("color: #2c3e50; margin: 30px 0 15px 0;")
        code_layout.addWidget(status_label)
        
        recent_status = [
            "✅ 14/11/2024 - Lập trình căn bản A1: Có mặt",
            "✅ 13/11/2024 - Cấu trúc dữ liệu B1: Có mặt",
            "❌ 12/11/2024 - Lập trình căn bản A1: Vắng không phép",
            "⚠️ 11/11/2024 - Cấu trúc dữ liệu B1: Vắng có phép"
        ]
        
        for status in recent_status:
            status_item = QLabel(status)
            status_item.setFont(QFont('Arial', 11))
            status_item.setStyleSheet("color: #7f8c8d; padding: 3px 0;")
            code_layout.addWidget(status_item)
        
        code_section.setLayout(code_layout)
        layout.addWidget(code_section)
        
        layout.addStretch()
        tab.setLayout(layout)
        return tab
        
    def create_lichhoc_tab(self):
        """Tạo tab lịch học & chuyên cần"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Lịch học & Chuyên cần")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Attendance statistics
        stats_frame = QFrame()
        stats_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 25px;
                margin-bottom: 20px;
            }
        """)
        
        stats_layout = QVBoxLayout()
        
        stats_title = QLabel("Thống kê chuyên cần cá nhân")
        stats_title.setFont(QFont('Arial', 18, QFont.Bold))
        stats_title.setStyleSheet("color: #2c3e50; margin-bottom: 15px;")
        stats_layout.addWidget(stats_title)
        
        # Progress bars for each subject
        subjects_stats = [
            ("Lập trình căn bản A1", 92.5, "#27ae60"),
            ("Cấu trúc dữ liệu B1", 87.5, "#f39c12"),
            ("OOP A1", 95.0, "#27ae60"),
            ("Cơ sở dữ liệu B2", 82.5, "#f39c12")
        ]
        
        for subject, rate, color in subjects_stats:
            subject_frame = QFrame()
            subject_frame.setStyleSheet("margin: 10px 0;")
            subject_layout = QVBoxLayout()
            subject_layout.setContentsMargins(0, 5, 0, 5)
            
            subject_label = QLabel(f"{subject} - {rate:.1f}%")
            subject_label.setFont(QFont('Arial', 12, QFont.Bold))
            subject_label.setStyleSheet("color: #2c3e50;")
            
            progress = QProgressBar()
            progress.setFixedHeight(20)
            progress.setValue(int(rate))
            progress.setStyleSheet(f"""
                QProgressBar {{
                    border: 1px solid #ddd;
                    border-radius: 10px;
                    text-align: center;
                    color: white;
                    font-weight: bold;
                }}
                QProgressBar::chunk {{
                    background-color: {color};
                    border-radius: 9px;
                }}
            """)
            
            subject_layout.addWidget(subject_label)
            subject_layout.addWidget(progress)
            subject_frame.setLayout(subject_layout)
            stats_layout.addWidget(subject_frame)
        
        # Overall statistics
        overall_label = QLabel(f"Tổng tỷ lệ chuyên cần: {self.attendance_rate:.1f}%")
        overall_label.setFont(QFont('Arial', 14, QFont.Bold))
        overall_label.setStyleSheet("color: #3498db; margin-top: 15px;")
        stats_layout.addWidget(overall_label)
        
        stats_frame.setLayout(stats_layout)
        layout.addWidget(stats_frame)
        
        # Schedule table
        schedule_title = QLabel("Danh sách tất cả buổi học")
        schedule_title.setFont(QFont('Arial', 18, QFont.Bold))
        schedule_title.setStyleSheet("color: #2c3e50; margin-bottom: 15px;")
        layout.addWidget(schedule_title)
        
        self.schedule_table = QTableWidget()
        self.schedule_table.setColumnCount(6)
        self.schedule_table.setHorizontalHeaderLabels([
            "Ngày", "Môn học", "Giờ học", "Phòng", "Trạng thái", "Ghi chú"
        ])
        self.schedule_table.setAlternatingRowColors(True)
        self.schedule_table.setStyleSheet("""
            QTableWidget {
                gridline-color: #ddd;
                selection-background-color: #3498db;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 10px;
                font-weight: bold;
            }
        """)
        
        # Sample schedule data
        schedule_data = [
            ["15/11/2024", "Lập trình căn bản A1", "07:00-09:30", "101", "Có mặt", ""],
            ["15/11/2024", "Cấu trúc dữ liệu B1", "13:30-16:00", "205", "Chưa học", ""],
            ["14/11/2024", "Lập trình căn bản A1", "07:00-09:30", "101", "Có mặt", ""],
            ["14/11/2024", "OOP A1", "10:00-12:30", "203", "Có mặt", ""],
            ["13/11/2024", "Cấu trúc dữ liệu B1", "13:30-16:00", "205", "Có mặt", ""],
            ["12/11/2024", "Lập trình căn bản A1", "07:00-09:30", "101", "Vắng KP", "Ốm"],
            ["12/11/2024", "Cơ sở dữ liệu B2", "15:00-17:30", "301", "Có mặt", ""],
            ["11/11/2024", "Cấu trúc dữ liệu B1", "13:30-16:00", "205", "Vắng P", "Có đơn"]
        ]
        
        self.schedule_table.setRowCount(len(schedule_data))
        for i, row in enumerate(schedule_data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                
                # Color coding for status
                if j == 4:  # Status column
                    if value == "Có mặt":
                        from PyQt5.QtGui import QColor
                        item.setForeground(QColor("#27ae60"))
                    elif value == "Vắng KP":
                        from PyQt5.QtGui import QColor
                        item.setForeground(QColor("#e74c3c"))
                    elif value == "Vắng P":
                        from PyQt5.QtGui import QColor
                        item.setForeground(QColor("#f39c12"))
                    elif value == "Chưa học":
                        from PyQt5.QtGui import QColor
                        item.setForeground(QColor("#95a5a6"))
                
                self.schedule_table.setItem(i, j, item)
        
        layout.addWidget(self.schedule_table)
        tab.setLayout(layout)
        return tab
        
    def create_navigation(self):
        """Tạo menu điều hướng"""
        # Điểm danh tab
        diemdanh_btn = self.add_nav_button("Điểm danh", "✅")
        diemdanh_btn.clicked.connect(self.show_diemdanh_tab)
        
        # Lịch học tab
        lichhoc_btn = self.add_nav_button("Lịch học & Chuyên cần", "📅")
        lichhoc_btn.clicked.connect(self.show_lichhoc_tab)
        
    def show_diemdanh_tab(self):
        """Hiển thị tab điểm danh"""
        self.content_area.setCurrentWidget(self.diemdanh_tab)
        
    def show_lichhoc_tab(self):
        """Hiển thị tab lịch học"""
        self.content_area.setCurrentWidget(self.lichhoc_tab)
        
    def submit_attendance_code(self):
        """Xử lý submit mã điểm danh"""
        code = self.code_input.text().strip().upper()
        
        if not code:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập mã điểm danh!")
            return
            
        # Mock validation
        valid_codes = ["LOP123", "CLASS456", "ATTENDANCE789"]
        
        if code in valid_codes:
            QMessageBox.information(
                self, 
                "Thành công", 
                f"Điểm danh thành công với mã: {code}\n"
                "Trạng thái: Có mặt\n"
                "Thời gian: " + "15/11/2024 08:30"
            )
            self.code_input.clear()
            
            # Update recent status (in real app, this would refresh from server)
            
        else:
            QMessageBox.warning(
                self, 
                "Lỗi", 
                f"Mã điểm danh '{code}' không hợp lệ!\n"
                "Vui lòng kiểm tra lại mã từ giảng viên."
            )
