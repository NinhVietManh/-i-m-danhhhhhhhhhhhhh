from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QStackedWidget, QMessageBox,
                             QTableWidget, QTableWidgetItem, QComboBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ui.common.base_window import BaseMainWindow

class WGiangVienMain(BaseMainWindow):
    """Cửa sổ chính cho Giảng viên"""
    
    def __init__(self, full_name, role):
        super().__init__(full_name, role)
        self.setup_giangvien_ui()
        
    def setup_giangvien_ui(self):
        """Thiết lập giao diện Giảng viên"""
        self.setWindowTitle('Hệ thống điểm danh - Giảng viên')
        
        # Create content pages
        self.create_content_pages()
        
        # Create navigation
        self.create_navigation()
        
        # Show default page
        self.show_dashboard()
        
    def create_content_pages(self):
        """Tạo các trang nội dung"""
        # Dashboard page
        self.dashboard_page = self.create_dashboard_page()
        self.content_area.addWidget(self.dashboard_page)
        
        # Lớp học phần page
        self.lophocphan_page = self.create_lophocphan_page()
        self.content_area.addWidget(self.lophocphan_page)
        
        # Báo cáo page
        self.baocao_page = self.create_baocao_page()
        self.content_area.addWidget(self.baocao_page)
        
    def create_dashboard_page(self):
        """Tạo trang dashboard"""
        dashboard = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Dashboard Giảng viên")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Statistics cards
        stats_layout = QHBoxLayout()
        
        # Create stat cards
        cards_data = [
            ("📚 Lớp phụ trách", "5", "#3498db"),
            ("👨‍🎓 Tổng sinh viên", "187", "#27ae60"),
            ("📅 Buổi học hôm nay", "3", "#f39c12"),
            ("✅ Đã điểm danh", "2", "#9b59b6")
        ]
        
        for title_text, value, color in cards_data:
            card = self.create_stat_card(title_text, value, color)
            stats_layout.addWidget(card)
            
        layout.addLayout(stats_layout)
        
        # Today's schedule
        schedule_title = QLabel("Lịch dạy hôm nay")
        schedule_title.setFont(QFont('Arial', 18, QFont.Bold))
        schedule_title.setStyleSheet("color: #2c3e50; margin: 30px 0 15px 0;")
        layout.addWidget(schedule_title)
        
        schedule_frame = QFrame()
        schedule_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        schedule_layout = QVBoxLayout()
        
        schedules = [
            "🕒 07:00-09:30: Lập trình căn bản A1 - Phòng 101 - 45 SV",
            "🕒 10:00-12:30: Cấu trúc dữ liệu B1 - Phòng 205 - 38 SV", 
            "🕒 13:30-16:00: Lập trình căn bản A2 - Phòng 101 - 42 SV"
        ]
        
        for i, schedule_text in enumerate(schedules):
            schedule_item = QFrame()
            schedule_item.setStyleSheet("""
                QFrame {
                    background-color: #f8f9fa;
                    border-left: 4px solid #3498db;
                    margin: 5px 0;
                    padding: 10px;
                    border-radius: 5px;
                }
            """)
            
            item_layout = QHBoxLayout()
            item_layout.setContentsMargins(10, 5, 10, 5)
            
            schedule_label = QLabel(schedule_text)
            schedule_label.setFont(QFont('Arial', 11))
            schedule_label.setStyleSheet("color: #2c3e50;")
            
            action_btn = QPushButton("Điểm danh")
            action_btn.setFixedSize(80, 30)
            action_btn.setStyleSheet("""
                QPushButton {
                    background-color: #27ae60;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    font-size: 10px;
                }
                QPushButton:hover {
                    background-color: #2ecc71;
                }
            """)
            action_btn.clicked.connect(lambda checked, idx=i: self.open_diemdanh(idx))
            
            item_layout.addWidget(schedule_label)
            item_layout.addStretch()
            item_layout.addWidget(action_btn)
            schedule_item.setLayout(item_layout)
            
            schedule_layout.addWidget(schedule_item)
            
        schedule_frame.setLayout(schedule_layout)
        layout.addWidget(schedule_frame)
        
        # Quick stats
        stats_title = QLabel("Thống kê nhanh")
        stats_title.setFont(QFont('Arial', 18, QFont.Bold))
        stats_title.setStyleSheet("color: #2c3e50; margin: 30px 0 15px 0;")
        layout.addWidget(stats_title)
        
        stats_frame = QFrame()
        stats_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        stats_frame_layout = QVBoxLayout()
        
        quick_stats = [
            "📊 Tỷ lệ điểm danh trung bình: 92.5%",
            "⚠️ Sinh viên vắng mặt nhiều: 3 người",
            "📈 Xu hướng điểm danh: Ổn định",
            "🎯 Mục tiêu tháng này: Tỷ lệ >95%"
        ]
        
        for stat in quick_stats:
            stat_label = QLabel(stat)
            stat_label.setFont(QFont('Arial', 11))
            stat_label.setStyleSheet("color: #7f8c8d; margin: 5px 0; padding: 8px;")
            stats_frame_layout.addWidget(stat_label)
            
        stats_frame.setLayout(stats_frame_layout)
        layout.addWidget(stats_frame)
        
        layout.addStretch()
        dashboard.setLayout(layout)
        return dashboard
        
    def create_lophocphan_page(self):
        """Tạo trang quản lý lớp học phần"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Lớp học phần của tôi")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Filter
        filter_layout = QHBoxLayout()
        
        hocky_combo = QComboBox()
        hocky_combo.addItems(["HK1-2024", "HK2-2024", "HK3-2024"])
        hocky_combo.setFixedHeight(35)
        
        filter_layout.addWidget(QLabel("Học kỳ:"))
        filter_layout.addWidget(hocky_combo)
        filter_layout.addStretch()
        
        # Table
        self.lhp_table = QTableWidget()
        self.lhp_table.setColumnCount(7)
        self.lhp_table.setHorizontalHeaderLabels([
            "Mã LHP", "Tên LHP", "Môn học", "Số SV", "Đã học", "Còn lại", "Thao tác"
        ])
        self.lhp_table.setAlternatingRowColors(True)
        self.lhp_table.setStyleSheet("""
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
        
        # Sample data
        sample_data = [
            ["LHP001", "Lập trình căn bản A1", "IT001", "45", "8/15", "7", "Chi tiết"],
            ["LHP002", "Lập trình căn bản A2", "IT001", "42", "8/15", "7", "Chi tiết"],
            ["LHP003", "Cấu trúc dữ liệu B1", "IT002", "38", "6/15", "9", "Chi tiết"],
            ["LHP007", "OOP A1", "IT003", "40", "5/15", "10", "Chi tiết"],
            ["LHP008", "Cơ sở dữ liệu B2", "IT004", "35", "7/15", "8", "Chi tiết"]
        ]
        
        self.lhp_table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                if j == 6:  # Action column
                    btn = QPushButton("📋 Chi tiết")
                    btn.setStyleSheet("""
                        QPushButton {
                            background-color: #3498db;
                            color: white;
                            border: none;
                            border-radius: 4px;
                            padding: 5px 10px;
                        }
                        QPushButton:hover {
                            background-color: #5dade2;
                        }
                    """)
                    btn.clicked.connect(lambda checked, idx=i: self.show_lhp_detail(idx))
                    self.lhp_table.setCellWidget(i, j, btn)
                else:
                    self.lhp_table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(filter_layout)
        layout.addWidget(self.lhp_table)
        page.setLayout(layout)
        return page
        
    def create_baocao_page(self):
        """Tạo trang báo cáo"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Báo cáo Giảng viên")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Report options
        reports_frame = QFrame()
        reports_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        reports_layout = QVBoxLayout()
        
        report_buttons = [
            ("📊 Báo cáo điểm danh theo lớp", self.export_diemdanh_lop),
            ("📈 Thống kê chuyên cần sinh viên", self.export_chuyencan),
            ("📅 Báo cáo theo thời gian", self.export_thoigian),
            ("⚠️ Danh sách sinh viên vắng nhiều", self.export_vang_nhieu),
            ("📋 Báo cáo tổng hợp", self.export_tonghop),
            ("📄 Xuất danh sách điểm danh", self.export_danhsach)
        ]
        
        for text, callback in report_buttons:
            btn = QPushButton(text)
            btn.setFixedHeight(50)
            btn.setFont(QFont('Arial', 12))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                    color: #2c3e50;
                    border: 1px solid #dee2e6;
                    border-radius: 5px;
                    text-align: left;
                    padding: 15px 20px;
                    margin: 5px 0;
                }
                QPushButton:hover {
                    background-color: #e9ecef;
                    border-color: #3498db;
                }
            """)
            btn.clicked.connect(callback)
            reports_layout.addWidget(btn)
            
        reports_frame.setLayout(reports_layout)
        layout.addWidget(reports_frame)
        layout.addStretch()
        
        page.setLayout(layout)
        return page
        
    def create_stat_card(self, title, value, color):
        """Tạo thẻ thống kê"""
        card = QFrame()
        card.setFixedHeight(120)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                border-left: 4px solid {color};
            }}
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)
        
        title_label = QLabel(title)
        title_label.setFont(QFont('Arial', 12))
        title_label.setStyleSheet("color: #7f8c8d;")
        
        value_label = QLabel(value)
        value_label.setFont(QFont('Arial', 24, QFont.Bold))
        value_label.setStyleSheet(f"color: {color};")
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        card.setLayout(layout)
        
        return card
        
    def create_navigation(self):
        """Tạo menu điều hướng"""
        # Dashboard
        dashboard_btn = self.add_nav_button("Dashboard", "📊")
        dashboard_btn.clicked.connect(self.show_dashboard)
        
        # Lớp học phần
        lhp_btn = self.add_nav_button("Lớp học phần", "📚")
        lhp_btn.clicked.connect(self.show_lophocphan)
        
        # Báo cáo
        baocao_btn = self.add_nav_button("Báo cáo", "📋")
        baocao_btn.clicked.connect(self.show_baocao)
        
    def show_dashboard(self):
        """Hiển thị dashboard"""
        self.content_area.setCurrentWidget(self.dashboard_page)
        
    def show_lophocphan(self):
        """Hiển thị trang lớp học phần"""
        self.content_area.setCurrentWidget(self.lophocphan_page)
        
    def show_baocao(self):
        """Hiển thị trang báo cáo"""
        self.content_area.setCurrentWidget(self.baocao_page)
        
    def open_diemdanh(self, schedule_index):
        """Mở cửa sổ điểm danh"""
        try:
            from ui.teacher.w_gv_diemdanh import WGVDiemDanh
            lhp_codes = ["LHP001", "LHP003", "LHP002"]
            if schedule_index < len(lhp_codes):
                self.diemdanh_window = WGVDiemDanh(lhp_codes[schedule_index])
                self.diemdanh_window.show()
        except ImportError:
            QMessageBox.information(
                self, 
                "Thông báo", 
                f"Mở điểm danh cho buổi {schedule_index + 1}\nCửa sổ điểm danh đang được phát triển!"
            )
            
    def show_lhp_detail(self, row_index):
        """Hiển thị chi tiết lớp học phần"""
        try:
            from ui.teacher.w_gv_chitiet_lhp import WGVChiTietLHP
            lhp_code = self.lhp_table.item(row_index, 0).text()
            self.detail_window = WGVChiTietLHP(lhp_code)
            self.detail_window.show()
        except ImportError:
            lhp_code = self.lhp_table.item(row_index, 0).text()
            QMessageBox.information(
                self, 
                "Thông báo", 
                f"Chi tiết LHP: {lhp_code}\nCửa sổ chi tiết đang được phát triển!"
            )
    
    # Report export methods
    def export_diemdanh_lop(self):
        QMessageBox.information(self, "Thông báo", "Xuất báo cáo điểm danh theo lớp")
        
    def export_chuyencan(self):
        QMessageBox.information(self, "Thông báo", "Xuất thống kê chuyên cần sinh viên")
        
    def export_thoigian(self):
        QMessageBox.information(self, "Thông báo", "Xuất báo cáo theo thời gian")
        
    def export_vang_nhieu(self):
        QMessageBox.information(self, "Thông báo", "Xuất danh sách sinh viên vắng nhiều")
        
    def export_tonghop(self):
        QMessageBox.information(self, "Thông báo", "Xuất báo cáo tổng hợp")
        
    def export_danhsach(self):
        QMessageBox.information(self, "Thông báo", "Xuất danh sách điểm danh")
