---
title: "Week 8 Worklog"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives:

* Understand the NoSQL data model and how Amazon DynamoDB stores application data.
* Learn how to design keys and organize data around application access patterns.
* Explore how a backend service can access DynamoDB securely and efficiently.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Study Amazon DynamoDB concepts, including tables, items, and attributes.<br>- Compare a key-value/document database with a relational database.<br>- Identify data that could be stored as recipe records. | 11/02/2026 | 11/02/2026 | [DynamoDB Introduction](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) |
| 2 | - Learn about partition keys and sort keys.<br>- Understand how primary-key design affects data distribution and retrieval.<br>- Consider possible keys for identifying recipes and grouping related records. | 11/03/2026 | 11/03/2026 | [DynamoDB Core Components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html) |
| 3 | - Review PutItem, GetItem, UpdateItem, and DeleteItem operations.<br>- Understand how structured attributes are represented in DynamoDB items.<br>- Explore how recipe names, ingredients, and instructions could be stored. | 11/04/2026 | 11/04/2026 | [Working with Items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html) |
| 4 | - Compare Query and Scan operations.<br>- Understand why Query is generally preferable when the partition key is known.<br>- Review the impact of reading unnecessary records on performance and cost. | 11/05/2026 | 11/05/2026 | [Querying Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) |
| 5 | - Study Global Secondary Indexes (GSI) and Local Secondary Indexes (LSI).<br>- Learn when an index is useful for querying by an attribute other than the table's primary key.<br>- Review the additional storage and write considerations of indexes. | 11/06/2026 | 11/06/2026 | [Secondary Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html) |
| 6 | - Explore how Python applications access DynamoDB through Boto3.<br>- Review IAM permissions required by an application to read and write table items.<br>- Learn about pagination and basic exception handling when retrieving records. | 11/07/2026 | 11/07/2026 | [DynamoDB with Python](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html)<br>[Boto3 DynamoDB Guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html) |

### Week 8 Achievements:

* Understood DynamoDB tables, items, attributes, and primary-key concepts.
* Learned how partition keys and sort keys support efficient data access.
* Distinguished common CRUD operations and the Query/Scan access patterns.
* Understood the purpose of secondary indexes and the considerations involved in using them.
* Became familiar with accessing DynamoDB from Python through Boto3 and granting permissions through IAM roles.
