from fastmcp import FastMCP

# Replace this with your actual Render URL
REMOTE_URL = "https://expense-tracker-mcp-ccbeb254.onrender.com/sse" 

# Create a local proxy that forwards requests to the remote server
mcp = FastMCP.as_proxy(
    url=REMOTE_URL,
    name="Remote Expense Proxy"
)

if __name__ == "__main__":
    mcp.run() # This runs in stdio mode (the default), which Claude/Cursor likes