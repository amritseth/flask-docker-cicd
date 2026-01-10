# 🚀 Dockerized Flask App with AWS CI/CD Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

</div>

## 📋 Project Overview
This project demonstrates a fully automated **DevOps pipeline** for a Python web application. 
It solves the "it works on my machine" problem by using **Docker** containers and automates deployment using **GitHub Actions**. Every time code is pushed to the `main` branch, it is automatically built, tested, and deployed to a live **AWS EC2** server.

---

## ⚙️ Architecture Workflow

```mermaid
graph LR
    A[💻 Dev Local] -->|Push Code| B[🐙 GitHub Repo]
    B -->|Trigger| C[⚙️ GitHub Actions]
    C -->|SSH Login| D[☁️ AWS EC2]
    subgraph AWS Server
      D -->|Pull Code| E[⬇️ Git Pull]
      E -->|Build| F[🐳 Docker Compose]
      F -->|Run| G[🚀 Flask Container]
      F -->|Proxy| H[🌐 Nginx Container]
    end
