---
title: "Week 3 Worklog"
date: 2026-09-28
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

### Week 3 Objectives:

* Nắm được cách lưu trữ dữ liệu tĩnh trên Amazon S3 và cách tổ chức bucket/object.
* Hiểu vai trò của CloudFront trong việc phân phối nội dung website và các thiết lập bảo mật cơ bản.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | **Thứ 2**<br>Tìm hiểu Amazon S3: bucket, object, key, Region và các trường hợp sử dụng lưu trữ file tĩnh; phân biệt S3 với ổ đĩa máy chủ. | https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html | https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html | undefined |
| 2 | **Thứ 3**<br>Đọc về S3 bucket policy, Block Public Access và quyền truy cập; tìm hiểu vì sao không nên công khai bucket chứa dữ liệu không dành cho người dùng. | https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html | https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html | undefined |
| 3 | **Thứ 4**<br>Tìm hiểu versioning, lifecycle configuration và cách quản lý vòng đời object; liên hệ với việc lưu trữ phiên bản file website và dữ liệu. | https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html | https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html | undefined |
| 4 | **Thứ 5**<br>Tìm hiểu static website hosting trên S3, index document, error document và giới hạn của endpoint website so với cách phân phối qua CloudFront. | https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html | https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html | undefined |
| 5 | **Thứ 6**<br>Tìm hiểu Amazon CloudFront: distribution, origin, cache behavior, TTL và cách CDN giúp giảm độ trễ khi phân phối website. | https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html | https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html | undefined |
| 6 | **Thứ 7**<br>Đọc về Origin Access Control (OAC) để hiểu cách CloudFront truy cập bucket S3 riêng tư mà không cần bật quyền public cho toàn bộ bucket. | https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html | https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html | undefined |

### Week 3 Achievements:

* Hiểu cấu trúc bucket/object và các tính năng lưu trữ cơ bản của S3.
* Phân biệt quyền truy cập công khai và riêng tư; nắm được Block Public Access.
* Hiểu cách triển khai website tĩnh và các giới hạn khi chỉ sử dụng S3 website endpoint.
* Nắm được vai trò của CloudFront, cache và OAC trong phân phối frontend an toàn.
