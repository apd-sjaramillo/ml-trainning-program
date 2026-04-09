from report_utils_everything import load_rows
from report_utils_everything import make_everything
from report_utils_everything import render_report


def run(path=None, minimum_hours=0, country=None, department=None, include_non_billable=True, mode="normal", sort_by="client"):
    rows = load_rows(path)
    data = make_everything(
        rows,
        minimum_hours=minimum_hours,
        country_filter=country,
        department_filter=department,
        include_non_billable=include_non_billable,
        mode=mode,
        sort_by=sort_by,
    )
    return render_report(data)


if __name__ == "__main__":
    print(run())
