---
title: "Bản đề xuất"
date: 2026-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# BẾP THÔNG MINH
## SMART KITCHEN PLATFORM

Đề xuất xây dựng nền tảng hỗ trợ khám phá ẩm thực, nấu ăn tại nhà và tìm kiếm địa điểm cung cấp nguyên liệu.

| Thông tin | Chi tiết |
|---|---|
| Project Repository | https://github.com/huynhhiep907-prog/AWS-Final-Project-Cooking |
| Deployed Website | https://d35j83bya6fr1q.cloudfront.net/cooking/ |
| AWS Region | Asia Pacific (Singapore) – ap-southeast-1 |
| Project Owner | [CẦN BỔ SUNG] |
| Date | November 2026 |

---

# 1. Background and Motivation

## 1.1. Project Background

Trong cuộc sống hiện đại, việc lựa chọn món ăn, tìm công thức nấu nướng và chuẩn bị nguyên liệu là những nhu cầu thường xuyên. Tuy nhiên, thông tin về món ăn, cách chế biến và địa điểm mua nguyên liệu thường nằm rải rác trên nhiều nền tảng. Người dùng có thể mất thời gian để lựa chọn món phù hợp với nguyên liệu sẵn có, ngân sách và điều kiện mua sắm của mình.

Bếp Thông Minh (Smart Kitchen) là nền tảng web hỗ trợ người dùng khám phá món ăn, tham khảo công thức nấu ăn tại nhà và tìm kiếm địa điểm cung cấp nguyên liệu theo vị trí hoặc địa chỉ được nhập. Dự án sử dụng các dịch vụ AWS để triển khai giao diện, xử lý yêu cầu, lưu trữ dữ liệu, kết nối dịch vụ tìm kiếm địa điểm và tích hợp khả năng xử lý AI thông qua Amazon Bedrock.

## 1.2. Motivation and Objectives

- Đơn giản hóa việc khám phá món ăn và lựa chọn công thức phù hợp với nhu cầu.
- Cung cấp thông tin nguyên liệu và hướng dẫn chế biến để hỗ trợ người dùng nấu ăn tại nhà.
- Hỗ trợ tìm kiếm địa điểm bán nguyên liệu gần vị trí hiện tại hoặc địa chỉ do người dùng cung cấp.
- Xây dựng ứng dụng web trên AWS theo kiến trúc có thể bảo trì và mở rộng.
- Tích hợp Amazon Bedrock để bổ sung khả năng xử lý yêu cầu bằng AI tạo sinh trong ứng dụng.

## 1.3. Expected Outcomes

- Website có thể được truy cập qua địa chỉ triển khai trên AWS.
- Người dùng có thể xem, tìm kiếm và lọc dữ liệu công thức được cung cấp trong hệ thống.
- Người dùng có thể xem nguyên liệu và hướng dẫn chế biến của món ăn.
- Hệ thống có thể tiếp nhận yêu cầu tìm kiếm địa điểm và trả kết quả từ Amazon Location Service.
- Hệ thống có thể gửi yêu cầu đến Amazon Bedrock và nhận phản hồi từ mô hình AI được tích hợp.
- Frontend, backend, cơ sở dữ liệu và dịch vụ AI được kết nối thông qua các dịch vụ AWS.

Các tiêu chí trên mô tả kết quả và phạm vi chức năng của dự án. Ảnh chụp AWS Console, mã nguồn, log và kết quả kiểm thử cụ thể được trình bày trong phần Workshop/Minh chứng, không lặp lại trong Proposal.

# 2. Solution Architecture

## 2.1. Architecture Overview

Bếp Thông Minh sử dụng kiến trúc web serverless trên AWS. Giao diện người dùng được lưu trữ trên Amazon S3 và phân phối thông qua Amazon CloudFront. Các yêu cầu nghiệp vụ từ frontend được gửi đến Amazon API Gateway, sau đó chuyển đến AWS Lambda để xử lý. Lambda truy xuất dữ liệu công thức từ Amazon DynamoDB, gọi Amazon Location Service khi cần tìm kiếm địa điểm hoặc gọi Amazon Bedrock khi cần thực hiện chức năng AI.

Amazon Bedrock được tích hợp vào luồng xử lý backend. AWS Lambda đóng vai trò trung gian tiếp nhận yêu cầu, gửi nội dung đến mô hình AI và xử lý phản hồi trước khi trả kết quả về frontend. Cách tổ chức này giúp thông tin xác thực và quyền truy cập dịch vụ được quản lý ở phía backend thay vì đặt trong mã nguồn giao diện người dùng.

