from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QTableWidget, QTableWidgetItem, 
                             QLineEdit, QComboBox, QFrame, QMessageBox, QTabWidget,
                             QFileDialog, QDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PageQuanLyNguoiDung(QWidget):
    """Trang Quản lý Người dùng"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Quản lý Người dùng")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Tabs for different user types
        tabs = QTabWidget()
        tabs.setStyleSheet("""
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
        
        # Tab 1: Quản lý Sinh viên
        sinhvien_tab = self.create_sinhvien_tab()
        tabs.addTab(sinhvien_tab, "👨‍🎓 Quản lý Sinh viên")
        
        # Tab 2: Quản lý Giảng viên
        giangvien_tab = self.create_giangvien_tab()
        tabs.addTab(giangvien_tab, "👨‍🏫 Quản lý Giảng viên")
        
        layout.addWidget(tabs)
        self.setLayout(layout)
        
    def create_sinhvien_tab(self):
        """Tạo tab quản lý sinh viên"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Search and filter
        search_layout = QHBoxLayout()
        
        lop_combo = QComboBox()
        lop_combo.addItems(["Tất cả lớp", "CNTT01", "CNTT02", "KT01", "QTKD01"])
        lop_combo.setFixedHeight(35)
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("Tìm kiếm sinh viên...")
        search_input.setFixedHeight(35)
        
        search_layout.addWidget(QLabel("Lớp:"))
        search_layout.addWidget(lop_combo)
        search_layout.addWidget(QLabel("Tìm kiếm:"))
        search_layout.addWidget(search_input)
        search_layout.addStretch()
        
        # Controls
        controls_layout = QHBoxLayout()
        
        add_btn = QPushButton("➕ Thêm SV")
        add_btn.setFixedHeight(35)
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        add_btn.clicked.connect(self.add_sinhvien)
        
        edit_btn = QPushButton("✏️ Sửa")
        edit_btn.setFixedHeight(35)
        edit_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5dade2;
            }
        """)
        
        delete_btn = QPushButton("🗑️ Xóa")
        delete_btn.setFixedHeight(35)
        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
        import_btn = QPushButton("📁 Nhập Excel/CSV")
        import_btn.setFixedHeight(35)
        import_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        import_btn.clicked.connect(self.import_sinhvien)
        
        detail_btn = QPushButton("👁️ Chi tiết")
        detail_btn.setFixedHeight(35)
        detail_btn.setStyleSheet("""
            QPushButton {
                background-color: #9b59b6;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #8e44ad;
            }
        """)
        detail_btn.clicked.connect(self.show_sinhvien_detail)
        
        controls_layout.addWidget(add_btn)
        controls_layout.addWidget(edit_btn)
        controls_layout.addWidget(delete_btn)
        controls_layout.addWidget(import_btn)
        controls_layout.addWidget(detail_btn)
        controls_layout.addStretch()
        
        # Table
        self.sinhvien_table = QTableWidget()
        self.sinhvien_table.setColumnCount(7)
        self.sinhvien_table.setHorizontalHeaderLabels([
            "MSV", "Họ tên", "Lớp", "Email", "SĐT", "Trạng thái", "Khuôn mặt"
        ])
        self.sinhvien_table.setAlternatingRowColors(True)
        self.sinhvien_table.setStyleSheet("""
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
            ["2021001", "Nguyễn Văn A", "CNTT01", "nva@student.edu", "0901234567", "Hoạt động", "Đã đăng ký"],
            ["2021002", "Trần Thị B", "CNTT01", "ttb@student.edu", "0901234568", "Hoạt động", "Chưa đăng ký"],
            ["2021003", "Lê Văn C", "CNTT02", "lvc@student.edu", "0901234569", "Hoạt động", "Đã đăng ký"],
            ["2022001", "Phạm Thị D", "KT01", "ptd@student.edu", "0901234570", "Hoạt động", "Chưa đăng ký"]
        ]
        
        self.sinhvien_table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                self.sinhvien_table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(search_layout)
        layout.addLayout(controls_layout)
        layout.addWidget(self.sinhvien_table)
        widget.setLayout(layout)
        
        return widget
        
    def create_giangvien_tab(self):
        """Tạo tab quản lý giảng viên"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Search and filter
        search_layout = QHBoxLayout()
        
        khoa_combo = QComboBox()
        khoa_combo.addItems(["Tất cả khoa", "CNTT", "KT", "QTKD"])
        khoa_combo.setFixedHeight(35)
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("Tìm kiếm giảng viên...")
        search_input.setFixedHeight(35)
        
        search_layout.addWidget(QLabel("Khoa:"))
        search_layout.addWidget(khoa_combo)
        search_layout.addWidget(QLabel("Tìm kiếm:"))
        search_layout.addWidget(search_input)
        search_layout.addStretch()
        
        # Controls
        controls_layout = QHBoxLayout()
        
        add_btn = QPushButton("➕ Thêm GV")
        edit_btn = QPushButton("✏️ Sửa")
        delete_btn = QPushButton("🗑️ Xóa")
        
        for btn in [add_btn, edit_btn, delete_btn]:
            btn.setFixedHeight(35)
            
        add_btn.setStyleSheet("background-color: #27ae60; color: white; border: none; border-radius: 5px; padding: 5px 15px; font-weight: bold;")
        edit_btn.setStyleSheet("background-color: #3498db; color: white; border: none; border-radius: 5px; padding: 5px 15px; font-weight: bold;")
        delete_btn.setStyleSheet("background-color: #e74c3c; color: white; border: none; border-radius: 5px; padding: 5px 15px; font-weight: bold;")
        
        controls_layout.addWidget(add_btn)
        controls_layout.addWidget(edit_btn)
        controls_layout.addWidget(delete_btn)
        controls_layout.addStretch()
        
        # Table
        table = QTableWidget()
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels([
            "Mã GV", "Họ tên", "Khoa", "Email", "SĐT", "Trạng thái"
        ])
        table.setAlternatingRowColors(True)
        table.setStyleSheet("""
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
            ["GV001", "TS. Nguyễn Văn X", "CNTT", "nvx@teacher.edu", "0909876543", "Hoạt động"],
            ["GV002", "ThS. Trần Thị Y", "CNTT", "tty@teacher.edu", "0909876544", "Hoạt động"],
            ["GV003", "PGS. Lê Văn Z", "KT", "lvz@teacher.edu", "0909876545", "Hoạt động"]
        ]
        
        table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(search_layout)
        layout.addLayout(controls_layout)
        layout.addWidget(table)
        widget.setLayout(layout)
        
        return widget
        
    def add_sinhvien(self):
        """Thêm sinh viên mới"""
        QMessageBox.information(self, "Thông báo", "Chức năng thêm sinh viên đang được phát triển!")
        
    def import_sinhvien(self):
        """Nhập danh sách sinh viên từ Excel/CSV"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Chọn file Excel/CSV", 
            "", 
            "Excel files (*.xlsx *.xls);;CSV files (*.csv)"
        )
        
        if file_path:
            QMessageBox.information(
                self, 
                "Thông báo", 
                f"Đã chọn file: {file_path}\nChức năng import đang được phát triển!"
            )
            
    def show_sinhvien_detail(self):
        """Hiển thị chi tiết sinh viên"""
        current_row = self.sinhvien_table.currentRow()
        if current_row >= 0:
            msv = self.sinhvien_table.item(current_row, 0).text()
            try:
                from ui.admin.w_admin_chitiet_sv import WAdminChiTietSV
                self.detail_window = WAdminChiTietSV(msv)
                self.detail_window.show()
            except ImportError:
                QMessageBox.information(
                    self, 
                    "Thông báo", 
                    f"Chi tiết sinh viên {msv}\nCửa sổ chi tiết đang được phát triển!"
                )
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một sinh viên!")
