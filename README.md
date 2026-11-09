# TraceZero: Local-First Hardware, Network & Packet Copilot

A real-time telemetry daemon and diagnostic copilot that captures OS bottlenecks, socket latency, DNS hops, and packet anomalies, translating cryptic system signals into clear troubleshooting steps.

Author: Avon Budhathoki (jtq19@txstate.edu)

## Overview

TraceZero bridges low-level hardware/network inspection with modern developer diagnostics:
- Continuous socket latency and DNS resolution tracking
- CPU core thermal, disk I/O, and memory leak detection
- Structured JSON output ready for local LLM troubleshooting

## Quickstart

```bash
git clone https://github.com/saurab200/tracezero.git
cd tracezero
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m tracezero.cli monitor
```
