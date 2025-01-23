# 🌤 Weather Notification Script

A Python script that fetches real-time weather data for a specified city and displays it as a notification on macOS. Stay updated with the latest temperature and weather conditions, delivered right to your desktop.

---

## 📜 Features

- Fetches live weather updates using the OpenWeatherMap API.
- Displays temperature and weather condition notifications.
- Configurable city and unit system (metric/Celsius by default).
- Runs periodically to provide hourly updates.

---

## 🛠️ Requirements

- **Python 3.x** installed on your system.
- A valid API key from [OpenWeatherMap](https://openweathermap.org/).
- macOS for notification support (uses `osascript`).

---

## 🚀 How to Use

1. Install required Python packages:
   ```bash
   pip install requests
   ```
2. Update the `API_KEY` and `CITY` constants in the script:
   - Replace `"Delhi"` with your desired city name.

3. Run the script:
   ```bash
   python weather.py
   ```

---

## ⚙️ Configuration

- **API_KEY:** Obtain it from [OpenWeatherMap API](https://openweathermap.org/api) and replace the placeholder in the script.
- **CITY:** Set your preferred city in the `CITY` variable.
- **Update Frequency:** The script is set to update every 10 seconds for testing. Modify `time.sleep(10)` to `time.sleep(3600)` for hourly updates.

---

## 🖥️ Example Notification

- **Title:** Weather Update for Delhi  
- **Message:**  
  ```
  Temperature: 25°C
  Condition: Clear sky
  ```

---

## 🛡️ Prerequisites

Ensure you have:
- A stable internet connection to fetch weather data.
- macOS for notifications (can be modified for other OS with platform-specific notification libraries like `plyer`).

---

## 🤔 Troubleshooting

- **Invalid API Key or City:** Ensure the `API_KEY` and `CITY` values are correct.
- **No Notifications:** Check if notifications are enabled for the terminal or script runner.
- **Errors:** Any exceptions are displayed in the notification for debugging.

---
