# Copyright (c) 2024, shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters: dict | None = None):
    """Return columns, data, and chart for the report."""
    columns = get_columns()
    data = get_data()

    # Check if there's data before generating a chart
    chart = get_chart_data(data) if data else None

    return columns, data, None, chart


def get_columns() -> list[dict]:
    """Return columns for the report."""
    return [
        {
            "label": _("Member"),
            "fieldname": "member",
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "label": _("Total Amount"),
            "fieldname": "total_amount",
            "fieldtype": "Currency",
            "width": 150,
        },
    ]


def get_data() -> list[dict]:
    """Fetch data from Gym Membership DocType."""
    try:
        return frappe.db.get_all(
            "Gym Membership",
            fields=["member", "total_amount"],
            order_by="creation desc",
        )
    except Exception as e:
        frappe.log_error(message=str(e), title="Error in Gym Membership Report")
        return []


def get_chart_data(data: list[dict]) -> dict:
    """Generate pie chart data from the fetched report data."""
    labels = [row["member"] for row in data]
    values = [row["total_amount"] for row in data]

    return {
        "data": {
            "labels": labels,
            "datasets": [{"values": values}],
        },
        "type": "pie",  # Chart type: pie
        "title": _("Revenue Distribution by Member"),
    }
