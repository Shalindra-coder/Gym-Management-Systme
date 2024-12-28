
import frappe

def execute():
    trainers = frappe.get_all('Trainer',pluck="name")

    for t in trainers:
     trainer =   frappe.db.set_value('Trainer',t)
     trainer.set_title()
     trainer.save()

    frappe.db.commit()
