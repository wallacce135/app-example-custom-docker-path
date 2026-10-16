import os

import redis
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
cache = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"))
compose_path = os.getenv("APP_COMPOSE_PATH", "unknown")


@app.get("/")
def index() -> str:
    visits = cache.incr("visits")
    return (
        "<h1>Timeweb Cloud + Flask = ❤️</h1>"
        f"<p>Compose: <code>{escape(compose_path)}</code></p>"
        f"<p>Visits: {visits}</p>"
    )


@app.get("/health")
def health() -> dict[str, str]:
    cache.ping()
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
