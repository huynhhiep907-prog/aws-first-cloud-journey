---
title: "Week 7 Worklog"
date: 2026-10-26
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:

* Understand how APIs allow a frontend application to communicate with backend services.
* Learn the main concepts of Amazon API Gateway and its integration with AWS Lambda.
* Review HTTP methods, request formats, CORS, and API security.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Review the client-server model and the role of an API between a browser and backend logic.<br>- Understand endpoints, resources, methods, requests, and responses.<br>- Identify API operations that a recipe discovery application may need. | 10/26/2026 | 10/26/2026 | [Amazon API Gateway User Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) |
| 2 | - Study REST API concepts and common HTTP methods: GET, POST, PUT, PATCH, and DELETE.<br>- Understand path parameters, query-string parameters, and request bodies.<br>- Review suitable methods for read and update operations. | 10/27/2026 | 10/27/2026 | [HTTP Request Methods – MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)<br>[API Gateway Concepts](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html) |
| 3 | - Learn the basic components of an API Gateway HTTP API.<br>- Explore routes, integrations, stages, and deployment concepts.<br>- Compare HTTP APIs and REST APIs at a high level. | 10/28/2026 | 10/28/2026 | [Choosing an API Gateway API Type](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)<br>[HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html) |
| 4 | - Study how API Gateway invokes a Lambda function through an integration.<br>- Understand the structure of an incoming event and the response returned by the function.<br>- Review how query parameters can be passed to backend logic for filtering or searching. | 10/29/2026 | 10/29/2026 | [Lambda Proxy Integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html) |
| 5 | - Learn what Cross-Origin Resource Sharing (CORS) is and why browsers enforce it.<br>- Review how allowed origins, methods, and headers affect frontend-to-API requests.<br>- Identify common CORS configuration mistakes. | 10/30/2026 | 10/30/2026 | [CORS for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html)<br>[MDN – CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) |
| 6 | - Review API authentication and authorization options at a high level.<br>- Learn the purpose of throttling, request validation, and access logging.<br>- Study common API response codes and distinguish client errors from backend errors. | 10/31/2026 | 10/31/2026 | [API Gateway Security](https://docs.aws.amazon.com/apigateway/latest/developerguide/security.html)<br>[API Gateway Monitoring](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring-cloudwatch.html) |

### Week 7 Achievements:

* Understood how APIs connect frontend requests with backend application logic.
* Learned common HTTP methods and the roles of path parameters, query parameters, and request bodies.
* Became familiar with API Gateway routes, integrations, stages, and API types.
* Understood how API Gateway can invoke Lambda and pass request data to a function.
* Learned the purpose of CORS, throttling, logging, and basic API security controls.
