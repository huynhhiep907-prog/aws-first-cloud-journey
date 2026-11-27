---
title: "Worklog Tuần 11"
date: 2026-11-23
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---


### Mục tiêu tuần 11:

* Tiếp tục hoàn thiện và kiểm thử workshop Bếp Thông Minh.
* Rà soát các chức năng tìm kiếm công thức, gợi ý bằng AI và tìm cửa hàng thực phẩm.
* Hoàn thiện tài liệu proposal, sơ đồ kiến trúc và ước tính chi phí AWS.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Kiểm tra lại chức năng tìm kiếm công thức theo nguyên liệu và các bộ lọc món ăn.<br>- Đối chiếu kết quả tìm kiếm với dữ liệu công thức trong DynamoDB.<br>- Ghi nhận các trường hợp kết quả chưa khớp yêu cầu để tiếp tục điều chỉnh. | 23/11/2026 | 23/11/2026 | [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb/) |
| 3 | - Rà soát chức năng tìm cửa hàng thực phẩm gần người dùng sử dụng Amazon Location Service.<br>- Kiểm tra quyền truy cập và dữ liệu địa điểm trả về từ backend.<br>- Đánh giá kết quả tìm kiếm theo phạm vi và loại cửa hàng mong muốn. | 24/11/2026 | 24/11/2026 | [Amazon Location Service](https://docs.aws.amazon.com/location/) |
| 4 | - Kiểm tra luồng chatbot/gợi ý món ăn sử dụng Amazon Bedrock với mô hình Nova Micro.<br>- Theo dõi phản hồi từ Lambda và ghi nhận lỗi giới hạn quota khi gọi mô hình.<br>- Rà soát phương án phản hồi dự phòng để chức năng vẫn có thể trả kết quả khi Bedrock chưa khả dụng. | 25/11/2026 | 25/11/2026 | [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/) |
| 5 | - Cập nhật nội dung proposal cho workshop Bếp Thông Minh.<br>- Hoàn thiện mô tả các dịch vụ AWS, luồng hoạt động và sơ đồ kiến trúc có CloudFront.<br>- Sử dụng AWS Pricing Calculator để lập ước tính chi phí theo các mức tải giả định; tổng hợp các dịch vụ và giả định sử dụng. | 26/11/2026 | 26/11/2026 | [AWS Pricing Calculator](https://calculator.aws/) |
| 6 | - Rà soát lại nội dung proposal, sơ đồ kiến trúc và bảng chi phí ước tính.<br>- Kiểm tra tính nhất quán giữa các dịch vụ được mô tả trong tài liệu và kiến trúc triển khai.<br>- Tổng hợp trạng thái workshop, các giới hạn còn tồn tại và những nội dung cần tiếp tục kiểm tra. | 27/11/2026 | 27/11/2026 | [AWS Architecture Center](https://aws.amazon.com/architecture/) |

### Kết quả đạt được tuần 11:

* Tiếp tục kiểm tra các chức năng chính của Bếp Thông Minh, gồm tìm kiếm công thức, lọc món ăn và tìm cửa hàng thực phẩm gần người dùng.
* Rà soát luồng tích hợp Amazon Location Service và ghi nhận các vấn đề cần lưu ý về dữ liệu địa điểm.
* Kiểm tra tích hợp Amazon Bedrock Nova Micro; ghi nhận lỗi giới hạn quota và duy trì phương án phản hồi dự phòng, không xem lời gọi mô hình trực tiếp là đã hoạt động ổn định.
* Cập nhật proposal, mô tả kiến trúc triển khai và bổ sung CloudFront vào luồng phân phối frontend.
* Lập bảng ước tính chi phí các dịch vụ AWS bằng AWS Pricing Calculator theo các giả định tải sử dụng. Đây là chi phí dự kiến, không phải hóa đơn thực tế.
* Tổng hợp được các hạng mục đã rà soát, các giới hạn còn tồn tại và nội dung cần tiếp tục hoàn thiện.
