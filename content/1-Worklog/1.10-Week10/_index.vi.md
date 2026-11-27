---
title: "Worklog Tuần 10"
date: 2026-11-16
weight: 2
chapter: false
pre: " <b> 1.10. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 10:

* Bắt đầu triển khai workshop với đề tài **Bếp Thông Minh**.
* Rà soát mã nguồn hiện có, xác định phạm vi chức năng và các dịch vụ AWS được sử dụng.
* Kiểm tra hoạt động của frontend, backend và cơ sở dữ liệu để lên kế hoạch hoàn thiện.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Xác định mục tiêu và phạm vi workshop Bếp Thông Minh.<br>- Rà soát các chức năng chính của website gợi ý món ăn và thống nhất tập trung vào chức năng gợi ý nấu ăn.<br>- Kiểm tra cấu trúc repository và phân chia các phần frontend, backend. | 16/11/2026 | 16/11/2026 | [GitHub - AWS Final Project Cooking](https://github.com/veexto/AWS-Final-Project-Cooking) |
| 3 | - Kiểm tra mã nguồn frontend và cách website gọi API.<br>- Rà soát các endpoint của API Gateway và chức năng xử lý trong AWS Lambda.<br>- Ghi nhận các điểm cần kiểm tra khi kết nối frontend với backend. | 17/11/2026 | 17/11/2026 | [AWS Lambda](https://docs.aws.amazon.com/lambda/) |
| 4 | - Rà soát cấu trúc dữ liệu công thức trong DynamoDB.<br>- Kiểm tra dữ liệu mẫu và các trường thông tin cần thiết cho chức năng tìm kiếm món ăn.<br>- Đối chiếu kết quả API trả về với dữ liệu công thức hiện có. | 18/11/2026 | 18/11/2026 | [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb/) |
| 5 | - Kiểm tra luồng triển khai frontend trên Amazon S3 và phân phối nội dung qua CloudFront.<br>- Rà soát cấu hình origin và đường dẫn truy cập website.<br>- Kiểm tra khả năng truy cập website sau khi phân phối qua CloudFront. | 19/11/2026 | 19/11/2026 | [Amazon S3](https://docs.aws.amazon.com/s3/) · [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront/) |
| 6 | - Tổng hợp các vấn đề phát hiện trong quá trình kiểm thử frontend, API và dữ liệu.<br>- Lập danh sách các hạng mục cần hoàn thiện cho tuần tiếp theo, bao gồm tìm kiếm công thức, gợi ý bằng AI và chức năng tìm cửa hàng thực phẩm gần người dùng. | 20/11/2026 | 21/11/2026 | [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/) |

### Kết quả đạt được tuần 10:

* Xác định được phạm vi workshop Bếp Thông Minh là website hỗ trợ tìm kiếm và gợi ý món ăn, không tập trung vào chức năng đặt hàng.
* Rà soát được cấu trúc tổng thể của mã nguồn frontend và backend.
* Hệ thống hóa luồng xử lý chính: người dùng thao tác trên website, frontend gửi yêu cầu đến API Gateway, Lambda xử lý và truy xuất dữ liệu từ DynamoDB.
* Kiểm tra lại phương án lưu trữ frontend trên S3 và phân phối nội dung thông qua CloudFront.
* Xây dựng danh sách các hạng mục cần tiếp tục kiểm thử và hoàn thiện trong tuần 11.
