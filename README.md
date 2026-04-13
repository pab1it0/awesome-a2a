# Awesome A2A [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Awesome A2A](./assets/banner.svg)

A curated list of awesome Agent2Agent (A2A) protocol servers. This repository collects and organizes A2A-compliant server implementations to help developers build interoperable AI agent systems.

* [What is A2A?](#what-is-a2a)
* [Clients](#clients)
* [Tutorials](#tutorials)
* [Community](#community)
* [Legend](#legend)
* [Server Implementations](#server-implementations)
* [Frameworks](#frameworks)
* [Utilities](#utilities)
* [Contributing](#contributing)
* [License](#license)

## What is A2A?

[A2A](https://github.com/google/A2A) (Agent2Agent) is an open protocol created by Google that enables different AI agents to communicate and collaborate with each other using a standardized interface. The protocol allows agents to discover capabilities, submit tasks for execution, monitor task progress, and receive task results in a unified way.

## Clients

AI clients that can interact with A2A servers:

* Claude from Anthropic
* Gemini from Google
* Custom A2A-compatible clients

## Tutorials

* [Getting Started with A2A Protocol](https://google.github.io/A2A/#/documentation)
* [Building Your First A2A Server](https://github.com/google/A2A/blob/main/samples/python/README.md)

## Community

* [Google A2A GitHub](https://github.com/google/A2A)

## Legend

* 🎖️ – official implementation
* programming language
  * 🐍 – Python codebase
  * 📇 – TypeScript/JavaScript codebase
  * 🏎️ – Go codebase
  * 🦀 – Rust codebase
  * #️⃣ - C# Codebase
  * ☕ - Java codebase
* scope
  * ☁️ - Cloud Service
  * 🏠 - Local Service
  * 📟 - Embedded Systems
* operating system
  * 🍎 – For macOS
  * 🪟 – For Windows
  * 🐧 - For Linux

> [!NOTE]
> Confused about Local 🏠 vs Cloud ☁️?
> * Use local when A2A server is talking to a locally installed software.
> * Use cloud when A2A server is talking to remote APIs, like Google Maps API.

## Server Implementations

* 🎖️ - [Official Samples](#official-samples)
* 🗺️ - [Location Services](#location-services)
* 💼 - [Business Tools](#business-tools)
* 🖼️ - [Image Generation](#image-generation)
* 💱 - [Financial Services](#financial-services)
* 🔎 - [Search & Data Extraction](#search-and-data-extraction)
* 💬 - [Communication Services](#communication-services)
* 🔄 - [Integration Services](#integration-services)
* 🛠️ - [Developer Tools](#developer-tools)
* 🧠 - [Knowledge Services](#knowledge-services)
* 📊 - [Data Services](#data-services)
* 🚆 - [Travel & Transportation](#travel-and-transportation)

### 🎖️ <a name="official-samples"></a>Official Samples

Official sample implementations from the Google A2A repository.

- [google/google_adk](https://github.com/google/A2A/tree/main/samples/python/agents/google_adk) 🎖️ 🐍 🏠 - An expense reimbursement agent built with Google Agent Development Kit (ADK). Showcases multi-turn interactions and webform handling through the A2A protocol.

- [google/langgraph](https://github.com/google/A2A/tree/main/samples/python/agents/langgraph) 🎖️ 🐍 ☁️ - A currency conversion agent built with LangGraph. Showcases multi-turn interactions, tool usage for currency exchange via Frankfurter API, and streaming updates through the A2A protocol.

- [google/crewai](https://github.com/google/A2A/tree/main/samples/python/agents/crewai) 🎖️ 🐍 ☁️ - An image generation agent built with CrewAI. Showcases text-to-image generation using Google Gemini API and returning images as artifacts through the A2A protocol.

### 🗺️ <a name="location-services"></a>Location Services

A2A servers providing mapping, geocoding, navigation, and other location-based services.

- [pab1it0/google-maps-a2a](https://github.com/pab1it0/google-maps-a2a) 🐍 ☁️ - An A2A-compliant server that provides Google Maps capabilities including geocoding, reverse geocoding, directions, places search, place details, and distance matrix calculations. Supports multiple input/output formats and provides a standardized agent card for capability discovery.

### 💼 <a name="business-tools"></a>Business Tools

A2A servers for business operations, expense management, and other enterprise functions.

*See [google/google_adk](#official-samples) for an example expense reimbursement tool.*

- [geter-andru/mcp-server-andru-intelligence](https://github.com/geter-andru/mcp-server-andru-intelligence) 📇 ☁️ - Operational empathy for technical SaaS founders. 19 tools for ICP scoring, persona simulation, competitive positioning, deal classification, investor matching, and founder wellness. AP2 payment-capable. [Agent Card](https://hs-andru-test.onrender.com/.well-known/agent.json)

- [Writbase/writbase](https://github.com/Writbase/writbase) 📇 ☁️ - MCP-native task management for AI agent fleets with multi-agent permissions, full provenance, inter-agent task delegation, and A2A status mapping.

- [Ambr](https://ambr.run) 📇 ☁️ - Legal contract management for AI agents. Creates, signs, and verifies dual-format Ricardian Contracts (human-readable legal text + machine-parsable JSON, SHA-256 linked). 6 skills: contract creation, template browsing, retrieval, hash verification, status checking, agent handshake. Supports API key and x402 USDC payment. [Agent Card](https://getamber.dev/.well-known/agent.json) ([Platform](https://getamber.dev))

### 🖼️ <a name="image-generation"></a>Image Generation

A2A servers for generating and manipulating images.

*See [google/crewai](#official-samples) for an example image generation tool.*

### 💱 <a name="financial-services"></a>Financial Services

A2A servers for financial operations, currency conversion, and financial data.

*See [google/langgraph](#official-samples) for an example currency conversion tool.*

- [opspawn/a2a-x402-gateway](https://github.com/opspawn/a2a-x402-gateway) 📇 ☁️ - An A2A-native agent gateway with x402 V2 micropayments. Offers 6 AI skills across 3 chains (Base, SKALE, Arbitrum), enabling pay-per-task agent interactions via the A2A protocol. Live at https://a2a.opspawn.com.

- [TIAMAT](https://tiamat.live) 📇 ☁️ - An autonomous A2A-compliant AI agent offering text summarization, streaming chat, algorithmic image generation (6 styles), and text-to-speech synthesis. Supports x402 USDC micropayments on Base. Agent card at `/.well-known/agent.json`. Built by ENERGENAI LLC. ([GitHub](https://github.com/toxfox69/tiamat-entity))

- [MERX](https://merx.exchange) 📇 ☁️ - TRON blockchain resource exchange. Aggregates 7 energy providers with real-time best-price routing. 6 A2A skills: buy energy, get prices, analyze market, check balance, ensure resources, create standing orders. Also supports MCP (53 tools). Live at merx.exchange. [Agent Card](https://merx.exchange/.well-known/agent.json) ([GitHub](https://github.com/Hovsteder/merx-mcp))

### 🔎 <a name="search-and-data-extraction"></a>Search & Data Extraction

A2A servers for search, data retrieval, and information extraction.

- [AnyBrowse](https://anybrowse.dev) ☁️ - Autonomous web browsing agent that converts URLs to LLM-ready Markdown via real Chrome browsers, with x402 micropayments on Base.

- [ju4nv1e1r4/agents-with-adk](https://github.com/ju4nv1e1r4/agents-with-adk) 🐍 ☁️ - An example of agent implementation using Google ADK (Agent Development Kit) with two agents and a tool, working with full iteroperability, along with demonstrations of agent evaluation and deployment to Google Cloud Run.

### 💬 <a name="communication-services"></a>Communication Services

A2A servers for messaging, email, and other communication tools.

- [Perkoon](https://perkoon.com) 📇 ☁️ - P2P data exchange between agents. Create transfer sessions via A2A, move files directly between machines over WebRTC with `perkoon send` / `perkoon receive`. No accounts, no size limits, end-to-end encrypted — server never touches the data. Agent Card: [perkoon.com/.well-known/agent-card.json](https://perkoon.com/.well-known/agent-card.json)
- [OpenStoa](https://www.openstoa.xyz) 📇 ☁️ - ZK-gated community where humans and AI agents coexist. Agents authenticate via Google OIDC zero-knowledge proofs, join topic discussions, post, comment, and chat. Topics can be gated by Coinbase KYC, Country, Google Workspace, or Microsoft 365 proofs. Agent Card at [openstoa.xyz/.well-known/agent-card.json](https://www.openstoa.xyz/.well-known/agent-card.json). 🏅 1st Place at The Synthesis Hackathon ("Agents That Keep Secrets" track, April 2026).

### 🔄 <a name="integration-services"></a>Integration Services

A2A servers that bridge to various APIs, platforms, and services.

- [Pinchwork](https://github.com/anneschuth/pinchwork) 🐍 ☁️ - Open-source agent-to-agent task marketplace with A2A Agent Card. Agents register, post tasks, pick up work, and earn credits. Serves Agent Card at `/.well-known/agent-card.json` for discovery.

- [Agent Café](https://github.com/brcrusoe72/agent-cafe) 🐍 ☁️ - Agent marketplace with behavioral trust scoring, job bidding, Stripe payments, and prompt injection defense. Agents register, browse jobs, bid, deliver, and build computed reputation. Discovery via `/.well-known/agent-card.json`. Live at [thecafe.dev](https://thecafe.dev).

### 🛠️ <a name="developer-tools"></a>Developer Tools

A2A servers for software development, coding, version control, and DevOps.

- [EmilLindfors/a2a-rs](https://github.com/EmilLindfors/a2a-rs) 🦀 🏠 - A Rust implementation of the A2A protocol that follows idiomatic Rust practices and hexagonal architecture principles. Features both client and server implementations, multiple transport options (HTTP and WebSocket), streaming support, and async/sync interfaces with flexible feature flags.
- [k-jarzyna/adk-modular-architecture](https://github.com/k-jarzyna/adk-modular-architecture) 🐍 🏠 - A flexible, multi-agent system for automating the presales process using Google's Agent Development Kit.
- [yeeaiclub/a2a-go](https://github.com/yeeaiclub/a2a-go) 🏎️ 🏠 - A Go implementation of the A2A protocol with middleware support, authentication, and complete protocol methods. Features high compatibility with the official a2a-python structure and interfaces.
- [Swival/swival](https://github.com/Swival/swival) 🐍 ☁️ 🏠 - A CLI coding agent with full A2A v1.0 client and server support. Works with any LLM provider including local models, with graduated context management designed for tight context windows.
- [Intelligent-Internet/opencode-a2a](https://github.com/Intelligent-Internet/opencode-a2a) 🐍 ☁️ - Full A2A Protocol implementation exposing OpenCode as an interoperable A2A service, focused on practical local + remote task execution for operator workflows.
- [liujuanjuan1984/codex-a2a](https://github.com/liujuanjuan1984/codex-a2a) 🐍 ☁️ - Full A2A Protocol implementation that exposes Codex runtimes through the A2A interface with task lifecycle, artifact, and session handling.

### 🧠 <a name="knowledge-services"></a>Knowledge Services

A2A servers for knowledge management, document handling, and information extraction.

*No entries yet. [Contribute](CONTRIBUTING.md)!*

### 📊 <a name="data-services"></a>Data Services

A2A servers for data processing, analytics, and database integration.

- [Cerebrus Pulse](https://cerebruspulse.xyz) 🐍 ☁️ 🐧 - Institutional-grade crypto derivatives intelligence via A2A + x402 micropayments. Multi-timeframe confluence scoring, regime detection, and open interest analysis for 51 perpetual markets. Pay-per-query with USDC on Base. Agent Card: [api.cerebruspulse.xyz/.well-known/agent-card.json](https://api.cerebruspulse.xyz/.well-known/agent-card.json)

### 🚆 <a name="travel-and-transportation"></a>Travel & Transportation

A2A servers for travel planning, booking, and transportation services.

*No entries yet. [Contribute](CONTRIBUTING.md)!*

## Frameworks
## [Hashgraph Online (HOL)](https://hol.org)
Universal agentic registry on Hedera Hashgraph with HCS-14 UAIDs. Bridges to A2A, ERC-8004, Virtuals, and x402 protocols.

Tools and frameworks for building A2A servers.

- [Google Agent Development Kit (ADK)](https://github.com/google/A2A) 🎖️ 🐍 - Google's framework for building A2A-compliant agents.
- [LangGraph](https://github.com/langchain-ai/langgraph) 🐍 - A framework for building stateful, multi-actor applications with LLMs, with A2A support.
- [CrewAI](https://github.com/crewai/crewai) 🐍 - Framework for orchestrating role-playing, autonomous AI agents with A2A support.
- [JamJet](https://github.com/jamjet-labs/jamjet) 🦀 🐍 - Durable, agent-native AI runtime with native A2A support. Rust core with Python authoring. Features graph-based workflows, durable execution, multi-agent coordination, and built-in MCP client + server.
- [Retool Agents](https://docs.retool.com/agents/concepts/a2a) ☁️ - Framework for building operational agents on top of business data with A2A support. 
- [OpenAgents](https://github.com/openagents-org/openagents) 🐍 - Open-source multi-agent platform with native A2A protocol support, plus MCP, WebSocket, gRPC, and HTTP. Build AI agent networks where multiple agents connect, communicate, and collaborate.
- [Inai](https://github.com/ch4r10t33r/inai) 📇 🐍 🦀 🏠 ☁️ - Framework for scaffolding and running P2P-discoverable, DID-native AI agents across TypeScript, Python, Rust, and Zig. Features libp2p-based peer discovery, ANR (Agent Name Records), on-chain discovery via ERC-8004, and multi-framework support for LangGraph, CrewAI, Google ADK, Agno, LlamaIndex, and smolagents.

## Utilities

Auxiliary tools that help with A2A server development, testing, and deployment.

- [UCP JavaScript SDK](https://github.com/OmnixHQ/ucp-js-sdk) 📇 - Runtime-validated Zod schemas and TypeScript types for the Universal Commerce Protocol. Auto-generated from the UCP JSON Schema spec with 100% coverage — checkout, orders, payments, payment handlers, fulfillment, discounts, buyer consent, AP2 mandates, discovery profiles (platform & business), identity linking, catalog, cart, and all inline enums. Supports MCP, A2A, REST, and Embedded transport bindings. Dual ESM/CJS build. Available on [npm](https://www.npmjs.com/package/@omnixhq/ucp-js-sdk).

- [TheRaLabs/legion-a2a](https://github.com/TheRaLabs/legion-a2a) 🐍 - A robust Python implementation of the A2A protocol with both Pydantic v2 and dataclass model implementations. Provides type-safe communication between agents with complete support for task management, messaging, file/data transfer, status updates, and error handling. Maintained by Legion AI.

- [pcingola/a2a_min](https://github.com/pcingola/a2a_min) 🐍 - A minimalistic Python SDK for Agent-to-Agent (A2A) communication. Features include client for communicating with A2A-compatible agents, server for implementing A2A-compatible agents, support for streaming responses, push notification support, and task management.

- [Gatana](https://www.gatana.ai/) ☁️ - An MCP gateway for Agent-to-Agent systems. Features access token trust, claim mapping, and flexible credential management to allow any token to access MCP tools.
- [Autonomous Commune](https://commune.autonomous-commune.ai/) Python Cloud - Live A2A marketplace for 12 autonomous AI agents spanning DeFi and TradFi. 52 pay-per-use services via USDC micropayments on Base L2 (x402 protocol). Agents include: Shrike (liquidation/MEV), Argus (intelligence), Ouroboros (derivatives), Dullahan (security), Fafnir (treasury), Kairos (options). [Agent Card](https://commune.autonomous-commune.ai/.well-known/agent.json)
- [liujuanjuan1984/a2a-client-hub](https://github.com/liujuanjuan1984/a2a-client-hub) 🐍 🏠 - A self-hosted A2A client hub for managing and invoking multiple agents across web/mobile clients with authentication and session-aware routing.

## Contributing

Your contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).
