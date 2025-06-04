from mcp.server.fastmcp import Context, FastMCP, Image
from mcp.server.fastmcp.prompts import base
from PIL import Image as PILImage

from utils import api_request

mcp = FastMCP("appointment-booker")


@mcp.tool(name="user_shifts")
async def get_agent_availability():
    data = await api_request("/shifts/")

    if not data:
        return "Unable to fetch the user's shift."

    return data


@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")


@mcp.tool()
async def long_task(files: list[str], ctx: Context) -> str:
    """Process multiple files with progress tracking"""
    for i, file in enumerate(files):
        ctx.info(f"Processing {file}")
        await ctx.report_progress(i, len(files))
        data, mime_type = await ctx.read_resource(f"file://{file}")
    return "Processing complete"


@mcp.resource("users://all", name="all_users", mime_type="application/json")
async def get_users():
    users = await api_request("/users/")

    if not users:
        return "Unable to fetch the user data."

    return users


@mcp.prompt()
def appointment_prompt():
    return base.UserMessage(
        """
            You are an AI assistant designed to help users check the availability of agents and book appointments.
            Use the tools provided to get available shifts and users.
            Make sure to respond clearly, and if you need availability data, use the `user_shifts` tool.
            You can also use the `all_users` resource to identify which agents are available.
        """
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
