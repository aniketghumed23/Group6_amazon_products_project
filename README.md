# Group6_amazon_products_project


# Project: Predictive Modeling for Best-Selling Products in E-commerce

## Project Scope and Business Goal

### Project Scope

The machine learning component of this project aims to address the specific problem of accurately predicting the best-selling products in the e-commerce industry. The focus is on developing a robust predictive model using advanced data analytics techniques. This aligns with the educational program goals of AWS Academy Cloud Foundations and Data Engineering, providing hands-on experience in applying machine learning concepts to real-world scenarios.

### Domain

**E-commerce Industry:**
- **Key Characteristics:** Highly dynamic, vast product range, diverse consumer preferences, and the need for efficient inventory management.
- **Challenges:** Predicting best-selling products, optimizing inventory, and improving decision-making processes.
- **Opportunities:** Enhancing customer experience, increasing profitability, and gaining a competitive edge in the market.
- **Stakeholders:** Retailers, marketers, supply chain managers, and consumers.


## Literature Review

### 1. Predictive Modeling in E-commerce

Various studies emphasize the use of predictive models for inventory optimization and sales forecasting.

- **Source:** "Predictive Analytics of E-Commerce Search Behavior for Conversion"
- **Link:** [Predictive Analytics of E-Commerce Search Behavior for Conversion](https://core.ac.uk/download/pdf/301371722.pdf)

### 2. Customer Behavior Analysis

Understanding consumer behavior through machine learning is crucial for personalized marketing and product recommendations.

- **Source:** "A detailed behavioral analysis on consumer and customer changing behavior with respect to social networking sites research paper"
- **Link:** [A detailed behavioral analysis on consumer and customer changing behavior with respect to social networking sites research paper](https://www.sciencedirect.com/science/article/abs/pii/S0969698920306238)

### 3. Dynamic Pricing Strategies

Machine learning techniques contribute to dynamic pricing models, allowing retailers to adjust prices based on demand and competition.

- **Source:** "A Systematic Literature Review of Dynamic Pricing Strategies"
- **Link:** [A Systematic Literature Review of Dynamic Pricing Strategies](https://www.researchgate.net/publication/359158596_A_Systematic_Literature_Review_of_Dynamic_Pricing_Strategies)

### 4. Supply Chain Optimization

Predictive analytics aids in supply chain optimization, reducing costs, and improving overall efficiency.

- **Source:** "Supply Chain Design and Optimization: Challenges and Opportunities"
- **Link:** [Supply Chain Design and Optimization: Challenges and Opportunities](https://tinyurl.com/5c39f67p)

### 5. Challenges in E-commerce Analytics

Privacy concerns, ethical considerations, and the need for interpretable models are highlighted as challenges in the e-commerce analytics landscape.

- **Source:** "Identification of Benefits, Challenges, and Pathways in E-commerce Industries: An integrated two-phase decision-making model"
- **Link:** [Identification of Benefits, Challenges, and Pathways in E-commerce Industries: An integrated two-phase decision-making model](https://www.sciencedirect.com/science/article/pii/S2666412723000156)


## Data Source

### Amazon Dataset

- **Availability:** Publicly available.
- **Nature:** Comprehensive dataset comprising 1.4 million products, encompassing information on product categories, pricing, customer reviews, and historical sales data.
- **Quality:** The dataset necessitates merging, cleansing, and preparation for machine learning to ensure its relevance to the project scope.
- **Source Link:** [Amazon Products Dataset 2023 (1.4M Products) on Kaggle](https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products)


### Domain-specific Challenges

- **Privacy and Ethics:** Protecting customer privacy is paramount in e-commerce. Any predictive model must comply with data protection regulations and ethical considerations.

- **Bias in Reviews:** Addressing potential biases in customer reviews that might influence the predictive model. Ensuring fairness in recommendations and predictions.

### KPIs (Key Performance Indicators)

**Metrics of Success:**
- **Accuracy:** Overall correctness of predictions.
- **Precision:** Proportion of correctly predicted best-selling products among those predicted.
- **Recall:** Proportion of actual best-selling products correctly predicted.
- **F1-Score:** A balance between precision and recall, considering both false positives and false negatives.

Setting clear KPIs will guide the optimization process and ensure the effectiveness of the predictive model in the e-commerce domain.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PROJECT DELIVERABLE 2

## Table of Contents

*Phase 2: Machine Learning Problem Framing, Data Pre-Processing*
   - *Set Up AWS Environment*
     - Account Setup
     - Team Access to AWS Learner Lab and GitHub - Gave team access to github
     - IAM Roles Creation - used LabRole which was alread specfied

   - *S3 Data Storage*
     - Created an S3 Bucket with name amazon_products_data
     - Uploading Data to the S3 Bucket to folders amazon_products and amazon_categories

   - *Data Exploration for Insight and Pre-processing*
     - Using Amazon Athena for Querying Transformed Data - Adding data to athena table named amazon_products and amazon_categories
     - SQL Queries for Data Exploration - Wrote queries such as average price, price category
     - Visualizations using Amazon QuickSight - created visualization on the data using amazon quicksight and athena

   - *AWS Glue ETL Job*
     - Creating an ETL Job in AWS Glue - Create ETL job for Filter, Aggregate, change data type etc
     - Performing Basic Data Transformations - Done

   - *Phase 2 Deliverable*
     - Project Repository on GitHub (Updated Table of Contents)
     - Deliverable 2 Document Accessibility in GitHub (with Screenshots)

