# Enterprise AI News Intelligence Platform (EANIP)

## Tagline

A production-grade enterprise data platform for AI-powered news intelligence.

---

## Vision

Build a scalable enterprise data platform that transforms raw global event data into trusted, analytics-ready datasets and evolves into an AI-powered business intelligence platform.

---

## High-Level Architecture

🚧 Coming in Release v0.2

(Architecture diagram will be added as the platform evolves.)

---


**Version:** v0.1.0

**Release Name:** Platform Foundation

**Status:** 🟢 Completed

Completed:
- Project Foundation
- Repository Structure
- Engineering Documentation
- Architecture Principles
- Initial Roadmap

Upcoming:
- GDELT Data Source
- Ingestion Framework
- Lakehouse Architecture

---

## Technology Roadmap

- Platform Foundation
- Enterprise Lakehouse
- Analytics Platform
- AI Enablement
- Enterprise AI Platform

---

## Project Status

| Release | Status |
|----------|--------|
| v0.1 Platform Foundation | 🚧 In Progress |
| v1 Enterprise Lakehouse | ⏳ Planned |
| v2 AI Enablement | ⏳ Planned |
| v3 Enterprise AI Platform | ⏳ Planned |


**Version:** v0.2.0

**Release Name:** GDELT Architecture

**Status:** 🟢 Completed

Completed:
- Business Problem Definition
- GDELT Dataset Evaluation
- Platform Vision
- Engineering Philosophy
- Architecture Principles
- Medallion Architecture Design
- Bronze Layer Design
- Initial Storage Layout
- ADR-001: Why GDELT?
- High-Level Architecture Diagram

Upcoming:
- Python Ingestion Architecture
- Data Ingestion Module
- ADR-002: Why Python?
- Initial Extraction Framework

---

## Technology Roadmap

- Platform Foundation ✅
- Business Architecture ✅
- Python Ingestion 🚧
- Airflow Orchestration
- Enterprise Lakehouse
- Analytics Platform
- AI Enablement
- Enterprise AI Platform

---

## Project Status

| Release | Status |
|----------|--------|
| v0.1.0 Platform Foundation | ✅ Completed |
| v0.2.0 GDELT Architecture | ✅ Completed |
| v0.3.0 Python Ingestion | ⏳ Planned |
| v0.5.0 Airflow Orchestration | ⏳ Planned |
| v0.8.0 Delta Lake | ⏳ Planned |
| v1.0.0 Enterprise Lakehouse | ⏳ Planned |
| v2.0.0 AI Enablement | ⏳ Planned |
| v3.0.0 Enterprise AI Platform | ⏳ Planned |

## Current Release

**Version:** v0.3.0

**Release Name:** Reliable Data Acquisition

**Status:** Status: ✅ Completed

This release establishes the first production-grade implementation of the Enterprise Data Ingestion Layer.

The platform now includes:

- Modular ingestion architecture
- Centralized configuration management
- GDELT dataset discovery
- Reliable HTTP download service
- Structured logging
- Production-ready project organization

The ingestion layer is designed using engineering best practices including separation of concerns, configurable execution, fail-fast validation, and reusable service components.

## Current Capabilities

The ingestion module now supports:

- Latest GDELT dataset discovery
- Streaming HTTP download
- Direct streaming upload to Amazon S3
- Partitioned Bronze storage
- Metadata generation
- Immutable raw data storage
- Structured logging
- Centralized configuration
- Fail-fast HTTP validation
- Production-ready project organization

Future releases will extend the ingestion layer with:

- Retry policies
- Airflow scheduling

## Bronze Layer Architecture

The ingestion service streams raw GDELT datasets directly into Amazon S3 without using permanent local storage.

Each ingestion creates a partitioned Bronze layout:
This design preserves immutable source data while enabling replay, auditing, and downstream Spark processing.

## Project Status

| Phase | Status |
|--------|--------|
| Platform Foundation | ✅ Completed |
| Business Architecture | ✅ Completed |
| Data Ingestion Engineering | 🚧 In Progress |
| Airflow Orchestration | ⏳ Planned |
| Enterprise Lakehouse | ⏳ Planned |
| AI Enablement | ⏳ Planned |
| Enterprise AI Platform | ⏳ Planned |

