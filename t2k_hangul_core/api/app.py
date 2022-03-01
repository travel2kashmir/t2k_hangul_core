from fastapi import FastAPI
from .routes import home
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="T2K Core"
)

# Trying CORS Middleware
# from fastapi.middleware.cors import CORSMiddleware
#
# api.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(home.router)


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Travel2Kashmir</title>
        </head>
        <body>
            <h1>Travel2Kashmir</h1>
        </body>
    </html>
    """
