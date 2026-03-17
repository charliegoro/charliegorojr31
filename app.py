

app = Flask(__name__)

# Sample in-memory attendance list
attendance = []

@app.route('/')
def home():
    return "Welcome to my Attendance API!"

# GET all attendance records
@app.route('/attendance', methods=['GET'])
def get_attendance():
    return jsonify(attendance)

# POST (add) a new attendance record
@app.route('/attendance', methods=['POST'])
def add_attendance():
    data = request.get_json()

    record = {
        "name": data.get("name"),
        "date": data.get("date"),
        "status": data.get("status")  # Present / Absent
    }

    attendance.append(record)
    return jsonify({
        "message": "Attendance recorded successfully!",
        "data": record
    }), 201

# Optional: clear all records
@app.route('/attendance/clear', methods=['DELETE'])
def clear_attendance():
    attendance.clear()
    return jsonify({"message": "All attendance records cleared."})

if __name__ == '__main__':
    app.run(debug=True)
