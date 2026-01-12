# DEKAI
Domain Expert Knowledge AI

```
The standard for a Domain Expert AI repository uses Model Context Protocol (MCP) for data connectivity and Agent Skills for specialized engineering reasoning.
GitHub Repository Architecture
This architecture separates user identity, specialized engineering data, and agent reasoning.

DEKAI
├── .github/
│   └── skills/                # 1. AGENTIC SKILLS (Specialized Reasoning)
│       └── mechatronics/
│           └── SKILL.md       # Multi-step instructions for robotics/mechanics
├── core/                      # 2. AGENTIC ORCHESTRATOR
│   ├── main.py                # Entry point: Integrates Identity + Domain
│   └── orchestrator.py        # Logic to route queries to specialized agents
├── domain/                    # 3. KNOWLEDGE BASE (RAG)
│   ├── mechanics/             # ISO standards, material stress tables
│   └── manufacturing/         # 2026 standards for additive manufacturing
├── infra/                     # 4. CONNECTIVITY LAYER (MCP)
│   └── mcp-servers/
│       ├── engineering_db.py  # Bridge to CAD/PLM databases
│       └── simulation_tool.py # Bridge to FEA/CFD simulation engines
├── agents/                    # 5. SPECIALIZED WORKERS
│   ├── mechanics_agent.py     # Worker for solid mechanics tasks
│   └── control_agent.py       # Worker for robotics & PID tuning
└── evaluation/                # 6. EXPERT VALIDATION
    └── test_sets/             # Industry-specific benchmark cases
Use code with caution.

Core Files & Implementation
1. The Expert Skill Definition
In 2026, a SKILL.md file with YAML frontmatter is the standard way to define specialized behaviors for AI agents.
File: .github/skills/mechatronics/SKILL.md
markdown
---
name: MechatronicsDesignExpert
description: Expert in robotic kinematics, sensor integration, and control loops.
---
# Mechatronics Design Expert

## Instructions
1. **Safety First**: Every proposed robotic path must follow ISO 10218 standards.
2. **Analysis**: Use the `simulation_tool` to run stress analysis before suggesting CAD changes.
3. **Control**: When tuning PIDs, always verify the Nyquist stability criterion.

## Guidelines
- Always prioritize 2026 energy-efficient components.
- Never suggest modifications to production hardware without an FEA simulation log.
Use code with caution.

2. The Model Context Protocol (MCP) Server
The MCP server allows the AI to securely "browse" and "use" specialized engineering tools like CAD software or local databases.
File: infra/mcp-servers/engineering_db.py
python
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
Use code with caution.

3. Agentic Orchestrator
This file bridges your Identity AI (user context) with the Domain Expert tools.
File: core/orchestrator.py
python
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

class DomainOrchestrator:
    def __init__(self, identity_profile):
        self.user = identity_profile
        self.server_params = StdioServerParameters(
            command="python", 
            args=["infra/mcp-servers/engineering_db.py"]
        )

    async def execute_task(self, query: str):
        # 1. Identity Check: Ensure user has 'Engineer' role
        if self.user.role != "SeniorEngineer":
            return "Unauthorized for engineering tool execution."

        # 2. Connect to Domain MCP Server
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                # 3. Route to Domain Expert Agent
                # Agent uses SKILL.md instructions to decide tool calls
                response = await session.call_tool("get_material_specs", {"material_name": "Steel"})
                return f"Expert Analysis: {response.content}"
Use code with caution.

4. Automated Knowledge Sync (RAG)
Ensures your AI has the most current engineering documents indexed.
File: domain/sync_knowledge.py
python
import firecrawl # 2026 standard for high-fidelity technical web-scraping

def update_standards():
    app = firecrawl.FirecrawlApp(api_key="your_key")
    # Scrape 2026 ISO updates and convert to clean Markdown for RAG
    result = app.scrape_url("www.iso.org")
    
    with open("domain/mechanics/2026_standards.md", "w") as f:
        f.write(result['markdown'])

```
