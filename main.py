import asyncio
import os
import sys
from aiohttp import web

def install_requirements():
    os.system(f"{sys.executable} -m pip install -r requirements.txt")

async def web_server():
    async def handle(request):
        return web.Response(text="Hello, Queen is running!")

    app = web.Application()
    app.add_routes([web.get('/', handle)])
    return app

async def run_mukesh_robot():
    try:
        process = await asyncio.create_subprocess_exec(
            sys.executable, "-m", "shivu",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            print(f"Error running MukeshRobot: {stderr.decode()}")
    except asyncio.CancelledError:
        process.terminate()
        await process.communicate()
        raise
    except Exception as e:
        print(f"Error running MukeshRobot: {e}")

async def main():
    install_requirements()

    app = await web_server()
    app_runner = web.AppRunner(app)
    await app_runner.setup()

    bind_address = "0.0.0.0"
    PORT = int(os.environ.get("PORT", 8080))  # Use PORT from environment variable or default to 8080
    
    try:
        await web.TCPSite(app_runner, bind_address, PORT).start()

        # Run MukeshRobot as a subprocess concurrently
        await run_mukesh_robot()
    
    finally:
        await app_runner.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
