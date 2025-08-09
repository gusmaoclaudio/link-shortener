# 🔗 Link Shortener API

![CI](https://github.com/gusmaoclaudio/link-shortener/actions/workflows/ci.yml/badge.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)

A lightweight URL shortening service built with **FastAPI**, **SQLite**, and **SQLAlchemy**.  
Provides RESTful API endpoints for creating, retrieving, deleting, and redirecting shortened links.  
Includes custom slug support, click tracking, and automated tests.

---

## 🚀 Features
- Create shortened URLs with random or custom slugs.
- Redirect to the original link.
- Track click count.
- Fully documented API with Swagger UI (`/docs`).
- Ready for containerized deployment with Docker.
- Automated tests with Pytest.
- GPL v3 licensed.

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/gusmaoclaudio/link-shortener.git
cd link-shortener
