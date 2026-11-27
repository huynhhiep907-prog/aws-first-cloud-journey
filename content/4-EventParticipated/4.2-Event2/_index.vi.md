---
title: "AWS Cloud and AI Day Hanoi 2026 – Ho Chi Minh City Watch Party Hub"
date: 2026-09-29
weight: 1
chapter: false
pre: " <b> 4.2. </b> "
---

# Bài thu hoạch sự kiện: AWS Cloud and AI Day Hanoi 2026 – Ho Chi Minh City Watch Party Hub

### Tổng quan sự kiện

- **Tên sự kiện:** AWS Cloud and AI Day Hanoi 2026 – Ho Chi Minh City Watch Party Hub
- **Thời gian:** Ngày 29 tháng 9 năm 2026
- **Hình thức tham gia:** Tham gia trực tiếp buổi Watch Party tại Thành phố Hồ Chí Minh, theo dõi các phiên Keynote và Developer Chats được phát trực tiếp từ địa điểm tổ chức tại Hà Nội cùng cộng đồng AWS First Cloud Journey.
- **Đơn vị tổ chức:** AWS Vietnam, AWS Community Builders và AWS First Cloud Journey (FCJ).

### Các chủ đề và nội dung nổi bật

#### 1. Từ ứng dụng công nghệ đến vận hành hệ thống ở quy mô thực tế

Một thông điệp quan trọng của sự kiện là hệ sinh thái Cloud và AI tại Việt Nam đang dần chuyển từ giai đoạn thử nghiệm Proof-of-Concept (PoC) sang việc vận hành các hệ thống thực tế một cách ổn định, an toàn và có khả năng mở rộng.

Để triển khai workload trong môi trường production, tổ chức cần xác định rõ trách nhiệm vận hành, phân quyền truy cập hợp lý, xây dựng hệ thống observability toàn diện, đảm bảo hạ tầng có khả năng phục hồi và duy trì quy trình quản lý chi phí có thể lặp lại. Đây là những yếu tố cần thiết để biến các bản thử nghiệm tiềm năng thành dịch vụ đáng tin cậy.

#### 2. Agentic AI và vai trò của Platform Engineering

Agentic AI là một trong những chủ đề trọng tâm của sự kiện. Các hệ thống AI đang phát triển từ những công cụ chủ yếu tạo nội dung thành các agent có khả năng gọi API, truy cập dữ liệu nội bộ, chỉnh sửa mã nguồn và khởi chạy quy trình triển khai.

Khi các agent ngày càng tự chủ và chu kỳ phát triển phần mềm được rút ngắn, Platform Engineering đóng vai trò tạo ra những ranh giới kiểm soát cần thiết. Cách tiếp cận này giúp chuẩn hóa quy trình triển khai, thiết lập cấu hình bảo mật mặc định, quản lý chuỗi cung ứng phần mềm và xác định những hành động mà AI agent được phép thực hiện hoặc cần có sự phê duyệt.

#### 3. Định danh workload và bảo mật AI agent trên AWS

Phiên Developer Chats do **Kha Van**, Cloud Security Engineer và AWS Community Builder, trình bày đã đề cập đến một câu hỏi bảo mật quan trọng: khi một workload gửi yêu cầu đến AWS API, danh tính nào thực sự được sử dụng?

Nội dung thảo luận nhấn mạnh sự gia tăng của các danh tính phi con người trong môi trường cloud, bao gồm Kubernetes Pods, pipeline CI/CD, serverless functions và AI agents. Những danh tính này cũng cần được quản lý và kiểm soát chặt chẽ như tài khoản người dùng thông thường.

Các giải pháp AWS được đề cập bao gồm **Amazon EKS Pod Identity**, thông tin xác thực tạm thời có thời hạn ngắn, quyền truy cập chi tiết ở cấp workload, IAM trust policies nghiêm ngặt và xác minh danh tính tại thời điểm chạy. Những phương pháp này giúp tránh việc workload kế thừa các quyền quá rộng từ EC2 node, đồng thời hỗ trợ nguyên tắc đặc quyền tối thiểu (least privilege).

#### 4. Phát triển hạ tầng AWS tại Việt Nam và kiến trúc Hybrid

