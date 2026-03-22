<div align="center">

<br/>

```
 █████╗ ███████╗ ██████╗ ██╗███████╗    ██████╗ ██╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝    ██╔══██╗██║
███████║█████╗  ██║  ███╗██║███████╗    ██████╔╝██║
██╔══██║██╔══╝  ██║   ██║██║╚════██║    ██╔══██╗██║
██║  ██║███████╗╚██████╔╝██║███████║    ██████╔╝██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝    ╚═════╝ ╚═╝
```

### **Agentic Business Intelligence Engine**
#### *Autonomous Market Intelligence - Research to Revenue-Grade Insights, Zero Human Latency*

<br/>

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF6B6B?style=for-the-badge)](https://crewai.com)
[![Power BI](https://img.shields.io/badge/Power%20BI-Ready-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST%20Interface-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)]()

<br/>

> **"From raw market signals to structured, Power BI-ready intelligence - fully orchestrated by autonomous AI agents, with zero manual intervention."**

<br/>

[**Live Demo**](https://drive.google.com/file/d/1OFE-7rCSHXr7AXO6XoiQJDa2WvEPygXg/view?usp=drive_link) - [**GitHub Repository**](https://github.com/Adhithyan006/Aegis-BI-Engine) - [**Quick Start**](#-quick-start) - [**Architecture**](#-system-architecture)

<br/>

</div>

---

## The Problem with Traditional Market Research

Enterprise intelligence workflows are broken. Analysts spend 70% of their time manually collecting, cleaning, and structuring data - leaving only 30% for actual analysis. Research cycles that should take hours stretch into weeks. By the time a report lands on a decision-maker's desk, the market has already moved.

**Aegis BI Engine eliminates this entirely.**

---

## What Aegis Does

Aegis is a **production-grade, multi-agent AI system** built on CrewAI that autonomously executes the full market research pipeline - from raw topic ingestion to structured, Power BI-ready datasets - with no human intervention between input and output.

You provide a **topic**. Aegis delivers **structured intelligence**.

```
INPUT:  "Analyze the EV battery market in Southeast Asia Q1 2025"
            │
            ▼
  ┌─────────────────────────────────────┐
  │     AEGIS BI ENGINE (Autonomous)    │
  │  ┌───────────┐    ┌──────────────┐  │
  │  │ Researcher│───▶│   Analyst    │  │
  │  │   Agent   │    │    Agent     │  │
  │  └───────────┘    └──────────────┘  │
  └─────────────────────────────────────┘
            │
            ▼
OUTPUT: market_intelligence.csv  +  Structured Insights Report
            │
            ▼
      Power BI Direct Load → Interactive Dashboard
```

---

## Core Capabilities

| Capability | Description |
|---|---|
| **Autonomous Research** | AI Researcher agent scours, synthesizes, and validates market data from multiple signal sources |
| **Analytical Processing** | AI Analyst agent transforms raw research into structured, insight-dense outputs |
| **Zero-Error CSV Generation** | Clean, standardized rows and columns - no manual formatting, no data fatigue |
| **Power BI Direct Compatibility** | Output files are immediately importable into Power BI without transformation |
| **REST API Interface** | FastAPI-powered endpoint for seamless integration with any existing workflow |
| **Configurable Intelligence** | Swap topics, adjust agent behavior, and scale research depth on demand |

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         AEGIS BI ENGINE                              │
│                                                                     │
│   ┌──────────────────────────────────────────────────────────────┐  │
│   │                    ORCHESTRATION LAYER                       │  │
│   │                    CrewAI Framework                          │  │
│   └──────────────────────┬───────────────────────────────────────┘  │
│                          │                                          │
│          ┌───────────────┴────────────────┐                         │
│          │                                │                         │
│   ┌──────▼──────────┐           ┌─────────▼───────────┐            │
│   │  RESEARCHER      │           │  ANALYST AGENT       │           │
│   │  AGENT           │           │                      │           │
│   │                  │           │  - Pattern Detection  │           │
│   │  - Market Scan   │──────────▶│  - Insight Synthesis  │          │
│   │  - Data Harvest  │  Passes   │  - Statistical Model  │          │
│   │  - Validation    │  Research │  - CSV Structuring    │          │
│   │  - Source Fusion │           │  - Report Generation  │          │
│   └──────────────────┘           └──────────┬──────────┘            │
│                                             │                        │
│   ┌──────────────────────────────────────────▼──────────────────┐   │
│   │                      OUTPUT LAYER                           │   │
│   │                                                             │   │
│   │   market_data.csv  ──────────────▶  Power BI Direct Load    │   │
│   │   insights_report  ──────────────▶  Decision Support        │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Agent Breakdown

**Researcher Agent**
- Autonomously scans, aggregates, and cross-validates market signals
- Applies source triangulation to filter noise from signal
- Produces structured research briefs passed directly to the Analyst

**Analyst Agent**
- Consumes Researcher output and applies business intelligence logic
- Identifies trends, anomalies, and market inflection points
- Generates clean CSV datasets structured for immediate BI tool consumption
- Produces human-readable insight reports alongside structured data

---

## Repository Structure

```
Aegis-BI-Engine/
│
├── app.py                  - FastAPI application entry point and REST interface
├── main.py                 - CrewAI agent orchestration and pipeline controller
├── requirements.txt        - Python dependency manifest
├── .env                    - Environment configuration (API keys, parameters)
├── .gitignore              - Version control exclusions
│
└── venv/                   - Isolated Python virtual environment
```

---

## Quick Start

### Prerequisites

- Python 3.11 or higher
- OpenAI API Key (or compatible LLM provider key)
- Power BI Desktop (for dashboard visualization)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Adhithyan006/Aegis-BI-Engine.git
cd Aegis-BI-Engine
```

**2. Create and activate virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment**

```bash
# Copy and edit the .env file
cp .env.example .env
```

Add your API keys to `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here   # Optional: for web search capability
```

**5. Run the engine**

```bash
# Direct execution via CrewAI pipeline
python main.py

# Or via FastAPI server
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

---

## Usage

### Direct Execution

Edit the topic input in `main.py` and execute:

```python
# In main.py
topic = "Global SaaS Market Trends Q1 2025"

# Run the autonomous pipeline
crew.kickoff(inputs={"topic": topic})
```

```bash
python main.py
```

Aegis will autonomously:
1. Deploy the Researcher Agent to gather and validate market intelligence
2. Pass structured research to the Analyst Agent for processing
3. Output a clean `.csv` file ready for Power BI ingestion
4. Generate a comprehensive insights report

### REST API

Start the FastAPI server and submit research requests via HTTP:

```bash
uvicorn app:app --reload
```

```bash
# Example API request
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"topic": "Renewable Energy Market Southeast Asia 2025"}'
```

### Power BI Integration

Once Aegis generates your `.csv` output:

1. Open **Power BI Desktop**
2. Select **Get Data - Text/CSV**
3. Navigate to and select the generated `.csv` file
4. Click **Load** - your data is immediately available for visualization

> **Note:** Dashboard construction remains a manual creative step in Power BI Desktop. Aegis handles the entire data pipeline up to the point of BI tool ingestion - giving analysts clean, structured data to build from, rather than hours of data preparation work.

---

## Output Format

Aegis produces structured CSV output with consistent schema across research runs:

```
Category, Metric, Value, Unit, Confidence, Source, Timestamp, Region
Market Size, Total Addressable Market, 4.2, USD Billion, High, Synthesized, 2025-Q1, Southeast Asia
Growth Rate, YoY CAGR, 18.5, Percentage, High, Synthesized, 2025-Q1, Southeast Asia
...
```

This schema is intentionally designed for direct Power BI ingestion - every column maps cleanly to BI visualization primitives without transformation overhead.

---

## Technical Stack

| Component | Technology | Role |
|---|---|---|
| **Agent Orchestration** | CrewAI | Multi-agent coordination and task delegation |
| **Language Models** | OpenAI GPT-4 / Compatible LLMs | Agent cognition and reasoning |
| **API Layer** | FastAPI | REST interface for external integrations |
| **Runtime** | Python 3.11+ | Core execution environment |
| **Output Format** | CSV (structured) | Power BI-compatible data export |
| **Configuration** | python-dotenv | Secure environment variable management |

---

## Key Design Decisions

**Why CrewAI?**
CrewAI's role-based agent architecture maps directly to how enterprise research teams actually function - a Researcher who gathers raw intelligence, and an Analyst who transforms it into actionable outputs. This separation of concerns produces dramatically higher-quality results than single-agent approaches.

**Why CSV output for Power BI?**
CSV as an output format is a deliberate architectural choice. It provides maximum compatibility across the Power BI ecosystem, requires zero transformation overhead, and allows analysts to immediately layer business logic through Power Query if needed. The structured schema Aegis produces is designed to be dashboard-ready from line one.

**Why FastAPI?**
The REST interface means Aegis is not a standalone script - it is an intelligence microservice that can be embedded into any enterprise workflow, triggered by external systems, or called from automation pipelines.

---

## Roadmap

- [ ] **Scheduled Intelligence Runs** - Cron-based automated market monitoring
- [ ] **Multi-Topic Parallel Processing** - Concurrent agent crews for portfolio-wide analysis
- [ ] **Power BI REST API Integration** - Programmatic dataset push to Power BI workspaces
- [ ] **Custom Agent Personas** - Domain-specialized researcher configurations (FinTech, HealthTech, etc.)
- [ ] **Historical Intelligence Versioning** - Track market evolution across research run history
- [ ] **Slack / Teams Delivery** - Push intelligence summaries directly to collaboration tools
- [ ] **Vector Memory Layer** - Persistent agent memory for longitudinal market analysis

---

## Contributing

Contributions are welcome. If you are building on top of Aegis or extending its capabilities:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/capability-name`)
3. Commit your changes with descriptive messages
4. Push to your branch and open a Pull Request

Please ensure any new agent configurations are documented and tested with at least one sample topic run.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for full terms.

---

## Author

**Adhithyan**
- GitHub: [@Adhithyan006](https://github.com/Adhithyan006)
- Repository: [Aegis-BI-Engine](https://github.com/Adhithyan006/Aegis-BI-Engine)

---

<div align="center">

**Built with CrewAI - Turning market questions into structured intelligence, autonomously.**

*If Aegis accelerated your research workflow, consider starring the repository.*

 **Star this repo** - it helps other engineers discover autonomous BI tooling

</div>
