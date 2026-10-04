import os
import re
import sqlite3
from contextlib import contextmanager

from plants_data import PLANTS
from problems_data import PROBLEMS, SYMPTOMS
from translations import NAMES as PLANT_NAMES
from translations import PROBLEMS as PROBLEM_NAMES
from translations import TEXT as PLANT_TEXT

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_NAME = os.environ.get(
    "NURSERYIQ_DB", os.path.join(BASE_DIR, "nurseryiq.db")
)

# Bump this whenever the schema or the seed data changes.
# On startup an out-of-date database is rebuilt automatically.
SCHEMA_VERSION = 3

VALID_SEASONS = ("summer", "monsoon", "winter")
SEVERITY_WEIGHT = {"high": 3, "medium": 2, "low": 1}


# =========================================================
# CONNECTION
# =========================================================

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


@contextmanager
def db():
    """Open a connection and always close it, even if a query fails."""
    connection = get_connection()
    try:
        yield connection
    finally:
        connection.close()


# =========================================================
# SCHEMA + SEED
# =========================================================

def create_database():
    with db() as connection:
        connection.executescript("""
            DROP TABLE IF EXISTS plants;
            DROP TABLE IF EXISTS problems;

            CREATE TABLE plants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                scientific_name TEXT NOT NULL,
                emoji TEXT NOT NULL,
                category TEXT NOT NULL,
                tags TEXT NOT NULL,
                sun TEXT NOT NULL,
                water TEXT NOT NULL,
                environment TEXT NOT NULL,
                difficulty TEXT NOT NULL,
                temperature TEXT,
                soil TEXT,
                seasons TEXT NOT NULL,
                description TEXT,
                care_instructions TEXT
            );

            CREATE TABLE problems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                emoji TEXT NOT NULL,
                symptoms TEXT NOT NULL,
                cause TEXT,
                solution TEXT,
                severity TEXT NOT NULL
            );

            CREATE INDEX idx_plants_category ON plants(category);
        """)
        connection.commit()


