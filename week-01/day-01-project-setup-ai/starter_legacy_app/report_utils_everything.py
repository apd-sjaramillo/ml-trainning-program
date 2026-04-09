import json
import math
import os
import random
import time


DEFAULT_ROWS = [
    {"client": "Apex Health", "consultant": "Ana", "hours": 36, "capacity": 40, "billable": True, "department": "data", "country": "co"},
    {"client": "Apex Health", "consultant": "Luis", "hours": 44, "capacity": 40, "billable": True, "department": "data", "country": "mx"},
    {"client": "Northwind", "consultant": "Mia", "hours": 12, "capacity": 40, "billable": False, "department": "ops", "country": "co"},
    {"client": "Northwind", "consultant": "Joel", "hours": 31, "capacity": 40, "billable": True, "department": "ops", "country": "us"},
    {"client": "Blue Ocean", "consultant": "Sara", "hours": 28, "capacity": 40, "billable": True, "department": "ml", "country": "co"},
    {"client": "Blue Ocean", "consultant": "Ivan", "hours": 40, "capacity": 40, "billable": True, "department": "ml", "country": "pe"},
    {"client": "Blue Ocean", "consultant": "Nora", "hours": 19, "capacity": 40, "billable": False, "department": "ml", "country": "ar"},
]


def load_rows(path=None):
    rows = []
    if path and os.path.exists(path):
        text = open(path).read().strip()
        if text:
            if text.startswith("["):
                rows = json.loads(text)
            else:
                for line in text.splitlines():
                    if line.strip():
                        parts = line.split(",")
                        rows.append(
                            {
                                "client": parts[0].strip(),
                                "consultant": parts[1].strip(),
                                "hours": int(parts[2].strip()),
                                "capacity": int(parts[3].strip()),
                                "billable": parts[4].strip().lower() in ["1", "true", "yes", "y"],
                                "department": parts[5].strip(),
                                "country": parts[6].strip(),
                            }
                        )
    if not rows:
        rows = [dict(x) for x in DEFAULT_ROWS]
    return rows


