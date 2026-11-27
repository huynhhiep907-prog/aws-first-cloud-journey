---
title: "Week 10 Worklog"
date: 2026-11-16
weight: 2
chapter: false
pre: " <b> 1.10. </b> "
---


### Week 10 Objectives:

* Begin the **Smart Kitchen (Bếp Thông Minh)** workshop.
* Review the existing source code, define the project scope, and identify the AWS services in use.
* Check the frontend, backend, and database to plan the remaining improvements.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Define the objectives and scope of the Bếp Thông Minh workshop.<br>- Review the main website features and confirm the focus on cooking recommendations.<br>- Inspect the repository structure and identify the frontend and backend components. | 11/16/2026 | 11/16/2026 | [GitHub - AWS Final Project Cooking](https://github.com/veexto/AWS-Final-Project-Cooking) |
| 3 | - Review the frontend source code and how the website calls the API.<br>- Inspect API Gateway endpoints and the request-handling logic in AWS Lambda.<br>- Record the areas that need to be checked when connecting the frontend and backend. | 11/17/2026 | 11/17/2026 | [AWS Lambda](https://docs.aws.amazon.com/lambda/) |
| 4 | - Review the recipe data structure in DynamoDB.<br>- Check the seed data and the fields required for recipe search.<br>- Compare API responses with the existing recipe records. | 11/18/2026 | 11/18/2026 | [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb/) |
| 5 | - Review frontend hosting on Amazon S3 and content delivery through CloudFront.<br>- Inspect the origin configuration and website access URL.<br>- Check whether the website is accessible through CloudFront. | 11/19/2026 | 11/19/2026 | [Amazon S3](https://docs.aws.amazon.com/s3/) · [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront/) |
| 6 | - Summarize issues found while checking the frontend, API, and recipe data.<br>- Prepare the next week's improvement checklist, including recipe search, AI-based suggestions, and nearby food-store discovery. | 11/20/2026 | 11/21/2026 | [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/) |

### Week 10 Achievements:

* Defined the workshop scope as a website for recipe search and cooking recommendations, rather than an ordering platform.
* Reviewed the overall frontend and backend source-code structure.
* Documented the main request flow: users interact with the website, the frontend sends requests to API Gateway, Lambda processes them, and recipe data is retrieved from DynamoDB.
* Reviewed the frontend hosting approach using S3 and content delivery through CloudFront.
* Prepared a checklist of items for further testing and improvement in Week 11.
