#Rover Distance and Time Calculator

📌 Description

This program calculates the distance between two coordinates on a 2D plane and estimates the time required for a rover to travel between them based on given motion parameters.

---

📥 Inputs

The program takes the following user inputs:

- Origin coordinates: (x1, y1)
- Destination coordinates: (x2, y2)
- Initial velocity (m/s)
- Acceleration (m/s²)
- Maximum speed (m/s)

---

⚙️ Functionality

1. Distance Calculation

The program calculates the distance using the Euclidean distance formula.

2. Time Calculation

Time is calculated based on:

- Initial velocity
- Acceleration
- Maximum speed constraint

3. Error Handling

The program includes basic validation for:

- Invalid inputs
- Negative values (where not applicable)

---

▶️ How to Run

For Python:

python main.py

---

📊 Example Input

Origin: (0, 0)
Destination: (100, 40)
Initial Velocity: 2
Acceleration: 1
Top Speed: 10

---

📈 Example Output

Distance to destination: 107.7 m
Time required: 13.2 seconds

---

🧠 Concepts Used

- Distance formula (Euclidean geometry)
- Basic kinematics equations
- Conditional logic and error handling

---

📁 File Structure

- rover.py  → Main program file

---

👤 Author

Archana K L
