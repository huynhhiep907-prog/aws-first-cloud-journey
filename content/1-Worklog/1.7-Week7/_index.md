---
title: "Week 7 Worklog"
date: 2026-10-26
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:

* Understand location-based application features and the role of geospatial data.
* Explore Amazon Location Service capabilities for searching places and working with coordinates.
* Learn how to handle location permissions, search parameters, and service costs responsibly.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Review latitude and longitude and understand how geographic coordinates represent a position on Earth.<br>- Learn the difference between a device location and a manually entered search location.<br>- Consider location-based use cases such as finding markets or grocery stores near a user. | 10/26/2026 | 10/26/2026 | [Geolocation API – MDN](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) |
| 2 | - Explore Amazon Location Service and its main capabilities, including Maps, Places, Routes, and Trackers.<br>- Identify which capability is appropriate for searching nearby businesses and places.<br>- Review the concept of a place index as a resource for place search. | 10/27/2026 | 10/27/2026 | [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html)<br>[Places](https://docs.aws.amazon.com/location/latest/developerguide/places.html) |
| 3 | - Study place search operations and the difference between searching by text and searching near coordinates.<br>- Review search filters, result limits, and relevance of returned place information.<br>- Consider how a user-entered address can be converted into a location for nearby search. | 10/28/2026 | 10/28/2026 | [Searching for Places](https://docs.aws.amazon.com/location/latest/developerguide/searching-for-places.html) |
| 4 | - Learn the browser Geolocation API workflow.<br>- Review permission prompts, success and error callbacks, and accuracy information.<br>- Understand why a website should provide manual address input when a user denies location permission. | 10/29/2026 | 10/29/2026 | [Geolocation getCurrentPosition](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) |
| 5 | - Study how location search results can be presented with distance and useful place details.<br>- Review coordinate-based distance calculations and the limitations of straight-line distance compared with actual travel distance.<br>- Consider how to communicate uncertain or incomplete place information to users. | 10/30/2026 | 10/30/2026 | [Amazon Location SearchNearby API](https://docs.aws.amazon.com/location/latest/APIReference/API_SearchNearby.html)<br>[Amazon Location Routes](https://docs.aws.amazon.com/location/latest/developerguide/routes.html) |
| 6 | - Review Amazon Location Service pricing dimensions and request-based usage.<br>- Learn why request volume, selected data provider, and feature usage should be considered when estimating costs.<br>- Summarize error handling and fallback behavior for location search when permission or service requests fail. | 10/31/2026 | 10/31/2026 | [Amazon Location Pricing](https://aws.amazon.com/location/pricing/)<br>[Amazon Location Quotas](https://docs.aws.amazon.com/location/latest/developerguide/location-quotas.html) |

### Week 7 Achievements:

* Understood geographic coordinates and common location-based application scenarios.
* Learned the role of Amazon Location Service Places for searching nearby locations.
* Became familiar with text-based and coordinate-based place search.
* Understood browser location permissions and why manual address entry is a useful fallback.
* Reviewed location result presentation, distance limitations, service quotas, and pricing considerations.
