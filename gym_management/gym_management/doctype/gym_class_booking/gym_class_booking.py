# Copyright (c) 2024, shalindra and contributors
# For license information, please see license.txt

# Import necessary module
from frappe.model.document import Document
import frappe

class GymClassBooking(Document):
    def validate(self):
        existing_bookings = frappe.get_all(
            "Gym Class Booking",
            filters={
                "trainer": self.trainer,
                "class_time": self.class_time,
                "name": ["!=", self.name],
            },
        )

        if existing_bookings:
            frappe.throw(
                f"Trainer {self.trainer} is already booked at {self.class_time}. Please select another time or trainer."
            )
