ROS2 Distance Communication

📌 Description

This project demonstrates communication between two ROS2 nodes using a publisher-subscriber model.

- The publisher node generates random distance values (simulating a rover sensor)
- The subscriber node listens to the topic and prints the received values in the terminal

---

⚙️ Functionality

🔹 Publisher Node

- Publishes random distance values every second
- Topic used: "/distance"

🔹 Subscriber Node

- Subscribes to "/distance"
- Prints received values to the terminal

---

▶️ How to Run

1. Open terminal and source ROS2:

source /opt/ros/humble/setup.bash

2. Run publisher node:

ros2 run <package_name> distance_publisher

3. Run subscriber node:

ros2 run <package_name> distance_subscriber

---

📊 Example Output

Received distance: 10
Received distance: 35
Received distance: 72

---

🧠 Explanation

The publisher node continuously sends random distance values to the "/distance" topic.
The subscriber node listens to this topic and displays the received values in real time.

---

📁 Files

- distance_publisher.py → Publishes distance values
- distance_subscriber.py → Receives and prints values

---

👤 Author

Archana KL
