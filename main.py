from contextlib import asynccontextmanager
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from starlette.exceptions import HTTPException as StarletteHTTPException

import database as db


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.initialize_database()
    yield


app = FastAPI(title="NurseryIQ API", version="2.0.0", lifespan=lifespan)

# The API is public and read-only (no cookies / logins), so any origin may call it.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# ERRORS: always answer with {"success": false, "message": ...}
# which is what script.js expects.
# =========================================================

@app.exception_handler(StarletteHTTPException)
async def http_error_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": str(exc.detail)},
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"success": False, "message": "Invalid request data"},
    )


# =========================================================
# REQUEST MODELS
# =========================================================

class RecommendRequest(BaseModel):
    environment: Optional[str] = "all"
    sunlight: Optional[str] = "all"
    water: Optional[str] = "all"
    experience: Optional[str] = "all"


class DiagnoseRequest(BaseModel):
    symptoms: List[str] = Field(default_factory=list)


# =========================================================
# ROUTES
# =========================================================

@app.get("/")
def home():
    return {"success": True, "message": "NurseryIQ Backend is working"}


@app.get("/api/stats")
def get_stats():
    return {"success": True, **db.get_stats()}


@app.get("/api/plants")
def get_plants(
    q: Optional[str] = None,
    category: Optional[str] = None,
    sun: Optional[str] = None,
    water: Optional[str] = None,
    environment: Optional[str] = None,
):
    plants = db.list_plants(q, category, sun, water, environment)
    return {"success": True, "plants": plants, "total": len(plants)}


# Must be declared before /api/plants/{plant_id}, or "search" is read as an id.
@app.get("/api/plants/search")
def search_plants(q: str = Query(..., min_length=1)):
    plants = db.list_plants(q=q)
    return {"success": True, "query": q, "plants": plants, "total": len(plants)}


@app.get("/api/plants/{plant_id}")
def get_plant(plant_id: int):
    plant = db.get_plant(plant_id)

    if plant is None:
        raise HTTPException(status_code=404, detail="Plant not found")

    return {"success": True, "plant": plant}


@app.get("/api/categories")
def get_categories():
    categories = db.list_categories()
    return {"success": True, "categories": categories, "total": len(categories)}


@app.post("/api/recommend")
def recommend_plants(request: RecommendRequest):
    plants, exact = db.recommend(
        request.environment, request.sunlight, request.water, request.experience
    )

    if not plants:
        message = "No plants matched. Try selecting fewer conditions."
    elif not exact:
        message = "No exact match, so these are the closest plants to your choices."
    else:
        message = f"Found {len(plants)} suitable plant(s)."

    return {
        "success": True,
        "exact": exact,
        "message": message,
        "plants": plants,
        "total": len(plants),
    }


@app.get("/api/problems")
def get_problems():
    problems = db.list_problems()
    return {"success": True, "problems": problems, "total": len(problems)}


@app.post("/api/diagnose")
def diagnose_plant(request: DiagnoseRequest):
    if not request.symptoms:
        raise HTTPException(status_code=400, detail="Select at least one symptom")

    problems = db.diagnose(request.symptoms)
    return {"success": True, "problems": problems, "total": len(problems)}


@app.get("/api/season/{season}")
def get_season_plants(season: str):
    season = season.lower()

    if season not in db.VALID_SEASONS:
        raise HTTPException(
            status_code=404,
            detail="Season must be summer, monsoon or winter",
        )

    plants, total = db.plants_for_season(season)
    return {
        "success": True,
        "season": season,
        "plants": plants,
        "shown": len(plants),
        "total": total,
    }
