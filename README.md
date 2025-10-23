# ✈️ Flight Deals Finder (Flight Club)

A Python automation project that searches for cheap flights using the **Amadeus API** and sends SMS alerts when prices drop below a target threshold.  
This project combines API handling, data management, and automation.

---

## 🚀 Features
- Fetches city IATA codes using Amadeus API  
- Searches for flights within a date range  
- Compares prices with preset lowest prices in Google Sheets (via **Sheety API**)  
- Sends SMS alerts via **Twilio** when cheaper deals are found  

---

## 🛠️ Technologies Used
- **Python**
- **Amadeus API**
- **Twilio API**
- **Sheety API**
- **Requests**, **Datetime**

---

## 🔐 Environment Variables
Create a `.env` file with:
