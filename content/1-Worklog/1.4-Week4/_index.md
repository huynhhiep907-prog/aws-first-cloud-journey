---
title: "Week 4 Worklog"
date: 2026-10-05
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

### Week 4 Objectives:

* Hiểu mô hình serverless và vòng đời xử lý của AWS Lambda.
* Nắm cách viết, cấu hình, cấp quyền và theo dõi một hàm Lambda bằng Python.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | **Thứ 2**<br>Tìm hiểu kiến trúc serverless, đặc điểm event-driven và cách Lambda tính toán theo lần gọi thay vì phải duy trì máy chủ liên tục. | https://docs.aws.amazon.com/lambda/latest/dg/welcome.html | https://docs.aws.amazon.com/lambda/latest/dg/welcome.html | undefined |
| 2 | **Thứ 3**<br>Đọc cấu trúc một Lambda function: handler, event, context, runtime và deployment package; tìm hiểu định dạng đầu vào/đầu ra JSON. | https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html | https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html | undefined |
| 3 | **Thứ 4**<br>Tìm hiểu cách cấu hình runtime Python, environment variables, timeout và memory; phân biệt cấu hình hàm với dữ liệu truyền trong event. | https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html | https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html | undefined |
| 4 | **Thứ 5**<br>Tìm hiểu Lambda execution role và cách cấp quyền tối thiểu cho hàm truy cập dịch vụ khác; xem xét vì sao không lưu Access Key trực tiếp trong code. | https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html | https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html | undefined |
| 5 | **Thứ 6**<br>Tìm hiểu CloudWatch Logs dành cho Lambda: log group, log stream, log event và cách ghi log để hỗ trợ tìm lỗi trong quá trình xử lý request. | https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html | https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html | undefined |
| 6 | **Thứ 7**<br>Đọc hướng dẫn kiểm thử Lambda bằng test event; tìm hiểu cách mô phỏng request, kiểm tra response và nhận diện lỗi do dữ liệu đầu vào không hợp lệ. | https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html | https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html | undefined |

### Week 4 Achievements:

* Hiểu mô hình serverless và cơ chế kích hoạt Lambda theo sự kiện.
* Nắm cấu trúc handler Python và cách Lambda nhận/trả dữ liệu JSON.
* Biết các cấu hình quan trọng như runtime, timeout, memory và environment variables.
* Hiểu cách sử dụng execution role, CloudWatch Logs và test event để quản lý, kiểm tra hàm.
