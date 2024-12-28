// Copyright (c) 2024, shalindra and contributors
// For license information, please see license.txt


frappe.ui.form.on("Gym Class Booking", {
    validate(frm) {
        let class_date = frm.doc.class_date;
        let current_date = frappe.datetime.nowdate();

        if (class_date < current_date) {
            frappe.throw(__('Class date cannot be in the past.'));
             
        }
    }
});
