# Task-1 PostgreSQL

This project provides an automated way to perform database migrations using **Alembic** and load data into **PostgreSQL** via **Python**. The project includes Dockerized services for **PostgreSQL**, **PgAdmin**, and a Python application to manage database operations.

The **".env"** file was not added to **".gitignore"** on purpose.

---


## 📁 Project Structure

```bash
task-1-postgresql/
├── data/                             # Mock data in CSV format
│   ├── department_positions.csv
│   ├── departments.csv
│   ├── employees.csv
│   ├── positions.csv
│   └── salaries.csv            
├── src/                              # Source code for migrations and models
│   ├── migrations/
│   │   ├── versions/                 # Alembic migration versions
│   │   │   ├── env.py
│   │   │   └── script.py.mako
│   │   ├── config.py                 # Alembic configuration
│   │   ├── database.py               # Database connection setup
│   │   └── models.py                 # SQLAlchemy models
├── tasks/                            # Task-specific queries
├── .env                              # Environment variables configuration
├── .gitignore                        # Git ignore file
├── alembic.ini                       # Alembic configuration file
├── docker-compose.yml                # Docker Compose setup
├── Dockerfile                        # Dockerfile to build the application
├── load_data.py                      # Script to load CSV data into PostgreSQL
├── README.md                         # Project documentation (you're here!)
└── requirements.txt                  # Python dependencies
```

***

## ⚙️ Running the Project
To start the project and initialize all necessary services (PostgreSQL, PgAdmin, and the application), execute the following command in your terminal:
```bash
docker-compose up --build
```
* **PostgreSQL Server:** A PostgreSQL database service is spun up and ready to be used.
* **PgAdmin:** A web-based PostgreSQL administration tool becomes accessible.
* **App:** The Python application will:
  * ``Run migrations using Alembic to create database tables based on models.py.``
  * ``Automatically load mock data from the data/ folder into the PostgreSQL database using load_data.py.``

***

## 📂 Task Solutions
***You can find specific task solutions in the tasks/ directory. These solutions include SQL queries or other scripts 
that can be used to interact with the database.***

***

## 🌐 Accessing PgAdmin
Once the services are running, you can access PgAdmin by visiting the following URL in your browser:

```bash
  http://localhost:5050/browser/
```
#### PgAdmin Login Credentials:
    Email: admin@admin.com 
    Password: 1234


### Setting Up a New Server in PgAdmin:
1. Click to **'Add New Server'**.
2. In the General tab, give your server a name (e.g., Postgres Server).
3. Switch to the **Connection** tab and enter the following details:
   * Host: try the ``db`` variable, if that doesn't work ``Refer to the hint below to find the PostgreSQL server host address.``
   * Database: ``"postgres"``
   * Username: ``"root"``
   * Password: ``"1234"``


### Hint: Retrieving PostgreSQL Server Host Address
Containers do not recognize localhost as a host, so you'll need to find the correct IP address of the PostgreSQL container. To do this:

1. List the running containers to find the PostgreSQL container ID:
```bash
  docker ps
```
2. Inspect the container to get its IP address:
```bash
  docker inspect <container_name_or_id> | grep "IPAddress" # for macOS & Linux
  docker inspect <container_name_or_id> | findstr "IPAddress" # for Windows
```
3. Use the retrieved IPAddress in PgAdmin under the Host field.
