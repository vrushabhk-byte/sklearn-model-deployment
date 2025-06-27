# sklearn-model-deployment

# ML Deployment API

This project demonstrates a minimal ML deployment pipeline using FastAPI, Docker, and GitHub Actions.

## ✅ Features

- `/health`: API status check
- `/predict`: ML prediction endpoint
- Preprocessing module for input data
- Dockerized for deployment
- CI/CD pipeline with GitHub Actions
- Deploys to remote Linux server via SSH

## 📦 Quick Start

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
