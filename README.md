<div align="center">

<h1 style="font-size:40px; font-weight:700;">🍽️ Restaurant Management System (Django REST API)</h1>

<p style="font-size:18px;">
A complete backend-only Restaurant Management System built with  
<b>Django</b>, <b>Django REST Framework</b>, <b>JWT Authentication</b>, and <b>SQLite</b>.  
Fully API-based — suitable for frontend integration.
</p>

<br>

<img src="https://img.shields.io/badge/Python-3.12-blue" />
<img src="https://img.shields.io/badge/Django-5.x-darkgreen" />
<img src="https://img.shields.io/badge/DRF-REST%20Framework-red" />
<img src="https://img.shields.io/badge/JWT-Authentication-yellow" />
<img src="https://img.shields.io/badge/Database-SQLite-lightgrey" />

<br><br>

</div>

---

<h2 style="color:#4CAF50;">📖 Project Overview</h2>

This project is a **complete backend REST API** for managing a restaurant.  
It supports:

- Menu Management  
- Table Reservations  
- Order Processing  
- Inventory Tracking  
- Auto-Inventory Updates  
- Daily Sales & Stock Alerts Reports  
- JWT Auth (Users & Admins)  
- Admin-only control for inventory & reporting  

It is designed for **learning Django**, **API development**, and **real-world backend design**.

---

<h2 style="color:#FF9800;">📁 Project Structure</h2>

```

restaurant_management/
│
├── restaurant/              # Main app
│   ├── models.py            # User, Menu, Orders, Tables, Inventory
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API logic
│   ├── urls.py              # App routes
│   └── permissions.py       # Admin-only permissions
│
├── media/                   # Image uploads (menu images)
│
├── config/
│   ├── settings.py          # Project settings & JWT config
│   └── urls.py              # Root routes
│
├── db.sqlite3               # SQLite DB
└── README.md

```

---

<h2 style="color:#03A9F4;">⚙️ Installation & Setup</h2>

#### 1️⃣ Clone the repo  
```

git clone https://github.com/hamna663/CodeAlpha_Restaurant-Management-System.git
cd restaurant-management-api

```

#### 2️⃣ Create virtual environment  
```

python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/macOS

```

#### 3️⃣ Install dependencies  
```

pip install django djangorestframework djangorestframework-simplejwt Pillow

```

#### 4️⃣ Run migrations  
```

python manage.py makemigrations
python manage.py migrate

```

#### 5️⃣ Create a superuser  
```

python manage.py createsuperuser

```

#### 6️⃣ Start server  
```

python manage.py runserver

```

---

<h2 style="color:#E91E63;">🖼️ Image Handling (Menu Images)</h2>

Menu images are stored locally in:

```

/media/menu/

```

To upload images, the API uses:

- `ImageField` in the Menu model  
- `Pillow` for image processing  
- DRF `MultiPartParser` in views  

Example Menu Image URL:

```

http://127.0.0.1:8000/media/menu/burger.png

```

---

<h2 style="color:#9C27B0;">📌 Database Models Overview</h2>

### ✔️ MenuItem  
- title  
- description  
- price  
- category  
- image  

### ✔️ Table  
- table_number  
- capacity  
- status  

### ✔️ Reservation  
- customer  
- table  
- date  
- time  
- auto-check for availability  

### ✔️ Order  
- items  
- table_or_takeaway  
- total_price  
- status (pending, cooking, served)  
- auto-inventory deduction  

### ✔️ Inventory  
- item_name  
- qty_available  
- threshold  
- auto stock alerts  

---

<h2 style="color:#8BC34A;">🚀 API Features</h2>

### 🔹 **Public (No Auth Required)**
- View menu  
- View available tables  

### 🔹 **JWT Auth Required**
- Place orders  
- Make reservations  

### 🔹 **Admin Only**
- Manage inventory  
- Generate reports  
- View daily sales  
- View stock alerts  

---

<h2 style="color:#FF5722;">🔐 JWT Authentication</h2>

Endpoints:

| Action | URL |
|--------|-----|
| Get Access Token | `/api/token/` |
| Refresh Token | `/api/token/refresh/` |

Send JWT in headers:

```

Authorization: Bearer <access_token>

```

---

<h2 style="color:#009688;">📊 Reporting Features (Admin Only)</h2>

- **Daily Sales Report**  
- **Top Selling Menu Items**  
- **Inventory Stock Alerts**  
- **Total Orders Count**  

All protected by custom permission:

```

IsAdminUser

```

---

<h2 style="color:#673AB7;">🧪 Sample API Endpoints</h2>

### ✔ Get Menu  
```

GET /api/menu/

```

### ✔ Place Order  
```

POST /api/orders/

```

### ✔ Reserve a Table  
```

POST /api/reservations/

```

### ✔ Update Inventory (Admin Only)  
```

PUT /api/inventory/<id>/

```

<h2 style="color:#3F51B5;">🤝 Contributing</h2>

```

Fork → Create Branch → Commit → PR

```

---

<div align="center">

<h2 style="color:#2196F3;">⭐ Give this project a star!</h2>

<p>If this helped you learn Django or build your own restaurant backend, please consider starring the repo.</p>

<br>

<h3>Made with ❤️ using Django REST Framework</h3>

</div>
