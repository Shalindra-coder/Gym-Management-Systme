# Copyright (c) 2024, shalindra and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe import _

class GymMember(Document):
    def before_save(self):
        if not self.start_date:
            frappe.throw(_("Start Date is required."))
