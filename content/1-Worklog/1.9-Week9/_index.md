---
title: "Week 9 Worklog"
date: 2026-11-09
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Week 9 Objectives:

* Explore location-based services that can support nearby ingredient-store discovery.
* Consolidate knowledge of monitoring, security, and cost management across the AWS services studied.
* Review the proposed application flow and prepare a clear task plan for the three-member group before the Workshop phase.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Explore Amazon Location Service and its main capabilities, including Maps, Places, Routes, and Geofences.<br>- Identify the Places capability as relevant to searching for nearby stores.<br>- Review the service's general use cases. | 11/09/2026 | 11/09/2026 | [What is Amazon Location Service?](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html) |
| 2 | - Study place search and nearby-place search.<br>- Understand the difference between text-based place discovery and searches based on geographic coordinates.<br>- Review how search position and geographic area affect returned results. | 11/10/2026 | 11/10/2026 | [Amazon Location Places](https://docs.aws.amazon.com/location/latest/developerguide/places.html)<br>[Search Nearby](https://docs.aws.amazon.com/location/latest/developerguide/search-nearby.html) |
| 3 | - Study geocoding and reverse geocoding.<br>- Understand how a typed address can be converted into coordinates and how coordinates can be converted into a readable address.<br>- Review browser Geolocation API permissions and a manual-address fallback when GPS is unavailable. | 11/11/2026 | 11/11/2026 | [Geocoding](https://docs.aws.amazon.com/location/latest/developerguide/geocoding.html)<br>[MDN Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) |
| 4 | - Review security considerations for application components and AWS service permissions.<br>- Understand why credentials should not be embedded in frontend code and why backend execution roles should follow least privilege.<br>- Study the AWS Well-Architected Framework, with attention to Security and Reliability. | 11/12/2026 | 11/12/2026 | [Amazon Location Security](https://docs.aws.amazon.com/location/latest/developerguide/security.html)<br>[AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) |
| 5 | - Explore Amazon CloudWatch metrics, logs, and alarms.<br>- Identify monitoring information that may be useful for Lambda functions and API requests.<br>- Learn how logs can help investigate errors, timeouts, and unexpected behavior. | 11/13/2026 | 11/13/2026 | [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br>[Lambda Monitoring](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html) |
| 6 | - Learn how AWS Pricing Calculator can estimate service costs and review the assumptions behind request, storage, and data-transfer estimates.<br>- Review AWS Budgets and Cost Explorer for monitoring actual spending.<br>- As a three-member group, review the high-level frontend, backend, database, and location-service responsibilities; record open questions and prepare the Workshop task allocation for the next phase. | 11/14/2026 | 11/14/2026 | [AWS Pricing Calculator](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html)<br>[AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html) |

### Week 9 Achievements:

* Understood the role of Amazon Location Service Places, nearby search, and geocoding for location-based features.
* Learned how browser location permissions and manual address input can support different user situations.
* Reviewed security responsibilities, least-privilege access, and relevant Well-Architected principles.
* Became familiar with CloudWatch monitoring and the use of logs to investigate application issues.
* Reviewed cost estimation and spending-monitoring tools.
* Prepared a preliminary three-member responsibility plan and a list of items to address during the Workshop phase in Weeks 10–11.
