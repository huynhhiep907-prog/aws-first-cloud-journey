---
title: "Worklog Tuần 6"
date: 2026-10-19
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:

* Hiểu mô hình điện toán serverless và vai trò của AWS Lambda.
* Tìm hiểu các khái niệm thực thi Lambda, event payloads, cấu hình runtime và quyền truy cập.
* Khám phá cách logic ứng dụng backend có thể chạy theo yêu cầu mà không cần quản lý máy chủ.

### Các công việc cần triển khai trong tuần này:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 1 | - Tìm hiểu kiến trúc serverless và so sánh với việc quản lý máy chủ luôn hoạt động.<br>- Hiểu cơ chế thực thi hướng sự kiện (event-driven) và mô hình tính phí theo mức sử dụng.<br>- Xác định các tác vụ phù hợp với serverless functions, chẳng hạn xử lý một yêu cầu tìm kiếm. | 19/10/2026 | 19/10/2026 | [AWS Serverless](https://aws.amazon.com/serverless/) |
| 2 | - Tìm hiểu cấu trúc cơ bản của một AWS Lambda function.<br>- Ôn tập các runtime được hỗ trợ, handler functions, deployment packages và environment variables.<br>- Hiểu sự khác nhau giữa mã nguồn của function và môi trường thực thi Lambda. | 20/10/2026 | 20/10/2026 | [Lambda Programming Model](https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html) |
| 3 | - Tìm hiểu các kiểu gọi Lambda và xử lý hướng sự kiện.<br>- Hiểu tổng quan về synchronous và asynchronous invocation.<br>- Ôn tập cách function nhận event và trả về response. | 21/10/2026 | 21/10/2026 | [Invoking Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html) |
| 4 | - Khám phá các tùy chọn cấu hình Lambda, bao gồm memory, timeout, temporary storage và environment variables.<br>- Hiểu cách các thiết lập này ảnh hưởng đến hoạt động và chi phí của function.<br>- Ôn tập lý do cấu hình timeout và memory cần phù hợp với workload. | 22/10/2026 | 22/10/2026 | [Configuring Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html) |
| 5 | - Tìm hiểu Lambda execution roles và các quyền cần thiết cho một function.<br>- Phân biệt execution role với quyền của người gọi function.<br>- Ôn tập cách một function chỉ nên được cấp những quyền cần thiết để truy cập nguồn dữ liệu. | 23/10/2026 | 23/10/2026 | [Lambda Execution Role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) |
| 6 | - Ôn tập việc ghi log của Lambda và cách sử dụng CloudWatch Logs.<br>- Tìm hiểu cách đọc invocation logs và xác định lỗi hoặc timeout.<br>- Khám phá các ví dụ AWS Lambda bằng Python để hiểu cấu trúc của một function xử lý request. | 24/10/2026 | 24/10/2026 | [Lambda Logging](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html)<br>[Python Lambda Handler](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html) |

### Kết quả đạt được tuần 6:

* Hiểu mô hình điện toán serverless và event-driven.
* Tìm hiểu cấu trúc của Lambda function và vai trò của handler, runtime và deployment package.
* Làm quen với các kiểu invocation và quy trình xử lý event/response.
* Hiểu cách memory, timeout và environment variables ảnh hưởng đến cấu hình function.
* Tìm hiểu tầm quan trọng của Lambda execution roles và CloudWatch Logs đối với vận hành an toàn, xử lý sự cố.
