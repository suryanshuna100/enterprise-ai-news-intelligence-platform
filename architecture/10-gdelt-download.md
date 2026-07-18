# GDELT Download Architecture

**Document Status:** 🟡 Architecture Design

---

# Purpose

The purpose of this document is to define how the Enterprise AI News Intelligence Platform will acquire datasets from the GDELT Project.

This document describes the structure of GDELT data publication, the download strategy, and the architectural considerations for building a reliable ingestion layer. Implementation details will be added in future releases.

---

# Dataset URL Structure

GDELT publishes datasets using a predictable URL structure that allows automated retrieval of newly available files.

The platform will use this structured URL pattern to identify and download the latest datasets without manual intervention.

The exact URL construction logic will be implemented during the ingestion phase.

---

# Update Frequency

The GDELT Project publishes new datasets every **15 minutes**.

This regular publication schedule makes GDELT well suited for batch-based ingestion, where the platform periodically checks for newly available data.

The ingestion schedule will later be automated using a workflow orchestration tool.

---

# File Naming Convention

Each GDELT dataset follows a timestamp-based naming convention.

The filename identifies:

- Date
- Time
- Dataset type
- Compression format

This predictable naming strategy allows the platform to determine which datasets have already been processed and which are newly available.

The filename will later be used for tracking ingestion history and supporting idempotent processing.

---

# Compression Format

GDELT datasets are distributed as compressed ZIP archives.

Compression provides several advantages:

- Faster downloads
- Reduced storage requirements
- Lower network bandwidth usage
- Efficient transfer of large datasets

After downloading, the platform will extract and validate the dataset before further processing.

---

# Download Workflow

The platform will follow a pull-based ingestion strategy.

```
GDELT Dataset

        │
        ▼

Locate Latest Dataset

        │
        ▼

Download Dataset

        │
        ▼

Validate Download

        │
        ▼

Store Raw Dataset

        │
        ▼

Generate Metadata

        │
        ▼

Record Execution Logs
```

Each stage is independent and will be implemented incrementally as the platform evolves.

---

# Open Decisions

The following implementation decisions will be finalized in future releases:

- Python download implementation
- HTTP request library selection
- Retry strategy
- Download timeout configuration
- File validation rules
- Metadata schema
- Logging framework
- Error recovery strategy
- Scheduling mechanism (Airflow)
- Cloud storage integration (AWS S3 Bronze Layer)

---

# Related Documents

- 02-business-problem.md
- 03-platform-vision.md
- 05-architecture-principles.md
- 06-medallion-architecture.md
- 07-bronze-layer.md
- 08-storage-layout.md
- 09-data-ingestion.md
- ADR-001: Why GDELT?