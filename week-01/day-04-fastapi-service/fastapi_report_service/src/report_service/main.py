from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from report_service.db import get_db
from report_service.models import ReportRequest
from report_service.schemas import ReportRequestCreate, ReportRequestRead


app = FastAPI(title="Report Service Exercise")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/report-requests/{request_id}", response_model=ReportRequestRead)
def get_report_request(
    request_id: int,
    db: Session = Depends(get_db),
) -> ReportRequestRead:
    # Intentionally too heavy for Day 4:
    # this route mixes HTTP concerns, data access, and business rules.
    row = db.get(ReportRequest, request_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Report request not found")

    if row.window_days < 7 or row.window_days > 90:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Stored report request has invalid window_days",
        )

    return ReportRequestRead.model_validate(row)


@app.post(
    "/report-requests",
    response_model=ReportRequestRead,
    status_code=status.HTTP_201_CREATED,
)
def create_report_request(
    payload: ReportRequestCreate,
    db: Session = Depends(get_db),
) -> ReportRequestRead:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implement create_report_request with service, repository, and tests",
    )
