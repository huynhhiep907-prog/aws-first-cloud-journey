---
title: "First Cloud AI Journey: Weekly Meet Up 24/10"
date: 2026-10-24
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---



# Event Report: “First Cloud AI Journey: Weekly Meet Up 24/10”

### Event Information

- **Event name:** First Cloud AI Journey: Weekly Meet Up 24/10
- **Date:** October 24, 2026
- **Organizers:** AWS First Cloud Journey (FCJ) and AWS Study Group

### Session Highlights

#### 1. Building Voice AI Agents and AI-powered Recruitment Interviews

- **Speaker:** Kiet Tran – Engineer at ReAI (AWS Partner).
- **Key topics:**
  - Introduced different approaches to building Voice AI systems, with a focus on low latency for natural conversations (a reference target of approximately 200ms). The session compared three architectures: Cascaded (ASR → LLM → TTS), Speech-to-Speech, and Full Speech-to-Speech combined with background reasoning models.
  - Explained the call-processing flow involving SIP Servers and Media Servers (WebRTC/UDP), together with noise cancellation and Voice Activity Detection (VAD). The presented system ran on Multi-AZ GPU infrastructure, connected through AWS PrivateLink, with an overall response time of approximately 1.8 seconds.
  - The live demo showcased an AI recruitment assistant that could call candidates and interview them on AWS topics such as EC2, S3, EKS, RDS, and VPC. Other practical topics included preparing Vietnamese text for TTS, applying Guardrails to moderate responses, and keeping operating costs at an indicative level of around VND 3,000 per call.

#### 2. Sharing Resources Across AWS Accounts with AWS Resource Access Manager (AWS RAM)

- **Speaker:** Long – AWS Study Group.
- **Key topics:**
  - Discussed centralized resource management in Multi-Account environments using AWS RAM. The service supports sharing more than 40 resource types, including VPC Subnets, Security Groups, and Reserved EC2 Instances, across accounts without a separate charge for the sharing operation.
  - Explained how AWS RAM Permissions work together with IAM Policies and Service Control Policies (SCPs) in AWS Organizations to govern resource access. EventBridge and CloudTrail were also mentioned as tools for monitoring related activities.
  - Highlighted implementation considerations for Terraform and CloudFormation, particularly the need to align Availability Zone IDs across accounts to avoid unintended data-transfer costs. The Hub-and-Spoke network model was also introduced as an approach to organizing infrastructure connectivity.

#### 3. Automated Security Testing with AWS Security Agent

- **Speaker:** Thinh – Engineer at Steel Solution.
- **Key topics:**
  - Presented three core capabilities of AWS Security Agent. Design Review evaluates Terraform infrastructure designs to identify architectural risks early; Code & Security Review integrates with GitHub/GitLab Pull Requests and CI/CD workflows; Automated Penetration Testing simulates user behavior to identify vulnerabilities and build attack graphs in SIT/UAT environments.
  - Discussed the Shared Responsibility Model and how security responsibilities are distributed. The session also covered using an agent or extension through a private tunnel to connect to a self-hosted GitLab server, supporting security checks while protecting internal source code.

#### 4. Bringing AI Agents to Production with Amazon Bedrock AgentCore

- **Speaker:** Nguyen Son An – Leader of the AWS Student Group at HCMUTE.
- **Key topics:**
  - Examined challenges that arise when moving AI Agents from experimentation to production, including security, session isolation, and conversation-state management.
  - Introduced Amazon Bedrock AgentCore through two main components:
    - **Runtime:** Provides a serverless execution environment in which each session is isolated in its own MicroVM. The session discussed an EC2 Spot Instance-based infrastructure approach and cost optimization through CPU-based charging during execution.
    - **Memory:** Manages information at two levels. Short-term Memory stores conversation data associated with a `sessionId` and supports session branching. Long-term Memory asynchronously extracts information to produce summaries and retain user preferences and long-term knowledge.

#### 5. Improving Software Development and 24/7 Operations Automation with Kiro

- **Speakers:** Hieu Nghi – Leader of the AWS Student Group, and Khoa – Tech Lead at ACB.
- **Key topics:**
  - Introduced Spec-Driven Development through the Plan → Design → Tasks workflow, helping teams clarify requirements and implementation steps before development. Safety measures were also discussed, such as masking secrets/passwords and requiring manual approval before potentially destructive infrastructure commands.
  - Shared enterprise use cases for Kiro, including connecting it to Telegram to check and report AWS resource status every five minutes, as well as automating GitHub Code Reviews based on internal standards.
  - Emphasized managing the Context Window carefully to use tokens efficiently and control costs when working with AI tools.

### Knowledge and Lessons Gained

#### Architectural Thinking

- Learned that AI system design requires balancing response latency, language-processing quality, scalability, and operating costs.
- Gained a better understanding of Multi-Account infrastructure, resource sharing, and selecting suitable connectivity models for different system requirements.

#### Security Throughout the Development Lifecycle

- Recognized the importance of introducing security checks early in the development lifecycle, from Infrastructure as Code design to Pull Request reviews.
- Understood that security should be maintained throughout development and operations rather than being treated as a final-stage activity.

#### Emerging AWS AI Technologies and Tools

- Gained further insight into operating AI Agents in production with Amazon Bedrock AgentCore, particularly session and memory management.
- Explored how Kiro can support specification-driven development, code reviews, and automation of operational tasks.

#### Applying the Knowledge to My Internship Project

- The discussion of Amazon Bedrock AgentCore helped me better understand the considerations involved in integrating AI capabilities into the Smart Kitchen project.
- The sessions on security, monitoring, and cost optimization also provided useful ideas for reviewing and improving the way AWS services are deployed in the project.
- The event reinforced the importance of evaluating solutions based on actual requirements, complexity, and cost instead of adopting technologies simply because they are trending.

### Event Experience

The event provided an opportunity to learn about several technologies and practices used in real-world environments, ranging from Voice AI and multi-account resource management to automated security testing and production AI Agents. The examples and demonstrations helped me better understand how AWS services and tools can work together to address practical business and engineering challenges.

Beyond the technical content, I learned to evaluate solutions from multiple perspectives, including architecture, security, performance, operability, and cost. These insights are valuable for my ongoing learning and for improving my internship project.
