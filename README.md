# 🔔 notifylib — A Loosely Coupled Observer-Based Notification Library

`notifylib` is a lightweight and flexible Python library that enables **loosely coupled communication** between components using the **Observer Design Pattern**. It supports event-driven architecture, modular plugin-like systems, and persistent notification states.

---

## 🚀 Features

- ✅ Decouples senders and receivers using Observer pattern
- ✅ Supports multiple observers for any event
- ✅ Simple API: `register`, `notify`, `unregister`
- ✅ Optional file-based persistence (`JSON`)
- ✅ Easily pluggable into any Python application
- ✅ Pure Python — no external dependencies

---

## 📦 Installation

You can install directly from GitHub:

```bash
pip install git+https://github.com/SaadMaqsood2023/notifylib.git
```

## 🧑‍💻 Quick Usage Example

```python
from notifylib import manager
from notifylib.observer import Observer

# Define a custom observer
class Logger(Observer):
    def update(self, event_name, data):
        print(f"[Logger] Received event: {event_name} | Data: {data}")

# Register the observer
logger = Logger()
manager.register("user_signup", logger)

# Send a notification
manager.notify("user_signup", {"username": "alice"}, persist=True)

# Recover event data (if it was persisted)
recovered_data = manager.recover("user_signup")
print("Recovered:", recovered_data)
```

🧩 API Reference
manager.register(event_name: str, observer: Observer)
Registers an observer to listen for a specific event.

manager.unregister(event_name: str, observer: Observer)
Unregisters an observer from a specific event.

manager.notify(event_name: str, data: dict = None, persist: bool = False)
Notifies all observers registered to an event. If persist=True, the data is stored in a JSON file.

manager.recover(event_name: str) -> dict
Loads previously persisted data for a given event.

🗃️ File Structure
graphql
Copy
Edit
notifylib/
├── notifylib/
│   ├── __init__.py           # Package initializer
│   ├── observer.py           # Observer base class
│   ├── subject.py            # Subject class with observer management
│   ├── manager.py            # User-facing API for notify, register, etc.
│   └── persistence.py        # JSON persistence logic
├── setup.py                  # Python package config
├── README.md                 # This file
└── LICENSE                   # MIT License
📜 License
MIT License
© 2025 Saad Maqsood

🤝 Contributing
Contributions, issues, and feature requests are welcome!

To contribute:

bash
Copy
Edit
# 1. Fork the repo
# 2. Create your feature branch
git checkout -b feature/your-feature

# 3. Commit your changes
git commit -m "Add your feature"

# 4. Push to your branch
git push origin feature/your-feature

# 5. Submit a pull request on GitHub
💬 Feedback & Support
For suggestions, improvements, or help, please open an issue on
https://github.com/SaadMaqsood2023/notifylib