def add_sample_plants():
    rows = [
        (
            p["name"], p["scientific_name"], p["emoji"], p["category"],
            ",".join(p["tags"]), p["sun"], p["water"],
            ",".join(p["environment"]), p["difficulty"], p["temperature"],
            p["soil"], ",".join(p["seasons"]), p["description"], p["care"],
        )
        for p in PLANTS
    ]

    with db() as connection:
        connection.executemany("""
            INSERT INTO plants (
                name, scientific_name, emoji, category, tags, sun, water,
                environment, difficulty, temperature, soil, seasons,
                description, care_instructions
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, rows)
        connection.commit()


def add_sample_problems():
    rows = [
        (
            p["name"], p["emoji"], ",".join(p["symptoms"]),
            p["cause"], p["solution"], p["severity"],
        )
        for p in PROBLEMS
    ]

    with db() as connection:
        connection.executemany("""
            INSERT INTO problems (name, emoji, symptoms, cause, solution, severity)
            VALUES (?, ?, ?, ?, ?, ?)
        """, rows)
        connection.commit()


def initialize_database():
    """Create and seed the database, rebuilding it if the schema is old."""
    with db() as connection:
        current = connection.execute("PRAGMA user_version").fetchone()[0]

    if current == SCHEMA_VERSION:
        return

    create_database()
    add_sample_plants()
    add_sample_problems()

    with db() as connection:
        # PRAGMA does not accept bound parameters.
        connection.execute(f"PRAGMA user_version = {int(SCHEMA_VERSION)}")
        connection.commit()


# =========================================================
# ROW -> JSON
# =========================================================

def _split(value):
    return [item for item in (value or "").split(",") if item]


def slugify(name):
    """'Bird's Nest Fern' -> 'birds-nest-fern' (also the image file name)."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace("'", "")).strip("-")


def plant_to_dict(row):
    name = row["name"]
    names = PLANT_NAMES.get(name, {})

    # Translated description / care tips are optional (see translations.py).
    texts = {
        lang: {"description": pair[0], "care": pair[1]}
        for lang, table in PLANT_TEXT.items()
        for pair in [table.get(name)]
        if pair
    }

    return {
        "slug": slugify(name),
        # Downloaded by fetch_images.py; the page falls back to the emoji.
        "image": f"images/plants/{slugify(name)}.jpg",
        "names": names,
        "texts": texts,
        "id": row["id"],
        "name": name,
        "scientificName": row["scientific_name"],
        "emoji": row["emoji"],
        "category": row["category"],
        "tags": _split(row["tags"]),
        "sun": row["sun"],
        "water": row["water"],
        "environment": _split(row["environment"]),
        "difficulty": row["difficulty"],
        "temperature": row["temperature"],
        "soil": row["soil"],
        "seasons": _split(row["seasons"]),
        "description": row["description"],
        "care": row["care_instructions"],
    }


def problem_to_dict(row):
    return {
        "id": row["id"],
        "name": row["name"],
        "names": PROBLEM_NAMES.get(row["name"], {}),
        "emoji": row["emoji"],
        "symptoms": _split(row["symptoms"]),
        "cause": row["cause"],
        "solution": row["solution"],
        "severity": row["severity"],
    }


def _clean(value):
    """Treat '', None and 'all' as 'no filter'."""
    if value is None:
        return None
    value = str(value).strip().lower()
    return None if value in ("", "all", "any") else value


def _all_plants():
    with db() as connection:
        rows = connection.execute("SELECT * FROM plants ORDER BY name").fetchall()
    return [plant_to_dict(row) for row in rows]


# =========================================================
# PLANT QUERIES
# =========================================================

def list_plants(q=None, category=None, sun=None, water=None, environment=None):
    q = (q or "").strip().lower()
    category, sun, water, environment = (
        _clean(category), _clean(sun), _clean(water), _clean(environment)
    )

    results = []
    for plant in _all_plants():
        if q:
            haystack = " ".join([
                plant["name"], plant["scientificName"], plant["category"],
                " ".join(plant["tags"]), " ".join(plant["names"].values()),
            ]).lower()
            if q not in haystack:
                continue

        if category and category not in [t.lower() for t in plant["tags"]]:
            continue
        if sun and plant["sun"] != sun:
            continue
        if water and plant["water"] != water:
            continue
        if environment and environment not in plant["environment"]:
            continue

        results.append(plant)

    return results


def get_plant(plant_id):
    with db() as connection:
        row = connection.execute(
            "SELECT * FROM plants WHERE id = ?", (plant_id,)
        ).fetchone()
    return plant_to_dict(row) if row else None


def list_categories():
    with db() as connection:
        rows = connection.execute("""
            SELECT category, COUNT(*) AS total
            FROM plants GROUP BY category ORDER BY category
        """).fetchall()
    return [{"name": r["category"], "total": r["total"]} for r in rows]


# =========================================================
# SMART RECOMMENDATION
# =========================================================

def recommend(environment=None, sunlight=None, water=None, experience=None, limit=12):
    """
    Returns (plants, exact).

    Location and experience are hard requirements (a banana tree is never
    "indoor", and beginners only see beginner-friendly plants).
    Sunlight and watering are preferences: if no plant matches both,
    the closest matches are returned with exact=False.

    'Experienced' users can grow anything, so they are not limited by difficulty.
    """
    environment, sunlight, water, experience = (
        _clean(environment), _clean(sunlight), _clean(water), _clean(experience)
    )

    pool = _all_plants()

    if environment:
        pool = [p for p in pool if environment in p["environment"]]
    if experience == "beginner":
        pool = [p for p in pool if p["difficulty"] == "beginner"]

    checks = []
    if sunlight:
        checks.append(lambda p: p["sun"] == sunlight)
    if water:
        checks.append(lambda p: p["water"] == water)

    if not checks:
        return pool[:limit], True

    scored = [(sum(1 for check in checks if check(p)), p) for p in pool]

    exact = [p for score, p in scored if score == len(checks)]
    if exact:
        return exact[:limit], True

    best = max((score for score, _ in scored), default=0)
    if best == 0:
        return [], False

    closest = [p for score, p in scored if score == best]
    return closest[:limit], False


# =========================================================
# SEASONAL GUIDE
# =========================================================

def plants_for_season(season, per_category=2):
    """A varied selection: a couple of plants from every category."""
    season = (season or "").strip().lower()
    matching = [p for p in _all_plants() if season in p["seasons"]]

    picked, counts = [], {}
    for plant in matching:
        count = counts.get(plant["category"], 0)
        if count < per_category:
            picked.append(plant)
            counts[plant["category"]] = count + 1

    return picked, len(matching)


# =========================================================
# PLANT PROBLEMS
# =========================================================

def list_problems():
    with db() as connection:
        rows = connection.execute("SELECT * FROM problems ORDER BY name").fetchall()
    return [problem_to_dict(row) for row in rows]


def diagnose(symptoms, limit=6):
    selected = {s.strip().lower() for s in symptoms} & SYMPTOMS
    if not selected:
        return []

    ranked = []
    for problem in list_problems():
        matched = [s for s in problem["symptoms"] if s in selected]
        if not matched:
            continue

        coverage = len(matched) / len(problem["symptoms"])
        problem["matchedSymptoms"] = matched
        ranked.append((
            len(matched),
            coverage,
            SEVERITY_WEIGHT.get(problem["severity"], 1),
            problem,
        ))

    # Most matching symptoms first, then best coverage, then most serious.
    ranked.sort(key=lambda item: (-item[0], -item[1], -item[2], item[3]["name"]))
    return [item[3] for item in ranked[:limit]]


# =========================================================
# STATS
# =========================================================

def get_stats():
    with db() as connection:
        plants = connection.execute("SELECT COUNT(*) FROM plants").fetchone()[0]
        categories = connection.execute(
            "SELECT COUNT(DISTINCT category) FROM plants"
        ).fetchone()[0]
        problems = connection.execute("SELECT COUNT(*) FROM problems").fetchone()[0]

    return {"plants": plants, "categories": categories, "problems": problems}
