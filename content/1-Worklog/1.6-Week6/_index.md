---
title: "Week 6 Worklog"
date: 2026-10-19
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:

* Hiểu mô hình cơ sở dữ liệu NoSQL và cách tổ chức dữ liệu theo access pattern.
* Nắm các thao tác cơ bản với DynamoDB và cách backend truy vấn dữ liệu hiệu quả.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | **Thứ 2**<br>Tìm hiểu Amazon DynamoDB: table, item, attribute và sự khác biệt giữa cơ sở dữ liệu NoSQL dạng key-value/document với cơ sở dữ liệu quan hệ. | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html | undefined |
| 2 | **Thứ 3**<br>Tìm hiểu partition key và sort key; phân tích cách lựa chọn khóa dựa trên câu hỏi ứng dụng cần trả lời thay vì chỉ dựa vào cấu trúc dữ liệu. | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html | undefined |
| 3 | **Thứ 4**<br>Đọc về các thao tác PutItem, GetItem, UpdateItem và DeleteItem; tìm hiểu cách biểu diễn dữ liệu món ăn/công thức dưới dạng item JSON. | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html | undefined |
| 4 | **Thứ 5**<br>So sánh Query và Scan; tìm hiểu vì sao Query thường phù hợp hơn khi truy vấn theo khóa và Scan có thể đọc nhiều dữ liệu hơn cần thiết. | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html | undefined |
| 5 | **Thứ 6**<br>Tìm hiểu Global Secondary Index (GSI) và Local Secondary Index (LSI); xem xét trường hợp cần tìm kiếm theo thuộc tính không phải khóa chính. | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html | undefined |
| 6 | **Thứ 7**<br>Tìm hiểu DynamoDB với AWS SDK for Python (Boto3), cách Lambda gọi thao tác database và các lưu ý về quyền IAM, phân trang và xử lý lỗi. | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html | undefined |

### Week 6 Achievements:

* Hiểu cấu trúc dữ liệu DynamoDB và cách phân biệt table, item, attribute.
* Biết vai trò của partition key/sort key trong thiết kế dữ liệu.
* Phân biệt thao tác CRUD, Query và Scan; hiểu mục đích của secondary index.
* Nắm cách backend Python tương tác với DynamoDB thông qua SDK và IAM role.
