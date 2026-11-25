---
title: "Week 6 Worklog"
date: 2026-10-19
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:

* Understand NoSQL databases and the key-value/document data model used by Amazon DynamoDB.
* Learn how to design partition keys, sort keys, and secondary indexes around application access patterns.
* Explore basic data operations and capacity modes for a small web application.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Compare relational databases and NoSQL databases.<br>- Understand tables, items, attributes, and primary keys in DynamoDB.<br>- Review use cases where a flexible schema is useful for application data such as recipes. | 10/19/2026 | 10/19/2026 | [What Is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) |
| 2 | - Study partition keys and sort keys and understand how DynamoDB distributes data.<br>- Learn why a suitable partition key is important for balanced access patterns.<br>- Draft example key structures for recipe records and recipe categories as a data-modeling exercise. | 10/20/2026 | 10/20/2026 | [DynamoDB Core Components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html) |
| 3 | - Learn basic DynamoDB operations, including PutItem, GetItem, UpdateItem, and DeleteItem.<br>- Compare Query and Scan and understand why Query is generally preferred when the key is known.<br>- Review how filtering and projections affect returned data. | 10/21/2026 | 10/21/2026 | [Working with Items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html)<br>[Query and Scan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) |
| 4 | - Study secondary indexes and the purpose of a Global Secondary Index (GSI).<br>- Understand how an index can support an access pattern not covered by the table's primary key.<br>- Consider possible search patterns such as retrieving recipes by category. | 10/22/2026 | 10/22/2026 | [DynamoDB Secondary Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html) |
| 5 | - Compare DynamoDB on-demand and provisioned capacity modes.<br>- Learn the meaning of read request units and write request units at a basic level.<br>- Review how workload patterns and traffic uncertainty influence capacity selection. | 10/23/2026 | 10/23/2026 | [Read/Write Capacity Modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)<br>[DynamoDB Pricing](https://aws.amazon.com/dynamodb/pricing/) |
| 6 | - Explore DynamoDB Time to Live (TTL) and its use for expiring temporary records.<br>- Review backup and point-in-time recovery options for protecting application data.<br>- Summarize data-modeling considerations for recipe records and future application features. | 10/24/2026 | 10/24/2026 | [DynamoDB TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html)<br>[DynamoDB Backup and Restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html) |

### Week 6 Achievements:

* Understood the differences between relational and NoSQL databases.
* Learned DynamoDB tables, items, attributes, partition keys, and sort keys.
* Became familiar with common item operations and the difference between Query and Scan.
* Understood how secondary indexes support additional data access patterns.
* Learned the differences between on-demand and provisioned capacity and reviewed data protection options.
