

import frappe
from frappe.utils import getdate, add_days, nowdate

def send_email():
        end_date = getdate(nowdate())
        start_date = add_days(end_date, -7)

        
        bookings = frappe.get_all(
            'Gym Class Booking',
            filters={
                'class_date': ['between', (start_date, end_date)],
                'status': 'Booked'  
            },
            fields=['class_type', 'class_date', 'class_time', 'trainer', 'email',"member"]
        )

        
        email_bookings = {}
        for booking in bookings:
            email = booking.email
            if email not in email_bookings:
                email_bookings[email] = []
            email_bookings[email].append(booking)

    
        for email, member_bookings in email_bookings.items():
            message = "<h3>Your Weekly Class Summary</h3>"
            message += "<table border='1' style='width:100%; border-collapse:collapse;'>"
            message += "<tr><th>Member</th><th>Class Type</th><th>Date</th><th>Time</th><th>Trainer</th></tr>"
            for booking in member_bookings:
                message += f"<tr><td>{booking.member}</td>"

                message += f"<tr><td>{booking.class_type}</td>"
                message += f"<td>{booking.class_date}</td>"
                message += f"<td>{booking.class_time}</td>"
                message += f"<td>{booking.trainer}</td></tr>"

            message += "</table>"
            try:
                frappe.sendmail(
                    recipients= email,
                    subject="Your Weekly Class Summary",
                    message=message
                )
            except Exception as e:
                print(f"Error sending email to {email}: {str(e)}")