## 2.2. AWS Architecture Diagram

**[BỔ SUNG SƠ ĐỒ KIẾN TRÚC AWS TỔNG THỂ TẠI ĐÂY]**

Sơ đồ cần thể hiện các luồng chính:

- Người dùng truy cập website thông qua CloudFront; CloudFront phân phối nội dung frontend được lưu trữ trên S3.
- Frontend gửi yêu cầu đến API Gateway, sau đó API Gateway chuyển yêu cầu đến Lambda.
- Lambda đọc/ghi dữ liệu công thức trong DynamoDB.
- Lambda gọi Amazon Location Service khi cần tìm kiếm địa điểm cung cấp nguyên liệu.
- Lambda gọi Amazon Bedrock khi người dùng sử dụng chức năng AI; kết quả được xử lý và trả về frontend.

## 2.3. AWS Services and Responsibilities

| AWS Service | Vai trò trong dự án |
|---|---|
| Amazon S3 | Lưu trữ các tệp frontend và tài nguyên tĩnh của website. |
| Amazon CloudFront | Phân phối nội dung website đến người dùng thông qua CDN. |
| Amazon API Gateway | Cung cấp API endpoint để frontend giao tiếp với backend. |
| AWS Lambda | Tiếp nhận và xử lý logic nghiệp vụ, truy xuất dữ liệu và điều phối lời gọi đến các dịch vụ AWS. |
| Amazon DynamoDB | Lưu trữ và truy xuất dữ liệu công thức nấu ăn. |
| Amazon Location Service | Hỗ trợ tìm kiếm địa điểm/cửa hàng theo vị trí hoặc địa chỉ. |
| Amazon Bedrock | Cung cấp quyền truy cập mô hình AI tạo sinh; dự án tích hợp Amazon Nova Micro để xử lý yêu cầu AI từ ứng dụng. |

## 2.4. Main Application Flows

- **Truy cập website:** Người dùng truy cập website được phân phối qua CloudFront; nội dung frontend được lấy từ S3.
- **Khám phá công thức:** Frontend gửi yêu cầu đến API Gateway; Lambda xử lý và truy xuất dữ liệu công thức từ DynamoDB trước khi trả kết quả.
- **Tìm kiếm địa điểm:** Người dùng cung cấp vị trí GPS hoặc nhập địa chỉ; Lambda gọi Amazon Location Service và trả kết quả về frontend.
- **Xử lý yêu cầu AI:** Frontend gửi yêu cầu đến API Gateway; Lambda tiếp nhận và kiểm tra dữ liệu đầu vào, sau đó gọi Amazon Bedrock với mô hình Amazon Nova Micro. Lambda tiếp nhận phản hồi từ mô hình, xử lý kết quả và trả về frontend.

## 2.5. Scalability and Reliability

Việc sử dụng các dịch vụ managed/serverless giúp giảm nhu cầu tự quản lý máy chủ và cho phép từng thành phần mở rộng theo nhu cầu sử dụng. S3 và CloudFront đảm nhiệm lưu trữ, phân phối nội dung; API Gateway và Lambda xử lý yêu cầu ứng dụng; DynamoDB cung cấp lớp lưu trữ dữ liệu. Amazon Location Service và Amazon Bedrock được gọi khi ứng dụng cần chức năng tìm kiếm địa điểm hoặc xử lý AI.

Các cơ chế giám sát, cảnh báo, sao lưu và tối ưu hiệu suất sẽ được xem xét theo nhu cầu vận hành và ngân sách. Đối với Amazon Bedrock, cần kiểm soát số lượng yêu cầu, hạn mức sử dụng và thời gian phản hồi để hạn chế ảnh hưởng đến trải nghiệm người dùng.

# 3. Security Design

Bảo mật được xem xét xuyên suốt quá trình thiết kế và triển khai. Các nguyên tắc dưới đây là yêu cầu thiết kế; trạng thái cấu hình thực tế cần được đối chiếu với tài khoản AWS trước khi mô tả là đã hoàn tất.

## 3.1. Identity and Access Management

