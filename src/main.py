from fastapi import FastAPI
from __init__ import __title__, __version__
from adapters.routers import user


app = FastAPI(title=__title__, version=__version__)

app.include_router(user.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
