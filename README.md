# Webinar Series

This repository contains the final code from our webinar series.

## Episode 1: Ingesting Test Data

### Join us for a masterclass in ingesting test data

**Tuesday, July 22nd | 9:30am EST / 2:30pm GMT / 3:30pm CET**

[Register here](#)

Modern electro-mechanical systems generate massive amounts of test data from diverse sources. Your test rigs might output CSV files to local file systems, stream real-time data through PLCs and LabView, or transmit telemetry via MQTT protocols. Whether you're testing drone flight controllers, automotive battery systems, or HVAC performance, the challenge remains the same: how do you reliably ingest, process, and store heterogeneous data from your test facilities?

## What you'll learn in 45 minutes

### Whiteboard session: Connecting to diverse industrial data sources
- Practical approaches for ingesting data from OPC-UA, MQTT, HTTP APIs, and file systems
- Why cloud processing outperforms edge processing for R&D workflows
- Architectures that prevent data loss during connectivity outages using Kafka buffering and stateful edge services

### Live coding demonstration
- Building MQTT and OPC-UA connectors for real-time data ingestion
- Implementing downsampling techniques for high-frequency sensor data
- Configuring data pipelines that handle TB-scale datasets from test campaigns

## Why this matters for your R&D organization

Senior R&D leaders face mounting pressure to accelerate design-validation cycles while maintaining compliance audit trails. Your teams are struggling with desktop-based workflows that limit collaboration and create knowledge silos. Manual data handling processes introduce human error and create bottlenecks at critical verification test rigs.

Software engineers on digitization teams know the technical challenges: you're tasked with integrating data from legacy systems, proprietary formats, and real-time streams, but you lack the resources and data engineering expertise to build robust solutions. Your IT infrastructure constraints slow down development, and service restarts disrupt ongoing test campaigns.

## Real-world impact

Companies using centralized data ingestion architectures report 40% faster root cause analysis and 60% reduction in time spent searching for historical test data. By moving from desktop-based file exchanges to cloud-native data pipelines, R&D teams can reuse configuration metadata across test programs and maintain complete audit trails for regulatory compliance.

## Episode 2: Test Data Normalisation

### A masterclass in test data normalisation using Python

**Monday, August 5th | 9:30am EST / 2:30pm BST / 3:30pm CET**

Join us as we first talk about then demonstrate why and how to consolidate test data, in all its formats, into a standardized schema.

We'll cover:

- Data sources, types and frequencies of data.
- Why data needs to be standardized.
- How to choose a transport protocol.
- Schema validation.
- How to normalize and synchronize time-series test data.

## Episode 3: Master class in test data schema preparation for analytics

Join us for this masterclass on preparing test data for advanced analytics and AI. This session continues from our previous webinars on Python-based data ingestion and normalization. This time we'll deep-dive into how to design data analytics-ready data schemas.

Here's where many R&D teams hit a wall: you've successfully normalized your drone telemetry, battery test results, and HVAC performance data into consistent formats. But when your engineers try to run analytics, queries take forever, visualizations break, and AI models can't find the patterns they need. The result - your Engineers spend more time fixing data schemas than actually analyzing test results.

We'll cover practical approaches for designing analytical schemas that support specific analytics use cases. You'll learn how to structure time-series data for fast querying, preserve engineering metadata that AI needs, and optimize data types for dramatically improved query performance. The session includes real examples of analytical schema design for comparative analysis across test campaigns, automated anomaly detection, and predictive modeling for design optimization.