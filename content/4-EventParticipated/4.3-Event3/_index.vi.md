---
title: "First Cloud AI Journey: Weekly Meet Up 14/11 "
date: 2026-11-14
weight: 1
chapter: false
pre: " <b> 4.3. </b> "
---

### Tổng quan sự kiện

- **Tên sự kiện:** First Cloud AI Journey: Weekly Meet Up 14/11
- **Thời gian:** ngày 14 tháng 11 năm 2026
- **Diễn giả:** Nguyễn Lâm Anh, Trần Phương Huyền, Phúc Khang, Huỳnh An Khương, Nguyễn Quốc Bảo (Thành viên AWS First Cloud Journey – FCJ)
- **Đơn vị tổ chức:** AWS First Cloud Journey (FCJ) và AWS Study Group

---

### Tổng quan nội dung chương trình

Ngày 14 tháng 11 năm 2026, cộng đồng AWS First Cloud Journey (FCJ) tiếp tục chuỗi hoạt động học tập kỹ thuật với buổi **AWS Cloud Mastery**, tập trung vào quá trình phát triển Amazon Bedrock Agents. Mục tiêu chính của chương trình là tìm hiểu cách đưa các giải pháp AI từ giai đoạn thử nghiệm ban đầu trở thành những ứng dụng an toàn, ổn định và sẵn sàng triển khai trong môi trường thực tế.

Được tổ chức tại văn phòng AWS Việt Nam ở Thành phố Hồ Chí Minh, buổi chia sẻ quy tụ các bạn sinh viên và những người quan tâm đến lĩnh vực công nghệ để cùng tìm hiểu kiến trúc phía sau **Amazon Bedrock AgentCore**. Thay vì chỉ tập trung vào việc xây dựng chatbot minh họa cơ bản, các diễn giả đã phân tích những yêu cầu kỹ thuật cần thiết khi triển khai AI Agent trong môi trường doanh nghiệp, đặc biệt là các yếu tố **bảo mật, độ tin cậy và khả năng mở rộng**.

---

### Các nội dung kỹ thuật nổi bật

#### 1. Chuyển đổi từ AI Prototype sang hệ thống Production

Chương trình bắt đầu với chủ đề **"From Prototype to Production: Secure, Reliable, Scalable Enterprise AI on the Cloud"**. Nội dung nhấn mạnh rằng xây dựng được một chatbot AI hoạt động là bước khởi đầu; để vận hành một AI Agent ở quy mô doanh nghiệp cần có cách tiếp cận kỹ thuật toàn diện hơn.

Ba thách thức chính được đề cập gồm:

- **Tối ưu hiệu năng và chi phí:** Đảm bảo AI Agent phản hồi hiệu quả, đồng thời kiểm soát chi phí suy luận mô hình và chi phí hạ tầng, đặc biệt khi số lượng yêu cầu tăng lên.
- **Tích hợp hệ thống và kiểm soát quyền truy cập:** Cho phép Agent giao tiếp với các ứng dụng doanh nghiệp và dịch vụ bên ngoài, nhưng vẫn phải thiết lập ranh giới quyền hạn rõ ràng và ngăn chặn những thao tác không được cấp phép.
- **Giám sát và đánh giá chất lượng:** Theo dõi quá trình suy luận, cách Agent sử dụng công cụ, đồng thời đánh giá xem câu trả lời được tạo ra và các hành động được thực thi có đáp ứng yêu cầu mong đợi hay không.

#### 2. Thiết kế giải pháp có khả năng mở rộng với Amazon Bedrock AgentCore

Các diễn giả giới thiệu cách **Amazon Bedrock AgentCore** hỗ trợ những môi trường doanh nghiệp có quy mô lớn, với hàng trăm Agent, hàng nghìn công cụ, hàng trăm máy chủ MCP và hơn 100.000 tenant.

Một số thành phần và khái niệm kiến trúc quan trọng được trình bày:

- **Xác thực và phân quyền cho các yêu cầu Inbound và Outbound:**
  - Buổi chia sẻ giới thiệu mô hình **Universal 5-Step Skeleton** có thể tái sử dụng để quản lý các tương tác an toàn thông qua **Bedrock AgentCore Gateway** và **AgentCore Identity**.
  - Các yêu cầu đầu vào cần được xác thực bằng những cơ chế như JWT hoặc thông tin xác thực IAM trước khi Agent được phép truy cập công cụ bên ngoài hoặc máy chủ MCP.
  - Cách tiếp cận này giúp thiết lập luồng giao tiếp có kiểm soát giữa người dùng, AI Agent và các dịch vụ được kết nối.

