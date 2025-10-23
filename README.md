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
AMADEUS_API_KEY=your_amadeus_key,
AMADEUS_API_SECRET=your_amadeus_secret,
TWILIO_ACCOUNT_SID=your_sid,
TWILIO_AUTH_TOKEN=your_token,
TWILIO_PHONE_NUMBER=your_twilio_number,
MY_PHONE_NUMBER=your_personal_number,
SHEETY_USER=your_sheety_username,
SHEETY_PASSWORD=your_sheety_password

⚠️ **Never upload `.env` or share your credentials publicly.**

---

> 🟢 Run the project by executing `main.py`

## 📌 Acknowledgement
Developed as part of my **100 Days of Python Bootcamp** learning journey.  
This capstone project deepened my understanding of API integration, authentication, and automation workflows.
