"""
TraceZero Telemetry Collector
Author: Avon Budhathoki
"""

import time
import socket
import psutil
from typing import Dict, Any, List

class SystemMonitor:
    def __init__(self, target_hosts: List[str] = None):
        self.target_hosts = target_hosts or ["1.1.1.1", "8.8.8.8"]

    def snapshot(self) -> Dict[str, Any]:
        """Collect instantaneous hardware and network metrics."""
        cpu = psutil.cpu_percent(percpu=True)
        mem = psutil.virtual_memory()
        net = psutil.net_io_counters()

        pings = {}
        for host in self.target_hosts:
            start = time.perf_counter()
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.5)
                s.connect((host, 53 if "." in host else 443))
                s.close()
                latency_ms = round((time.perf_counter() - start) * 1000, 2)
                pings[host] = {"connected": True, "latency_ms": latency_ms}
            except Exception as e:
                pings[host] = {"connected": False, "error": str(e)}

        return {
            "timestamp": time.time(),
            "cpu_per_core_percent": cpu,
            "memory_used_percent": mem.percent,
            "bytes_sent": net.bytes_sent,
            "bytes_recv": net.bytes_recv,
            "network_probes": pings
        }
