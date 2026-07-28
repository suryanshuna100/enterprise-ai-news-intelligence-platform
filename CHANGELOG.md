## [v0.2.0] - Business Architecture

### Added

#### Business Analysis
- Defined the business context and problem statement.
- Documented current business challenges.
- Defined expected business outcomes.
- Evaluated GDELT as the primary enterprise data source.

#### Architecture
- Designed the initial high-level platform architecture.
- Defined the Medallion Architecture (Bronze, Silver, Gold).
- Documented Bronze layer design.
- Designed the logical storage layout.
- Established platform vision.
- Defined engineering philosophy.
- Documented architecture principles.

#### Architecture Decisions
- Completed ADR-001: Why GDELT?
- Documented the technology evaluation framework.
- Defined architecture decision methodology.

#### Documentation
- Expanded project README.
- Added business architecture documentation.
- Introduced architecture design documents.
- Updated project roadmap.

### Changed

- Updated project vision from a traditional data pipeline to an Enterprise AI News Intelligence Platform.
- Adopted an architecture-first development approach.
- Introduced release-driven repository evolution.

### Status

✅ Business architecture completed.

Next milestone:
- Python ingestion design
- Data ingestion architecture
- Technology evaluation for Python and AWS S3
- Initial ingestion implementation

## [v0.3.0] - Reliable Data Acquisition

### Added

#### Engineering

- Designed the engineering architecture for the Data Ingestion Layer.
- Introduced centralized configuration management.
- Implemented configurable HTTP request settings.
- Added reusable download service.
- Implemented latest GDELT dataset discovery.
- Added structured logging support.
- Introduced fail-fast HTTP validation using `raise_for_status()`.
- Implemented production-ready module separation.

#### Platform

- Created `platform/ingestion/config.py`.
- Implemented `extract_gdelt.py`.
- Added dataset URL discovery service.
- Added dataset download service.
- Introduced reusable ingestion components.

#### Engineering Principles

- Applied Single Responsibility Principle.
- Separated discovery, download, validation, and storage responsibilities.
- Adopted configuration-driven development.
- Established reusable service architecture.

### Changed

- Transitioned from architecture-only documentation to executable ingestion services.
- Improved platform modularity.
- Enhanced reliability through centralized configuration.
- Standardized HTTP communication across ingestion modules.

### Status

🚧 Reliable Data Acquisition is in progress.

Completed:

- Configuration management
- Dataset discovery
- Dataset download
- HTTP validation
- Logging foundation

Next milestone:

- File validation
- Bronze layer persistence
- Metadata generation
- Retry implementation
- Checkpoint management

## [v0.4.0] - AWS S3 Bronze Layer

### Added

#### Engineering

- Designed the engineering architecture for the Bronze Layer.
- Implemented direct streaming ingestion from GDELT into Amazon S3.
- Introduced partitioned Bronze storage using ingestion date and ingestion time.
- Added metadata generation for each ingested dataset.
- Implemented incremental ingestion using the latest GDELT dataset feed.
- Preserved original GDELT source filenames during upload.
- Standardized UTC-based ingestion timestamps.
- Added centralized Amazon S3 upload services for datasets and metadata.

#### Platform

- Created the Amazon S3 Bronze bucket.
- Implemented reusable stream upload service.
- Implemented reusable metadata upload service.
- Added partition-based storage layout.
- Added metadata generation module.
- Established immutable raw dataset storage.
- Implemented end-to-end Bronze ingestion workflow.

#### Engineering Principles

- Applied cloud-native streaming architecture.
- Eliminated permanent local staging during ingestion.
- Preserved immutable raw datasets for replay and auditing.
- Separated orchestration, ingestion, metadata, and storage responsibilities.
- Established partitioned storage for scalable downstream processing.

### Changed

- Transitioned from local ingestion services to cloud-based Bronze storage.
- Replaced generic dataset names with original GDELT source filenames.
- Updated ingestion workflow to generate metadata after successful dataset upload.
- Improved storage organization using partition-based object keys.
- Standardized the Bronze Layer for future Spark and Delta Lake processing.

### Status

✅ AWS S3 Bronze Layer is completed.

Completed:

- Amazon S3 Bronze storage
- Streaming ingestion
- Partitioned storage
- Metadata generation
- Incremental ingestion
- End-to-end Bronze workflow

Next milestone:

- Apache Spark processing engine
- Bronze → Silver transformation pipeline
- Distributed data processing
- Schema validation
- Partitioned Parquet storage
- Silver Layer architecture