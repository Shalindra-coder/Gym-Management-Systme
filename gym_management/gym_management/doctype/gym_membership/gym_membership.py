# Copyright (c) 2024, shalindra and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GymMembership(Document):
	def before_save(self):
		self.total_amount = self.membership_how_many_months*self.price
