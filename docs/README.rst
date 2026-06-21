.. include:: ../README.rst
# 🛡️ Secure SSH Honeypot Platform for Cyber Threat-Intelligence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Cowrie](https://img.shields.io/badge/Cowrie-Honeypot-green)](https://github.com/cowrie/cowrie)

A high-interaction SSH honeypot platform built using **Cowrie**, **Docker**, and the **ELK Stack** to capture, analyze, and visualize attacker behavior. The project leverages deception techniques and secure containerization to collect actionable cyber threat intelligence while maintaining complete isolation from production environments.

---

## 📖 Overview

ThreatLens is designed to simulate a realistic Linux server environment that attracts attackers and records their activities. By providing convincing user accounts, directories, and honeyfiles, the honeypot encourages adversaries to interact with the system, enabling detailed observation of attack patterns, credential usage, command execution, and post-exploitation behavior.

### Objectives

* Collect real-world attack data
* Analyze attacker techniques and procedures
* Visualize threats through centralized dashboards
* Provide a secure environment for cybersecurity research
* Demonstrate practical deception technology and active defense concepts

---

## ✨ Key Features

### 🎭 High-Fidelity Deception

* Realistic Linux filesystem structure
* Simulated users and home directories
* Fake credentials and sensitive-looking files
* Convincing server banners and shell environment

### 🐳 Secure Containerization

* Fully isolated Docker deployment
* Non-root execution
* Easy deployment and maintenance
* Reduced risk to host systems

### 📊 Threat Intelligence Collection

* Session recording
* Command logging
* Credential harvesting
* File download monitoring
* IP tracking and geolocation analysis

### 📈 ELK Stack Integration

* Elasticsearch for log storage
* Logstash for processing
* Kibana dashboards for visualization
* Real-time monitoring and analytics

---

## 🏗️ Architecture

The system follows a layered architecture that captures attacker interactions and transforms raw logs into actionable intelligence.

```text
Internet
    │
    ▼
┌─────────────────┐
│ SSH Honeypot    │
│ (Cowrie)        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Log Collection  │
│ (Filebeat)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Logstash        │
│ Processing      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Elasticsearch   │
│ Storage         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Kibana          │
│ Visualization   │
└─────────────────┘
```

### Architecture Diagram

```markdown
docs/images/architecture.png
```

Add your architecture screenshot here:

```text
images/
├── architecture.png
├── elk_pipeline.png
├── dashboard.png
└── honeyfiles.png
```

---

## 📂 Project Structure

```bash
ThreatLens/
│
├── docker-compose.yml
├── Dockerfile
├── cowrie/
│   ├── cowrie.cfg
│   ├── honeyfs/
│   ├── fs.pickle
│   └── logs/
│
├── elk/
│   ├── elasticsearch/
│   ├── logstash/
│   └── kibana/
│
├── filebeat/
│
├── scripts/
│
├── docs/
│   └── images/
│
└── README.md
```

---

## 🔧 Honeypot Engineering

### 1. Custom Filesystem

The virtual filesystem is customized to resemble a production Linux server.

Examples include:

```bash
/home/admin/
/home/devops/
/var/www/html/
/etc/apache2/
/opt/backups/
```

This increases attacker engagement and provides richer intelligence data.

---

### 2. Strategic Honeyfiles

Fake but realistic files are intentionally placed throughout the system.

Examples:

```bash
.env
config.php
database_backup.sql
credentials.txt
aws_keys.txt
```

These files contain fabricated credentials designed to reveal attacker objectives and techniques.

---

### 3. User Persona Simulation

Example fake accounts:

```bash
admin
devops
backup
webadmin
developer
```

These accounts make the environment appear authentic and encourage further interaction.

---

## 📊 Threat Monitoring Dashboard

Collected attack data is visualized using Kibana dashboards.

Metrics include:

* Top attacking IP addresses
* Geographic distribution
* Most attempted usernames
* Most common passwords
* Frequently executed commands
* Session timelines
* Downloaded malware samples

Example Dashboard:

```markdown
docs/images/dashboard.png
```

---

##  Deployment

### Prerequisites

* Docker
* Docker Compose
* Linux Server (Ubuntu Recommended)
* Minimum 4 GB RAM

---

### Clone Repository

```bash
git clone https://github.com/speedw124/Secure-SSH-Honeypot-Platform-for-Cyber-Threat-Intelligence

cd Secure-SSH-Honeypot-Platform-for-Cyber-Threat-Intelligence
```

---

### Build Containers

```bash
docker-compose build
```

---

### Start Services

```bash
docker-compose up -d
```

---

### Verify Deployment

```bash
docker ps
```

Expected services:

```bash
cowrie
filebeat
elasticsearch
logstash
kibana
```

---

## 🔍 Viewing Logs

Cowrie logs:

```bash
docker logs cowrie
```

Session logs:

```bash
cowrie/var/log/cowrie/
```

Monitor live activity:

```bash
tail -f cowrie.log
```

---

## 🔐 Security Considerations

* Honeypot runs inside isolated containers
* No direct access to host filesystem
* Non-root service execution
* Network segmentation recommended
* Deploy on a dedicated VPS or isolated network
* Regularly monitor collected malware samples

---

## 📈 Future Enhancements

* Multiple honeypot nodes (Honeynet)
* Threat intelligence feeds integration
* Malware sandbox automation
* Machine learning anomaly detection
* Real-time alerting via Slack/Discord
* GeoIP attack mapping
* Automated IOC extraction

---

## 🧪 Technologies Used

| Technology    | Purpose                    |
| ------------- | -------------------------- |
| Cowrie        | SSH/Telnet Honeypot        |
| Docker        | Containerization           |
| Python        | Automation & Customization |
| Elasticsearch | Log Storage                |
| Logstash      | Log Processing             |
| Kibana        | Visualization              |
| Filebeat      | Log Shipping               |
| Linux         | Deployment Environment     |

---

## 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

## 👨‍💻 Author

Developed as a Cybersecurity Graduation Project focusing on:

* Deception Technology
* Active Defense
* Threat Intelligence Collection
* Honeypot Engineering
* Security Monitoring

⭐ If you find this project useful, consider giving it a star on GitHub.
