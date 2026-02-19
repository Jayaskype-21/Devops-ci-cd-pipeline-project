# Devops-ci-cd-pipeline-project

### 🧱 Project Overview

**Project name:** Grocery App
**Goal:** Whenever code (for example, price in your app) changes in GitHub, automatically update the live website running on EC2 (port 5000) without manual commands.
That’s Continuous Integration (CI) + Continuous Deployment (CD).

---

## 🔹 Step 1 — EC2 Instance Setup

**Purpose:** Server for hosting Jenkins + Docker.

**Actions:**

* AWS EC2 instance (Ubuntu or Amazon Linux) உருவாக்கினாய்.
* Inside EC2:

  * **Jenkins** installed → CI tool to automate build/test/deploy.
  * **Docker** installed → to containerize your app.

💡 *Why:*
Jenkins + Docker combination lets you automatically build and run the updated image inside containers every time your code changes.

---

## 🔹 Step 2 — Dockerize Your Application

**File:** `Dockerfile`
**App:** `app.py`

**Purpose:** Package your app (Python Flask web app) and dependencies into a portable Docker image.

**Command used:**

```bash
docker build -t jayasreek793/grocery-app .
```

💡 *Why:*
So your app runs the same everywhere — EC2, laptop, or any server — avoiding “it works on my machine” issues.

---

## 🔹 Step 3 — Push Image to Docker Hub

**Purpose:** Store and version your image in a registry.

**Action in Jenkins Pipeline:**

```bash
docker push jayasreek793/grocery-app:latest
```

💡 *Why:*
Now anyone (or Jenkins itself) can pull this image anywhere for deployment.

---

## 🔹 Step 4 — Jenkins Pipeline Configuration

**Purpose:** Automate build + deployment.

You wrote a Jenkinsfile (script) similar to this:

```bash
docker build -t jayasreek793/grocery-app:latest .
docker push jayasreek793/grocery-app:latest
docker rm -f grocery-app || true
docker pull jayasreek793/grocery-app:latest
docker run -d -p 5000:5000 --name grocery-app jayasreek793/grocery-app:latest
```

💡 *Why:*
Every build step executes automatically — no manual commands.
Old containers stop; new ones start with the latest code.

---

## 🔹 Step 5 — GitHub Webhook Setup

**Purpose:** Connect GitHub to Jenkins.

**What you did:**

* GitHub → Repository Settings → Webhooks → Added Jenkins URL
  (Example: `http://<ec2-public-ip>:8080/github-webhook/`)
* Select events: “Just the push event”

💡 *How it works:*
When you push a change (e.g., modify price in code),
GitHub immediately sends a **HTTP POST** to Jenkins.
Jenkins triggers your build job automatically — no manual “Build Now.”

---

## 🔹 Step 6 — CI/CD in Action

**Process flow:**

1. You change something in GitHub (e.g., update price in `app.py`).
2. GitHub sends a webhook trigger to Jenkins.
3. Jenkins builds a new Docker image.
4. Jenkins pushes it to Docker Hub.
5. Jenkins pulls and redeploys the updated container on EC2.
6. You refresh the website (`http://<ec2-ip>:5000`) → Price updated instantly 🎉

💡 *Why this is powerful:*
No manual redeploy. Full automation = **Continuous Delivery**.

---

## 🔹 Step 7 — Result (Your Achievement)

✅ Fully automated CI/CD Pipeline
✅ Real-time deployment via GitHub Webhooks
✅ Amazon EC2 instance serving containerized Flask app
✅ Docker Hub storing versioned images
✅ Jenkins automating build + deploy

---


<img width="1360" height="687" alt="image" src="https://github.com/user-attachments/assets/faa02587-8578-42d5-a88f-c85909c52cfd" />
