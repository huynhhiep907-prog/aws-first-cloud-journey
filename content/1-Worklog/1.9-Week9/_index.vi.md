---
title: "Worklog Tuần 9"
date: 2026-11-09
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu tuần 9:

* Khám phá các dịch vụ dựa trên vị trí có thể hỗ trợ tìm kiếm cửa hàng bán nguyên liệu gần người dùng.
* Tổng hợp kiến thức về giám sát, bảo mật và quản lý chi phí trên các dịch vụ AWS đã tìm hiểu.
* Ôn tập luồng hoạt động dự kiến của ứng dụng và chuẩn bị kế hoạch phân công rõ ràng cho nhóm ba thành viên trước giai đoạn Workshop.

### Các công việc cần triển khai trong tuần này:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 1 | - Khám phá Amazon Location Service và các khả năng chính, bao gồm Maps, Places, Routes và Geofences.<br>- Xác định khả năng Places phù hợp với chức năng tìm kiếm cửa hàng gần người dùng.<br>- Ôn tập các trường hợp sử dụng tổng quát của dịch vụ. | 09/11/2026 | 09/11/2026 | [Amazon Location Service là gì?](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html) |
| 2 | - Tìm hiểu place search và nearby-place search.<br>- Hiểu sự khác nhau giữa tìm kiếm địa điểm bằng văn bản và tìm kiếm dựa trên tọa độ địa lý.<br>- Ôn tập cách vị trí tìm kiếm và phạm vi địa lý ảnh hưởng đến kết quả trả về. | 10/11/2026 | 10/11/2026 | [Amazon Location Places](https://docs.aws.amazon.com/location/latest/developerguide/places.html)<br>[Search Nearby](https://docs.aws.amazon.com/location/latest/developerguide/search-nearby.html) |
| 3 | - Tìm hiểu geocoding và reverse geocoding.<br>- Hiểu cách chuyển địa chỉ được nhập thành tọa độ và chuyển tọa độ thành địa chỉ dễ đọc.<br>- Ôn tập quyền truy cập của Browser Geolocation API và phương án nhập địa chỉ thủ công khi GPS không khả dụng. | 11/11/2026 | 11/11/2026 | [Geocoding](https://docs.aws.amazon.com/location/latest/developerguide/geocoding.html)<br>[MDN Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) |
| 4 | - Ôn tập các vấn đề bảo mật đối với thành phần ứng dụng và quyền truy cập dịch vụ AWS.<br>- Hiểu lý do không nhúng thông tin xác thực vào mã frontend và lý do backend execution roles cần tuân theo nguyên tắc đặc quyền tối thiểu.<br>- Tìm hiểu AWS Well-Architected Framework, tập trung vào Security và Reliability. | 12/11/2026 | 12/11/2026 | [Bảo mật Amazon Location](https://docs.aws.amazon.com/location/latest/developerguide/security.html)<br>[AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) |
| 5 | - Khám phá metrics, logs và alarms của Amazon CloudWatch.<br>- Xác định thông tin giám sát hữu ích cho Lambda functions và API requests.<br>- Tìm hiểu cách log hỗ trợ điều tra lỗi, timeout và các hành vi bất thường. | 13/11/2026 | 13/11/2026 | [Amazon CloudWatch là gì?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br>[Lambda Monitoring](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html) |
| 6 | - Tìm hiểu cách AWS Pricing Calculator ước tính chi phí dịch vụ và xem xét các giả định về request, storage và data transfer.<br>- Ôn tập AWS Budgets và Cost Explorer để theo dõi chi tiêu thực tế.<br>- Với vai trò nhóm ba thành viên, rà soát trách nhiệm tổng quan về frontend, backend, database và location service; ghi lại các câu hỏi còn tồn tại và chuẩn bị phân công nhiệm vụ Workshop cho giai đoạn tiếp theo. | 14/11/2026 | 14/11/2026 | [AWS Pricing Calculator](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html)<br>[AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html) |

### Kết quả đạt được tuần 9:

* Hiểu vai trò của Amazon Location Service Places, nearby search và geocoding đối với các tính năng dựa trên vị trí.
* Tìm hiểu cách quyền truy cập vị trí của trình duyệt và việc nhập địa chỉ thủ công hỗ trợ các tình huống sử dụng khác nhau.
* Ôn tập trách nhiệm bảo mật, quyền truy cập theo nguyên tắc đặc quyền tối thiểu và các nguyên tắc Well-Architected liên quan.
* Làm quen với hoạt động giám sát bằng CloudWatch và cách sử dụng logs để điều tra vấn đề của ứng dụng.
* Ôn tập các công cụ ước tính chi phí và theo dõi chi tiêu.
* Chuẩn bị kế hoạch phân chia trách nhiệm sơ bộ cho ba thành viên và danh sách các nội dung cần xử lý trong giai đoạn Workshop ở tuần 10–11.
