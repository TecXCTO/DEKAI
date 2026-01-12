from mcp.server.fastmcp import FastMCP

# 2026 Standard: FastMCP for quick tool exposure
mcp = FastMCP("EngineeringKnowledgeBase")

@mcp.tool()
def get_material_specs(material_name: str) -> str:
    """Retrieve thermal and mechanical properties for a material."""
    # Logic to fetch from internal engineering database
    return f"Spec for {material_name}: Yield Strength 250MPa, Thermal Cond: 50W/mK"

@mcp.resource("config://safety-standards")
def get_safety_rules() -> str:
    """Provides current 2026 mechanical safety regulations."""
    return "All moving joints require a 15% torque buffer."

if __name__ == "__main__":
    mcp.run()
  
