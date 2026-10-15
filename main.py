import os
import staypresent

staypresent.web.json({"status": "running"})

staypresent.run(
    "bot.py",
    port=int(os.getenv("PORT", 8080)),
    restart_on_crash=True,
    max_restarts=5
)
