---
title: "Week 3 Worklog"
date: 2026-09-28
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Week 3 Objectives:

* Understand the basic networking components used by AWS workloads.
* Learn how Amazon VPC provides an isolated network for cloud resources.
* Explore EC2 compute fundamentals and the relationship between instances, storage, and network security.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Study the purpose of Amazon Virtual Private Cloud (VPC).<br>- Understand CIDR notation, IP addresses, and the role of a VPC address range.<br>- Review how subnets divide a VPC into smaller network segments. | 09/28/2026 | 09/28/2026 | [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| 2 | - Learn the differences between public and private subnets.<br>- Study route tables, internet gateways, and how traffic is routed.<br>- Understand at a high level how a resource in a public subnet can communicate with the internet. | 09/29/2026 | 09/29/2026 | [VPC Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)<br>[Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) |
| 3 | - Review security groups and network access control lists (network ACLs).<br>- Understand stateful versus stateless traffic filtering.<br>- Learn why inbound and outbound rules should allow only required traffic. | 09/30/2026 | 09/30/2026 | [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)<br>[Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| 4 | - Study Amazon EC2 and its role as a virtual compute service.<br>- Learn about Amazon Machine Images (AMIs), instance types, and instance states.<br>- Understand the difference between stopping, starting, and terminating an instance. | 10/01/2026 | 10/01/2026 | [Amazon EC2 Concepts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) |
| 5 | - Explore EC2 storage options, especially Amazon Elastic Block Store (EBS).<br>- Understand the relationship between an instance and its attached EBS volumes.<br>- Review key-pair use for Linux instance access and basic SSH connection concepts. | 10/02/2026 | 10/02/2026 | [Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)<br>[Connect to a Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect.html) |
| 6 | - Review common EC2 cost factors, including instance running time, EBS storage, and data transfer.<br>- Learn how to select an instance size appropriate to a workload rather than over-provisioning.<br>- Summarize how VPC, subnet, security group, EC2, and EBS work together. | 10/03/2026 | 10/03/2026 | [EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)<br>[Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing/) |

### Week 3 Achievements:

* Understood VPC, CIDR ranges, subnets, route tables, and internet gateways.
* Learned how security groups and network ACLs control network traffic.
* Became familiar with EC2 instances, AMIs, instance types, and lifecycle operations.
* Understood the role of EBS and key pairs when working with EC2.
* Gained a foundation for understanding how AWS resources communicate within a network.