- Áp dụng nguyên tắc Least Privilege, chỉ cấp quyền cần thiết cho từng thành phần.
- Sử dụng IAM Role cho Lambda khi truy cập DynamoDB, Amazon Location Service và Amazon Bedrock.
- Cấp quyền gọi mô hình Bedrock ở mức cần thiết, chẳng hạn quyền thực hiện thao tác InvokeModel đối với mô hình được sử dụng.
- Không đưa Access Key, Secret Key hoặc thông tin xác thực vào mã nguồn frontend hoặc repository công khai.
- Tách biệt quyền quản trị tài nguyên AWS với quyền thực thi của ứng dụng.

## 3.2. Data and API Protection

- Ưu tiên sử dụng HTTPS cho kết nối giữa người dùng và website/API.
- Kiểm tra và xác thực dữ liệu đầu vào trước khi xử lý.
- Không trả thông tin nhạy cảm, thông tin xác thực hoặc chi tiết nội bộ trong phản hồi API.
- Cấu hình CORS, xác thực và giới hạn tần suất truy cập phù hợp với yêu cầu thực tế của ứng dụng.
- Kiểm soát nội dung gửi đến Amazon Bedrock, tránh gửi thông tin cá nhân hoặc dữ liệu nhạy cảm không cần thiết.
- Xử lý và kiểm tra phản hồi từ mô hình AI trước khi trả kết quả về giao diện người dùng.

## 3.3. Monitoring and Logging

Amazon CloudWatch có thể được sử dụng để theo dõi log, lỗi và các chỉ số của Lambda cũng như những thành phần AWS liên quan. Đối với luồng tích hợp Bedrock, cần theo dõi lỗi gọi mô hình, thời gian phản hồi và tình trạng vượt hạn mức. Việc thiết lập cảnh báo, thời gian lưu log và mức độ giám sát sẽ được điều chỉnh theo nhu cầu vận hành và ngân sách. Không ghi thông tin xác thực hoặc dữ liệu nhạy cảm của người dùng vào log.

# 4. Project Scope and Deliverables

## 4.1. In Scope – Phạm vi hiện tại

### A. Cooking and Recipe Discovery

- Hiển thị danh sách công thức nấu ăn.
- Hỗ trợ tìm kiếm và khám phá món ăn theo các tiêu chí được thiết kế.
- Hiển thị thông tin nguyên liệu và hướng dẫn chế biến.
- Cung cấp dữ liệu công thức để người dùng tham khảo khi nấu ăn tại nhà.

### B. Nearby Ingredient Store Discovery

- Cho phép người dùng cung cấp vị trí hiện tại nếu cấp quyền GPS hoặc nhập địa chỉ thủ công.
- Gửi yêu cầu tìm kiếm địa điểm đến backend.
- Sử dụng Amazon Location Service để tìm kiếm địa điểm phù hợp và trả kết quả cho giao diện.

### C. AI Integration with Amazon Bedrock

- Tích hợp Amazon Bedrock vào backend để xử lý yêu cầu AI từ ứng dụng.
- Sử dụng mô hình Amazon Nova Micro thông qua luồng xử lý backend.
- Tiếp nhận yêu cầu từ frontend, gửi đến mô hình AI và trả phản hồi về giao diện người dùng.
- Xử lý lỗi phát sinh trong quá trình gọi mô hình và phản hồi từ dịch vụ.

## 4.2. Future Scope

- Mở rộng khả năng cá nhân hóa gợi ý dựa trên nguyên liệu, ngân sách, sở thích và nhu cầu của người dùng.
- Cải thiện khả năng kết hợp dữ liệu công thức với phản hồi AI để hỗ trợ người dùng lập kế hoạch bữa ăn.
- Mở rộng khả năng khám phá dịch vụ ăn uống và kết nối với nhà hàng/đơn vị kinh doanh.

## 4.3. Out of Scope

- Thanh toán trực tuyến hoàn chỉnh.
- Quản lý kho hàng và đồng bộ tồn kho theo thời gian thực.
- Hệ thống vận chuyển hoặc theo dõi đơn hàng thực tế.
- Quản lý toàn diện hoạt động kinh doanh của nhà hàng.
- Phân tích dữ liệu quy mô lớn.

## 4.4. Project Deliverables

- Website Bếp Thông Minh được triển khai trên AWS.
- Frontend được lưu trữ trên Amazon S3 và phân phối qua CloudFront.
- Backend/API sử dụng API Gateway và AWS Lambda.
- Cơ sở dữ liệu công thức trên Amazon DynamoDB.
- Chức năng tìm kiếm địa điểm tích hợp Amazon Location Service.
- Chức năng AI tích hợp Amazon Bedrock với mô hình Amazon Nova Micro.
- Tài liệu Proposal và sơ đồ kiến trúc tổng thể.

