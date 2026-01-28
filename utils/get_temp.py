import asyncio
from typing import List


async def run_cmd(cmd:List[str], timeout:int=5) -> str:
    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await asyncio.wait_for(
            proc.communicate(),
            timeout
        )

        return stdout.decode()

    except asyncio.TimeoutError:
        return "⏱ Команда зависла"
