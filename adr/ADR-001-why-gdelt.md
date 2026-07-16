# ADR-001: Why GDELT as the Primary Data Source?

## Status

Accepted

Proposed
## Context

The objective of this project is to build a production-grade Enterprise Data Platform capable of processing large-scale datasets using modern Data Engineering technologies such as Python, Apache Spark, Delta Lake, Apache Airflow, AWS S3, Snowflake, and Power BI.

A suitable dataset should:

- Continuously generate new data.
- Scale from gigabytes to terabytes.
- Represent real-world business scenarios.
- Support incremental ingestion.
- Contain structured and semi-structured information.
- Be freely available for learning and experimentation.
- Enable future AI use cases such as semantic search, embeddings, and Retrieval-Augmented Generation (RAG).


## Decision

GDELT (Global Database of Events, Language, and Tone) has been selected as the primary data source for the platform.

The implementation will begin with the **Events** dataset to establish a reliable data ingestion and lakehouse architecture.

As the platform evolves, **Mentions** and **Global Knowledge Graph (GKG)** datasets will be integrated to enrich the analytics and AI capabilities.

## Alternatives Considered

### 1. Kaggle Datasets

**Pros**
- Easy to download.
- Good for learning SQL and analytics.

**Cons**
- Static datasets.
- No incremental updates.
- Limited scalability.
- Do not represent production data pipelines.

**Decision:** Rejected.


### 2. Public APIs (Weather, Finance, etc.)

**Pros**
- Simple ingestion.
- Real-time updates.

**Cons**
- Small data volume.
- API rate limits.
- Difficult to demonstrate distributed processing.

**Decision:** Rejected.

---

### 3. GDELT

**Pros**
- Continuously updated every 15 minutes.
- Large historical archive.
- Multiple related datasets (Events, Mentions, GKG).
- Ideal for Medallion Architecture.
- Supports batch processing and future AI enrichment.
- Suitable for Spark, Delta Lake, and Data Lake concepts.
- Free and publicly available.

**Cons**
- Steeper learning curve.
- Larger storage requirements.
- Requires understanding of multiple schemas.

**Decision:** Accepted.


## Consequences

### Positive

- Demonstrates enterprise-scale Data Engineering.
- Justifies the use of Apache Spark.
- Enables implementation of Medallion Architecture.
- Supports incremental ingestion.
- Provides realistic data modeling scenarios.
- Can be extended with AI enrichment, embeddings, and semantic search.

### Negative

- More complex than beginner datasets.
- Requires careful schema management.
- Longer implementation time.
- Larger compute and storage requirements.


## Future Considerations

The platform will evolve incrementally:

- Release v1.0 — Events
- Release v1.1 — Events + Mentions
- Release v2.0 — Events + Mentions + GKG
- Release v3.0 — AI Enablement (Embeddings, Vector Search, RAG)

This phased approach allows the platform to grow in complexity while keeping each implementation milestone manageable.