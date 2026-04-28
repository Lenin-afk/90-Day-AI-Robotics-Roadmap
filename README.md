# 90-Day AI Robotics & Cloud Roadmap

## Phase 1: Foundations of Intelligent Systems

### Week 1 Milestone: Sensor Navigation Pipeline

This project demonstrates a production-ready data pipeline for a robotic navigation system using **Python** and **NumPy**.

#### Key Features:

1. **Data Sanitization:** Uses Boolean indexing to identify and replace sensor "glitches" (noise/outliers) without slow loops.
2. **Signal Smoothing:** Implements a sliding window moving average to reduce hardware jitter for smoother mechanical movement.
3. **Statistical Safety:** Utilizes Standard Deviation ($\sigma$) to measure environmental stability and trigger safety warnings.

#### Skills Mastered:

- **OOP:** Class-based system architecture.
- **Vectorized Math:** High-performance data manipulation with NumPy.
- **Algorithm Design:** Designing multi-stage processing pipelines.
- **DevOps Basics:** Professional Git workflow and documentation.

---

_Next Step: Week 2 - Transitioning to Backend APIs and Cloud Connectivity._

## Week 2 Milestone: Backend Architecture & Security

Successfully transitioned the local navigation logic into a secure, cloud-ready Web API.

### Key Skills Implemented:

- **RESTful API Development:** Built using **FastAPI** for high-performance data exchange.
- **System Security:** Implemented **API Key Authentication** to protect robot endpoints.
- **Asynchronous Processing:** Utilized **BackgroundTasks** for non-blocking cloud telemetry sync.
- **Data Persistence:** Developed a JSON-based logging system for historical data retrieval.
- **Client-Server Architecture:** Managed Request/Response cycles with Pydantic data validation.

---

_Next Step: Week 3 - Advanced Data Visualization & Real-time Dashboards._
