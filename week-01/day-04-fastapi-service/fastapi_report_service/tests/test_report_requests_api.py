import pytest


@pytest.mark.skip(reason="Write this refactor test during the Day 4 exercise")
def test_get_report_request_returns_seeded_row(client) -> None:
    response = client.get("/report-requests/1")

    assert response.status_code == 200
    assert response.json()["client_name"] == "Test Client"


@pytest.mark.skip(reason="Write this refactor test during the Day 4 exercise")
def test_get_report_request_returns_404_for_missing_row(client) -> None:
    response = client.get("/report-requests/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Report request not found"}


@pytest.mark.skip(reason="Write this new endpoint test during the Day 4 exercise")
def test_create_report_request_returns_201(client) -> None:
    response = client.post(
        "/report-requests",
        json={
            "client_name": "Launchpad Labs",
            "report_type": "utilization",
            "window_days": 30,
            "requested_by": "launchpad@aimpointdigital.com",
        },
    )

    assert response.status_code == 201
    assert response.json()["status"] == "queued"
