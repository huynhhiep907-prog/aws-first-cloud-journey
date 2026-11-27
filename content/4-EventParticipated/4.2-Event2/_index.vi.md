---
title: "First Cloud AI Journey: Weekly Meet Up 24/10"
date: 2026-10-24
weight: 1
chapter: false
pre: " <b> 4.2. </b> "
---

# Báo cáo tham gia sự kiện “First Cloud AI Journey: Weekly Meet Up 24/10”

### Thông tin chung về sự kiện

- **Tên sự kiện:** First Cloud AI Journey: Weekly Meet Up 24/10
- **Thời gian:** Ngày 24/10/2026
- **Đơn vị tổ chức:** AWS First Cloud Journey (FCJ) và AWS Study Group

### Nội dung các phiên chia sẻ

#### 1. Phát triển Voice AI Agent và ứng dụng AI trong phỏng vấn tuyển dụng

- **Diễn giả:** Anh Kiệt Trần – Engineer tại ReAI (AWS Partner).
- **Nội dung chính:**
  - Giới thiệu những hướng tiếp cận khi xây dựng hệ thống Voice AI, trong đó tập trung vào yêu cầu độ trễ thấp để duy trì hội thoại tự nhiên (mốc tham chiếu khoảng 200ms). Ba kiến trúc được phân tích gồm Cascaded (ASR → LLM → TTS), Speech-to-Speech và Full Speech-to-Speech kết hợp mô hình suy luận chạy nền.
  - Mô tả luồng xử lý cuộc gọi qua SIP Server và Media Server (WebRTC/UDP), kết hợp khử nhiễu (Noise Canceller) và phát hiện thời điểm kết thúc lời nói (VAD). Hệ thống được triển khai trên hạ tầng GPU Multi-AZ, kết nối bằng AWS PrivateLink và có thời gian phản hồi tổng thể được chia sẻ khoảng 1,8 giây.
  - Phần Live Demo trình diễn trợ lý tuyển dụng AI có thể gọi điện và phỏng vấn ứng viên về EC2, S3, EKS, RDS và VPC. Phiên này cũng đề cập đến việc chuẩn hóa văn bản tiếng Việt cho TTS, sử dụng Guardrails để kiểm soát nội dung và tối ưu chi phí vận hành ở mức tham khảo khoảng 3.000 đồng mỗi cuộc gọi.

#### 2. Chia sẻ tài nguyên đa tài khoản với AWS Resource Access Manager (AWS RAM)

- **Diễn giả:** Anh Long – AWS Study Group.
- **Nội dung chính:**
  - Trình bày cách quản lý tài nguyên tập trung trong môi trường Multi-Account bằng AWS RAM. Dịch vụ hỗ trợ chia sẻ hơn 40 loại tài nguyên, ví dụ VPC Subnets, Security Groups và Reserved EC2 Instances, giữa các tài khoản mà không tính phí riêng cho thao tác chia sẻ.
  - Làm rõ sự phối hợp giữa AWS RAM Permissions, IAM Policy và Service Control Policies (SCP) thuộc AWS Organizations để kiểm soát quyền sử dụng tài nguyên. EventBridge và CloudTrail cũng được đề cập trong việc theo dõi, giám sát các hoạt động liên quan.
  - Chia sẻ một số lưu ý khi triển khai bằng Terraform hoặc CloudFormation, đặc biệt là việc đồng bộ Availability Zone ID giữa các tài khoản nhằm hạn chế chi phí truyền dữ liệu không mong muốn. Mô hình mạng Hub-and-Spoke được giới thiệu như một cách tổ chức kết nối giữa các thành phần hạ tầng.

#### 3. Tự động kiểm tra bảo mật với AWS Security Agent

- **Diễn giả:** Anh Thịnh – Engineer tại Steel Solution.
- **Nội dung chính:**
  - Giới thiệu ba nhóm chức năng của AWS Security Agent. Design Review hỗ trợ rà soát thiết kế hạ tầng Terraform để nhận diện rủi ro từ sớm; Code & Security Review tích hợp vào Pull Request trên GitHub/GitLab và quy trình CI/CD; Automated Penetration Testing mô phỏng hành vi người dùng để tìm lỗ hổng và xây dựng đồ thị tấn công trong môi trường SIT/UAT.
  - Thảo luận về Shared Responsibility Model và cách phân chia trách nhiệm bảo mật giữa các bên. Bên cạnh đó, phiên chia sẻ đề cập đến phương án sử dụng agent hoặc extension kết nối qua đường hầm riêng tư đến máy chủ GitLab self-hosted, giúp hỗ trợ kiểm tra mà vẫn bảo vệ mã nguồn nội bộ.

#### 4. Đưa AI Agent vào môi trường Production với Amazon Bedrock AgentCore