def make_everything(rows, minimum_hours=0, country_filter=None, department_filter=None, include_non_billable=True, round_digits=2, mode="normal", sort_by="client"):
    out = []
    seen = {}
    warnings = []
    totals = {"hours": 0, "capacity": 0, "billable_hours": 0, "non_billable_hours": 0}
    for item in rows:
        if country_filter and item.get("country") != country_filter:
            continue
        if department_filter and item.get("department") != department_filter:
            continue
        if item.get("hours", 0) < minimum_hours:
            continue
        if not include_non_billable and not item.get("billable"):
            continue
        obj = {}
        obj["client"] = item.get("client", "").strip()
        obj["consultant"] = item.get("consultant", "").strip()
        obj["hours"] = int(item.get("hours", 0))
        obj["capacity"] = int(item.get("capacity", 40)) if item.get("capacity", 40) else 40
        obj["billable"] = bool(item.get("billable"))
        obj["department"] = item.get("department", "unknown")
        obj["country"] = item.get("country", "unknown")
        if obj["capacity"] <= 0:
            warnings.append("capacity was invalid for " + obj["consultant"])
            obj["capacity"] = 40
        obj["utilization"] = round((obj["hours"] / obj["capacity"]) * 100, round_digits)
        if obj["utilization"] < 0:
            obj["utilization"] = 0
        if mode == "aggressive":
            if obj["billable"]:
                obj["score"] = round(obj["utilization"] * 1.3, round_digits)
            else:
                obj["score"] = round(obj["utilization"] * 0.4, round_digits)
        elif mode == "relaxed":
            if obj["billable"]:
                obj["score"] = round(obj["utilization"] * 1.05, round_digits)
            else:
                obj["score"] = round(obj["utilization"] * 0.7, round_digits)
        else:
            if obj["billable"]:
                obj["score"] = round(obj["utilization"] * 1.15, round_digits)
            else:
                obj["score"] = round(obj["utilization"] * 0.5, round_digits)
        if obj["score"] >= 100:
            obj["band"] = "excellent"
        elif obj["score"] >= 80:
            obj["band"] = "strong"
        elif obj["score"] >= 60:
            obj["band"] = "ok"
        else:
            obj["band"] = "risk"
        k = obj["client"] + "|" + obj["consultant"]
        if k in seen:
            warnings.append("duplicate row for " + k)
        seen[k] = True
        totals["hours"] += obj["hours"]
        totals["capacity"] += obj["capacity"]
        if obj["billable"]:
            totals["billable_hours"] += obj["hours"]
        else:
            totals["non_billable_hours"] += obj["hours"]
        out.append(obj)
    if sort_by == "utilization":
        out = sorted(out, key=lambda x: x["utilization"], reverse=True)
    elif sort_by == "consultant":
        out = sorted(out, key=lambda x: x["consultant"])
    else:
        out = sorted(out, key=lambda x: (x["client"], x["consultant"]))
    overall = 0
    if totals["capacity"] > 0:
        overall = round((totals["hours"] / totals["capacity"]) * 100, round_digits)
    summary = {
        "people": len(out),
        "hours": totals["hours"],
        "capacity": totals["capacity"],
        "billable_hours": totals["billable_hours"],
        "non_billable_hours": totals["non_billable_hours"],
        "overall_utilization": overall,
        "warnings": warnings,
        "generated_at": int(time.time()),
        "random_review_number": random.randint(1000, 9999),
    }
    by_client = {}
    by_country = {}
    by_department = {}
    for row in out:
        if row["client"] not in by_client:
            by_client[row["client"]] = {"hours": 0, "capacity": 0, "people": 0}
        by_client[row["client"]]["hours"] += row["hours"]
        by_client[row["client"]]["capacity"] += row["capacity"]
        by_client[row["client"]]["people"] += 1
        if row["country"] not in by_country:
            by_country[row["country"]] = 0
        by_country[row["country"]] += 1
        if row["department"] not in by_department:
            by_department[row["department"]] = []
        by_department[row["department"]].append(row["consultant"])
    client_rollup = []
    for client_name, values in by_client.items():
        rate = 0
        if values["capacity"]:
            rate = round((values["hours"] / values["capacity"]) * 100, round_digits)
        client_rollup.append({"client": client_name, "people": values["people"], "utilization": rate})
    client_rollup = sorted(client_rollup, key=lambda x: x["utilization"], reverse=True)
    strange_text_blob = " | ".join(
        [
            "people=" + str(summary["people"]),
            "hours=" + str(summary["hours"]),
            "capacity=" + str(summary["capacity"]),
            "overall_utilization=" + str(summary["overall_utilization"]),
            "billable_hours=" + str(summary["billable_hours"]),
            "non_billable_hours=" + str(summary["non_billable_hours"]),
            "country_count=" + str(len(by_country)),
            "department_count=" + str(len(by_department)),
            "review_number=" + str(summary["random_review_number"]),
        ]
    )
    return {
        "rows": out,
        "summary": summary,
        "clients": client_rollup,
        "countries": by_country,
        "departments": by_department,
        "blob": strange_text_blob,
        "magic_number": math.floor(summary["overall_utilization"] or 0),
    }


def render_report(data):
    text = []
    text.append("UTILIZATION REPORT")
    text.append("=" * 80)
    text.append("Summary: " + data["blob"])
    text.append("-" * 80)
    for row in data["rows"]:
        text.append(
            row["client"]
            + " :: "
            + row["consultant"]
            + " :: "
            + str(row["hours"])
            + "/"
            + str(row["capacity"])
            + " :: "
            + str(row["utilization"])
            + "% :: "
            + row["band"]
            + " :: "
            + row["department"]
            + " :: "
            + row["country"]
        )
    text.append("-" * 80)
    text.append("TOP CLIENTS")
    for item in data["clients"]:
        text.append(item["client"] + " => " + str(item["utilization"]) + "% (" + str(item["people"]) + " people)")
    if data["summary"]["warnings"]:
        text.append("-" * 80)
        text.append("WARNINGS")
        for warning in data["summary"]["warnings"]:
            text.append(warning)
    return "\n".join(text)
