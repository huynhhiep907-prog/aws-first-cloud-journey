---
title: "Worklog Tuần 4"
date: 2026-10-05
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:

* Hiểu về object storage và cách Amazon S3 tổ chức các tệp của ứng dụng.
* Tìm hiểu cách bảo vệ tệp được lưu trữ thông qua kiểm soát quyền truy cập, versioning và encryption.
* Khám phá các khái niệm quản lý lưu trữ phù hợp với tài nguyên website tĩnh và dữ liệu công thức nấu ăn.

### Các công việc cần triển khai trong tuần này:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 1 | - Tìm hiểu object storage và so sánh object, block và file storage.<br>- Tìm hiểu mối liên hệ giữa S3 bucket, object key, metadata và object body.<br>- Xác định các trường hợp sử dụng S3 phù hợp như hình ảnh, tài liệu và tài nguyên website tĩnh. | 05/10/2026 | 05/10/2026 | [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |
| 2 | - Ôn tập cách đặt tên bucket, tổ chức object và tải object lên/xuống.<br>- Tìm hiểu cách dùng prefix để tổ chức tệp theo tính năng hoặc loại nội dung.<br>- Xem xét cấu trúc thư mục hợp lý cho hình ảnh công thức và tài nguyên frontend. | 06/10/2026 | 06/10/2026 | [Tổ chức Object trong S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) |
| 3 | - Tìm hiểu S3 Block Public Access và rủi ro khi vô tình công khai các tệp được lưu trữ.<br>- Hiểu bucket policy khác IAM identity policy như thế nào.<br>- Ôn tập nguyên tắc chỉ cấp quyền truy cập đối với những tài nguyên thực sự cần thiết. | 07/10/2026 | 07/10/2026 | [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)<br>[Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) |
| 4 | - Tìm hiểu cách S3 Versioning lưu giữ các phiên bản object trước đó.<br>- Ôn tập khả năng khôi phục khi vô tình ghi đè hoặc xóa dữ liệu.<br>- Xác định những trường hợp versioning hữu ích đối với tệp website và tài nguyên dự án. | 08/10/2026 | 08/10/2026 | [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) |
| 5 | - Tìm hiểu mã hóa mặc định của S3 và các tùy chọn server-side encryption.<br>- Hiểu encryption at rest và mối liên hệ giữa thiết lập mã hóa với quyền truy cập.<br>- Ôn tập lý do không nên cho phép truy cập công khai đối với các tệp nhạy cảm. | 09/10/2026 | 09/10/2026 | [S3 Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) |
| 6 | - Khám phá S3 Lifecycle rules và các storage classes.<br>- Tìm hiểu cách object có thể được chuyển sang lớp lưu trữ có chi phí thấp hơn hoặc tự động hết hạn sau một khoảng thời gian xác định.<br>- Ôn tập tác động đến chi phí và thời gian lưu giữ khi lưu trữ tài nguyên website, bản sao lưu. | 10/10/2026 | 10/10/2026 | [S3 Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)<br>[S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/) |

### Kết quả đạt được tuần 4:

* Hiểu S3 bucket, object, key và các trường hợp sử dụng object storage phổ biến.
* Tìm hiểu cách tổ chức tài nguyên website và kiểm soát quyền truy cập đối với object được lưu trữ.
* Làm quen với Block Public Access, bucket policy, versioning và encryption.
* Hiểu cách lifecycle rules và storage classes hỗ trợ quản lý thời gian lưu trữ và chi phí.
