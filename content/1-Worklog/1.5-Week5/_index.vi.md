---
title: "Worklog Tuần 5"
date: 2026-10-12
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu tuần 5:

* Hiểu cách Content Delivery Network (CDN) cải thiện việc phân phối nội dung web tĩnh.
* Tìm hiểu CloudFront distributions, origins, cache behaviors và invalidation.
* Ôn tập các khái niệm DNS, HTTPS và HTTP cần thiết để xuất bản, xử lý sự cố website.

### Các công việc cần triển khai trong tuần này:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 1 | - Tìm hiểu mục đích của CDN và cách edge locations giúp giảm độ trễ.<br>- Hiểu sự khác nhau giữa origin server và cache location.<br>- Xác định các tài nguyên phù hợp để cache, chẳng hạn CSS, JavaScript và hình ảnh công thức. | 12/10/2026 | 12/10/2026 | [CDN là gì?](https://aws.amazon.com/what-is/cdn/) |
| 2 | - Tìm hiểu các thành phần chính của CloudFront distribution.<br>- Hiểu origins, origin paths, default root objects và tên miền distribution.<br>- Ôn tập cách CloudFront lấy nội dung tĩnh từ S3 origin. | 13/10/2026 | 13/10/2026 | [Cách CloudFront hoạt động](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) |
| 3 | - Tìm hiểu CloudFront cache behaviors và path patterns.<br>- Tìm hiểu cách cache policies kiểm soát giá trị TTL và những request parameters được đưa vào cache key.<br>- Xem xét nhu cầu cache khác nhau đối với hình ảnh, script và các tệp thường xuyên thay đổi. | 14/10/2026 | 14/10/2026 | [Cache Behaviors](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesCacheBehavior.html)<br>[Cache Policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html) |
| 4 | - Tìm hiểu cách CloudFront invalidation hoạt động sau khi tệp website được cập nhật.<br>- So sánh invalidation với việc sử dụng tên tệp có version cho tài nguyên tĩnh.<br>- Ôn tập các nguyên nhân phổ biến khiến người dùng vẫn nhìn thấy trang cũ đã được cache. | 15/10/2026 | 15/10/2026 | [Invalidating Files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) |
| 5 | - Ôn tập các khái niệm DNS, bao gồm domain names, DNS records và name resolution.<br>- Hiểu cách một domain name có thể trỏ đến CloudFront distribution.<br>- Tìm hiểu HTTPS và chứng chỉ TLS khi xuất bản website. | 16/10/2026 | 16/10/2026 | [Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)<br>[AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) |
| 6 | - Tìm hiểu các mã trạng thái phản hồi HTTP phổ biến, bao gồm 200, 301, 403, 404 và 5xx.<br>- Phân biệt lỗi phía trình duyệt, lỗi origin và lỗi liên quan đến quyền truy cập.<br>- Chuẩn bị danh sách kiểm tra xử lý sự cố cho website tĩnh được phân phối thông qua CloudFront. | 17/10/2026 | 17/10/2026 | [HTTP Semantics – RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)<br>[CloudFront Troubleshooting](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting-response-errors.html) |

### Kết quả đạt được tuần 5:

* Hiểu vai trò của CDN và cách CloudFront sử dụng edge locations để phân phối nội dung tĩnh.
* Tìm hiểu mối quan hệ giữa S3 origin và CloudFront distribution.
* Làm quen với cache behaviors, cache policies, giá trị TTL và invalidation.
* Ôn tập các khái niệm DNS, HTTPS và TLS cần thiết để xuất bản website.
* Xây dựng phương pháp cơ bản để chẩn đoán các lỗi phân phối website và lỗi HTTP phổ biến.
