---
title: "Worklog Tuần 2"
date: 2026-09-21
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:

* Xây dựng nền tảng kiến thức về điện toán đám mây và các nhóm dịch vụ chính của AWS.
* Tìm hiểu hạ tầng toàn cầu của AWS, Regions và Availability Zones.
* Tìm hiểu bảo mật tài khoản cơ bản, các khái niệm IAM và phương thức truy cập AWS an toàn.

### Các công việc cần triển khai trong tuần này:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 1 | - Ôn tập các đặc điểm của điện toán đám mây, bao gồm tài nguyên theo nhu cầu, khả năng co giãn và mô hình tính phí theo mức sử dụng.<br>- So sánh hạ tầng đám mây với hạ tầng truyền thống tại chỗ (on-premises).<br>- Phân biệt các mô hình dịch vụ IaaS, PaaS và SaaS. | 21/09/2026 | 21/09/2026 | [Điện toán đám mây là gì?](https://aws.amazon.com/what-is-cloud-computing/) |
| 2 | - Khám phá các nhóm dịch vụ AWS chính: compute, storage, networking, database và security.<br>- Xác định ví dụ về các dịch vụ trong từng nhóm và mục đích sử dụng tổng quát của chúng.<br>- Liên hệ các nhóm dịch vụ này với nhu cầu của một ứng dụng web. | 22/09/2026 | 22/09/2026 | [Các sản phẩm AWS](https://aws.amazon.com/products/) |
| 3 | - Tìm hiểu hạ tầng toàn cầu của AWS, bao gồm Regions và Availability Zones.<br>- Hiểu cách lựa chọn Region ảnh hưởng đến độ trễ, khả năng cung cấp dịch vụ và chi phí.<br>- Xem xét Region Singapore như một địa điểm tiềm năng cho dự án phục vụ người dùng tại Việt Nam. | 23/09/2026 | 23/09/2026 | [Hạ tầng toàn cầu AWS](https://aws.amazon.com/about-aws/global-infrastructure/) |
| 4 | - Tìm hiểu mục đích của AWS Identity and Access Management (IAM).<br>- Phân biệt users, groups, roles và policies.<br>- Hiểu sự khác nhau giữa authentication và authorization cũng như nguyên tắc đặc quyền tối thiểu (least privilege). | 24/09/2026 | 24/09/2026 | [IAM là gì?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)<br>[Các phương pháp thực hành tốt nhất về IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) |
| 5 | - Ôn tập cách bảo vệ root user, xác thực đa yếu tố (MFA) và an toàn thông tin xác thực.<br>- Hiểu sự khác nhau giữa thông tin đăng nhập Console và thông tin xác thực truy cập bằng chương trình.<br>- Tìm hiểu lý do không được commit access key vào mã nguồn hoặc chia sẻ trong repository công khai. | 25/09/2026 | 25/09/2026 | [Thông tin xác thực bảo mật IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)<br>[Bảo vệ Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html) |
| 6 | - Khám phá AWS Management Console và AWS CloudShell như những phương thức truy cập dịch vụ AWS.<br>- Ôn tập mục đích của AWS CLI và các khái niệm cấu hình cơ bản, bao gồm profile và Region.<br>- Tìm hiểu cách kiểm tra danh tính đang hoạt động và Region đã cấu hình mà không làm lộ thông tin xác thực. | 26/09/2026 | 26/09/2026 | [AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html)<br>[Cấu hình AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)<br>[AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) |

### Kết quả đạt được tuần 2:

* Hiểu mô hình điện toán đám mây cơ bản và các nhóm dịch vụ phổ biến trong AWS.
* Tìm hiểu mối liên hệ giữa Regions, Availability Zones với vị trí triển khai và tính sẵn sàng.
* Làm quen với IAM identities, policies, MFA và nguyên tắc đặc quyền tối thiểu.
* Nhận thức được tầm quan trọng của việc bảo vệ thông tin xác thực root và access key dùng cho truy cập bằng chương trình.
* Nắm được mục đích sử dụng của AWS Console, CloudShell và AWS CLI.
