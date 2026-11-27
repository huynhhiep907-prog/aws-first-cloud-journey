---
title: "Trò chuyện cùng Dr. Werner"
date: 2026-10-02
weight: 4
chapter: false
pre: " <b> 4.4. </b> "
---

### Tổng quan sự kiện

- **Tên sự kiện:** Fireside Chat with Dr. Werner: Navigating the Future of Cloud & AI in Vietnam
- **Diễn giả khách mời:** Dr. Werner Vogels (Phó Chủ tịch kiêm Giám đốc Công nghệ – CTO của Amazon)
- **Thời gian:** Ngày 2 tháng 10 năm 2026
- **Đơn vị tổ chức:** AWS First Cloud Journey (FCJ), AWS Heroes và AWS Community Builders Vietnam

---

### Những nội dung nổi bật từ buổi trò chuyện

#### 1. Hành trình phát triển hệ thống phân tán của Amazon và sự ra đời của DynamoDB

- **Giải quyết giới hạn cơ sở dữ liệu khi hệ thống mở rộng:** Dr. Werner chia sẻ về những khó khăn Amazon gặp phải hơn 20 năm trước, khi các hệ quản trị cơ sở dữ liệu quan hệ truyền thống không còn đáp ứng tốt lượng truy cập tăng cao trong các mùa mua sắm lễ hội. Khi cùng thực tập sinh Swami (hiện là Phó Chủ tịch phụ trách AI tại AWS) phân tích các mẫu truy cập dữ liệu thực tế, nhóm kỹ sư nhận thấy khoảng 70% truy vấn chỉ là những thao tác tra cứu **Key-Value** đơn giản. Phát hiện này đã đặt nền móng cho **Dynamo**, tiền thân có ảnh hưởng quan trọng đến sự phát triển của **Amazon DynamoDB** sau này.

- **Xây dựng văn hóa vận hành đáng tin cậy:**
  - **Tập trung vào Tail Latency:** Thay vì chỉ dựa vào thời gian phản hồi trung bình, Amazon chú trọng đo lường và tối ưu độ trễ tại **phân vị 99,9% (p99.9)** để hiểu rõ hơn trải nghiệm của những người dùng gặp phải phản hồi chậm nhất.
  - **Thực hành Game Days:** Các nhóm chủ động mô phỏng những sự cố hạ tầng nghiêm trọng, chẳng hạn như ngắt kết nối toàn bộ một trung tâm dữ liệu hoặc Availability Zone. Những bài diễn tập này giúp phát hiện điểm lỗi đơn, tự động hóa quy trình chuyển đổi dự phòng và xây dựng cơ chế đối soát dữ liệu đáng tin cậy khi hạ tầng hoạt động trở lại.
  - **Thay đổi mô hình sử dụng dịch vụ CNTT:** Amazon chuyển từ mô hình hợp đồng truyền thống yêu cầu cam kết chi phí lớn trong nhiều năm sang hình thức **pay-as-you-go** (trả phí theo mức sử dụng), giúp khách hàng linh hoạt và chủ động hơn trong việc kiểm soát ngân sách.

#### 2. Tư duy "Renaissance Developer" trong kỷ nguyên AI

Dr. Werner đề cập đến năm phẩm chất quan trọng mà kỹ sư cần phát triển để thích nghi với sự thay đổi liên tục của công nghệ và AI:

1. **Ham học hỏi và không ngừng khám phá:** Ngôn ngữ lập trình, môi trường phát triển và công cụ luôn thay đổi. Kỹ sư đã chuyển dần từ các công nghệ như C, Java sang Rust; đồng thời quy trình phát triển cũng tiến từ những IDE truyền thống đến các công cụ như Kiro và Cursor. Vì vậy, tinh thần tò mò và học tập suốt đời là yếu tố thiết yếu.

2. **Tư duy hệ thống:** Lập trình viên cần hiểu cách các dịch vụ và thành phần phối hợp với nhau trong toàn bộ hệ thống phân tán. Nhìn nhận vấn đề vượt ra ngoài một tác vụ hoặc một thành phần riêng lẻ giúp kỹ sư nhận diện các mối phụ thuộc và đưa ra quyết định kiến trúc phù hợp hơn.

