---
title: "Week 7 Worklog"
date: 2026-10-26
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:

* Explore location-based services that can support nearby ingredient-store discovery.
* Understand how location input, geocoding, and permission handling work in a web application.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Explore Amazon Location Service and its main capabilities, including Maps, Places, Routes, and Geofences.<br>- Identify the Places capability as relevant to searching for nearby stores.<br>- Review the service's general use cases. | 10/26/2026 | 10/26/2026 | [What is Amazon Location Service?](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html) |
| 2 | - Study place search and text-based place discovery.<br>- Understand the difference between searching by a free-text query and searching by a place category.<br>- Consider how a user might search for markets, grocery stores, or ingredient shops. | 10/27/2026 | 10/27/2026 | [Amazon Location Places](https://docs.aws.amazon.com/location/latest/developerguide/places.html) |
| 3 | - Learn about nearby-place search using geographic coordinates.<br>- Review how a search position and geographic area affect returned results.<br>- Consider how the application could present multiple nearby locations to a user. | 10/28/2026 | 10/28/2026 | [Search Nearby](https://docs.aws.amazon.com/location/latest/developerguide/search-nearby.html) |
| 4 | - Study geocoding and reverse geocoding.<br>- Understand how a typed address can be converted into coordinates and how coordinates can be converted into a readable address.<br>- Review why address input can be a fallback when GPS is unavailable. | 10/29/2026 | 10/29/2026 | [Geocoding](https://docs.aws.amazon.com/location/latest/developerguide/geocoding.html) |
| 5 | - Explore the browser Geolocation API and its permission model.<br>- Understand the requirements for requesting a user's location and how to handle permission denial or unavailable position data.<br>- Consider a manual-address alternative for users who do not share GPS location. | 10/30/2026 | 10/30/2026 | [MDN Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) |
| 6 | - Review security considerations for Amazon Location Service.<br>- Understand why sensitive credentials should remain on the backend and why a Lambda execution role is preferable to embedding credentials in frontend code.<br>- Review the permissions required for location search operations. | 10/31/2026 | 10/31/2026 | [Amazon Location Security](https://docs.aws.amazon.com/location/latest/developerguide/security.html) |

### Week 7 Achievements:

* Understood the main capabilities of Amazon Location Service and the role of Places in place discovery.
* Learned the difference between text search, nearby search, and geocoding.
* Understood how browser location permissions work and why a manual-address fallback is useful.
* Recognized the security requirements for calling location services from a backend application.
