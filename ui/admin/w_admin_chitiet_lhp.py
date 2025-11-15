from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QTableWidget, QTableWidgetItem,
                             QLineEdit, QComboBox, QFrame, QMessageBox, QTabWidget,
                             QGroupBox, QFormLayout, QSpinBox, QTimeEdit, QDateEdit,
                             QTextEdit, QCheckBox, QDialog, QDialogButtonBox)
from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtGui import QFont

class WAdminChiTietLHP(QMainWindow):
    """Cửa sổ Chi tiết Lớp học phần cho Admin"""
    
    def __init__(self, lhp_code):
        super().__init__()
        self.lhp_code = lhp_code
        self.init_ui()
        self.load_lhp_data()
        
    def init_ui(self):
        self.setWindowTitle(f'Chi tiết Lớp học phần - {self.lhp_code}')
        self.setGeometry(100, 100, 1200, 800)
        
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
        
        # Tab 1: Thông tin lớp học phần
        self.info_tab = self.create_info_tab()
        self.tabs.addTab(self.info_tab, "📋 Thông tin LHP")
        
        # Tab 2: Quản lý sinh viên
        self.student_tab = self.create_student_tab()
        self.tabs.addTab(self.student_tab, "👥 Quản lý Sinh viên")
        
        # Tab 3: Quản lý buổi học
        self.session_tab = self.create_session_tab()
        self.tabs.addTab(self.session_tab, "📅 Quản lý Buổi học")
        
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
        """Tạo header thông tin lớp học phần"""
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
        
        # LHP info
        info_layout = QVBoxLayout()
        
        self.lhp_name = QLabel(f"Đang tải...")
        self.lhp_name.setFont(QFont('Arial', 16, QFont.Bold))
        
        self.lhp_subject = QLabel(f"Mã LHP: {self.lhp_code}")
        self.lhp_subject.setFont(QFont('Arial', 12))
        
        self.lhp_teacher = QLabel("Giảng viên: Đang tải...")
        self.lhp_teacher.setFont(QFont('Arial', 11))
        
        self.lhp_semester = QLabel("Học kỳ: Đang tải...")
        self.lhp_semester.setFont(QFont('Arial', 11))
        
        info_layout.addWidget(self.lhp_name)
        info_layout.addWidget(self.lhp_subject)
        info_layout.addWidget(self.lhp_teacher)
        info_layout.addWidget(self.lhp_semester)
        
        # Quick stats
        stats_layout = QVBoxLayout()
        
        self.student_count = QLabel("Sinh viên: 0")
        self.student_count.setFont(QFont('Arial', 12, QFont.Bold))
        self.student_count.setAlignment(Qt.AlignCenter)
        
        self.session_count = QLabel("Buổi học: 0/15")
        self.session_count.setFont(QFont('Arial', 11))
        self.session_count.setAlignment(Qt.AlignCenter)
        
        self.attendance_rate = QLabel("Tỷ lệ DD: 0%")
        self.attendance_rate.setFont(QFont('Arial', 11))
        self.attendance_rate.setAlignment(Qt.AlignCenter)
        self.attendance_rate.setStyleSheet("color: #2ecc71;")
        
        stats_layout.addWidget(self.student_count)
        stats_layout.addWidget(self.session_count)
        stats_layout.addWidget(self.attendance_rate)
        
        layout.addLayout(info_layout)
        layout.addStretch()
        layout.addLayout(stats_layout)
        
        header.setLayout(layout)
        return header
        
    def create_info_tab(self):
        """Tạo tab thông tin lớp học phần"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Basic information
        basic_group = QGroupBox("Thông tin cơ bản")
        basic_group.setFont(QFont('Arial', 12, QFont.Bold))
        basic_layout = QFormLayout()
        
        self.lhp_code_input = QLineEdit()
        self.lhp_code_input.setText(self.lhp_code)
        self.lhp_code_input.setReadOnly(True)
        
        self.lhp_name_input = QLineEdit()
        
        self.subject_combo = QComboBox()
        self.subject_combo.addItems([
            "IT001 - Lập trình căn bản",
            "IT002 - Cấu trúc dữ liệu", 
            "IT003 - OOP",
            "AC001 - Kế toán tài chính"
        ])
        
        self.teacher_combo = QComboBox()
        self.teacher_combo.addItems([
            "TS. Nguyễn Văn X",
            "ThS. Trần Thị Y",
            "PGS. Lê Văn Z"
        ])
        
        self.semester_combo = QComboBox()
        self.semester_combo.addItems(["HK1-2024", "HK2-2024", "HK3-2024"])
        
        basic_layout.addRow("Mã LHP:", self.lhp_code_input)
        basic_layout.addRow("Tên LHP:", self.lhp_name_input)
        basic_layout.addRow("Môn học:", self.subject_combo)
        basic_layout.addRow("Giảng viên:", self.teacher_combo)
        basic_layout.addRow("Học kỳ:", self.semester_combo)
        
        basic_group.setLayout(basic_layout)
        
        # Schedule information
        schedule_group = QGroupBox("Thông tin lịch học")
        schedule_group.setFont(QFont('Arial', 12, QFont.Bold))
        schedule_layout = QFormLayout()
        
        self.room_input = QLineEdit()
        
        self.day_combo = QComboBox()
        self.day_combo.addItems([
            "Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"
        ])
        
        self.start_time = QTimeEdit()
        self.start_time.setTime(QTime(7, 0))
        
        self.end_time = QTimeEdit()
        self.end_time.setTime(QTime(9, 30))
        
        self.total_sessions = QSpinBox()
        self.total_sessions.setRange(10, 20)
        self.total_sessions.setValue(15)
        
        schedule_layout.addRow("Phòng học:", self.room_input)
        schedule_layout.addRow("Thứ trong tuần:", self.day_combo)
        schedule_layout.addRow("Giờ bắt đầu:", self.start_time)
        schedule_layout.addRow("Giờ kết thúc:", self.end_time)
        schedule_layout.addRow("Tổng số buổi:", self.total_sessions)
        
        schedule_group.setLayout(schedule_layout)
        
        # Status and notes
        status_group = QGroupBox("Trạng thái và ghi chú")
        status_group.setFont(QFont('Arial', 12, QFont.Bold))
        status_layout = QFormLayout()
        
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Đang học", "Hoàn thành", "Tạm dừng", "Hủy"])
        
        self.notes_input = QTextEdit()
        self.notes_input.setFixedHeight(80)
        
        status_layout.addRow("Trạng thái:", self.status_combo)
        status_layout.addRow("Ghi chú:", self.notes_input)
        
        status_group.setLayout(status_layout)
        
        layout.addWidget(basic_group)
        layout.addWidget(schedule_group)
        layout.addWidget(status_group)
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
        
    def create_student_tab(self):
        """Tạo tab quản lý sinh viên"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Controls
        controls_layout = QHBoxLayout()
        
        add_student_btn = QPushButton("➕ Thêm SV")
        add_student_btn.setFixedHeight(35)
        add_student_btn.setStyleSheet("""
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
        add_student_btn.clicked.connect(self.add_student)
        
        remove_student_btn = QPushButton("➖ Xóa SV")
        remove_student_btn.setFixedHeight(35)
        remove_student_btn.setStyleSheet("""
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
        remove_student_btn.clicked.connect(self.remove_student)
        
        add_by_class_btn = QPushButton("👥 Thêm theo Lớp HC")
        add_by_class_btn.setFixedHeight(35)
        add_by_class_btn.setStyleSheet("""
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
        add_by_class_btn.clicked.connect(self.add_students_by_class)
        
        export_btn = QPushButton("📤 Xuất DS")
        export_btn.setFixedHeight(35)
        export_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        
        controls_layout.addWidget(add_student_btn)
        controls_layout.addWidget(remove_student_btn)
        controls_layout.addWidget(add_by_class_btn)
        controls_layout.addWidget(export_btn)
        controls_layout.addStretch()
        
        # Search
        search_layout = QHBoxLayout()
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("Tìm kiếm sinh viên...")
        search_input.setFixedHeight(35)
        
        class_filter = QComboBox()
        class_filter.addItems(["Tất cả lớp", "CNTT01", "CNTT02", "KT01"])
        class_filter.setFixedHeight(35)
        
        search_layout.addWidget(QLabel("Tìm kiếm:"))
        search_layout.addWidget(search_input)
        search_layout.addWidget(QLabel("Lớp:"))
        search_layout.addWidget(class_filter)
        search_layout.addStretch()
        
        # Students table
        self.students_table = QTableWidget()
        self.students_table.setColumnCount(6)
        self.students_table.setHorizontalHeaderLabels([
            "MSV", "Họ tên", "Lớp HC", "Email", "SĐT", "Trạng thái"
        ])
        self.students_table.setAlternatingRowColors(True)
        self.students_table.setStyleSheet("""
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
        
        # Sample student data
        students_data = [
            ["2021001", "Nguyễn Văn A", "CNTT01", "nva@student.edu", "0901234567", "Đang học"],
            ["2021002", "Trần Thị B", "CNTT01", "ttb@student.edu", "0901234568", "Đang học"],
            ["2021003", "Lê Văn C", "CNTT02", "lvc@student.edu", "0901234569", "Đang học"],
            ["2021004", "Phạm Thị D", "CNTT01", "ptd@student.edu", "0901234570", "Đang học"],
            ["2021005", "Hoàng Văn E", "CNTT02", "hve@student.edu", "0901234571", "Đang học"]
        ]
        
        self.students_table.setRowCount(len(students_data))
        for i, row in enumerate(students_data):
            for j, value in enumerate(row):
                self.students_table.setItem(i, j, QTableWidgetItem(value))
        
        layout.addLayout(controls_layout)
        layout.addLayout(search_layout)
        layout.addWidget(self.students_table)
        
        widget.setLayout(layout)
        return widget
        
    def create_session_tab(self):
        """Tạo tab quản lý buổi học"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Controls
        controls_layout = QHBoxLayout()
        
        add_session_btn = QPushButton("➕ Tạo Buổi học")
        add_session_btn.setFixedHeight(35)
        add_session_btn.setStyleSheet("""
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
        add_session_btn.clicked.connect(self.add_session)
        
        edit_session_btn = QPushButton("✏️ Sửa")
        edit_session_btn.setFixedHeight(35)
        edit_session_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        
        delete_session_btn = QPushButton("🗑️ Xóa")
        delete_session_btn.setFixedHeight(35)
        delete_session_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        delete_session_btn.clicked.connect(self.delete_session)
        
        auto_generate_btn = QPushButton("🔄 Tạo tự động")
        auto_generate_btn.setFixedHeight(35)
        auto_generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
        """)
        auto_generate_btn.clicked.connect(self.auto_generate_sessions)
        
        controls_layout.addWidget(add_session_btn)
        controls_layout.addWidget(edit_session_btn)
        controls_layout.addWidget(delete_session_btn)
        controls_layout.addWidget(auto_generate_btn)
        controls_layout.addStretch()
        
        # Sessions table
        self.sessions_table = QTableWidget()
        self.sessions_table.setColumnCount(7)
        self.sessions_table.setHorizontalHeaderLabels([
            "Buổi", "Ngày", "Giờ", "Phòng", "Nội dung", "Trạng thái", "Tỷ lệ DD"
        ])
        self.sessions_table.setAlternatingRowColors(True)
        self.sessions_table.setStyleSheet("""
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
        
        # Sample session data
        sessions_data = [
            ["1", "14/10/2024", "07:00-09:30", "101", "Giới thiệu môn học", "Hoàn thành", "95.5%"],
            ["2", "21/10/2024", "07:00-09:30", "101", "Chương 1: Khái niệm", "Hoàn thành", "91.1%"],
            ["3", "28/10/2024", "07:00-09:30", "101", "Chương 2: Biến và kiểu dữ liệu", "Hoàn thành", "88.9%"],
            ["4", "04/11/2024", "07:00-09:30", "101", "Chương 3: Cấu trúc điều khiển", "Hoàn thành", "93.3%"],
            ["5", "11/11/2024", "07:00-09:30", "101", "Bài tập thực hành", "Hoàn thành", "86.7%"],
            ["6", "18/11/2024", "07:00-09:30", "101", "Chương 4: Hàm", "Chưa học", "-"],
            ["7", "25/11/2024", "07:00-09:30", "101", "Bài tập hàm", "Chưa học", "-"]
        ]
        
        self.sessions_table.setRowCount(len(sessions_data))
        for i, row in enumerate(sessions_data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                
                # Color coding for status
                if j == 5:  # Status column
                    if value == "Hoàn thành":
                        item.setStyleSheet("color: #27ae60; font-weight: bold;")
                    elif value == "Chưa học":
                        item.setStyleSheet("color: #95a5a6;")
                        
                self.sessions_table.setItem(i, j, item)
        
        layout.addLayout(controls_layout)
        layout.addWidget(self.sessions_table)
        
        widget.setLayout(layout)
        return widget
        
    def load_lhp_data(self):
        """Tải dữ liệu lớp học phần"""
        # Mock data
        lhp_data = {
            "LHP001": {
                "name": "Lập trình căn bản A1",
                "subject": "IT001 - Lập trình căn bản",
                "teacher": "TS. Nguyễn Văn X",
                "semester": "HK1-2024",
                "student_count": 45,
                "session_count": "5/15",
                "attendance_rate": "91.2%"
            }
        }
        
        if self.lhp_code in lhp_data:
            data = lhp_data[self.lhp_code]
            
            # Update header
            self.lhp_name.setText(data['name'])
            self.lhp_subject.setText(f"Mã LHP: {self.lhp_code} - {data['subject']}")
            self.lhp_teacher.setText(f"Giảng viên: {data['teacher']}")
            self.lhp_semester.setText(f"Học kỳ: {data['semester']}")
            
            self.student_count.setText(f"Sinh viên: {data['student_count']}")
            self.session_count.setText(f"Buổi học: {data['session_count']}")
            self.attendance_rate.setText(f"Tỷ lệ DD: {data['attendance_rate']}")
            
            # Update form
            self.lhp_name_input.setText(data['name'])
            self.subject_combo.setCurrentText(data['subject'])
            self.teacher_combo.setCurrentText(data['teacher'])
            self.semester_combo.setCurrentText(data['semester'])
            
    # Event handlers
    def add_student(self):
        """Thêm sinh viên vào lớp"""
        QMessageBox.information(self, "Thông báo", "Chức năng thêm sinh viên đang được phát triển!")
        
    def remove_student(self):
        """Xóa sinh viên khỏi lớp"""
        current_row = self.students_table.currentRow()
        if current_row >= 0:
            msv = self.students_table.item(current_row, 0).text()
            reply = QMessageBox.question(self, 'Xác nhận', 
                                       f'Bạn có chắc chắn muốn xóa sinh viên {msv} khỏi lớp?',
                                       QMessageBox.Yes | QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                self.students_table.removeRow(current_row)
                QMessageBox.information(self, "Thành công", f"Đã xóa sinh viên {msv} khỏi lớp!")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn sinh viên cần xóa!")
            
    def add_students_by_class(self):
        """Thêm sinh viên theo lớp hành chính"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Thêm sinh viên theo Lớp HC")
        dialog.setFixedSize(400, 200)
        
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Chọn lớp hành chính:"))
        
        class_combo = QComboBox()
        class_combo.addItems(["CNTT01", "CNTT02", "KT01", "QTKD01"])
        layout.addWidget(class_combo)
        
        layout.addWidget(QLabel("Tất cả sinh viên trong lớp sẽ được thêm vào LHP."))
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec_() == QDialog.Accepted:
            selected_class = class_combo.currentText()
            QMessageBox.information(self, "Thành công", 
                                  f"Đã thêm sinh viên từ lớp {selected_class} vào LHP!")
            
    def add_session(self):
        """Thêm buổi học mới"""
        QMessageBox.information(self, "Thông báo", "Chức năng thêm buổi học đang được phát triển!")
        
    def delete_session(self):
        """Xóa buổi học"""
        current_row = self.sessions_table.currentRow()
        if current_row >= 0:
            session_num = self.sessions_table.item(current_row, 0).text()
            reply = QMessageBox.question(self, 'Xác nhận', 
                                       f'Bạn có chắc chắn muốn xóa buổi học {session_num}?',
                                       QMessageBox.Yes | QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                self.sessions_table.removeRow(current_row)
                QMessageBox.information(self, "Thành công", f"Đã xóa buổi học {session_num}!")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn buổi học cần xóa!")
            
    def auto_generate_sessions(self):
        """Tự động tạo các buổi học"""
        reply = QMessageBox.question(self, 'Xác nhận', 
                                   'Tự động tạo 15 buổi học dựa trên lịch đã cấu hình?',
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Thành công", "Đã tự động tạo 15 buổi học!")
            
    def save_changes(self):
        """Lưu thay đổi"""
        QMessageBox.information(self, "Thành công", "Đã lưu thay đổi thông tin lớp học phần!")
        
    def closeEvent(self, event):
        event.accept()
