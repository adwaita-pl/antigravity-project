# Antigravity Setup

This repository contains a local setup for a Google Antigravity agent.

## Overview

- **`main.py`**: The entry point that initializes the `LocalAgentConfig` and runs a simple "Hello, World!" chat prompt using `asyncio`.
- **`mcp_config.json`**: The Model Context Protocol (MCP) configuration. It sets up a `sysadmin-tools` server that provides tools for reading systemd journals, checking firewalld rules, and retrieving network status.
- **`.env.example`**: Example environment variables template.

## Running

1. Create a `.env` file based on `.env.example` and add your API keys or necessary environment variables.
2. Install dependencies (likely via a virtual environment in `.venv/`).
3. Run `python main.py` to start the agent.

## Features
- **sysadmin-tools MCP Server**: Exposes commands like `read_journalctl`, `check_firewall`, and `network_status` to the agent.
