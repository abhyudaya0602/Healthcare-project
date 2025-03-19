# 🏥 Healthcare Management System

A **Flask-based** web application for managing **appointments, doctors, and health records**. This project includes a **backend API** and a **Flask-powered frontend**, both containerized using **Docker**.

---

## 📌 Features  
✅ **User Authentication** – Register & login securely  
✅ **Book Appointments** – Schedule and manage doctor visits  
✅ **Doctors List** – View & consult healthcare professionals  
✅ **Health Records** – Store and access medical history  
✅ **Dockerized Deployment** – Run using Docker  
✅ **Role-Based Access Control** – Different views for patients and doctors  
✅ **Secure Password Hashing** – User credentials stored securely  
✅ **RESTful API** – Well-structured API endpoints for frontend integration  
✅ **Mobile Responsive UI** – Works on desktops, tablets, and mobile devices  

---

## 📂 Project Structure

```
healthcare_project/
│── backend/
│   ├── app.py           # Main Flask backend application
│   ├── models.py        # MongoDB database models
│   ├── routes.py        # API routes for user and healthcare management
│   ├── config.py        # Configuration settings
│   ├── requirements.txt # Backend dependencies
│   ├── Dockerfile       # Dockerfile for backend containerization
│   ├── utils.py         # Utility functions for authentication & data processing
│
│── frontend/
│   ├── app.py           # Main Flask frontend application
│   ├── static/
│   │   ├── styles.css   # Styles for UI
│   │   ├── scripts.js   # JavaScript for frontend interactivity
│   ├── templates/
│   │   ├── index.html   # Homepage
│   │   ├── login.html   # Login Page
│   │   ├── register.html # Registration Page
│   │   ├── dashboard.html # User Dashboard
│   │   ├── appointment.html # Appointment Booking Page
│   │   ├── profile.html  # User Profile Page
│   ├── requirements.txt # Frontend dependencies
│   ├── Dockerfile       # Dockerfile for frontend containerization
│
│── database/
│   ├── init_db.py       # Initialize MongoDB collections
│
│── docker-compose.yml   # Compose file to manage multi-container setup
│── README.md            # Project documentation
```

---

## 🚀 Installation & Setup

### 1️⃣ Prerequisites
- **Python 3.8+**
- **Docker & Docker Compose**
- **MongoDB 4.4 (Dockerized)**

### 2️⃣ Clone Repository
```sh
git clone https://github.com/yourusername/healthcare_project.git
cd healthcare_project
```

### 3️⃣ Setup Backend
```sh
cd backend
pip install -r requirements.txt
python app.py
```

### 4️⃣ Setup Frontend
```sh
cd frontend
pip install -r requirements.txt
python app.py
```

### 5️⃣ Run with Docker Compose
```sh
docker-compose up --build
```

---

## 🛠 API Endpoints

### 🔹 Authentication
- **`POST /register`** → Register a new user
- **`POST /login`** → Login with email & password

### 🔹 Appointments
- **`POST /appointments`** → Book an appointment
- **`GET /appointments`** → Fetch user appointments
- **`DELETE /appointments/<id>`** → Cancel an appointment

### 🔹 Doctors
- **`GET /doctors`** → View available doctors
- **`POST /doctors`** → Add a new doctor (Admin Only)

### 🔹 User Profile
- **`GET /profile`** → View user profile
- **`PUT /profile`** → Update user details

---

## 🎨 UI Design
The frontend is designed using **HTML, CSS, and JavaScript**, providing a **user-friendly and responsive interface**.

### 🔹 Pages & Features
✅ **Home Page** – Introduction to the healthcare system  
✅ **Login & Registration** – Secure authentication system  
✅ **User Dashboard** – View upcoming appointments & health records  
✅ **Doctor Listing** – Browse and book doctor consultations  
✅ **Profile Management** – Update personal details & medical history  
✅ **Mobile-Friendly UI** – Ensuring a seamless experience across all devices  

---

## 📦 Deployment
### 🔹 Local Deployment
```sh
python backend/app.py
python frontend/app.py
```

### 🔹 Docker Deployment
```sh
docker-compose up --build
```

### 🔹 Cloud Deployment (Optional)
- Can be deployed using **AWS, Azure, or Google Cloud**
- CI/CD pipelines can be set up for automated deployment

---

## 🤝 Contributing
We welcome contributions! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Added new feature'`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📜 License
This project is licensed under the **MIT License**.

---

🚀 **Developed with ❤️ using Flask, MongoDB, and Docker!**