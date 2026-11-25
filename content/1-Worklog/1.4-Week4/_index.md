---
title: "Week 4 Worklog"
date: 2026-10-05
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Week 4 Objectives:

* Understand object storage and the way Amazon S3 organizes application files.
* Learn how to protect stored files through access controls, versioning, and encryption.
* Explore storage management concepts relevant to static website assets and recipe data.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Study object storage and compare object, block, and file storage.<br>- Learn the relationship between an S3 bucket, object key, metadata, and object body.<br>- Identify suitable S3 use cases such as images, documents, and static website assets. | 10/05/2026 | 10/05/2026 | [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |
| 2 | - Review bucket naming, object organization, and uploading/downloading objects.<br>- Learn how prefixes organize files by feature or content type.<br>- Consider a logical folder structure for recipe images and frontend assets. | 10/06/2026 | 10/06/2026 | [Organizing Objects in S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) |
| 3 | - Study S3 Block Public Access and the risks of exposing stored files unintentionally.<br>- Understand bucket policies and how they differ from IAM identity policies.<br>- Review the principle of granting access only to the required resources. | 10/07/2026 | 10/07/2026 | [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)<br>[Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) |
| 4 | - Learn how S3 Versioning preserves previous object versions.<br>- Review recovery from accidental overwrites or deletions.<br>- Identify when versioning is useful for website files and project assets. | 10/08/2026 | 10/08/2026 | [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) |
| 5 | - Study S3 default encryption and server-side encryption options.<br>- Understand encryption at rest and the relationship between encryption settings and access permissions.<br>- Review why sensitive files should not be made publicly accessible. | 10/09/2026 | 10/09/2026 | [S3 Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) |
| 6 | - Explore S3 Lifecycle rules and storage classes.<br>- Learn how objects can transition to lower-cost storage or expire after a defined period.<br>- Review the cost and retention implications of storing website assets and backups. | 10/10/2026 | 10/10/2026 | [S3 Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)<br>[S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/) |

### Week 4 Achievements:

* Understood S3 buckets, objects, keys, and common object-storage use cases.
* Learned how to organize website assets and control access to stored objects.
* Became familiar with Block Public Access, bucket policies, versioning, and encryption.
* Understood how lifecycle rules and storage classes can help manage storage retention and cost.
