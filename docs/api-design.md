# FinVerse API Design

## Overview

This document defines the REST API endpoints for FinVerse.

The APIs follow REST principles and JSON communication.

Base URL

/api/v1

---

# Authentication

POST /auth/register

Registers a new user.

POST /auth/login

Authenticates a user.

POST /auth/logout

Logs out user.

GET /auth/me

Returns logged in user.

---

# Wallets

GET /wallets

Returns all wallets.

GET /wallets/{id}

Returns wallet details.

POST /wallets

Creates wallet.

PUT /wallets/{id}

Updates wallet.

DELETE /wallets/{id}

Deletes wallet.

---

# Categories

GET /categories

POST /categories

PUT /categories/{id}

DELETE /categories/{id}

---

# Transactions

GET /transactions

GET /transactions/{id}

POST /transactions

PUT /transactions/{id}

DELETE /transactions/{id}

---

# Budgets

GET /budgets

POST /budgets

PUT /budgets/{id}

DELETE /budgets/{id}

---

# Dashboard

GET /dashboard

Returns

- Total Balance
- Monthly Income
- Monthly Expense
- Budget Status
- Recent Transactions

---

# Response Format

Success

{
    "success": true,
    "data": {}
}

Error

{
    "success": false,
    "message": "Resource not found"
}

---

# Authentication

JWT Bearer Token

Authorization: Bearer <token>

---

# Status Codes

200 OK

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

500 Internal Server Error