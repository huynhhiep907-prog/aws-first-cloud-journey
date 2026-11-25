---
title: "Week 5 Worklog"
date: 2026-10-12
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:

* Hiểu cách thiết kế API để frontend giao tiếp với backend serverless.
* Nắm các khái niệm route, method, integration, CORS và cơ chế xử lý lỗi HTTP.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | **Thứ 2**<br>Tìm hiểu API Gateway và vai trò làm cổng tiếp nhận request; phân biệt REST API và HTTP API ở mức mục đích sử dụng và tính năng. | https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html | https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html | undefined |
| 2 | **Thứ 3**<br>Ôn tập HTTP request/response: method GET, POST, PUT, DELETE; status code, header, query string và request body; liên hệ với API tra cứu dữ liệu. | https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview | https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview | undefined |
| 3 | **Thứ 4**<br>Tìm hiểu cách tạo route và kết nối API Gateway với Lambda; đọc về Lambda proxy integration và cấu trúc event mà Lambda nhận được. | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html | undefined |
| 4 | **Thứ 5**<br>Tìm hiểu CORS: origin, allowed methods, allowed headers và preflight OPTIONS; xác định vì sao trình duyệt có thể chặn request giữa hai domain. | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html | undefined |
| 5 | **Thứ 6**<br>Tìm hiểu cách thiết kế response API nhất quán: status code, message, dữ liệu JSON và xử lý trường hợp thiếu tham số hoặc không tìm thấy dữ liệu. | https://developer.mozilla.org/en-US/docs/Web/HTTP/Status | https://developer.mozilla.org/en-US/docs/Web/HTTP/Status | undefined |
| 6 | **Thứ 7**<br>Tìm hiểu quy trình kiểm tra API bằng công cụ gửi HTTP request; thực hành đọc response, kiểm tra header và phân biệt lỗi từ API Gateway với lỗi bên trong Lambda. | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-testing.html | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-testing.html | undefined |

### Week 5 Achievements:

* Phân biệt được API Gateway REST API và HTTP API ở mức cơ bản.
* Hiểu cấu trúc HTTP request/response và các method thường dùng.
* Nắm được cách API Gateway chuyển request đến Lambda thông qua integration.
* Hiểu CORS và biết cách đọc status code, response JSON để khoanh vùng lỗi API.
