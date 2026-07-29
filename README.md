# 🐳 Docker Private Registry with Authentication

## 📌 Project Overview

This project demonstrates how to set up a **Docker Private Registry** using **Docker Registry v2** with **Basic Authentication (htpasswd)**. It covers image management, authentication, and testing Docker image push and pull operations.

---

## 🚀 Features

- Create a Local Docker Registry
- Push Docker Images
- Pull Docker Images
- Configure Basic Authentication using `htpasswd`
- Docker Login & Logout
- Test Secure Image Access
- Sample Flask Application

---

## 🛠️ Technologies Used

- Docker
- Docker Registry v2
- Python
- Flask

---

## 📂 Project Structure

```text
docker-private-registry-project/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── Commands.md
```

---

## ▶️ Running the Flask Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://localhost:6000
```

---

## 🐳 Docker Commands Used

### Check Docker Version

```bash
docker --version
```

### Run Docker Registry

```bash
docker run -d -p 5000:5000 --name registry registry:2
```

### Pull Ubuntu Image

```bash
docker pull ubuntu
```

### Tag Image

```bash
docker tag ubuntu localhost:5000/my-ubuntu
```

### Push Image

```bash
docker push localhost:5000/my-ubuntu
```

### Pull Image

```bash
docker pull localhost:5000/my-ubuntu
```

---

## 🔐 Authentication Setup

Generate password file:

```bash
docker run --entrypoint htpasswd httpd:2 -Bbn nainshi mypass123 > auth.txt
```

Remove old registry:

```bash
docker rm -f registry
```

Run authenticated registry:

```bash
docker run -d -p 5000:5000 --name registry ^
-v %cd%/auth.txt:/auth/htpasswd ^
-e REGISTRY_AUTH=htpasswd ^
-e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd ^
-e REGISTRY_AUTH_HTPASSWD_REALM="Registry Realm" ^
registry:2
```

Login:

```bash
docker login localhost:5000
```

Logout:

```bash
docker logout localhost:5000
```

---

## 📖 Workflow

1. Install Docker
2. Create a Docker Registry
3. Pull the Ubuntu image
4. Tag the image
5. Push the image to the private registry
6. Configure authentication
7. Login to the registry
8. Pull the image from the authenticated registry

---

## 📷 Screenshots

Project screenshots can be added in the `screenshots` folder.

---

## 👩‍💻 Author

**Nainshi K**

Data Science Undergraduate | AI & Machine Learning Enthusiast
