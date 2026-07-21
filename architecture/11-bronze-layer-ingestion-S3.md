# Architecture Decision: Bronze Layer

**Document ID:** ARCH-011  
**Title:** AWS Bronze Layer Architecture  
**Version:** v0.4.0  
**Status:** Approved  
**Author:** Suryanshu Singh  
**Date:** July 2026

---

# 1. Purpose

The Bronze Layer is the first persistent storage layer of the Enterprise AI News Intelligence Platform (EANIP).

Its primary responsibility is to ingest raw data from external sources and store it in Amazon S3 exactly as received, without any transformations.

The Bronze Layer serves as the immutable source of truth for downstream processing.

---

# 2. Business Problem

Enterprise data platforms continuously ingest data from multiple external providers.

These datasets are often:

- Large
- Continuously updated
- Unstructured or semi-structured
- Needed for historical replay
- Required for auditing and compliance

Without a dedicated raw storage layer:

- Original data may be lost
- Data lineage becomes difficult
- Failed processing cannot be replayed
- Debugging becomes significantly harder

The platform therefore requires a durable, scalable, and cost-effective storage layer that preserves raw data exactly as received.

---

# 3. Why Amazon S3?

Amazon S3 was selected because it provides enterprise-grade object storage with virtually unlimited scalability.

Benefits include:

- Highly durable (11 nines durability)
- Virtually unlimited storage
- Low storage cost
- Native integration with Spark
- Native integration with Databricks
- Native integration with AWS services
- Supports large-scale analytical workloads

S3 has become the industry standard storage layer for modern data lakes.

---

# 4. Bronze Layer Responsibilities

The Bronze Layer is responsible for:

- Receiving raw datasets from external sources
- Preserving original files without modification
- Maintaining immutable storage
- Recording ingestion metadata
- Supporting historical replay
- Providing reliable input for Silver processing

The Bronze Layer does **not**:

- Clean data
- Validate business rules
- Remove duplicates
- Transform schemas
- Aggregate records

Those responsibilities belong to downstream layers.

---

# 5. Streaming Ingestion Architecture

Instead of downloading files to local storage, EANIP streams datasets directly into Amazon S3.

Benefits include:

- Eliminates unnecessary disk I/O
- Reduces infrastructure requirements
- Improves scalability
- Simplifies deployment on EC2, ECS, Kubernetes, and Lambda
- Better aligns with cloud-native architectures

High-level workflow:

```
             GDELT
               │
       HTTP Streaming Download
               │
               ▼
        Amazon S3 Bronze
               │
        ├── Raw ZIP
        └── metadata.json
```

The ingestion service does not permanently store downloaded files on the local filesystem.

---

# 6. Why Streaming?

Traditional pipelines often follow:

```
API
 │
 ▼
Local File
 │
 ▼
Amazon S3
```

This approach introduces:

- Additional disk writes
- Extra storage usage
- Slower ingestion
- More infrastructure dependencies

```
EANIP instead uses:

              lastupdate.txt
                     │
                     ▼
      Resolve Latest Dataset URL
                     │
                     ▼
        Download HTTP Stream
                     │
                     ▼
       Stream Upload to Amazon S3
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
Original ZIP             metadata.json
                     │
                     ▼
                  Spark
                     │
                     ▼
                Silver Layer
```

Advantages:

- Lower latency
- Reduced storage requirements
- Cloud-native architecture
- Easier horizontal scaling

---

# 7. Bronze Storage Layout

The Bronze Layer follows a partitioned layout.

```
s3://enterprise-ai-news/

bronze/

    gdelt/

        ingestion_date=YYYY-MM-DD/

            ingestion_time=HHMMSS/

                20260721001500.export.CSV.zip

                metadata.json
```

Partitioning by ingestion timestamp provides:

- Efficient historical replay
- Easier operational debugging
- Simplified lifecycle management
- Better Spark partition pruning

---

# 8. Object Storage

Unlike traditional file systems, Amazon S3 stores objects.

Each object consists of:

- Object Key
- Object Data
- Object Metadata

Example:

```
Object Key

bronze/gdelt/
ingestion_date=2026-07-19/
ingestion_time=103015/
gdelt_export.zip
```

Directories shown in the AWS Console are logical prefixes rather than physical folders.

---

# 9. Metadata Strategy

Each ingested dataset is accompanied by a metadata file.

```
metadata.json
```

Example contents:

- Dataset URL
- Ingestion Timestamp
- HTTP Status
- File Size
- Content Type
- Ingestion Status
- Checksum (future enhancement)

Keeping metadata separate from the raw dataset preserves immutability while enabling operational monitoring.

---

# 10. Immutability

Files stored in the Bronze Layer are never modified.

If a dataset changes upstream, a new object is written instead of overwriting the existing one.

Benefits include:

- Complete audit trail
- Historical reproducibility
- Replay capability
- Reliable debugging

---

# 11. Historical Backfill

The Bronze Layer supports two ingestion modes.

## Incremental Ingestion

New datasets are ingested as they become available.

```
Latest Dataset

↓

Bronze
```

## Historical Backfill

Previously published datasets can be ingested using the same storage layout.

```
Historical Dataset

↓

Bronze
```

Both ingestion modes produce identical Bronze structures.

---

# 12. Integration with Spark

Spark reads directly from Amazon S3.

```
Amazon S3 Bronze

↓

Spark

↓

Silver Layer
```

Because Bronze preserves raw files, downstream jobs can always be re-executed without re-downloading source data.

---

# 13. Future Enhancements

Future releases may introduce:

- Multipart uploads
- Server-side encryption (SSE-KMS)
- Object versioning
- Lifecycle policies
- Intelligent Tiering
- Automatic checksum validation
- Parallel ingestion
- Compression validation

---

# 14. Benefits

This architecture provides:

- Cloud-native ingestion
- Highly durable storage
- Immutable raw data
- Historical replay
- Enterprise scalability
- Low operational cost
- Native Spark compatibility
- Clear separation between Bronze and Silver layers

---

# 15. Architecture Summary

```
                   GDELT
                     │
          HTTP Streaming Download
                     │
                     ▼
              Amazon S3 Bronze
                     │
       ┌─────────────┴─────────────┐
       │                           │
       ▼                           ▼
 gdelt_export.zip             metadata.json
                     │
                     ▼
                  PySpark
                     │
                     ▼
               Silver Layer
                     │
                     ▼
                Gold Layer
```

# 16. Module Reponsibilities

run_ingestion.py
    │
    │  Orchestrates workflow
    ▼

gdelt_client.py
    │
    │  Downloads HTTP streams
    ▼

gdelt_urls.py
    │
    │  Builds GDELT URLs
    ▼

metadata.py
    │
    │  Creates metadata.json
    ▼

s3_storage.py
    │
    │  Uploads streams and metadata
    ▼

Amazon S3
---

# Key Design Decisions

| Decision | Rationale |
|-----------|-----------|
| Amazon S3 | Durable, scalable object storage |
| Streaming ingestion | Eliminates unnecessary local storage |
| Immutable raw data | Supports replay and auditing |
| Partition by ingestion time | Efficient organization and querying |
| Metadata alongside raw data | Operational observability |
| Separate Bronze layer | Preserves original datasets |