---
title: "Week 5 Worklog"
date: 2026-10-12
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:

* Understand how a Content Delivery Network improves delivery of static web content.
* Learn CloudFront distributions, origins, cache behaviors, and invalidation.
* Review DNS, HTTPS, and HTTP concepts needed to publish and troubleshoot a website.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Study the purpose of a CDN and how edge locations reduce latency.<br>- Understand the difference between an origin server and a cache location.<br>- Identify assets suitable for caching, such as CSS, JavaScript, and recipe images. | 10/12/2026 | 10/12/2026 | [What is a CDN?](https://aws.amazon.com/what-is/cdn/) |
| 2 | - Learn the main components of a CloudFront distribution.<br>- Understand origins, origin paths, default root objects, and distribution domain names.<br>- Review how CloudFront retrieves static content from an S3 origin. | 10/13/2026 | 10/13/2026 | [How CloudFront Works](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) |
| 3 | - Study CloudFront cache behaviors and path patterns.<br>- Learn how cache policies control TTL values and which request parameters are included in the cache key.<br>- Consider different caching needs for images, scripts, and frequently changing files. | 10/14/2026 | 10/14/2026 | [Cache Behaviors](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesCacheBehavior.html)<br>[Cache Policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html) |
| 4 | - Learn how CloudFront invalidation works after website files are updated.<br>- Compare invalidation with using versioned filenames for static assets.<br>- Review common causes of users seeing an older cached page. | 10/15/2026 | 10/15/2026 | [Invalidating Files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) |
| 5 | - Review DNS concepts, including domain names, DNS records, and name resolution.<br>- Understand how a domain name can point to a CloudFront distribution.<br>- Study HTTPS and TLS certificates when publishing a website. | 10/16/2026 | 10/16/2026 | [Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)<br>[AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) |
| 6 | - Study common HTTP response status codes, including 200, 301, 403, 404, and 5xx responses.<br>- Learn the difference between browser-side errors, origin errors, and permission-related errors.<br>- Prepare a troubleshooting checklist for a static website delivered through CloudFront. | 10/17/2026 | 10/17/2026 | [HTTP Semantics – RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)<br>[CloudFront Troubleshooting](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting-response-errors.html) |

### Week 5 Achievements:

* Understood the role of a CDN and how CloudFront uses edge locations to deliver static content.
* Learned the relationship between an S3 origin and a CloudFront distribution.
* Became familiar with cache behaviors, cache policies, TTL values, and invalidation.
* Reviewed DNS, HTTPS, and TLS concepts required for publishing a website.
* Developed a basic approach to diagnosing common website delivery and HTTP errors.
