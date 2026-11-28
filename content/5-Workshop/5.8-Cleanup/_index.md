---
title: "Clean Up Resources"
date: 2026-11-27
weight: 8
chapter: false
pre: "<b>5.8. </b>"
---

To avoid incurring further charges after completing the lab, delete the resources in the following order:

1. **Amazon CloudFront: Disable and delete the distribution pointing to `recipe-suggestion-website`.**.
2. **Amazon S3: Empty and delete the `recipe-suggestion-website` bucket.**.
3. **Amazon API Gateway: Delete the `BepThongMinhAPI` HTTP API.**
4. **AWS Lambda: Delete the `RecipeSearchFunction` function.**
5. **Amazon CloudWatch Logs: Delete the `/aws/lambda/RecipeSearchFunction` log group.**
6. **Amazon DynamoDB: Delete the `RecipesTable` table.**
7. **AWS IAM: Delete the `RecipesLambdaRole` role, including the `RecipesLambdaPolicy` and `AmazonLocationGeoPlacesAccess` inline policies.**
