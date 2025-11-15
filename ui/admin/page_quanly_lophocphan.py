from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QTableWidget, QTableWidgetItem, 
                             QLineEdit, QComboBox, QFrame, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PageQuanLyLopHocPhan(QWidget):
    """Trang Quản lý Lớp học phần"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Quản lý Lớp học phần")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Search and filter
        search_layout = QHBoxLayout()
        
        hocky_combo = QComboBox()
        hocky_combo.addItems(["Tất cả học kỳ", "HK1-2024", "HK2-2024", "HK3-2024"])
        hocky_combo.setFixedHeight(35)
        
        mon_combo = QComboBox()
        mon_combo.addItems(["Tất cả môn", "Lập trình căn bản", "Cấu trúc dữ liệu", "Kế toán tài chính"])
        mon_combo.setFixedHeight(35)
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("Tìm kiếm lớp học phần...")
        search_input.setFixedHeight(35)
        
        search_layout.addWidget(QLabel("Học kỳ:"))
        search_layout.addWidget(hocky_combo)
        search_layout.addWidget(QLabel("Môn học:"))
        search_layout.addWidget(mon_combo)
        search_layout.addWidget(QLabel("Tìm kiếm:"))
        search_layout.addWidget(search_input)
        search_layout.addStretch()
        
        # Controls
        controls_layout = QHBoxLayout()
        
        add_btn = QPushButton("➕ Tạo LHP")
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
        add_btn.clicked.connect(self.create_lophocphan)
        
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
        
        assign_gv_btn = QPushButton("👨‍🏫 Gán GV")
        assign_gv_btn.setFixedHeight(35)
        assign_gv_btn.setStyleSheet("""
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
        assign_gv_btn.clicked.connect(self.assign_giangvien)
        
        detail_btn = QPushButton("📋 Chi tiết")
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
        detail_btn.clicked.connect(self.show_lophocphan_detail)
        
        controls_layout.addWidget(add_btn)
        controls_layout.addWidget(edit_btn)
        controls_layout.addWidget(delete_btn)
        controls_layout.addWidget(assign_gv_btn)
        controls_layout.addWidget(detail_btn)
        controls_layout.addStretch()
        
        # Table
        self.lophocphan_table = QTableWidget()
        self.lophocphan_table.setColumnCount(8)
        self.lophocphan_table.setHorizontalHeaderLabels([
            "Mã LHP", "Tên LHP", "Môn học", "Giảng viên", "Học kỳ", "Số SV", "Trạng thái", "Ghi chú"
        ])
        self.lophocphan_table.setAlternatingRowColors(True)
        self.lophocphan_table.setStyleSheet("""
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
            ["LHP001", "Lập trình căn bản A1", "IT001", "TS. Nguyễn Văn X", "HK1-2024", "45", "Đang học", ""],
            ["LHP002", "Lập trình căn bản A2", "IT001", "ThS. Trần Thị Y", "HK1-2024", "42", "Đang học", ""],
            ["LHP003", "Cấu trúc dữ liệu B1", "IT002", "TS. Nguyễn Văn X", "HK1-2024", "38", "Đang học", ""],
            ["LHP004", "Kế toán tài chính K1", "AC001", "PGS. Lê Văn Z", "HK1-2024", "35", "Đang học", ""],
            ["LHP005", "Lập trình căn bản A3", "IT001", "Chưa gán", "HK2-2024", "0", "Chuẩn bị", "Chờ gán GV"]
        ]
        
        self.lophocphan_table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                self.lophocphan_table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(search_layout)
        layout.addLayout(controls_layout)
        layout.addWidget(self.lophocphan_table)
        self.setLayout(layout)
        
    def create_lophocphan(self):
        """Tạo lớp học phần mới"""
        QMessageBox.information(self, "Thông báo", "Chức năng tạo lớp học phần đang được phát triển!")
        
    def assign_giangvien(self):
        """Gán giảng viên cho lớp học phần"""
        current_row = self.lophocphan_table.currentRow()
        if current_row >= 0:
            lhp_code = self.lophocphan_table.item(current_row, 0).text()
            QMessageBox.information(
                self, 
                "Thông báo", 
                f"Gán giảng viên cho LHP: {lhp_code}\nChức năng đang được phát triển!"
            )
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một lớp học phần!")
            
    def show_lophocphan_detail(self):
        """Hiển thị chi tiết lớp học phần"""
        current_row = self.lophocphan_table.currentRow()
        if current_row >= 0:
            lhp_code = self.lophocphan_table.item(current_row, 0).text()
            try:
                from ui.admin.w_admin_chitiet_lhp import WAdminChiTietLHP
                self.detail_window = WAdminChiTietLHP(lhp_code)
                self.detail_window.show()
            except ImportError:
                QMessageBox.information(
                    self, 
                    "Thông báo", 
                    f"Chi tiết LHP: {lhp_code}\nCửa sổ chi tiết đang được phát triển!"
                )
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một lớp học phần!")
