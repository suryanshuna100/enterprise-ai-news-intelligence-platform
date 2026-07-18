# ADR-003: Why the Requests Library?

**Status:** Accepted

**Date:** 2026-07-17

---

# Context

The Enterprise AI News Intelligence Platform requires a reliable mechanism to download GDELT datasets published over HTTP.

The ingestion service is responsible for retrieving raw data from external sources before it enters the data lake. Since this is the first interaction with an external system, the download component must be simple, reliable, maintainable, and easy to extend.

The engineering team evaluated available options for making HTTP requests in Python before implementing the ingestion layer.

---

# Business Problem

The platform must automatically download GDELT datasets without manual intervention.

The selected solution should:

- Communicate with HTTP endpoints reliably.
- Handle network failures gracefully.
- Support configurable timeouts.
- Be easy to maintain and understand.
- Form the foundation for future production enhancements such as retries and authentication.

---

# Decision

Use the **Python `requests` library** as the standard HTTP client for the ingestion service.

---

# Decision Drivers

The decision was based on the following engineering considerations:

- Simple and readable API.
- Excellent documentation and community adoption.
- Built-in support for request timeouts.
- Straightforward exception handling.
- Easy integration with logging and retry mechanisms.
- Widely used in enterprise Python applications.

These characteristics align with the project's goals of building a maintainable and production-ready ingestion pipeline.

---

# Alternatives Considered

## Option 1 — Requests (Selected)

### Advantages

- Clean and intuitive syntax.
- Easy timeout configuration.
- Comprehensive exception hierarchy.
- Strong community support.
- Excellent readability for future contributors.

### Disadvantages

- External dependency that must be installed.

---

## Option 2 — urllib

### Advantages

- Included in Python's standard library.
- No additional installation required.

### Disadvantages

- More verbose API.
- Less intuitive error handling.
- More boilerplate code for common operations.
- Reduced readability compared to `requests`.

---

## Option 3 — Command-line Tools (curl / wget)

### Advantages

- Useful for manual operations and shell scripting.

### Disadvantages

- Introduces operating system dependencies.
- Harder to integrate into Python applications.
- Poor portability across environments.
- Not suitable as the primary ingestion mechanism.

---

# Trade-offs

Choosing `requests` introduces an additional project dependency.

However, the benefits of improved readability, maintainability, and developer productivity outweigh the small overhead of managing one external package.

For a production data platform, maintainability is prioritized over minimizing dependencies.

---

# Consequences

## Positive

- Cleaner implementation of the ingestion service.
- Easier debugging and maintenance.
- Simpler integration with logging and retry logic.
- Better developer experience for future contributors.

## Negative

- Requires dependency management through `requirements.txt`.
- Future updates to the library should be monitored for compatibility and security.

---

# Future Considerations

As the platform evolves, additional capabilities may be incorporated, including:

- Retry strategies with exponential backoff.
- HTTP session reuse for performance.
- Authentication support for secured APIs.
- Request metrics for monitoring and observability.

These enhancements can be implemented without replacing the chosen HTTP client.

---

# Interview Perspective

**Question:** Why did you choose the `requests` library instead of `urllib`?

**Answer:**

I selected `requests` because it provides a cleaner and more maintainable API for HTTP communication. It simplifies timeout management, exception handling, and future integration with logging and retry mechanisms. While `urllib` is part of Python's standard library, its interface is more verbose and less readable. Since the goal of this project is to build an enterprise-grade ingestion service that is easy to maintain and extend, `requests` was the more appropriate choice.