Sự kiện cũng cập nhật những bước phát triển hạ tầng AWS tại Việt Nam, trong đó có **AWS Direct Connect tại Hà Nội** và **Hanoi AWS Local Zone**.

Các lựa chọn này mang đến cho doanh nghiệp sự linh hoạt hơn trong kết nối riêng tư, triển khai ứng dụng yêu cầu độ trễ thấp và xử lý workload có yêu cầu về vị trí lưu trữ dữ liệu. Đồng thời, chúng mở rộng các phương án thiết kế kiến trúc hybrid, kết hợp hạ tầng tại chỗ (on-premises) với dịch vụ cloud.

Khi đưa ra quyết định kiến trúc, cần cân bằng giữa độ trễ, khả năng phục hồi, yêu cầu tuân thủ, bảo mật và chi phí thay vì chỉ tập trung vào một yếu tố riêng lẻ.

#### 5. Chuyển đổi doanh nghiệp và cộng đồng Cloud tại Việt Nam

**Câu chuyện khách hàng TCBS (TCBS Customer Story)** cho thấy AI có thể hỗ trợ chuyển đổi quy trình phát triển phần mềm khi được tích hợp vào các hoạt động hằng ngày như viết mã, review, kiểm thử và phát hành phần mềm. Hiệu quả ứng dụng AI nên được đánh giá thông qua những cải thiện có thể đo lường trong hoạt động thực tế, thay vì chỉ đơn giản bổ sung thêm một công cụ vào hệ thống công nghệ.

Bài keynote cũng chia sẻ các số liệu thể hiện sự phát triển của hệ sinh thái Cloud và AI tại Việt Nam:

- Hơn **157.000** người đã được đào tạo về Cloud và AI.
- Hơn **54.000** thành viên trong cộng đồng **AWS Study Group**.
- Hơn **15.000** người tham gia hệ sinh thái **First Cloud and AI Journey (FCJ)**.

Những con số này phản ánh sự quan tâm ngày càng tăng đối với kiến thức Cloud và AI của cộng đồng lập trình viên và nhân sự công nghệ tại Việt Nam.

### Trải nghiệm tại Ho Chi Minh City Watch Party

Mặc dù sự kiện chính được tổ chức tại Hà Nội, việc tham gia Watch Party tại Thành phố Hồ Chí Minh giúp tôi có cơ hội theo dõi các phiên chia sẻ trực tiếp cùng các thực tập sinh và mentor trong cộng đồng FCJ.

Buổi gặp mặt tại địa phương tạo điều kiện để mọi người trao đổi ý tưởng, thảo luận về các quyết định thiết kế kiến trúc trong thực tế và học hỏi lẫn nhau trong lúc theo dõi livestream. Đây cũng là dịp giúp tôi kết nối gần hơn với cộng đồng AWS tại Thành phố Hồ Chí Minh.

### Những kiến thức rút ra và cách áp dụng vào kỳ thực tập

#### 1. Hình thành tư duy ưu tiên môi trường Production

Một bản demo hoạt động được không đồng nghĩa với việc ứng dụng đã sẵn sàng triển khai trong môi trường production. Logging, monitoring, observability, độ tin cậy và kiểm soát chi phí cần được cân nhắc ngay từ giai đoạn thiết kế ban đầu.

#### 2. Ưu tiên bảo mật dựa trên danh tính

Không nên cấp quyền truy cập quá rộng cho workload hoặc AI agent chỉ vì sự tiện lợi. Việc sử dụng thông tin xác thực tạm thời, IAM policies giới hạn đúng phạm vi và tuân thủ nguyên tắc đặc quyền tối thiểu giúp giảm thiểu các rủi ro bảo mật không cần thiết.

#### 3. Học hỏi và chia sẻ thông qua cộng đồng

Việc học hỏi từ những người có kinh nghiệm thực tế, mentor và AWS Community Builders mang lại góc nhìn ứng dụng vượt ra ngoài tài liệu kỹ thuật. Ghi lại và chia sẻ những kiến thức này cũng giúp tôi củng cố hiểu biết về kiến trúc cloud và các phương pháp kỹ thuật phần mềm.

### Hình ảnh sự kiện

*Thêm hình ảnh ghi lại quá trình tham gia sự kiện tại đây.*

