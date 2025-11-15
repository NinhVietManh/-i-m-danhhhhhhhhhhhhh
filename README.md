# Hệ thống Quản lý Điểm danh

Ứng dụng quản lý điểm danh hiện đại với giao diện thân thiện, hỗ trợ đa vai trò người dùng.

## Tính năng chính

### 🔐 Hệ thống đăng nhập
- Phân quyền theo vai trò: **Admin**, **Giảng viên**, **Sinh viên**
- Giao diện đăng nhập đẹp mắt và bảo mật

### 👤 Tài khoản Demo
- **Admin**: `admin` / `admin123`
- **Giảng viên**: `teacher` / `teacher123`  
- **Sinh viên**: `student` / `student123`

## Giao diện theo Vai trò

### 🔧 ADMIN - Quản trị viên
**Cửa sổ chính: W_Admin_Main**
- Dashboard với thống kê tổng quan
- Menu sidebar điều hướng đầy đủ

**Các trang quản lý:**
1. **📚 Quản lý Khoa/Lớp/Môn** (Page_QuanLyChung)
   - Thêm, sửa, xóa Khoa
   - Quản lý Lớp Hành Chính  
   - Quản lý Môn Học

2. **👥 Quản lý Người dùng** (Page_QuanLyNguoiDung)
   - Tab Sinh viên: Thêm/Sửa/Xóa, Import Excel/CSV
   - Tab Giảng viên: Quản lý thông tin GV
   - Mở chi tiết sinh viên (W_Admin_ChiTietSV)

3. **📖 Quản lý Lớp học phần** (Page_QuanLyLopHocPhan)
   - Tạo/Sửa/Xóa Lớp Học Phần
   - Gán Giảng viên phụ trách
   - Mở chi tiết LHP (W_Admin_ChiTietLHP)

4. **📊 Báo cáo & Lịch sử** (Page_BaoCao)
   - Báo cáo toàn diện (1-8)
   - Lịch sử Audit Log
   - Xuất Excel

**Chi tiết Sinh viên (W_Admin_ChiTietSV):**
- Tab thông tin cá nhân (cập nhật Email, SĐT, Địa chỉ...)
- Tab đăng ký khuôn mặt (Camera, chụp ảnh/quay video)
- Tab lịch sử điểm danh

**Chi tiết LHP (W_Admin_ChiTietLHP):**
- Tab thông tin LHP
- Tab quản lý sinh viên (Thêm/Xóa SV, thêm theo lớp HC)
- Tab quản lý buổi học (Tạo/Sửa/Xóa buổi học)

### 👨‍🏫 GIẢNG VIÊN - Teacher
**Cửa sổ chính: W_GiangVien_Main**
- Dashboard với lịch dạy hôm nay
- Thống kê lớp học phần được phân công

**Chức năng chính:**
1. **📚 Lớp học phần** - Xem các LHP được phân công
2. **🎯 Điểm danh** (W_GV_DiemDanh) - 5 phương thức:
   - ✋ **Điểm danh Thủ công**: Tick 3 trạng thái (Có mặt/Vắng P/Vắng KP)
   - 👤 **Điểm danh Khuôn mặt**: Camera nhận diện SV
   - 🔢 **Nhập Mã điểm danh**: GV tự tạo mã (VD: "LOP123")
   - 📱 **Tạo Mã QR**: Tự động tạo QR cho SV quét
   - 👀 **Theo dõi điểm danh**: Xem IP và thời gian điểm danh
3. **📊 Báo cáo** - Xuất các báo cáo GV (9-14)

### 👨‍🎓 SINH VIÊN - Student  
**Cửa sổ chính: W_SinhVien_Main**
- **⚠️ Thanh Cảnh báo Chuyên cần** cố định trên cùng:
  - 🟢 Tốt (<10% vắng)
  - 🟡 Cảnh báo (10-20% vắng)  
  - 🔴 Nguy hiểm (≥20% vắng - nguy cơ cấm thi)

**Các Tab chức năng:**
1. **✅ Tab Điểm danh**
   - Hiển thị lớp học hôm nay
   - Nhập mã điểm danh (từ GV)
   - Trạng thái điểm danh gần đây

2. **📅 Tab Lịch học & Chuyên cần**
   - Thống kê % chuyên cần cá nhân (15, 16)
   - Danh sách TẤT CẢ buổi học (đã học + sắp học)
   - Trạng thái từng buổi (Có mặt/Vắng P/Vắng KP)

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
