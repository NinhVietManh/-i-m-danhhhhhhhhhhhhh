from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QTableWidget, QTableWidgetItem, 
                             QLineEdit, QComboBox, QFrame, QMessageBox, QTabWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PageQuanLyChung(QWidget):
    """Trang Quản lý Khoa/Lớp/Môn học"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Quản lý Khoa/Lớp/Môn học")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Tabs for different management sections
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
        
        # Tab 1: Quản lý Khoa
        khoa_tab = self.create_khoa_tab()
        tabs.addTab(khoa_tab, "🏛️ Quản lý Khoa")
        
        # Tab 2: Quản lý Lớp
        lop_tab = self.create_lop_tab()
        tabs.addTab(lop_tab, "👥 Quản lý Lớp HC")
        
        # Tab 3: Quản lý Môn học
        mon_tab = self.create_mon_tab()
        tabs.addTab(mon_tab, "📚 Quản lý Môn học")
        
        layout.addWidget(tabs)
        self.setLayout(layout)
        
    def create_khoa_tab(self):
        """Tạo tab quản lý khoa"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Controls
        controls_layout = QHBoxLayout()
        
        add_btn = QPushButton("➕ Thêm Khoa")
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
        
        controls_layout.addWidget(add_btn)
        controls_layout.addWidget(edit_btn)
        controls_layout.addWidget(delete_btn)
        controls_layout.addStretch()
        
        # Table
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Mã Khoa", "Tên Khoa", "Mô tả"])
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
            ["CNTT", "Công nghệ Thông tin", "Khoa Công nghệ Thông tin"],
            ["KT", "Kế toán", "Khoa Kế toán"],
            ["QTKD", "Quản trị Kinh doanh", "Khoa Quản trị Kinh doanh"]
        ]
        
        table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(controls_layout)
        layout.addWidget(table)
        widget.setLayout(layout)
        
        return widget
        
    def create_lop_tab(self):
        """Tạo tab quản lý lớp hành chính"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Search and filter
        search_layout = QHBoxLayout()
        
        khoa_combo = QComboBox()
        khoa_combo.addItems(["Tất cả khoa", "Công nghệ TT", "Kế toán", "Quản trị KD"])
        khoa_combo.setFixedHeight(35)
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("Tìm kiếm lớp...")
        search_input.setFixedHeight(35)
        
        search_layout.addWidget(QLabel("Khoa:"))
        search_layout.addWidget(khoa_combo)
        search_layout.addWidget(QLabel("Tìm kiếm:"))
        search_layout.addWidget(search_input)
        search_layout.addStretch()
        
        # Controls
        controls_layout = QHBoxLayout()
        
        add_btn = QPushButton("➕ Thêm Lớp HC")
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
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Mã Lớp", "Tên Lớp", "Khoa", "Niên khóa", "Số SV"])
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
            ["CNTT01", "Công nghệ TT 01", "CNTT", "2021-2025", "45"],
            ["CNTT02", "Công nghệ TT 02", "CNTT", "2021-2025", "42"],
            ["KT01", "Kế toán 01", "KT", "2022-2026", "38"]
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
        
    def create_mon_tab(self):
        """Tạo tab quản lý môn học"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Controls
        controls_layout = QHBoxLayout()
        
        add_btn = QPushButton("➕ Thêm Môn học")
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
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Mã Môn", "Tên Môn", "Số tín chỉ", "Khoa", "Mô tả"])
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
            ["IT001", "Lập trình căn bản", "3", "CNTT", "Môn học cơ sở"],
            ["IT002", "Cấu trúc dữ liệu", "3", "CNTT", "Môn học chuyên ngành"],
            ["AC001", "Kế toán tài chính", "4", "KT", "Môn học cơ sở"],
            ["MG001", "Quản trị học", "3", "QTKD", "Môn học cơ sở"]
        ]
        
        table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(controls_layout)
        layout.addWidget(table)
        widget.setLayout(layout)
        
        return widget
