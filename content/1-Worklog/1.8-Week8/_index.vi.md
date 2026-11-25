---
title: "Worklog Tuần 8"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:

* Hiểu mô hình dữ liệu NoSQL và cách Amazon DynamoDB lưu trữ dữ liệu ứng dụng.
* Tìm hiểu cách thiết kế keys và tổ chức dữ liệu dựa trên các mẫu truy cập của ứng dụng.
* Khám phá cách backend service truy cập DynamoDB một cách an toàn và hiệu quả.

### Các công việc cần triển khai trong tuần này:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 1 | - Tìm hiểu các khái niệm Amazon DynamoDB, bao gồm tables, items và attributes.<br>- So sánh cơ sở dữ liệu key-value/document với cơ sở dữ liệu quan hệ.<br>- Xác định dữ liệu có thể được lưu trữ dưới dạng các bản ghi công thức nấu ăn. | 02/11/2026 | 02/11/2026 | [Giới thiệu DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) |
| 2 | - Tìm hiểu partition keys và sort keys.<br>- Hiểu cách thiết kế primary key ảnh hưởng đến việc phân phối và truy xuất dữ liệu.<br>- Xem xét các key phù hợp để định danh công thức và nhóm các bản ghi có liên quan. | 03/11/2026 | 03/11/2026 | [Các thành phần cốt lõi của DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html) |
| 3 | - Ôn tập các thao tác PutItem, GetItem, UpdateItem và DeleteItem.<br>- Hiểu cách các attributes có cấu trúc được biểu diễn trong DynamoDB items.<br>- Khám phá cách lưu trữ tên món ăn, nguyên liệu và hướng dẫn chế biến. | 04/11/2026 | 04/11/2026 | [Làm việc với Items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html) |
| 4 | - So sánh hai thao tác Query và Scan.<br>- Hiểu lý do Query thường được ưu tiên khi đã biết partition key.<br>- Ôn tập tác động của việc đọc các bản ghi không cần thiết đến hiệu suất và chi phí. | 05/11/2026 | 05/11/2026 | [Truy vấn Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) |
| 5 | - Tìm hiểu Global Secondary Indexes (GSI) và Local Secondary Indexes (LSI).<br>- Tìm hiểu khi nào index hữu ích cho việc truy vấn theo một attribute khác với primary key của table.<br>- Ôn tập các yếu tố bổ sung về dung lượng lưu trữ và thao tác ghi khi sử dụng indexes. | 06/11/2026 | 06/11/2026 | [Secondary Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html) |
| 6 | - Khám phá cách ứng dụng Python truy cập DynamoDB thông qua Boto3.<br>- Ôn tập các quyền IAM cần thiết để ứng dụng đọc và ghi các items trong table.<br>- Tìm hiểu pagination và xử lý exception cơ bản khi truy xuất bản ghi. | 07/11/2026 | 07/11/2026 | [DynamoDB với Python](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html)<br>[Boto3 DynamoDB Guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html) |

### Kết quả đạt được tuần 8:

* Hiểu DynamoDB tables, items, attributes và các khái niệm primary key.
* Tìm hiểu cách partition keys và sort keys hỗ trợ truy cập dữ liệu hiệu quả.
* Phân biệt các thao tác CRUD phổ biến và cách truy cập dữ liệu bằng Query/Scan.
* Hiểu mục đích của secondary indexes và các yếu tố cần cân nhắc khi sử dụng.
* Làm quen với việc truy cập DynamoDB từ Python thông qua Boto3 và cấp quyền bằng IAM roles.
