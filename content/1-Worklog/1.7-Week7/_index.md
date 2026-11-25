---
title: "Week 7 Worklog"
date: 2026-10-26
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:

* Tìm hiểu dịch vụ định vị và tìm kiếm địa điểm để hỗ trợ chức năng tìm cửa hàng gần người dùng.
* Hiểu luồng xử lý vị trí, quyền truy cập và các phương án dự phòng khi không lấy được GPS.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | **Thứ 2**<br>Tìm hiểu Amazon Location Service và các nhóm chức năng Maps, Places, Routes và Geofences; xác định Places phù hợp với bài toán tìm kiếm địa điểm. | 10/26/2026 | 10/26/2026 | https://docs.aws.amazon.com/location/latest/developerguide/what-is.html |
| 2 | **Thứ 3**<br>Tìm hiểu Places API và chức năng tìm kiếm địa điểm theo từ khóa; phân biệt tìm kiếm tự do với tìm kiếm theo danh mục/loại địa điểm. | 10/27/2026 | 10/27/2026 | https://docs.aws.amazon.com/location/latest/developerguide/places.html |
| 3 | **Thứ 4**<br>Đọc về tìm kiếm địa điểm gần tọa độ và các tham số vị trí, bán kính/phạm vi tìm kiếm; tìm hiểu cách xử lý kết quả có nhiều loại địa điểm. | 10/28/2026 | 10/28/2026 | https://docs.aws.amazon.com/location/latest/developerguide/search-nearby.html |
| 4 | **Thứ 5**<br>Tìm hiểu Geocoding và Reverse Geocoding; phân tích cách chuyển địa chỉ người dùng nhập thành tọa độ và cách chuyển tọa độ thành địa chỉ dễ đọc. | 10/29/2026 | 10/29/2026 | https://docs.aws.amazon.com/location/latest/developerguide/geocoding.html |
| 5 | **Thứ 6**<br>Tìm hiểu Geolocation API trên trình duyệt: yêu cầu quyền người dùng, điều kiện HTTPS và cách xử lý trường hợp người dùng từ chối chia sẻ vị trí. | 10/30/2026 | 10/30/2026 | https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API |
| 6 | **Thứ 7**<br>Tìm hiểu cách bảo vệ tài nguyên Amazon Location bằng IAM và cách backend gọi dịch vụ thay cho việc để thông tin xác thực nhạy cảm ở frontend. | 10/31/2026 | 10/31/2026 | https://docs.aws.amazon.com/location/latest/developerguide/security.html |

### Week 7 Achievements:

* Hiểu các chức năng chính của Amazon Location Service và vai trò của Places.
* Nắm được khác biệt giữa tìm kiếm theo từ khóa, tìm kiếm gần tọa độ và geocoding.
* Hiểu luồng lấy vị trí GPS trên trình duyệt và phương án nhập địa chỉ thủ công khi người dùng từ chối quyền.
* Nhận biết các yêu cầu bảo mật khi tích hợp dịch vụ vị trí vào backend.
