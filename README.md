# MCP Weather Server

A simple **Model Context Protocol (MCP) server** that provides current weather information for **Delhi, India** using the [Open-Meteo API](https://open-meteo.com/).

## 📌 Features

* Built with Python
* Uses MCP `MCPServer`
* Provides a `get_weather` MCP tool
* Fetches real-time weather data from Open-Meteo
* Provides an example MCP resource using `echo://`
* Uses asynchronous HTTP requests with `httpx`

## 🛠️ Technologies

* Python 3.12+
* MCP
* httpx
* Open-Meteo API
* uv

## 📁 Project Structure

```text
MCP-Weather/
│
├── weather_server.py
├── README.md
└── pyproject.toml
```

## ⚙️ Installation

Create a project:

```powershell
uv init
```

Install dependencies:

```powershell
uv add "mcp[cli]" httpx
```

## 🚀 Run the Server

Run the MCP server:

```powershell
uv run python weather_server.py
```

For MCP development/testing:

```powershell
uv run mcp dev weather_server.py
```

## 🔧 Available MCP Tool

### `get_weather`

Gets the current weather for Delhi.

Example:

```text
get_weather("Delhi")
```

Example response:

```text
Weather for Delhi, India

Temperature: 29.4 °C
Feels Like: 31.2 °C
Humidity: 62%
Wind Speed: 12.5 km/h
```

> Weather values change because they are retrieved from the weather API.

## 📚 MCP Resource

The server also provides an example resource:

```text
echo://{message}
```

Example:

```text
echo://Hello MCP
```

Response:

```text
Resource echo: Hello MCP
```

## 🔄 How It Works

```text
User
  ↓
AI Agent
  ↓
MCP Client
  ↓
MCP Weather Server
  ↓
get_weather()
  ↓
Open-Meteo API
  ↓
Weather Data
  ↓
AI Agent
  ↓
User
```

## 🧠 What This Project Demonstrates

This project demonstrates the basic concepts of **MCP**:

* MCP Server
* MCP Tools
* MCP Resources
* API integration
* Async Python
* External data access through an AI-compatible interface

## ⚠️ Current Limitation

The example currently supports **Delhi, India** only.

The coordinates used are:

```text
Latitude: 28.6139
Longitude: 77.2090
```

The project can later be extended to support any city by using a geocoding API.

## 📄 License

This project is for learning and educational purposes.
