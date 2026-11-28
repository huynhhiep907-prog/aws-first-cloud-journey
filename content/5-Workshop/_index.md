---
title: "Workshop"
date: 2026-11-27
weight: 5
chapter: false
pre: "<b>5. </b>"
---

# Bếp Thông Minh (Smart Kitchen) – AWS Workshop

## Overview

This workshop documents the implementation and deployment of **Bếp Thông Minh (Smart Kitchen)**, a recipe recommendation application built with AWS managed services. The application helps users discover recipes based on available ingredients, budget, cooking time, dietary preferences, mood, and weather. It also provides nearby ingredient-store lookup.

The solution separates the static frontend from the serverless backend. Amazon S3 stores the frontend files, while Amazon CloudFront delivers the website over HTTPS. Amazon API Gateway exposes the application endpoints and invokes AWS Lambda. The Lambda function retrieves recipe data from Amazon DynamoDB and integrates with Amazon Location Service for address geocoding and nearby place searches. Amazon Bedrock is integrated for conversational recipe suggestions, with a fallback response path when model invocation is unavailable.

## AWS Services

| AWS Service | Purpose |
| :--- | :--- |
| Amazon S3 | Hosts the static frontend files |
| Amazon CloudFront | Delivers the frontend over HTTPS |
| Amazon API Gateway | Exposes the application HTTP routes |
| AWS Lambda | Handles recipe search, nearby-store lookup, and chatbot requests |
| Amazon DynamoDB | Stores recipe records |
| Amazon Location Service | Geocodes manually entered addresses and searches for nearby stores |
| Amazon Bedrock | Supports AI-based recipe suggestions |
| Amazon CloudWatch | Stores Lambda execution logs |

## Workshop Contents

1. [Overview and Prerequisites](5.1-Workshop-overview/)
2. [Create the DynamoDB Database](5.2-Setup-Dynamodb/)
3. [Configure the AWS IAM Role](5.3-Configure-IAM-role/)
4. [Deploy the AWS Lambda Backend](5.4-Deploy-Lambda-backend/)
5. [Configure Amazon API Gateway](5.5-Configure-API-gateway/)
6. [Deploy the Frontend to S3 and CloudFront](5.6-Deploy-S3-Cloudfront/)
7. [Application Testing](5.7-Test-Application/)
8. [Clean Up Resources](5.8-Cleanup/)

