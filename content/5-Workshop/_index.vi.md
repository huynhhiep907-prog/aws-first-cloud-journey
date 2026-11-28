---
title: "Workshop"
date: 2026-11-27
weight: 5
chapter: false
pre: "<b>5. </b>"
---

# Bếp Thông Minh (Smart Kitchen) – AWS Workshop

## Tổng quan

Workshop này trình bày quá trình xây dựng và triển khai **Bếp Thông Minh (Smart Kitchen)**, một ứng dụng gợi ý công thức nấu ăn được phát triển trên các dịch vụ được quản lý của AWS. Ứng dụng hỗ trợ người dùng tìm kiếm món ăn dựa trên nguyên liệu sẵn có, ngân sách, thời gian nấu, chế độ ăn uống, tâm trạng và thời tiết. Ngoài ra, ứng dụng còn hỗ trợ tìm kiếm các cửa hàng bán nguyên liệu ở gần người dùng.

Giải pháp được thiết kế với frontend tĩnh và backend serverless tách biệt. Amazon S3 lưu trữ các tệp frontend, trong khi Amazon CloudFront phân phối website qua HTTPS. Amazon API Gateway cung cấp các endpoint cho ứng dụng và chuyển tiếp yêu cầu đến AWS Lambda. Hàm Lambda truy xuất dữ liệu công thức từ Amazon DynamoDB và tích hợp với Amazon Location Service để chuyển đổi địa chỉ thành tọa độ cũng như tìm kiếm các địa điểm gần đó. Amazon Bedrock được tích hợp để hỗ trợ gợi ý công thức nấu ăn qua hội thoại; ứng dụng có cơ chế phản hồi dự phòng khi không thể gọi mô hình AI.

## Các dịch vụ AWS sử dụng

| Dịch vụ AWS | Vai trò |
| :--- | :--- |
| Amazon S3 | Lưu trữ các tệp frontend tĩnh |
| Amazon CloudFront | Phân phối frontend qua HTTPS |
| Amazon API Gateway | Cung cấp các HTTP route cho ứng dụng |
| AWS Lambda | Xử lý tìm kiếm công thức, tìm cửa hàng gần vị trí người dùng và yêu cầu chatbot |
| Amazon DynamoDB | Lưu trữ dữ liệu công thức nấu ăn |
| Amazon Location Service | Chuyển đổi địa chỉ người dùng nhập thành tọa độ và tìm kiếm cửa hàng gần đó |
| Amazon Bedrock | Hỗ trợ gợi ý công thức nấu ăn bằng AI |
| Amazon CloudWatch | Lưu trữ log trong quá trình thực thi Lambda |

## Nội dung Workshop

1. [Tổng quan và các yêu cầu chuẩn bị](5.1-Workshop-overview/)
2. [Tạo cơ sở dữ liệu DynamoDB](5.2-Setup-Dynamodb/)
3. [Cấu hình IAM Role](5.3-Configure-IAM-role/)
4. [Triển khai backend bằng AWS Lambda](5.4-Deploy-Lambda-backend/)
5. [Cấu hình Amazon API Gateway](5.5-Configure-API-gateway/)
6. [Triển khai frontend lên S3 và CloudFront](5.6-Deploy-S3-Cloudfront/)
7. [Kiểm thử ứng dụng](5.7-Test-Application/)
8. [Dọn dẹp tài nguyên](5.8-Cleanup/)