3. **Giao tiếp hiệu quả:** Đây là kỹ năng thường bị đánh giá thấp trong lĩnh vực kỹ thuật. Nhà phát triển cần tìm hiểu nhu cầu kinh doanh thực sự đằng sau yêu cầu của khách hàng, đồng thời giải thích rõ lợi ích, chi phí và giới hạn của từng quyết định kỹ thuật. Ví dụ, hệ thống thanh toán có thể cần mức khả dụng 99,99%, trong khi dịch vụ gợi ý chỉ cần 99,9%. Việc lựa chọn phải dựa trên yêu cầu thực tế thay vì mặc định sử dụng GenAI cho mọi vấn đề.

4. **Tinh thần làm chủ và trách nhiệm:** Các trợ lý lập trình ứng dụng AI có thể nâng cao năng suất, nhưng không thể thay thế trách nhiệm của kỹ sư. Nhà phát triển vẫn phải chịu trách nhiệm về chất lượng mã nguồn, các lỗ hổng bảo mật tiềm ẩn và yêu cầu tuân thủ trước khi đưa phần mềm vào môi trường production.

5. **Kiến thức chuyên sâu kết hợp hiểu biết đa lĩnh vực:** Một kỹ sư lý tưởng cần có chuyên môn vững chắc trong một lĩnh vực, đồng thời hiểu biết thực tiễn về các lớp liên quan như UI, business logic, bảo mật và formal verification. Cách tiếp cận T-shaped hoặc polymath này hỗ trợ làm việc hiệu quả trong các nhóm nhỏ, linh hoạt theo mô hình **Two-Pizza Teams**, thường có khoảng 10–12 thành viên.

#### 3. Kết hợp tạo Prototype bằng AI với phương pháp Working Backwards của Amazon

- **Tăng tốc phát triển nhưng vẫn duy trì kỷ luật kỹ thuật:** Phương pháp **Working Backwards** của Amazon bắt đầu bằng việc xác định trải nghiệm khách hàng thông qua tài liệu PR/FAQ nội bộ trước khi tiến hành xây dựng sản phẩm. Việc sử dụng AI để tạo prototype giúp nhóm thử nghiệm ý tưởng và xây dựng bản minh họa ban đầu nhanh hơn. Tuy nhiên, tốc độ phát triển không được đánh đổi bằng chất lượng. Kỹ sư vẫn cần đánh giá mức độ rủi ro của từng thay đổi và thực hiện code review tương ứng, thay vì mặc nhiên tin tưởng mã nguồn do AI tạo ra.

- **Sử dụng AI để phát huy năng lực con người:** Dr. Werner nhấn mạnh rằng mục tiêu cuối cùng của công nghệ là phục vụ con người và tạo ra giá trị thiết thực. AI nên được xem là công cụ hỗ trợ và khuếch đại năng lực con người, không phải yếu tố thay thế con người. Những phẩm chất như **khả năng phán đoán, sáng tạo, sự đồng cảm và niềm tự hào nghề nghiệp** vẫn đóng vai trò quan trọng trong quá trình thiết kế, xây dựng và duy trì các hệ thống đáng tin cậy, kể cả những hạ tầng và dịch vụ mà người dùng không trực tiếp nhìn thấy.

---

### Những kiến thức và giá trị thu nhận được

1. **Lựa chọn công nghệ dựa trên nhu cầu thực tế:** Buổi trò chuyện giúp tôi nhận ra rằng không phải lúc nào sử dụng GenAI chỉ vì xu hướng cũng là quyết định đúng đắn. Trước khi lựa chọn giải pháp, kỹ sư cần đánh giá yêu cầu của workload và cân nhắc sự đánh đổi giữa chi phí, độ trễ và độ tin cậy khi vận hành.

2. **Chủ động chịu trách nhiệm khi phát triển phần mềm với AI:** Khi sử dụng các công cụ AI hỗ trợ lập trình trong dự án, nhà phát triển cần kiểm tra kỹ mã nguồn được tạo ra, thử nghiệm hành vi, rà soát nguy cơ bảo mật và hiểu rõ những gì mình triển khai. AI có thể hỗ trợ quá trình thực hiện, nhưng trách nhiệm đối với sản phẩm cuối cùng vẫn thuộc về kỹ sư.

3. **Rèn luyện kỹ năng giao tiếp và tư duy vượt ra ngoài từng thành phần:** Tôi hiểu rõ hơn tầm quan trọng của việc gắn các quyết định kỹ thuật với mục tiêu kinh doanh. Khả năng tư duy hệ thống và giải thích rõ những đánh đổi trong kiến trúc là các kỹ năng cần thiết. Bên cạnh đó, việc chia sẻ kiến thức và kinh nghiệm với các thành viên trong cộng đồng AWS First Cloud Journey cũng là cách thiết thực để cùng nhau phát triển.
