# Medallion Architecture

## Overview

The Enterprise AI News Intelligence Platform follows the Medallion Architecture pattern to progressively improve data quality and prepare trusted datasets for analytics and future AI applications.

The architecture separates data into three logical layers—Bronze, Silver, and Gold—allowing raw data to be preserved while enabling reliable transformations and business-ready data products.

This layered approach improves data quality, scalability, maintainability, and supports incremental data processing.

---

# Bronze Layer

## Business Purpose

The Bronze layer acts as the landing zone for all raw GDELT data received from the source.

Its primary objective is to preserve the original dataset exactly as it was received without applying any business transformations.

Keeping an immutable copy of the source data enables auditing, debugging, reproducibility, and recovery if downstream processing fails.

## Design Decision

The platform will store historical and future incremental GDELT files in AWS S3 using a partitioned folder structure.

Only minimal technical metadata, such as ingestion timestamp and source information, will be added.

Business logic will not be applied at this stage.

## Benefits

- Preserves raw source data
- Enables data replay and recovery
- Simplifies debugging
- Provides a single source of truth for ingestion

## Implementation Status

🚧 Planned for Release v1.0

---

# Silver Layer

## Business Purpose

The Silver layer transforms raw data into clean, validated, and standardized datasets suitable for downstream processing.

This layer improves data quality while maintaining detailed event-level information.

## Design Decision

Spark will perform data cleansing, schema validation, data type standardization, null handling, and deduplication before writing the refined datasets into Delta Lake.

This layer will also prepare the data for dimensional modeling.

## Benefits

- Improves data quality
- Standardizes schemas
- Removes duplicate records
- Creates trusted operational datasets

## Implementation Status

🚧 Planned for Release v1.0

---

# Gold Layer

## Business Purpose

The Gold layer provides curated, business-ready datasets optimized for analytics and reporting.

These datasets will power dashboards, business intelligence reports, and future AI services.

## Design Decision

Business-oriented tables, including fact and dimension models, will be created from the Silver layer.

Only trusted and validated data will be promoted into Gold.

The Gold layer will serve as the primary data source for Snowflake and Power BI.

## Benefits

- Optimized for business analytics
- Supports dimensional modeling
- Improves dashboard performance
- Provides governed enterprise data

## Implementation Status

🚧 Planned for Release v1.0

---

# Incremental Processing

## Business Purpose

The platform should process only newly available data instead of reprocessing the complete historical dataset during every execution.

This reduces execution time, compute cost, and improves scalability.

## Design Decision

The project will initially perform a historical data load to establish the platform.

Subsequent executions will ingest only newly published GDELT files, enabling incremental processing.

The orchestration workflow will later be managed by Apache Airflow.

## Benefits

- Faster pipeline execution
- Lower compute costs
- Better scalability
- Suitable for continuously growing datasets

## Implementation Status

🚧 Planned for Release v1.1

---

# Schema Evolution

## Business Purpose

External datasets may evolve over time as new fields are introduced or existing fields change.

The platform must be capable of adapting without requiring complete redesigns.

## Design Decision

Delta Lake will be used to support controlled schema evolution while preserving historical data.

Schema changes will be validated before promotion into downstream layers.

## Benefits

- Handles evolving datasets
- Reduces maintenance effort
- Protects downstream consumers
- Supports long-term platform evolution

## Implementation Status

🚧 Planned for Release v1.1

---

# Partition Strategy

## Business Purpose

Efficient partitioning improves query performance and reduces unnecessary data scanning.

As data volume increases, partitioning becomes essential for scalable distributed processing.

## Design Decision

The initial partitioning strategy will be based on ingestion date to simplify incremental loading and operational management.

Additional partitioning strategies based on event date or business requirements may be introduced as the platform evolves.

## Benefits

- Faster query performance
- Reduced storage scanning
- Improved Spark processing efficiency
- Better scalability for large datasets

## Implementation Status

🚧 Initial strategy planned for Release v1.0 and will be refined as data volume grows.

---

# Future Evolution

The Medallion Architecture will evolve throughout the project.

### Release v1.0
- Bronze Layer
- Silver Layer
- Gold Layer

### Release v2.0
- AI-assisted metadata generation
- AI-powered data quality validation
- AI enrichment

### Release v3.0
- Embedding generation
- Vector database
- RAG Business Assistant
