---
title: "AWS Cloud and AI Day Hanoi 2026 – Ho Chi Minh City Watch Party Hub"
date: 2026-09-29
weight: 1
chapter: false
pre: " <b> 4.2. </b> "
---

{{% notice warning %}}
⚠️ **Note:** The information below is for reference purposes only. Please **do not copy it verbatim** into your report, including this warning.
{{% /notice %}}

# Event Report: AWS Cloud and AI Day Hanoi 2026 – Ho Chi Minh City Watch Party Hub

### Event Overview

- **Event Name:** AWS Cloud and AI Day Hanoi 2026 – Ho Chi Minh City Watch Party Hub
- **Date:** September 29, 2026
- **Participation Format:** Attended the in-person Watch Party in Ho Chi Minh City, following the livestreamed Keynotes and Developer Chats from the Hanoi venue alongside the AWS First Cloud Journey community.
- **Organizers:** AWS Vietnam, AWS Community Builders, and AWS First Cloud Journey (FCJ).

### Main Topics and Insights

#### 1. Moving from Technology Adoption to Operational Maturity

A key message from the event was that Vietnam's cloud and AI ecosystem is moving beyond Proof-of-Concept (PoC) experiments toward operating production systems reliably, securely, and at scale.

Production workloads require clearly assigned ownership, well-defined access boundaries, comprehensive observability, resilient infrastructure, and repeatable cost-management practices. These capabilities are essential for turning promising prototypes into dependable services.

#### 2. Agentic AI and the Role of Platform Engineering

Agentic AI was one of the central themes. AI systems are evolving from tools that primarily generate content into agents that can call APIs, access internal data, modify code, and initiate deployment workflows.

As these agents become more autonomous and development cycles accelerate, Platform Engineering provides important engineering guardrails. It helps standardize deployment processes, establish secure defaults, govern software supply chains, and define approval boundaries for actions performed by AI agents.

#### 3. Workload Identity and AI Agent Security on AWS

The Developer Chats session presented by **Kha Van**, Cloud Security Engineer and AWS Community Builder, examined an important security question: when a workload makes an AWS API request, which identity is actually being used?

The discussion highlighted the growing number of non-human identities in cloud environments, including Kubernetes Pods, CI/CD pipelines, serverless functions, and AI agents. These identities need appropriate governance just as human users do.

AWS approaches discussed included **Amazon EKS Pod Identity**, short-lived temporary credentials, fine-grained workload-level permissions, strict IAM trust policies, and runtime identity verification. These practices help avoid relying on overly broad permissions inherited from EC2 nodes and support the principle of least privilege.

#### 4. AWS Infrastructure Development in Vietnam and Hybrid Architectures

The event highlighted AWS infrastructure developments in Vietnam, including **AWS Direct Connect in Hanoi** and the **Hanoi AWS Local Zone**.

These options give organizations more flexibility for private connectivity, low-latency applications, and workloads with data locality requirements. They also create more choices when designing hybrid architectures that combine on-premises infrastructure and cloud services.

Architecture decisions should balance latency, resilience, compliance, security, and cost rather than focusing on only one factor.

#### 5. Enterprise Transformation and Vietnam's Cloud Community

The **TCBS Customer Story** demonstrated how AI can transform software engineering when it becomes part of everyday development activities, including writing, reviewing, testing, and delivering code. The value of AI adoption should be assessed through measurable operational improvements, not simply by adding another tool to the technology stack.

The keynote also shared figures illustrating the growth of Vietnam's cloud and AI ecosystem:

- More than **157,000** individuals trained in cloud and AI.
- Over **54,000** members in the **AWS Study Group**.
- More than **15,000** participants in the **First Cloud and AI Journey (FCJ)** ecosystem.

These figures reflect the increasing interest in cloud and AI knowledge among developers and technology professionals in Vietnam.

### Ho Chi Minh City Watch Party Experience

Although the main event took place in Hanoi, joining the Ho Chi Minh City Watch Party provided an opportunity to follow the sessions with fellow FCJ interns and mentors in person.

The local gathering made it possible to exchange ideas, discuss real-world architecture decisions, and learn from other participants while watching the livestreamed sessions. It also helped strengthen connections within the Ho Chi Minh City AWS community.

### Key Takeaways and Application to My Internship

#### 1. Adopt a Production-First Mindset

A working demonstration does not automatically mean that an application is ready for production. Logging, monitoring, observability, reliability, and cost controls should be considered from the beginning of the design process.

#### 2. Prioritize Identity-Centered Security

Workloads and AI agents should not be given broad permissions simply for convenience. Temporary credentials, narrowly scoped IAM policies, and the principle of least privilege help reduce unnecessary security risks.

#### 3. Learn and Share Through the Community

Learning from experienced practitioners, mentors, and AWS Community Builders provides practical perspectives beyond technical documentation. Recording and sharing these insights can also improve my understanding of cloud architecture and engineering practices.

### Event Photos

*Add your event photos here.*

> Overall, AWS Cloud and AI Day Hanoi 2026 provided valuable perspectives on the development of cloud computing and AI in Vietnam. The sessions reinforced the importance of secure, observable, resilient, and cost-aware architectures, as well as the engineering practices required to move from prototypes to reliable production systems.
