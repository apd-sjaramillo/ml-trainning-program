from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ReportRequestCreate(BaseModel):
    client_name: str = Field(min_length=3, max_length=100)
    report_type: Literal["utilization", "forecast", "cost"]
    window_days: int
    requested_by: EmailStr


class ReportRequestRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_name: str
    report_type: str
    window_days: int
    requested_by: str
    status: str
