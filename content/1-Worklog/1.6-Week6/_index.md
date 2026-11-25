---
title: "Week 6 Worklog"
date: 2026-10-19
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:

* Understand the NoSQL data model and how to organize data around application access patterns.
* Learn the basic DynamoDB operations and how a backend service can retrieve data efficiently.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Study Amazon DynamoDB concepts, including tables, items, and attributes.<br>- Compare a key-value/document database with a relational database.<br>- Identify data that could be stored as recipe records. | 10/19/2026 | 10/19/2026 | [DynamoDB Introduction](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) |
| 2 | - Learn about partition keys and sort keys.<br>- Understand how primary-key design affects data distribution and retrieval.<br>- Consider possible keys for identifying recipes and grouping related records. | 10/20/2026 | 10/20/2026 | [Core Components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html) |
| 3 | - Review PutItem, GetItem, UpdateItem, and DeleteItem operations.<br>- Understand how JSON-like attributes are represented in DynamoDB items.<br>- Explore how recipe names, ingredients, and instructions could be stored. | 10/21/2026 | 10/21/2026 | [Working with Items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html) |
| 4 | - Compare Query and Scan operations.<br>- Understand why Query is generally preferable when the partition key is known.<br>- Review the impact of reading unnecessary records on performance and cost. | 10/22/2026 | 10/22/2026 | [Querying Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) |
| 5 | - Study Global Secondary Indexes (GSI) and Local Secondary Indexes (LSI).<br>- Learn when an index is useful for querying by an attribute other than the table's primary key.<br>- Review the additional storage and write considerations of indexes. | 10/23/2026 | 10/23/2026 | [Secondary Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html) |
| 6 | - Explore how Python applications access DynamoDB through Boto3.<br>- Review IAM permissions required by an application to read and write table items.<br>- Learn about pagination and basic exception handling when retrieving records. | 10/24/2026 | 10/24/2026 | [DynamoDB with Python](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html) |

### Week 6 Achievements:

* Understood DynamoDB tables, items, attributes, and primary-key concepts.
* Learned how partition keys and sort keys support efficient data access.
* Distinguished common CRUD operations and the Query/Scan access patterns.
* Understood the purpose of secondary indexes and the considerations involved in using them.
* Became familiar with accessing DynamoDB from Python through Boto3 and granting permissions through IAM roles.
