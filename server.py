from mcp.server.fastmcp import FastMCP

from utils import api_request

mcp = FastMCP("appointment-booker")


@mcp.tool()
async def get_agent_availability():
    data = await api_request("/shifts/")

    if not data:
        return "Unable to fetch the user data."

    return data


if __name__ == "__main__":
    mcp.run(transport="stdio")