- **Quản lý ngữ cảnh và hội thoại với AgentCore Memory:**
  - **Short-term Memory (Bộ nhớ ngắn hạn):** Lưu giữ các tin nhắn hội thoại và thông tin phiên theo cách đồng bộ, giúp Agent duy trì ngữ cảnh trong một tương tác đang diễn ra.
  - **Long-term Memory (Bộ nhớ dài hạn):** Sử dụng quy trình trích xuất bộ nhớ tự động để phân tích các tương tác trước đó theo cách bất đồng bộ, sau đó tổ chức thông tin hữu ích thành những nhóm khác nhau:
    - **Semantic:** Kiến thức và thông tin có ý nghĩa được trích xuất từ các tương tác.
    - **User Preferences:** Thói quen và sở thích riêng của người dùng.
    - **Summarization:** Nội dung tóm tắt ngắn gọn từ các cuộc hội thoại trước.
    - **Episodic:** Ghi lại những tác vụ và trải nghiệm trước đây để hỗ trợ định hướng các hành động trong tương lai.

- **Hạ tầng AWS ở cấp độ Production:**
  - Nội dung cũng đề cập đến việc triển khai ứng dụng trên nhiều Availability Zone (**Multi-AZ**) nhằm cải thiện tính sẵn sàng và khả năng chịu lỗi.
  - Các thành phần hạ tầng quan trọng bao gồm phân tách public subnet và private subnet, triển khai cân bằng tải (load balancing), xây dựng lớp điều phối Agent (agent orchestration) và tích hợp khả năng quan sát hệ thống (observability).
  - Những thực tiễn kiến trúc này góp phần tạo nền tảng vững chắc và có khả năng phục hồi cho các ứng dụng AI khi vận hành ở quy mô lớn.

---

### Không khí tương tác và kết nối cộng đồng

- **Thảo luận kỹ thuật và hỏi đáp:** Chương trình khuyến khích sinh viên và những người yêu thích công nghệ tại Thành phố Hồ Chí Minh tích cực trao đổi. Các câu hỏi tập trung vào những vấn đề thực tế như giới hạn quyền của AI Agent khi kết nối với backend production, quản lý chi phí vận hành và chuẩn bị cho cơ hội nghề nghiệp trong lĩnh vực Cloud và AI.
- **Ôn tập kiến thức qua Quiz tương tác:** Một phần quiz được tổ chức vào cuối chương trình nhằm củng cố các kiến thức kỹ thuật đã trình bày. Người tham dự có cơ hội ôn lại những nội dung như phân quyền Gateway, bộ nhớ ngắn hạn và dài hạn của AgentCore, cũng như triển khai hạ tầng Multi-AZ.
- **Hoạt động cộng đồng sắp tới:** Trước khi kết thúc chương trình, ban tổ chức giới thiệu **AWS Student Community Day Vietnam 2026**, một sự kiện lớn sắp diễn ra nhằm tạo thêm cơ hội để sinh viên học hỏi, trao đổi ý tưởng và kết nối với các thành viên trong cộng đồng AWS.

---

### Những kiến thức và kinh nghiệm rút ra

1. **Xây dựng hệ thống vượt xa một Prototype có thể hoạt động:** Tôi nhận ra rằng phát triển một AI Agent sẵn sàng phục vụ doanh nghiệp không chỉ dừng lại ở việc triển khai tính năng hội thoại. Các cơ chế bảo mật thông qua Gateway và Identity, quản lý bộ nhớ dài hạn có cấu trúc và giám sát hành vi liên tục cần được tính đến ngay từ đầu.

2. **Hiểu rõ kiến trúc tổng thể của hệ thống:** Buổi chia sẻ giúp tôi có cái nhìn toàn diện hơn về việc kết hợp **Amazon Bedrock AgentCore** với hạ tầng VPC Multi-AZ. Sự kết hợp này tạo nền tảng quan trọng để xây dựng các hệ thống AI có tính sẵn sàng cao, có khả năng mở rộng và hỗ trợ số lượng lớn Agent, công cụ cũng như tác vụ.

3. **Học hỏi liên tục thông qua cộng đồng AWS:** Tham gia các buổi chia sẻ chuyên sâu tại văn phòng AWS mang đến cơ hội tìm hiểu những dịch vụ AWS mới, tiếp cận các phương pháp triển khai thực tế và mở rộng kiến thức về kiến trúc hệ thống thông qua kinh nghiệm của các diễn giả và thành viên cộng đồng.