Ảnh chụp AWS Console, mã nguồn, hướng dẫn triển khai từng bước, log và kết quả kiểm thử chi tiết thuộc tài liệu Workshop/Implementation Evidence, không phải nội dung chính của Proposal.

# 5. Implementation Roadmap

Dự án được chia thành các giai đoạn chính. Thời gian cụ thể có thể điều chỉnh theo tiến độ thực tế và nguồn lực của nhóm.

| Giai đoạn | Công việc chính | Kết quả |
|---|---|---|
| Phase 1: Planning | Xác định vấn đề, mục tiêu, yêu cầu và phạm vi dự án. | Yêu cầu và kế hoạch dự án. |
| Phase 2: Application Development | Xây dựng giao diện, backend và các chức năng cốt lõi. | Frontend và backend. |
| Phase 3: AWS Infrastructure and Data | Thiết lập S3, CloudFront, API Gateway, Lambda và DynamoDB. | Các thành phần ứng dụng được triển khai và kết nối. |
| Phase 4: External Service and AI Integration | Tích hợp Amazon Location Service và Amazon Bedrock; cấu hình quyền truy cập cần thiết, kết nối mô hình Amazon Nova Micro với backend và kiểm tra luồng phản hồi. | Chức năng tìm kiếm địa điểm và chức năng AI được tích hợp vào ứng dụng. |
| Phase 5: Documentation and Handover | Hoàn thiện tài liệu dự án, kiến trúc, chi phí và tài liệu Workshop. | Bộ tài liệu dự án. |

Mốc thời gian bắt đầu/kết thúc sẽ được bổ sung theo lịch triển khai thực tế; nhật ký công việc theo tuần được trình bày trong Worklog.

# 6. AWS Cost Estimation

## 6.1. Cost Estimation Approach

Dự án sử dụng các dịch vụ AWS theo mô hình serverless/managed nhằm hạn chế việc duy trì máy chủ liên tục. Chi phí phụ thuộc vào mức sử dụng thực tế như dung lượng lưu trữ, lưu lượng truyền dữ liệu, số lượng API request, thời gian thực thi Lambda, thao tác cơ sở dữ liệu, số lần truy vấn địa điểm và số lượng token xử lý qua Amazon Bedrock.

## 6.2. Actual AWS Cost – November 2026

Theo số liệu Billing được người thực hiện kiểm tra trong giai đoạn phát triển và thử nghiệm tháng 11/2026, Amazon Location Service là dịch vụ đã ghi nhận chi phí 0.55 USD. Các dịch vụ còn lại, bao gồm Amazon Bedrock, chưa có khoản phí được ghi nhận trong bảng kiểm tra tại thời điểm lập Proposal.

| AWS Service | Chi phí ghi nhận (USD) |
|---|---:|
| Amazon S3 | Chưa ghi nhận |
| Amazon CloudFront | Chưa ghi nhận |
| Amazon API Gateway | Chưa ghi nhận |
| AWS Lambda | Chưa ghi nhận |
| Amazon DynamoDB | Chưa ghi nhận |
| Amazon Location Service | 0.55 |
| Amazon Bedrock | Chưa ghi nhận |
| **Tổng chi phí đã ghi nhận** | **0.55** |

Đây là chi phí đã ghi nhận tại thời điểm kiểm tra, không phải dự báo chi phí vận hành hàng tháng. “Chưa ghi nhận” không đồng nghĩa dịch vụ chắc chắn miễn phí; chi phí có thể chưa vượt ngưỡng tính phí, nằm trong ưu đãi/Free Tier hoặc chưa được cập nhật đầy đủ. Việc tích hợp và kiểm thử thành công Amazon Bedrock không đồng nghĩa đã phát sinh một khoản phí được ghi nhận trong Billing tại thời điểm kiểm tra.

Chi phí Amazon Bedrock phụ thuộc vào mô hình được sử dụng, lượng token đầu vào và đầu ra cũng như số lượng yêu cầu. Cần tiếp tục theo dõi Billing sau khi có mức sử dụng thực tế.

## 6.3. Cost Optimization

