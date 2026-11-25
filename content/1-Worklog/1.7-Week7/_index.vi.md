---
title: "Worklog Tuần 7"
date: 2026-10-26
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:

* Hiểu cách API cho phép ứng dụng frontend giao tiếp với các dịch vụ backend.
* Tìm hiểu các khái niệm chính của Amazon API Gateway và cách tích hợp với AWS Lambda.
* Ôn tập HTTP methods, định dạng request, CORS và bảo mật API.

### Các công việc cần triển khai trong tuần này:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 1 | - Ôn tập mô hình client-server và vai trò của API giữa trình duyệt với logic backend.<br>- Hiểu endpoints, resources, methods, requests và responses.<br>- Xác định các thao tác API mà một ứng dụng khám phá công thức nấu ăn có thể cần. | 26/10/2026 | 26/10/2026 | [Amazon API Gateway User Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) |
| 2 | - Tìm hiểu các khái niệm REST API và những HTTP methods phổ biến: GET, POST, PUT, PATCH và DELETE.<br>- Hiểu path parameters, query-string parameters và request bodies.<br>- Ôn tập các method phù hợp cho thao tác đọc và cập nhật dữ liệu. | 27/10/2026 | 27/10/2026 | [HTTP Request Methods – MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)<br>[API Gateway Concepts](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html) |
| 3 | - Tìm hiểu các thành phần cơ bản của API Gateway HTTP API.<br>- Khám phá routes, integrations, stages và khái niệm deployment.<br>- So sánh tổng quan HTTP APIs và REST APIs. | 28/10/2026 | 28/10/2026 | [Chọn loại API Gateway API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)<br>[HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html) |
| 4 | - Tìm hiểu cách API Gateway gọi Lambda function thông qua integration.<br>- Hiểu cấu trúc event đầu vào và response được function trả về.<br>- Ôn tập cách query parameters được truyền đến backend để lọc hoặc tìm kiếm dữ liệu. | 29/10/2026 | 29/10/2026 | [Lambda Proxy Integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html) |
| 5 | - Tìm hiểu Cross-Origin Resource Sharing (CORS) là gì và lý do trình duyệt áp dụng cơ chế này.<br>- Ôn tập cách allowed origins, methods và headers ảnh hưởng đến request từ frontend đến API.<br>- Xác định các lỗi cấu hình CORS thường gặp. | 30/10/2026 | 30/10/2026 | [CORS cho HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html)<br>[MDN – CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) |
| 6 | - Ôn tập các tùy chọn xác thực và phân quyền API ở mức tổng quan.<br>- Tìm hiểu mục đích của throttling, request validation và access logging.<br>- Tìm hiểu các mã phản hồi API phổ biến và phân biệt lỗi phía client với lỗi backend. | 31/10/2026 | 31/10/2026 | [API Gateway Security](https://docs.aws.amazon.com/apigateway/latest/developerguide/security.html)<br>[API Gateway Monitoring](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring-cloudwatch.html) |

### Kết quả đạt được tuần 7:

* Hiểu cách API kết nối request từ frontend với logic xử lý của backend.
* Tìm hiểu các HTTP methods phổ biến và vai trò của path parameters, query parameters và request bodies.
* Làm quen với routes, integrations, stages và các loại API của API Gateway.
* Hiểu cách API Gateway có thể gọi Lambda và truyền dữ liệu request đến function.
* Tìm hiểu mục đích của CORS, throttling, logging và các biện pháp bảo mật API cơ bản.
