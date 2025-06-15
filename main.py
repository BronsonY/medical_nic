from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import institute, course, candidate, round, allocation, institutequota

app = FastAPI(
    title="College Counselling API",
    description="API for managing institutes, courses, candidates, rounds, and allocations.",
    version="1.0.0"
)

# CORS setup
origins = [
    "*",
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # Add production domains here, e.g., "https://yourfrontend.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],   # Allow all headers
)

# Include routers with their prefixes + tags
app.include_router(institute.router, prefix="/api/institutes", tags=["Institutes"])
app.include_router(course.router, prefix="/api/courses", tags=["Courses"])
app.include_router(candidate.router, prefix="/api/candidates", tags=["Candidates"])
app.include_router(round.router, prefix="/api/rounds", tags=["Rounds"])
app.include_router(allocation.router, prefix="/api/allocations", tags=["Allocations"])
app.include_router(institutequota.router, prefix="/api/institutequota", tags=["Quota"])
