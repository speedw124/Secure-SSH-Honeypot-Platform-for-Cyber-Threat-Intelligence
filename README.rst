# Containerized Secure SSH Honeypot for Threat Intelligence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)

A high-fidelity SSH Honeypot (Cowrie) system engineered with a focus on **Deception Technology** and **Active Defense**. This project utilizes containerization to provide a secure, isolated, and highly realistic environment for capturing and analyzing attacker behavior to gather actionable threat intelligence.

---

## 🚀 Project Overview

This project implements a sophisticated decoy system designed to mimic a production Linux server. By meticulously crafting virtual filesystems and user personas, we maximize attacker "dwell time," allowing for the collection of deep insights into their methodologies without risking actual production assets.

### Key Highlights:

*   **High-Fidelity Deception**: Custom-engineered filesystem (`fs.pickle`) and realistic user environments.
*   **Robust Isolation**: Full containerization using Docker to prevent any potential host compromise.
*   **Scalable Architecture**: Easily deployable as a single node or a distributed Honeynet.
*   **Real-time Analytics**: Integrated pipeline for log aggregation and visualization.

---

## 🏗️ System Architecture

The system follows a modular architecture where incoming malicious traffic is isolated and analyzed in real-time.

![High-Level Architecture](images/architecture.png)
*Figure 1: High-Level System Architecture & Traffic Flow*

### The ELK Data Pipeline

We utilize the ELK Stack (Elasticsearch, Logstash, Kibana) combined with Filebeat to transform raw attack logs into visual intelligence.

![ELK Pipeline](images/elk_pipeline.png)
*Figure 2: Data Aggregation and Visualization Pipeline*

---

## 🛠️ Core Features & Engineering

### 1. Filesystem Engineering

We used `fsctl.py` to build a convincing directory structure that mimics a live production server, including common system paths and application-specific directories.

![Filesystem Realism](images/filesystem_users.png)
*Figure 3: Customized virtual filesystem showing realistic user home directories.*

### 2. Strategic Honeyfiles

Decoy files (e.g., `.env`, `config.php`, `backup.sql`) containing fake but realistic credentials are planted to lure attackers into revealing their specific objectives.

![Honeyfile Example](images/honeyfile_config_php.png)
*Figure 4: Example of a planted honeyfile with fake API keys and DB credentials.*

### 3. Threat Visualization

All captured interactions are visualized through custom Kibana dashboards, allowing for immediate identification of attack patterns and originations.

![Kibana Dashboard](images/kibana_dashboard.png)
*Figure 5: Real-time Threat Intelligence Dashboard.*

---

## 🚦 Getting Started

### Prerequisites

*   Docker & Docker Compose
*   Linux Environment (Recommended)

### Installation

1. **Clone the Repo:**

   ```bash
   git clone https://github.com/black1892004-cloud/Containerized-Secure-SSH-Honeypot-for-Threat-Intelligence.git
   cd Containerized-Secure-SSH-Honeypot-for-Threat-Intelligence
   ```

2. **Deploy with Docker Compose:**

   ```bash
   docker-compose up --build -d
   ```

3. **Verify Deployment:**

   ```bash
   docker ps
   ```

---

## 🛡️ Security & Isolation

*   **Non-Root Execution**: Cowrie runs as a non-privileged user inside the container.
*   **Network Isolation**: Docker bridge networking restricts the honeypot's visibility of the host network.
*   **Stateless Operation**: Container restarts revert any unauthorized changes made by attackers.

---

## 🤝 Contribution & License

Contributions are welcome! Please feel free to submit a Pull Request.
This project is licensed under the MIT License.

---

Project developed as a Graduation Thesis in Cybersecurity.
