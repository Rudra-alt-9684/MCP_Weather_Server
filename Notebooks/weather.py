from typing import Any
import httpx

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("weather")


async def make_request(url: str) -> dict[str, Any] | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None


@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for a city.

    Currently supports Delhi, India.
    """

    if city.lower() != "delhi":
        return "Currently this example only supports Delhi."

    # Delhi coordinates
    latitude = 28.6139
    longitude = 77.2090

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,"
        "apparent_temperature,wind_speed_10m"
    )

    data = await make_request(url)

    if not data or "current" not in data:
        return "Unable to fetch weather data."

    current = data["current"]

    return f"""
Weather for Delhi, India

Temperature: {current["temperature_2m"]} °C
Feels Like: {current["apparent_temperature"]} °C
Humidity: {current["relative_humidity_2m"]}%
Wind Speed: {current["wind_speed_10m"]} km/h
"""


@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    return f"Resource echo: {message}"


if __name__ == "__main__":
    mcp.run()