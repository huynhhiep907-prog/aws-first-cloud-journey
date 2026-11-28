---
title: "Configure Amazon API Gateway"
date: 2026-11-27
weight: 5
chapter: false
pre: "<b>5.5. </b>"
---

#### Procedure

1. Go to **API Gateway → Create API → HTTP API → Build**.
2. Choose **Add integration** → select **Lambda** → point to `RecipeSearchFunction` and name the API `BepThongMinhAPI`.

![lambda](lambda.png)

3. Create three **routes**, all integrated with `RecipeSearchFunction`:
   * `GET /search`
   * `GET /nearby-stores`
   * `POST /chat`

![routes](routes.png)

4. Name the stage `prod` and complete the setup.

![prod](prod.png)

5. Open the API's **CORS** section and configure:
   * **Access-Control-Allow-Origin:** `*`
   * **Access-Control-Allow-Methods:** `GET, POST, OPTIONS`
   * **Access-Control-Allow-Headers:** `Content-Type, Authorization`

![cors](cors.png)

6. Save the **Invoke URL** (`https://1f10tq33a6.execute-api.ap-southeast-1.amazonaws.com/prod`) and assign it to the `API_BASE` variable in the frontend.
