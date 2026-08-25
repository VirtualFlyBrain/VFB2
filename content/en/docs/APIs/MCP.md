---
title: "Model Context Protocol (MCP) Server"
linkTitle: "MCP Server"
weight: 5
date: 2026-08-25
description: >
  The VFB MCP server lets AI assistants and LLM agents explore Virtual Fly Brain data through natural language.
---

The **VFB Model Context Protocol (MCP) server** exposes Virtual Fly Brain data to AI assistants and agents (Claude, GitHub Copilot, and any other [MCP](https://modelcontextprotocol.io/)-compatible client). Once connected, you can explore VFB neuroanatomy, imaging data, and connectomics using natural language, and the assistant retrieves answers directly from VFB's live data services.

This page is the endpoint reference. For a worked guide to connecting a client and querying the data — with example prompts, the full tool set, and per-client setup — see the **[VFB MCP Tool Guide](/docs/tutorials/vfb-mcp-guide/)**.

## Endpoint

| | |
|---|---|
| **URL** | `https://vfb3-mcp.virtualflybrain.org` |
| **Transport** | Streamable HTTP |
| **Authentication** | None — no API key or account |

The hosted service page at [vfb3-mcp.virtualflybrain.org](https://vfb3-mcp.virtualflybrain.org/) always states the deployed version and the current, authoritative client setup instructions.

## Quick Connect (Claude Code)

```bash
claude mcp add --transport http virtual-fly-brain https://vfb3-mcp.virtualflybrain.org
```

Add `--scope user` to make it available in every project rather than just the current directory. For every other client — Claude Desktop, VS Code, GitHub Copilot, Gemini and others — see the [VFB MCP Tool Guide](/docs/tutorials/vfb-mcp-guide/).

## Source Code

The VFB MCP server is open source and maintained by the Virtual Fly Brain team:

[https://github.com/VirtualFlyBrain/VFB3-MCP](https://github.com/VirtualFlyBrain/VFB3-MCP)

Please file issues and feature requests against that repository.

## Related Access Options

The MCP server is built on the same underlying data services documented elsewhere in this section. For programmatic access from your own code rather than an AI assistant, see the [VFBconnect library](https://vfb-connect.readthedocs.io/) or the [direct APIs](/docs/apis/).
