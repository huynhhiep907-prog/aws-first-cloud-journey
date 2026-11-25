---
title: "Week 2 Worklog"
date: 2026-09-21
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives:

* Understand object storage and the way Amazon S3 organizes application files.
* Learn how to protect stored files through bucket policies, versioning, and encryption.
* Explore how static website assets and structured data files can be prepared for a web application.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Study object storage concepts and compare objects, files, and block storage.<br>- Learn the relationship between an S3 bucket, object key, metadata, and object body.<br>- Identify suitable S3 use cases such as images, documents, and static website assets. | 09/21/2026 | 09/21/2026 | [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |
| 2 | - Review S3 bucket naming, object organization, and uploading/downloading objects.<br>- Learn how prefixes organize files by feature or content type.<br>- Consider a folder structure for recipe images and website assets. | 09/22/2026 | 09/22/2026 | [Organizing Objects in S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) |
| 3 | - Study S3 Block Public Access and risks of exposing stored files unintentionally.<br>- Understand the difference between bucket policies and IAM identity policies.<br>- Review how access should be limited to required resources. | 09/23/2026 | 09/23/2026 | [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)<br>[Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) |
| 4 | - Learn how S3 Versioning preserves previous object versions.<br>- Review recovery from accidental overwrites or deletions.<br>- Identify cases where versioning is useful for website files and project data. | 09/24/2026 | 09/24/2026 | [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) |
| 5 | - Study S3 default encryption and the difference between SSE-S3 and SSE-KMS.<br>- Understand encryption at rest and why sensitive data should not be publicly accessible.<br>- Review the relationship between encryption settings and access permissions. | 09/25/2026 | 09/25/2026 | [S3 Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) |
| 6 | - Explore S3 Lifecycle rules and storage classes.<br>- Learn how objects can transition to lower-cost storage or expire after a defined period.<br>- Review a retention policy for temporary files and old project assets. | 09/26/2026 | 09/26/2026 | [S3 Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)<br>[S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/) |

### Week 2 Achievements:

* Understood how Amazon S3 stores objects and how buckets and object keys organize data.
* Learned how to organize website assets and distinguish public content from private files.
* Became familiar with S3 Block Public Access, bucket policies, and least-privilege access.
* Understood the role of versioning and server-side encryption in protecting stored data.
* Learned how lifecycle rules and storage classes can help manage long-term storage costs.
