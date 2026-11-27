---
title: "Week 11 Worklog"
date: 2026-11-23
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Week 11 Objectives:

* Continue improving and testing the Bếp Thông Minh workshop.
* Review recipe search, AI-based suggestions, and nearby food-store discovery.
* Complete the proposal, architecture diagram, and AWS cost estimates.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Test recipe search by ingredients and the available recipe filters.<br>- Compare search results with recipe records in DynamoDB.<br>- Record cases where results do not yet meet the expected behavior for further adjustment. | 11/23/2026 | 11/23/2026 | [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb/) |
| 3 | - Review nearby food-store discovery using Amazon Location Service.<br>- Check backend permissions and the returned place data.<br>- Evaluate search results against the expected search radius and store categories. | 11/24/2026 | 11/24/2026 | [Amazon Location Service](https://docs.aws.amazon.com/location/) |
| 4 | - Check the recipe chatbot/suggestion flow using Amazon Bedrock and the Nova Micro model.<br>- Monitor Lambda responses and record the quota limitation encountered when invoking the model.<br>- Review the fallback response approach so the feature can still return results when Bedrock is unavailable. | 11/25/2026 | 11/25/2026 | [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/) |
| 5 | - Update the Bếp Thông Minh workshop proposal.<br>- Complete the AWS service descriptions, workflow, and architecture diagram including CloudFront.<br>- Use AWS Pricing Calculator to estimate costs under assumed usage levels and summarize the services and usage assumptions. | 11/26/2026 | 11/26/2026 | [AWS Pricing Calculator](https://calculator.aws/) |
| 6 | - Review the proposal, architecture diagram, and estimated-cost table.<br>- Check consistency between the services described in the document and the deployed architecture.<br>- Summarize workshop progress, remaining limitations, and items that require further verification. | 11/27/2026 | 11/27/2026 | [AWS Architecture Center](https://aws.amazon.com/architecture/) |

### Week 11 Achievements:

* Continued reviewing the main Bếp Thông Minh features, including recipe search, recipe filters, and nearby food-store discovery.
* Reviewed the Amazon Location Service integration flow and documented considerations related to returned place data.
* Tested the Amazon Bedrock Nova Micro integration and recorded the quota limitation; a fallback response approach was retained, so direct model invocation was not treated as stable.
* Updated the proposal, documented the deployment architecture, and included CloudFront in the frontend delivery flow.
* Prepared AWS service cost estimates with AWS Pricing Calculator based on assumed usage levels. These are estimates, not actual billing charges.
* Summarized the reviewed items, remaining limitations, and areas requiring further improvement.
