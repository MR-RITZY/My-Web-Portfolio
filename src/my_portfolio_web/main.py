from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()


BASE_DIR = Path(__file__).parent.resolve()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


html_path = BASE_DIR/"static/index.html"

@app.get("/mr-ritzy/portfolio", response_class=HTMLResponse)
async def portfolio():
    return HTMLResponse(
        content=html_path.read_text(encoding="utf-8"),
    )

@app.get("/")
async def home():
    return RedirectResponse(url="/mr-ritzy/portfolio",
                            status_code=status.HTTP_302_FOUND)
