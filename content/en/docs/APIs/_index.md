
---
title: "VFB APIs"
linkTitle: "VFB APIs"
weight: 600
date: 2017-01-05
description: >
  All available VFB APIs and underlying schemas.
---

VFB provides access to its data through several APIs and databases. The core data infrastructure consists of Neo4j graph databases that store integrated neuroanatomical data, complemented by OWL reasoning services for advanced ontological queries and SOLR search for fast text-based queries.

## User Access Options

**For Regular Users (GUI Access):**
- **VFB Web Interface**: [https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto) - User-friendly web interface for browsing and querying VFB data

**For AI Assistants and LLM Agents:**
- **VFB MCP Server**: [https://vfb3-mcp.virtualflybrain.org](https://vfb3-mcp.virtualflybrain.org) - Model Context Protocol server that lets Claude, GitHub Copilot, and other MCP-compatible assistants explore VFB data through natural language. See the [MCP Server documentation](/docs/apis/mcp/) to connect a client.

**For Programmatic Access:**
- **CATMAID pass-through API** (recommended for CATMAID/connectomics data): [https://v3-cached.virtualflybrain.org/](https://v3-cached.virtualflybrain.org/) - the fastest and simplest way to pull data out of VFB's hosted CATMAID instances (FAFB, FANC, L1EM and others). Takes VFB ids as well as native skeleton ids (skids), needs no token or CSRF cookie, and is documented interactively at the link above. See the [CATMAID API reference](/docs/apis/catmaid/).
- **VFBconnect Library**: [https://vfb-connect.readthedocs.io/](https://vfb-connect.readthedocs.io/) - Python library that provides high-level access to VFB data and queries. See also: [VFB API Tutorial](/docs/tutorials/apis/vfb_api_overview/)

**For LLMs and AI assistants:**
- **VFB MCP server**: `https://vfb3-mcp.virtualflybrain.org` - a Model Context Protocol server that gives Claude, GitHub Copilot and other MCP clients direct, tool-based access to VFB terms, images, connectivity and expression data. No installation, API key or account is needed:

  ```bash
  claude mcp add --transport http virtual-fly-brain https://vfb3-mcp.virtualflybrain.org
  ```

  Source code and client configuration for other assistants: [VirtualFlyBrain/VFB3-MCP](https://github.com/VirtualFlyBrain/VFB3-MCP). Worked examples: [VFB MCP tool guide](/docs/tutorials/vfb-mcp-guide/).

**For Advanced Data Access:**
- **Direct APIs** (documented below): Low-level access to underlying databases and reasoning services

## Important Notes

These API documentations describe the schemas used for data storage and basic interfaces. **Most VFB queries are constructed from combined query chains** that integrate multiple services (Neo4j, OWL reasoning, SOLR search) rather than single API calls. For details on how queries are orchestrated, see the [VFB query chains documentation](https://github.com/VirtualFlyBrain/geppetto-vfb/blob/master/model/README.md).

The APIs documented here are intended for:
- Advanced users needing direct database access
- Developers building custom tools or integrations
- Researchers requiring low-level data access for specialized analyses

For most use cases, we recommend starting with the [VFBconnect library](https://vfb-connect.readthedocs.io/) or the [web interface](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto).
