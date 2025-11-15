from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QStackedWidget, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ui.common.base_window import BaseMainWindow
from ui.admin.page_quanly_chung import PageQuanLyChung
from ui.admin.page_quanly_nguoidung import PageQuanLyNguoiDung
from ui.admin.page_quanly_lophocphan import PageQuanLyLopHocPhan
from ui.admin.page_baocao import PageBaoCao

class WAdminMain(BaseMainWindow):
    """Cửa sổ chính cho Admin"""
    
    def __init__(self, full_name, role):
        super().__init__(full_name, role)
        self.setup_admin_ui()
        
    def setup_admin_ui(self):
        """Thiết lập giao diện Admin"""
        self.setWindowTitle('Hệ thống điểm danh - Admin Dashboard')
        
        # Create content pages
        self.create_content_pages()
        
        # Create navigation buttons
        self.create_navigation()
        
        # Show default page
        self.show_dashboard()
        
    def create_content_pages(self):
        """Tạo các trang nội dung"""
        try:
            # Dashboard page
            self.dashboard_page = self.create_dashboard_page()
            self.content_area.addWidget(self.dashboard_page)
            
            # Quản lý chung page
            self.quanly_chung_page = PageQuanLyChung()
            self.content_area.addWidget(self.quanly_chung_page)
            
            # Quản lý người dùng page
            self.quanly_nguoidung_page = PageQuanLyNguoiDung()
            self.content_area.addWidget(self.quanly_nguoidung_page)
            
            # Quản lý lớp học phần page
            self.quanly_lophocphan_page = PageQuanLyLopHocPhan()
            self.content_area.addWidget(self.quanly_lophocphan_page)
            
            # Báo cáo page
            self.baocao_page = PageBaoCao()
            self.content_area.addWidget(self.baocao_page)
            
        except ImportError as e:
            print(f"Warning: Could not import admin pages: {e}")
            # Create placeholder pages if imports fail
            self.create_placeholder_pages()
    
    def create_placeholder_pages(self):
        """Tạo các trang placeholder nếu không import được"""
        self.dashboard_page = self.create_dashboard_page()
        self.content_area.addWidget(self.dashboard_page)
        
        for name in ['Quản lý chung', 'Quản lý người dùng', 'Quản lý lớp học phần', 'Báo cáo']:
            placeholder = QWidget()
            layout = QVBoxLayout()
            label = QLabel(f"Trang {name}\n(Đang phát triển)")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont('Arial', 16))
            label.setStyleSheet("color: #7f8c8d; padding: 50px;")
            layout.addWidget(label)
            placeholder.setLayout(layout)
            self.content_area.addWidget(placeholder)
        
    def create_dashboard_page(self):
        """Tạo trang dashboard"""
        dashboard = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Dashboard Admin")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Statistics cards
        stats_layout = QHBoxLayout()
        
        # Create stat cards
        cards_data = [
            ("👥 Tổng sinh viên", "1,234", "#3498db"),
            ("👨‍🏫 Tổng giảng viên", "56", "#27ae60"),
            ("📚 Tổng môn học", "89", "#f39c12"),
            ("📊 Lớp học phần", "145", "#9b59b6")
        ]
        
        for title_text, value, color in cards_data:
            card = self.create_stat_card(title_text, value, color)
            stats_layout.addWidget(card)
            
        layout.addLayout(stats_layout)
        
        # Recent activities
        activities_title = QLabel("Hoạt động gần đây")
        activities_title.setFont(QFont('Arial', 18, QFont.Bold))
        activities_title.setStyleSheet("color: #2c3e50; margin: 30px 0 15px 0;")
        layout.addWidget(activities_title)
        
        activities_frame = QFrame()
        activities_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        activities_layout = QVBoxLayout()
        
        activities = [
            "📝 Thêm sinh viên mới: Nguyễn Văn A - 5 phút trước",
            "📚 Tạo lớp học phần: Toán cao cấp A1 - 15 phút trước",
            "👨‍🏫 Cập nhật thông tin giảng viên: TS. Trần Thị B - 30 phút trước",
            "📊 Xuất báo cáo điểm danh tháng 11 - 1 giờ trước"
        ]
        
        for activity in activities:
            activity_label = QLabel(activity)
            activity_label.setFont(QFont('Arial', 11))
            activity_label.setStyleSheet("color: #7f8c8d; margin: 5px 0; padding: 8px;")
            activities_layout.addWidget(activity_label)
            
        activities_frame.setLayout(activities_layout)
        layout.addWidget(activities_frame)
        
        layout.addStretch()
        dashboard.setLayout(layout)
        return dashboard
        
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
        
        # Quản lý chung
        quanly_chung_btn = self.add_nav_button("Quản lý Khoa/Lớp/Môn", "📚")
        quanly_chung_btn.clicked.connect(self.show_quanly_chung)
        
        # Quản lý người dùng
        quanly_nguoidung_btn = self.add_nav_button("Quản lý Người dùng", "👥")
        quanly_nguoidung_btn.clicked.connect(self.show_quanly_nguoidung)
        
        # Quản lý lớp học phần
        quanly_lhp_btn = self.add_nav_button("Quản lý Lớp học phần", "📖")
        quanly_lhp_btn.clicked.connect(self.show_quanly_lophocphan)
        
        # Báo cáo
        baocao_btn = self.add_nav_button("Báo cáo & Lịch sử", "📊")
        baocao_btn.clicked.connect(self.show_baocao)
        
    def show_dashboard(self):
        """Hiển thị dashboard"""
        self.content_area.setCurrentWidget(self.dashboard_page)
        
    def show_quanly_chung(self):
        """Hiển thị trang quản lý chung"""
        self.content_area.setCurrentIndex(1)
        
    def show_quanly_nguoidung(self):
        """Hiển thị trang quản lý người dùng"""
        self.content_area.setCurrentIndex(2)
        
    def show_quanly_lophocphan(self):
        """Hiển thị trang quản lý lớp học phần"""
        self.content_area.setCurrentIndex(3)
        
    def show_baocao(self):
        """Hiển thị trang báo cáo"""
        self.content_area.setCurrentIndex(4)
