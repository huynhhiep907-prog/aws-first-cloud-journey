---
title: "Week 2 Worklog"
date: 2026-09-21
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives:

* Hiểu cách quản lý danh tính và quyền truy cập trong AWS theo nguyên tắc đặc quyền tối thiểu.
* Làm quen với công cụ dòng lệnh và môi trường thao tác AWS phục vụ các bước triển khai sau này.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | **Thứ 2**<br>Tìm hiểu IAM User, Group, Role và Policy; phân biệt danh tính người dùng với vai trò mà dịch vụ AWS đảm nhận. | https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html | https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html | undefined |
| 2 | **Thứ 3**<br>Đọc cấu trúc IAM Policy: Effect, Action, Resource và Condition; thực hành phân tích một policy mẫu để xác định quyền được cấp. | https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html | https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html | undefined |
| 3 | **Thứ 4**<br>Tìm hiểu MFA, thông tin xác thực dài hạn và temporary credentials; ghi chú cách bảo vệ tài khoản root và tránh đưa Access Key lên GitHub. | https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html | https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html | undefined |
| 4 | **Thứ 5**<br>Tìm hiểu AWS CloudShell: môi trường terminal trên trình duyệt, các công cụ có sẵn và cách kiểm tra Region/tài khoản trước khi thao tác. | https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html | https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html | undefined |
| 5 | **Thứ 6**<br>Tìm hiểu AWS CLI profile, lệnh cấu hình và cách kiểm tra danh tính hiện tại bằng sts get-caller-identity; lưu ý không chia sẻ file credentials. | https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html | https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html | undefined |
| 6 | **Thứ 7**<br>Tìm hiểu cách cấp quyền cho Lambda thông qua execution role thay vì nhúng Access Key vào mã nguồn; đọc ví dụ policy giới hạn quyền truy cập dịch vụ. | https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html | https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html | undefined |

### Week 2 Achievements:

* Phân biệt IAM User, Group, Role và Policy.
* Biết đọc policy cơ bản và hiểu nguyên tắc least privilege.
* Nắm được vai trò của MFA, temporary credentials và cách bảo vệ Access Key.
* Làm quen CloudShell/AWS CLI và hiểu vì sao Lambda cần execution role riêng.
