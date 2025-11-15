from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QTableWidget, QTableWidgetItem, 
                             QLineEdit, QComboBox, QFrame, QMessageBox, QTabWidget,
                             QTextEdit, QDateEdit, QFileDialog)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont

class PageBaoCao(QWidget):
    """Trang Báo cáo & Lịch sử"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Báo cáo & Lịch sử")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Tabs for different reports
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
        
        # Tab 1: Báo cáo Admin
        baocao_tab = self.create_baocao_tab()
        tabs.addTab(baocao_tab, "📊 Báo cáo Admin")
        
        # Tab 2: Lịch sử chỉnh sửa
        lichsu_tab = self.create_lichsu_tab()
        tabs.addTab(lichsu_tab, "📝 Lịch sử Audit")
        
        layout.addWidget(tabs)
        self.setLayout(layout)
        
    def create_baocao_tab(self):
        """Tạo tab báo cáo admin"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Filter controls
        filter_layout = QHBoxLayout()
        
        # Date range
        from_date = QDateEdit()
        from_date.setDate(QDate.currentDate().addDays(-30))
        from_date.setFixedHeight(35)
        
        to_date = QDateEdit()
        to_date.setDate(QDate.currentDate())
        to_date.setFixedHeight(35)
        
        # Report type
        report_combo = QComboBox()
        report_combo.addItems([
            "Tất cả báo cáo",
            "1. Danh sách sinh viên theo lớp",
            "2. Danh sách giảng viên theo khoa", 
            "3. Danh sách lớp học phần",
            "4. Thống kê điểm danh theo lớp",
            "5. Thống kê vắng mặt cao",
            "6. Báo cáo hoạt động hệ thống",
            "7. Thống kê sử dụng chức năng",
            "8. Báo cáo tổng hợp cuối kỳ"
        ])
        report_combo.setFixedHeight(35)
        
        filter_layout.addWidget(QLabel("Từ ngày:"))
        filter_layout.addWidget(from_date)
        filter_layout.addWidget(QLabel("Đến ngày:"))
        filter_layout.addWidget(to_date)
        filter_layout.addWidget(QLabel("Loại báo cáo:"))
        filter_layout.addWidget(report_combo)
        filter_layout.addStretch()
        
        # Action buttons
        action_layout = QHBoxLayout()
        
        view_btn = QPushButton("👁️ Xem báo cáo")
        view_btn.setFixedHeight(35)
        view_btn.setStyleSheet("""
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
        view_btn.clicked.connect(self.view_report)
        
        export_btn = QPushButton("📥 Xuất Excel")
        export_btn.setFixedHeight(35)
        export_btn.setStyleSheet("""
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
        export_btn.clicked.connect(self.export_excel)
        
        refresh_btn = QPushButton("🔄 Làm mới")
        refresh_btn.setFixedHeight(35)
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        
        action_layout.addWidget(view_btn)
        action_layout.addWidget(export_btn)
        action_layout.addWidget(refresh_btn)
        action_layout.addStretch()
        
        # Report display area
        self.report_table = QTableWidget()
        self.report_table.setColumnCount(6)
        self.report_table.setHorizontalHeaderLabels([
            "STT", "Loại báo cáo", "Ngày tạo", "Người tạo", "Trạng thái", "Thao tác"
        ])
        self.report_table.setAlternatingRowColors(True)
        self.report_table.setStyleSheet("""
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
            ["1", "Thống kê điểm danh tháng 11", "15/11/2024", "admin", "Hoàn thành", "Tải xuống"],
            ["2", "Danh sách SV theo lớp", "14/11/2024", "admin", "Hoàn thành", "Tải xuống"],
            ["3", "Báo cáo vắng mặt cao", "13/11/2024", "admin", "Hoàn thành", "Tải xuống"],
            ["4", "Thống kê hoạt động hệ thống", "12/11/2024", "admin", "Hoàn thành", "Tải xuống"]
        ]
        
        self.report_table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                self.report_table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(filter_layout)
        layout.addLayout(action_layout)
        layout.addWidget(QLabel("Danh sách báo cáo:"))
        layout.addWidget(self.report_table)
        
        widget.setLayout(layout)
        return widget
        
    def create_lichsu_tab(self):
        """Tạo tab lịch sử audit"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Filter controls
        filter_layout = QHBoxLayout()
        
        # Date range
        from_date = QDateEdit()
        from_date.setDate(QDate.currentDate().addDays(-7))
        from_date.setFixedHeight(35)
        
        to_date = QDateEdit()
        to_date.setDate(QDate.currentDate())
        to_date.setFixedHeight(35)
        
        # Action type
        action_combo = QComboBox()
        action_combo.addItems([
            "Tất cả thao tác",
            "Đăng nhập/Đăng xuất",
            "Thêm/Sửa/Xóa dữ liệu",
            "Chỉnh sửa điểm danh",
            "Xuất báo cáo",
            "Quản lý người dùng"
        ])
        action_combo.setFixedHeight(35)
        
        # User filter
        user_combo = QComboBox()
        user_combo.addItems(["Tất cả người dùng", "admin", "teacher1", "teacher2"])
        user_combo.setFixedHeight(35)
        
        filter_layout.addWidget(QLabel("Từ ngày:"))
        filter_layout.addWidget(from_date)
        filter_layout.addWidget(QLabel("Đến ngày:"))
        filter_layout.addWidget(to_date)
        filter_layout.addWidget(QLabel("Loại thao tác:"))
        filter_layout.addWidget(action_combo)
        filter_layout.addWidget(QLabel("Người dùng:"))
        filter_layout.addWidget(user_combo)
        filter_layout.addStretch()
        
        # Search
        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Tìm kiếm trong lịch sử...")
        search_input.setFixedHeight(35)
        
        search_btn = QPushButton("🔍 Tìm kiếm")
        search_btn.setFixedHeight(35)
        search_btn.setStyleSheet("""
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
        
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_btn)
        search_layout.addStretch()
        
        # Audit log table
        self.audit_table = QTableWidget()
        self.audit_table.setColumnCount(6)
        self.audit_table.setHorizontalHeaderLabels([
            "Thời gian", "Người dùng", "Thao tác", "Đối tượng", "Chi tiết", "IP Address"
        ])
        self.audit_table.setAlternatingRowColors(True)
        self.audit_table.setStyleSheet("""
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
        
        # Sample audit data
        audit_data = [
            ["15/11/2024 14:30", "admin", "Sửa điểm danh", "LHP001-Buoi5", "Đổi SV 2021001 từ Vắng -> Có mặt", "192.168.1.10"],
            ["15/11/2024 14:25", "teacher1", "Điểm danh", "LHP001-Buoi5", "Điểm danh 45 sinh viên", "192.168.1.15"],
            ["15/11/2024 14:00", "admin", "Thêm sinh viên", "2024001", "Thêm SV Nguyễn Văn E vào lớp CNTT03", "192.168.1.10"],
            ["15/11/2024 13:45", "teacher2", "Đăng nhập", "Hệ thống", "Đăng nhập thành công", "192.168.1.20"],
            ["15/11/2024 13:30", "admin", "Xuất báo cáo", "BaoCao_DD_T11", "Xuất báo cáo điểm danh tháng 11", "192.168.1.10"]
        ]
        
        self.audit_table.setRowCount(len(audit_data))
        for i, row in enumerate(audit_data):
            for j, value in enumerate(row):
                self.audit_table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(filter_layout)
        layout.addLayout(search_layout)
        layout.addWidget(QLabel("Lịch sử thao tác:"))
        layout.addWidget(self.audit_table)
        
        widget.setLayout(layout)
        return widget
        
    def view_report(self):
        """Xem báo cáo"""
        QMessageBox.information(self, "Thông báo", "Chức năng xem báo cáo đang được phát triển!")
        
    def export_excel(self):
        """Xuất báo cáo Excel"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Lưu báo cáo", 
            "BaoCao_DiemDanh.xlsx", 
            "Excel files (*.xlsx)"
        )
        
        if file_path:
            QMessageBox.information(
                self, 
                "Thông báo", 
                f"Báo cáo sẽ được lưu tại: {file_path}\nChức năng xuất Excel đang được phát triển!"
            )
