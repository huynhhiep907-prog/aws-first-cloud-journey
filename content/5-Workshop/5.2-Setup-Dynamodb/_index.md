---
title: "Create the DynamoDB Database"
date: 2026-11-27
weight: 2
chapter: false
pre: "<b>5.2. </b>"
---

#### Procedure

1. Open the **AWS Management Console**, search for **DynamoDB**, and choose **Create table**.
2. Enter the table configuration:
   * **Table name:** `RecipesTable`
   * **Partition key:** `RecipeID` (Kiểu dữ liệu: `String`)
   * **Table settings:** Select **Default settings** (On-demand capacity mode).
3. Choose **Create table** and wait until the table status changes to **Active**.
4. Open `RecipesTable` → **Explore table items** → **Create item** to add sample data with the following attributes: `RecipeID`, `Name`, `Category`, `Ingredients`, `EstimatedCostVND`, `CookingTimeMinutes`, `MoodTags`, `DietTags`, `CookingSteps`.

![anh2](anh2.png)

![anh3](anh3.png)
