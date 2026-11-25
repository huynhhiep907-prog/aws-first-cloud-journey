---
title: "Week 6 Worklog"
date: 2026-10-19
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:

* Understand the serverless computing model and the role of AWS Lambda.
* Learn Lambda execution concepts, event payloads, runtime configuration, and permissions.
* Explore how backend application logic can run on demand without managing servers.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Study serverless architecture and compare it with managing a continuously running server.<br>- Understand event-driven execution and the pay-per-use model.<br>- Identify suitable tasks for serverless functions, such as processing a search request. | 10/19/2026 | 10/19/2026 | [AWS Serverless](https://aws.amazon.com/serverless/) |
| 2 | - Learn the basic structure of an AWS Lambda function.<br>- Review supported runtimes, handler functions, deployment packages, and environment variables.<br>- Understand the difference between function code and the Lambda execution environment. | 10/20/2026 | 10/20/2026 | [Lambda Programming Model](https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html) |
| 3 | - Study Lambda invocation types and event-driven processing.<br>- Understand synchronous and asynchronous invocation at a high level.<br>- Review how a function receives an event and returns a response. | 10/21/2026 | 10/21/2026 | [Invoking Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html) |
| 4 | - Explore Lambda configuration options, including memory, timeout, temporary storage, and environment variables.<br>- Understand how these settings affect function behavior and cost.<br>- Review why timeout and memory settings should match the workload. | 10/22/2026 | 10/22/2026 | [Configuring Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html) |
| 5 | - Learn about Lambda execution roles and the permissions required by a function.<br>- Distinguish the execution role from the permissions of a person invoking the function.<br>- Review how a function should receive only the permissions needed to access its data source. | 10/23/2026 | 10/23/2026 | [Lambda Execution Role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) |
| 6 | - Review Lambda logging and the use of CloudWatch Logs.<br>- Learn how to read invocation logs and identify errors or timeouts.<br>- Explore AWS Lambda Python examples to understand the structure of a request-processing function. | 10/24/2026 | 10/24/2026 | [Lambda Logging](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html)<br>[Python Lambda Handler](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html) |

### Week 6 Achievements:

* Understood the serverless and event-driven computing model.
* Learned the structure of a Lambda function and the role of its handler, runtime, and deployment package.
* Became familiar with invocation types and event/response processing.
* Understood how memory, timeout, and environment variables influence function configuration.
* Learned why Lambda execution roles and CloudWatch Logs are important for secure operation and troubleshooting.
