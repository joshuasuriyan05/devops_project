import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Absolute paths to templates and static directories
TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = "devops-secret-key"

appointments = []  # In-memory storage

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/appointments', methods=['GET', 'POST'])
def manage_appointments():
    if request.method == 'POST':
        patient = request.form.get('patient')
        doctor = request.form.get('doctor')
        time = request.form.get('time')

        if not patient or not doctor or not time:
            flash("⚠️ All fields are required!", "error")
        else:
            appointment = {
                "id": len(appointments) + 1,
                "patient": patient,
                "doctor": doctor,
                "time": time
            }
            appointments.append(appointment)
            flash("✅ Appointment booked successfully!", "success")

        return redirect(url_for('manage_appointments'))

    return render_template('appointments.html', appointments=appointments)

@app.route('/delete/<int:appointment_id>')
def delete_appointment(appointment_id):
    global appointments
    appointments = [appt for appt in appointments if appt["id"] != appointment_id]
    flash("Appointment canceled successfully!", "success")
    return redirect(url_for('manage_appointments'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
