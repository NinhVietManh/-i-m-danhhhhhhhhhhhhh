# Attendance Management System - PyQt5

Hệ thống quản lý điểm danh sinh viên được xây dựng bằng Python và PyQt5.

## Cấu trúc dự án

```
frontend/
├── main.py                 # File chính để chạy ứng dụng
├── requirements.txt        # Các thư viện cần thiết
├── ui/
│   ├── __init__.py
│   ├── login_window.py     # Màn hình đăng nhập
│   ├── main_window.py      # Cửa sổ chính với sidebar
│   └── attendance_page.py  # Trang quản lý điểm danh
└── README.md
```

## Cài đặt

1. Cài đặt Python 3.8 trở lên

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
python main.py
```

## Thông tin đăng nhập mặc định

- **Username:** admin
- **Password:** admin

## Tính năng

### Màn hình đăng nhập
- Giao diện hiện đại với form đăng nhập
- Xác thực người dùng
- Thông báo lỗi khi đăng nhập sai

### Giao diện chính
- **Sidebar** với các menu:
  - Dashboard
  - User Management
  - Academic (Attendance, Learning Field, Session, Grade, Certificate)
  - Settings
  
- **Trang Attendance Management:**
  - Breadcrumb navigation
  - 3 tabs: Record Attendance, Course Summary, Student summary
  - Attendance Calendar - lịch để chọn ngày điểm danh
  - Quick Attendance - form ghi nhận điểm danh nhanh
    - Chọn khóa học
    - Chọn session/năm học
    - Chọn ngày
    - Nút Record Attendance và Generate Report

## Công nghệ sử dụng

- **Python 3.x**
- **PyQt5** - Framework UI desktop
- **QCalendarWidget** - Widget lịch tích hợp sẵn

## Tùy chỉnh

Bạn có thể tùy chỉnh:
- Màu sắc trong các file `.setStyleSheet()`
- Thêm chức năng backend kết nối database
- Thêm các trang mới trong menu
- Customize calendar và form điểm danh

## Phát triển tiếp

Để kết nối với backend Python:
1. Thêm module API client (requests, httpx)
2. Tạo service layer để gọi API
3. Xử lý dữ liệu từ server và hiển thị lên UI
4. Thêm database (SQLite, PostgreSQL, MySQL)

## Lưu ý

- Đảm bảo đã cài đặt đầy đủ PyQt5
- Nếu gặp lỗi import, chạy: `pip install --upgrade PyQt5`
- Trên một số hệ thống Linux cần cài: `sudo apt-get install python3-pyqt5`
