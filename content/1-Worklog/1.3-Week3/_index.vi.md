---
title: "Worklog Tuần 3"
date: 2026-09-28
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:

* Tìm hiểu các thành phần mạng cơ bản được sử dụng bởi các workload trên AWS.
* Tìm hiểu cách Amazon VPC cung cấp một mạng riêng biệt cho tài nguyên đám mây.
* Khám phá kiến thức nền tảng về EC2 và mối liên hệ giữa instance, lưu trữ và bảo mật mạng.

### Các công việc cần triển khai trong tuần này:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 1 | - Tìm hiểu mục đích của Amazon Virtual Private Cloud (VPC).<br>- Hiểu ký hiệu CIDR, địa chỉ IP và vai trò của dải địa chỉ VPC.<br>- Ôn tập cách subnet chia VPC thành các phân đoạn mạng nhỏ hơn. | 28/09/2026 | 28/09/2026 | [Amazon VPC là gì?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| 2 | - Tìm hiểu sự khác nhau giữa public subnet và private subnet.<br>- Tìm hiểu route tables, internet gateways và cách định tuyến lưu lượng mạng.<br>- Hiểu ở mức tổng quan cách tài nguyên trong public subnet có thể giao tiếp với Internet. | 29/09/2026 | 29/09/2026 | [VPC Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)<br>[Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) |
| 3 | - Ôn tập security groups và network access control lists (network ACLs).<br>- Hiểu sự khác nhau giữa lọc lưu lượng có trạng thái (stateful) và không trạng thái (stateless).<br>- Tìm hiểu lý do các quy tắc inbound và outbound chỉ nên cho phép lưu lượng thực sự cần thiết. | 30/09/2026 | 30/09/2026 | [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)<br>[Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| 4 | - Tìm hiểu Amazon EC2 và vai trò của dịch vụ điện toán máy chủ ảo này.<br>- Tìm hiểu Amazon Machine Images (AMIs), instance types và các trạng thái của instance.<br>- Hiểu sự khác nhau giữa việc dừng, khởi động và chấm dứt một instance. | 01/10/2026 | 01/10/2026 | [Các khái niệm Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) |
| 5 | - Khám phá các tùy chọn lưu trữ của EC2, đặc biệt là Amazon Elastic Block Store (EBS).<br>- Hiểu mối liên hệ giữa instance và các EBS volume được gắn vào.<br>- Ôn tập cách sử dụng key pair để truy cập instance Linux và các khái niệm kết nối SSH cơ bản. | 02/10/2026 | 02/10/2026 | [Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)<br>[Kết nối đến Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect.html) |
| 6 | - Ôn tập các yếu tố chi phí EC2 phổ biến, bao gồm thời gian instance chạy, dung lượng EBS và truyền dữ liệu.<br>- Tìm hiểu cách chọn kích thước instance phù hợp với workload thay vì cấp phát tài nguyên vượt nhu cầu.<br>- Tổng kết cách VPC, subnet, security group, EC2 và EBS phối hợp với nhau. | 03/10/2026 | 03/10/2026 | [Giá EC2 On-Demand](https://aws.amazon.com/ec2/pricing/on-demand/)<br>[Giá Amazon EBS](https://aws.amazon.com/ebs/pricing/) |

### Kết quả đạt được tuần 3:

* Hiểu VPC, dải CIDR, subnet, route table và internet gateway.
* Tìm hiểu cách security groups và network ACLs kiểm soát lưu lượng mạng.
* Làm quen với EC2 instances, AMIs, instance types và các thao tác trong vòng đời instance.
* Hiểu vai trò của EBS và key pair khi làm việc với EC2.
* Xây dựng được kiến thức nền tảng về cách các tài nguyên AWS giao tiếp trong một mạng.