- Theo dõi AWS Billing định kỳ để phát hiện chi phí phát sinh.
- Tối ưu số lượng request đến API và Amazon Location Service.
- Kiểm soát số lần gọi Amazon Bedrock và lượng token đầu vào/đầu ra.
- Sử dụng các dịch vụ serverless/managed phù hợp với lưu lượng thực tế.
- Đánh giá mức sử dụng và cấu hình tài nguyên trước khi mở rộng hệ thống.
- Thiết lập cảnh báo ngân sách để kịp thời phát hiện chi phí tăng bất thường.

Dự toán chi phí vận hành trong tương lai sẽ được lập bằng AWS Pricing Calculator khi xác định được các giả định như số người dùng, số request mỗi tháng, dung lượng lưu trữ, lưu lượng truyền dữ liệu và mức sử dụng mô hình AI. Không sử dụng số liệu chi phí hiện tại để suy diễn thành chi phí vận hành dài hạn.

# 7. Project Management, Risks and Conclusion

## 7.1. Project Owner and Team

| Thành viên | Vai trò | Trách nhiệm |
|---|---|---|
| [Tên thành viên] | [Vai trò] | [Nhiệm vụ thực tế] |
| [Tên thành viên] | [Vai trò] | [Nhiệm vụ thực tế] |
| [Tên thành viên] | [Vai trò] | [Nhiệm vụ thực tế] |

## 7.2. Risks and Mitigation

| Rủi ro | Ảnh hưởng | Biện pháp giảm thiểu |
|---|---|---|
| AWS Service Quota | Một số dịch vụ hoặc mô hình có thể gặp giới hạn về quota hoặc quyền truy cập. | Theo dõi hạn mức, kiểm tra quyền truy cập và điều chỉnh mức sử dụng phù hợp. |
| API Failure | Frontend không nhận được dữ liệu từ backend. | Ghi log, xử lý ngoại lệ và kiểm tra trạng thái API. |
| Database Performance | Truy vấn có thể chậm khi dữ liệu hoặc lượng truy cập tăng. | Tối ưu thiết kế dữ liệu và cách truy vấn. |
| Location Accuracy | Kết quả địa điểm có thể không đầy đủ hoặc chưa chính xác. | Cho phép nhập địa chỉ thủ công và xử lý kết quả trả về. |
| AI Response Quality | Phản hồi do mô hình AI tạo ra có thể chưa chính xác hoặc chưa phù hợp với yêu cầu. | Kiểm tra dữ liệu đầu vào, xử lý phản hồi và thông báo phù hợp cho người dùng. |
| AI Availability and Limits | Yêu cầu AI có thể thất bại khi dịch vụ không khả dụng hoặc chạm giới hạn sử dụng. | Xử lý lỗi, theo dõi hạn mức và cung cấp thông báo khi không thể nhận phản hồi. |
| Unexpected AWS Costs | Chi phí tăng khi lưu lượng hoặc mức sử dụng dịch vụ vượt dự kiến. | Theo dõi Billing, kiểm soát request/token và thiết lập cảnh báo ngân sách. |

## 7.3. Conclusion

Bếp Thông Minh hướng đến việc cung cấp một nền tảng hỗ trợ khám phá món ăn, tham khảo công thức nấu ăn và tìm kiếm địa điểm cung cấp nguyên liệu. Việc sử dụng Amazon S3, CloudFront, API Gateway, AWS Lambda, DynamoDB và Amazon Location Service tạo nền tảng để triển khai các chức năng cốt lõi trên AWS. Bên cạnh đó, Amazon Bedrock với mô hình Amazon Nova Micro đã được tích hợp vào backend, bổ sung khả năng xử lý yêu cầu bằng AI tạo sinh cho ứng dụng.

Proposal này xác định bối cảnh, mục tiêu, kiến trúc, phạm vi, yêu cầu bảo mật, kế hoạch triển khai, chi phí và các rủi ro chính của dự án. Các minh chứng chi tiết về quá trình tích hợp, mã nguồn và kết quả kiểm thử được trình bày trong phần Workshop/Implementation Evidence.

---

## Project Information

| Thông tin | Chi tiết |
|---|---|
| Project | Bếp Thông Minh – Smart Kitchen Platform |
| Repository | https://github.com/huynhhiep907-prog/AWS-Final-Project-Cooking |
| Deployed Website | https://d35j83bya6fr1q.cloudfront.net/cooking/ |
| AWS Region | ap-southeast-1 (Singapore) |
| Project Owner | [CẦN BỔ SUNG] |
| Date | November 2026 |