- **Diễn giả:** Anh Nguyễn Sơn An – Leader AWS Student Group tại HCMUTE.
- **Nội dung chính:**
  - Phân tích các vấn đề cần quan tâm khi chuyển AI Agent từ giai đoạn thử nghiệm sang vận hành thực tế, chẳng hạn như bảo mật, cô lập phiên làm việc và quản lý trạng thái hội thoại.
  - Giới thiệu Amazon Bedrock AgentCore với hai thành phần được tập trung trình bày:
    - **Runtime:** Cung cấp môi trường thực thi serverless, trong đó mỗi phiên được cô lập trong một MicroVM riêng biệt. Phiên chia sẻ đề cập đến nền tảng EC2 Spot Instance và cách tối ưu chi phí thông qua việc tính phí CPU trong thời gian thực thi.
    - **Memory:** Quản lý thông tin theo hai phạm vi. Short-term Memory lưu nội dung hội thoại theo `sessionId` và hỗ trợ phân nhánh phiên; Long-term Memory trích xuất thông tin bất đồng bộ để tạo bản tóm tắt, ghi nhận sở thích và lưu trữ tri thức dài hạn.

#### 5. Tối ưu phát triển phần mềm và tự động hóa vận hành với Kiro

- **Diễn giả:** Anh Hiếu Nghị – Leader AWS Student Group và anh Khoa – Tech Lead tại ACB.
- **Nội dung chính:**
  - Giới thiệu phương pháp Spec-Driven Development theo trình tự Plan → Design → Tasks, giúp làm rõ yêu cầu và kế hoạch trước khi triển khai. Các biện pháp an toàn cũng được đề cập, bao gồm che giấu secrets/passwords và yêu cầu phê duyệt thủ công trước những thao tác có thể xóa hạ tầng.
  - Chia sẻ cách ứng dụng Kiro trong môi trường doanh nghiệp, chẳng hạn kết nối Telegram để kiểm tra và thông báo tình trạng tài nguyên AWS định kỳ mỗi 5 phút, cũng như tự động hỗ trợ Code Review trên GitHub theo bộ tiêu chuẩn nội bộ.
  - Nhấn mạnh việc kiểm soát Context Window để sử dụng token hợp lý, góp phần tối ưu hiệu quả và chi phí khi làm việc với công cụ AI.

### Kiến thức và kinh nghiệm thu nhận

#### Tư duy thiết kế kiến trúc

- Nhận thấy việc xây dựng hệ thống AI cần cân bằng giữa tốc độ phản hồi, chất lượng xử lý ngôn ngữ, khả năng mở rộng và chi phí vận hành.
- Hiểu thêm về cách tổ chức hạ tầng Multi-Account, chia sẻ tài nguyên và lựa chọn mô hình kết nối phù hợp với quy mô hệ thống.

#### Bảo mật trong quy trình phát triển

- Nhận thức rõ hơn về việc đưa hoạt động kiểm tra bảo mật vào sớm trong vòng đời phát triển, từ bước thiết kế Infrastructure as Code đến kiểm duyệt Pull Request.
- Hiểu rằng bảo mật cần được duy trì xuyên suốt quá trình phát triển và vận hành, thay vì chỉ thực hiện ở giai đoạn cuối.

#### Công nghệ AI và công cụ AWS mới

- Có thêm góc nhìn về việc vận hành AI Agent trong môi trường Production thông qua Amazon Bedrock AgentCore, đặc biệt là quản lý phiên và bộ nhớ.
- Tìm hiểu cách Kiro hỗ trợ quy trình phát triển theo đặc tả, rà soát mã nguồn và tự động hóa các tác vụ vận hành.

#### Liên hệ với dự án thực tập

- Những nội dung về Amazon Bedrock AgentCore giúp tôi hiểu rõ hơn các yếu tố cần cân nhắc khi tích hợp chức năng AI vào dự án Bếp Thông Minh.
- Các chia sẻ về bảo mật, giám sát và tối ưu chi phí cũng là cơ sở để xem xét, cải thiện cách triển khai các dịch vụ AWS trong dự án.
- Qua sự kiện, tôi nhận ra cần đánh giá giải pháp dựa trên nhu cầu thực tế, mức độ phức tạp và chi phí, thay vì chỉ lựa chọn công nghệ theo xu hướng.

### Trải nghiệm tham gia sự kiện

Sự kiện mang đến cơ hội tiếp cận nhiều chủ đề đang được ứng dụng trong môi trường doanh nghiệp, từ Voice AI, quản trị tài nguyên đa tài khoản đến tự động hóa kiểm thử bảo mật và triển khai AI Agent. Các ví dụ và phần trình diễn giúp tôi hình dung rõ hơn cách những dịch vụ, công cụ AWS được kết hợp để giải quyết các bài toán thực tế.
