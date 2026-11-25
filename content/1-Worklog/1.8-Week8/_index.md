---
title: "Week 8 Worklog"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives:

* Learn how to monitor serverless applications and investigate failures across API Gateway and Lambda.
* Understand practical application testing, logging, and troubleshooting workflows.
* Review AWS cost estimation and prepare technical knowledge for the upcoming project workshop.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Study the purpose of Amazon CloudWatch in monitoring AWS resources and applications.<br>- Understand metrics, logs, dashboards, and alarms at a high level.<br>- Identify useful indicators for a serverless web application, such as request count, latency, and function errors. | 11/02/2026 | 11/02/2026 | [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) |
| 2 | - Learn how Lambda sends execution logs to CloudWatch Logs.<br>- Review log groups, log streams, timestamps, and retention settings.<br>- Study how log messages and request identifiers can help trace a failed invocation. | 11/03/2026 | 11/03/2026 | [Viewing Lambda Logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html)<br>[CloudWatch Logs Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.html) |
| 3 | - Review API Gateway metrics and access logging.<br>- Learn how to investigate 4xx and 5xx responses and distinguish gateway errors from backend function errors.<br>- Prepare a troubleshooting flow from browser request to API Gateway, Lambda, and data source. | 11/04/2026 | 11/04/2026 | [Monitoring API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring-cloudwatch.html)<br>[HTTP API Troubleshooting](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-troubleshooting.html) |
| 4 | - Study API testing concepts using request tools such as Postman or curl.<br>- Review how to test query parameters, request headers, status codes, and JSON response bodies.<br>- Learn how to keep test cases repeatable and record expected versus actual results. | 11/05/2026 | 11/05/2026 | [Postman – Sending the First Request](https://learning.postman.com/docs/getting-started/first-steps/sending-the-first-request/)<br>[curl Manual](https://curl.se/docs/manpage.html) |
| 5 | - Explore AWS Pricing Calculator and learn to estimate costs from service usage assumptions.<br>- Review cost dimensions relevant to the planned application, including S3 storage, CloudFront data transfer, API requests, Lambda duration, DynamoDB capacity, and Location Service requests.<br>- Understand that estimates depend on Region, usage volume, and configuration. | 11/06/2026 | 11/06/2026 | [AWS Pricing Calculator](https://calculator.aws/)<br>[AWS Pricing Overview](https://aws.amazon.com/pricing/) |
| 6 | - Review AWS Well-Architected Framework principles, especially operational excellence, security, reliability, and cost optimization.<br>- Summarize key concepts studied during Weeks 1–8 and relate them to a small serverless web application.<br>- Prepare a learning checklist for the Workshop phase scheduled for Weeks 9–11. | 11/07/2026 | 11/07/2026 | [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)<br>[Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) |

### Week 8 Achievements:

* Understood how CloudWatch metrics, logs, dashboards, and alarms support application monitoring.
* Learned how to trace Lambda execution logs and investigate API Gateway errors.
* Reviewed a repeatable approach to testing HTTP endpoints and checking JSON responses.
* Became familiar with AWS Pricing Calculator and the main cost dimensions of the planned application.
* Connected the topics studied in Weeks 1–8 with the operational and architectural needs of the upcoming Workshop phase.
