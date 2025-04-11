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

* 👖‍ — official implementation
* programming language
  * 🐍 — Python codebase
  * 📗 — TypeScript/JavaScript codebase
  * 🏎️‍ — Go codebase
  * 🦀 — Rust codebase
  * #️⃣🎮 - C# Codebase
  * ☕ - Java codebase
* scope
  * ⚁‍ - Cloud Service
  * 🏠 - Local Service
  * 📟 - Embedded Systems
* operating system
  * 🍎 — For macOS
  * 🏯 — For Windows
  * 🐧 - For Linux

> [!NOTE]
> Confused about Local 🏠 vs Cloud ⚁‍?
> * Use local when A2A server is talking to a locally installed software.
> * Use cloud when A2A server is talking to remote APIs, like Google Maps API.

## Server Implementations

* 👖‍ - [Official Samples](#official-samples)
* 🗺️‍ - [Location Services](#location-services)
* 🏢 - [Business Tools](#business-tools)
* 🖼️‍ - [Image Generation](#image-generation)
* 🏦 - [Financial Services](#financial-services)
* 🔎 - [Search & Data Extraction](#search-and-data-extraction)
* 🏬 - [Communication Services](#communication-services)
* 🔄 - [Integration Services](#integration-services)
* 👨‍💻‍ - [Developer Tools](#developer-tools)
* 🧠 - [Knowledge Services](#knowledge-services)
* 📊 - [Data Services](#data-services)
* 🚆 - [Travel & Transportation](#travel-and-transportation)

### 👖‍ <a name="official-samples"></a>Official Samples

Official sample implementations from the Google A2A repository.

- [google/google_adk](https://github.com/google/A2A/tree/main/samples/python/agents/google_adk) 👖‍ 🐍 🏠 - An expense reimbursement agent built with Google Agent Development Kit (ADK). Showcases multi-turn interactions and webform handling through the A2A protocol.

- [google/langgraph](https://github.com/google/A2A/tree/main/samples/python/agents/langgraph) 👖‍ 🐍 ⚁‍ - A currency conversion agent built with LangGraph. Showcases multi-turn interactions, tool usage for currency exchange via Frankfurter API, and streaming updates through the A2A protocol.

- [google/crewai](https://github.com/google/A2A/tree/main/samples/python/agents/crewai) 👖‍ 🐍 ⚁‍ - An image generation agent built with CrewAI. Showcases text-to-image generation using Google Gemini API and returning images as artifacts through the A2A protocol.

### 🗺️‍ <a name="location-services"></a>Location Services

A2A servers providing mapping, geocoding, navigation, and other location-based services.

- [pab1it0/google-maps-a2a](https://github.com/pab1it0/google-maps-a2a) 🐍 ⚁‍ - An A2A-compliant server that provides Google Maps capabilities including geocoding, reverse geocoding, directions, places search, place details, and distance matrix calculations. Supports multiple input/output formats and provides a standardized agent card for capability discovery.

### 🏢 <a name="business-tools"></a>Business Tools

A2A servers for business operations, expense management, and other enterprise functions.

*See [google/google_adk](#official-samples) for an example expense reimbursement tool.*

### 🖼️‍ <a name="image-generation"></a>Image Generation

A2A servers for generating and manipulating images.

*See [google/crewai](#official-samples) for an example image generation tool.*

### 🏦 <a name="financial-services"></a>Financial Services

A2A servers for financial operations, currency conversion, and financial data.

*See [google/langgraph](#official-samples) for an example currency conversion tool.*

### 🔎 <a name="search-and-data-extraction"></a>Search & Data Extraction

A2A servers for search, data retrieval, and information extraction.

*No additional entries yet. [Contribute](CONTRIBUTING.md)!*

### 🏬 <a name="communication-services"></a>Communication Services

A2A servers for messaging, email, and other communication tools.

*No entries yet. [Contribute](CONTRIBUTING.md)!*

### 🔄 <a name="integration-services"></a>Integration Services

A2A servers that bridge to various APIs, platforms, and services.

*No entries yet. [Contribute](CONTRIBUTING.md)!*

### 👨‍💻‍ <a name="developer-tools"></a>Developer Tools

A2A servers for software development, coding, version control, and DevOps.

- [EmilLindfors/a2a-rs](https://github.com/EmilLindfors/a2a-rs) 🦀 🏠 - A Rust implementation of the A2A protocol that follows idiomatic Rust practices and hexagonal architecture principles. Features both client and server implementations, multiple transport options (HTTP and WebSocket), streaming support, and async/sync interfaces with flexible feature flags.

### 🧠 <a name="knowledge-services"></a>Knowledge Services

A2A servers for knowledge management, document handling, and information extraction.

*No entries yet. [Contribute](CONTRIBUTING.md)!*

### 📊 <a name="data-services"></a>Data Services

A2A servers for data processing, analytics, and database integration.

*No entries yet. [Contribute](CONTRIBUTING.md)!*

### 🚆 <a name="travel-and-transportation"></a>Travel & Transportation

A2A servers for travel planning, booking, and transportation services.

*No entries yet. [Contribute](CONTRIBUTING.md)!*

## Frameworks

Tools and frameworks for building A2A servers.

- [Google Agent Development Kit (ADK)](https://github.com/google/A2A) 👖‍ 🐍 - Google's framework for building A2A-compliant agents.
- [LangGraph](https://github.com/langchain-ai/langgraph) 🐍 - A framework for building stateful, multi-actor applications with LLMs, with A2A support.
- [CrewAI](https://github.com/crewai/crewai) 🐍 - Framework for orchestrating role-playing, autonomous AI agents with A2A support.

## Utilities

Auxiliary tools that help with A2A server development, testing, and deployment.

*No entries yet. [Contribute](CONTRIBUTING.md)!*

## Contributing

Your contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).