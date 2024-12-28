// Copyright (c) 2024, shalindra and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
    // When the 'Start Date' field is changed
    start_date: function(frm) {
        if (frm.doc.start_date && frm.doc.how_many_month_take_subscription) {
            var end_date = frappe.datetime.add_days(frm.doc.start_date, frm.doc.how_many_month_take_subscription * 30);
            frm.set_value('end_date', end_date); 
        }
    },

    how_many_month_take_subscription: function(frm) {
        if (frm.doc.start_date && frm.doc.how_many_month_take_subscription) {
            var end_date = frappe.datetime.add_days(frm.doc.start_date, frm.doc.how_many_month_take_subscription * 30);
            frm.set_value('end_date', end_date);
        }
    }
});
