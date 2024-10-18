# weather-monitoring
Real-Time Weather Monitoring System

Overview

This project implements a real-time data processing system to monitor weather conditions using the OpenWeatherMap API. It continuously retrieves weather data for major metros in India, processes the data, and provides summarized insights with rollups and aggregates.

Codebase

The code for this project is hosted on GitHub: [Weather Monitoring GitHub Repository](https://github.com/Deeksha0307/weather-monitoring)

Features

	•	Real-time weather data retrieval every 5 minutes.
	•	Conversion of temperature values from Kelvin to Celsius or Fahrenheit based on user preference.
	•	Daily weather summary including:
	•	Average temperature
	•	Maximum temperature
	•	Minimum temperature
	•	Dominant weather condition
	•	User-configurable alert thresholds for extreme weather conditions.
	•	Visualization of weather trends using Matplotlib.
	•	Supports additional parameters like humidity and wind speed (Bonus features).

Design Choices

	•	API Usage: The project uses the OpenWeatherMap API for retrieving weather data.
	•	Data Processing: Python is used for data processing, leveraging libraries like Pandas for data manipulation and Matplotlib for visualization.
	•	Configuration: The system is designed to be easily configurable, allowing users to set preferences for temperature units and alert thresholds.

Dependencies

Before running the application, ensure you have the following dependencies installed:

	•	Python 3.x
	•	Requests library for API calls
	•	Pandas for data manipulation
	•	Matplotlib for data visualization

You can install the dependencies using pip:

pip install requests pandas matplotlib

Setup Instructions

	1.	Obtain OpenWeatherMap API Key:
	•	Sign up at OpenWeatherMap.
	•	Create an API key from your dashboard.
	2.	Clone the Repository:
Clone this repository to your local machine using:

git clone https://github.com/yourusername/weather-monitoring.git


	3.	Navigate to the Project Directory:
Change into the project directory:

cd weather-monitoring


	4.	Update API Key:
	•	Open the weather_monitor.py file.
	•	Replace your_api_key_here with your actual OpenWeatherMap API key.
	5.	Run the Script:
You can run the application using:

python weather_monitor.py


	6.	Select Temperature Unit:
When prompted, enter your preferred temperature unit:
	•	Enter C for Celsius
	•	Enter F for Fahrenheit
	•	Enter K for Kelvin

Example Output

After starting the script, you will see output like the following:

---Current Weather Data---
        city      main        temp  feels_like  humidity  wind_speed                  dt temp_unit
0    Mumbai       Haze  28.75       30.02      70       6.20    2024-10-18 12:58:13      °C
1     Delhi       Haze  29.05       30.34      65       5.10    2024-10-18 12:58:13      °C
...

Alerts

The program will notify you if any city’s temperature exceeds user-defined thresholds:

---ALERT---
High temperature alert for the following cities:
       city      temp
0    Delhi      37.25
---END ALERT---

Additional Information

	•	Contributions: Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.
	•	License: This project is licensed under the MIT License - see the LICENSE file for details.
	•	Acknowledgements: Special thanks to OpenWeatherMap API for providing weather data and Matplotlib for data visualization tools.

Conclusion

This project serves as a robust solution for monitoring real-time weather conditions and generating insightful summaries for better decision-making. Feel free to explore, contribute, and enhance the application!