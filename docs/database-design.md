# FinVerse - Database Design

## Overview

This document defines the database design for FinVerse.

The objective is to create a scalable, normalized, and maintainable relational database for managing users, financial accounts, transactions, budgets, and future financial modules.

Database: PostgreSQL

---

# Design Principles

- One source of truth for each entity
- Avoid duplicate data
- Maintain referential integrity
- Use foreign keys
- Keep tables normalized
- Support future scalability

---

# Entity Relationship Overview

User
│
├── Wallet
│      │
│      └── Transaction
│
├── Category
│      │
│      └── Transaction
│
└── Budget

---

# User

Purpose

Stores registered users.

Fields

- id
- first_name
- last_name
- email
- password_hash
- created_at
- updated_at

Constraints

- email must be unique
- password stored as hash

Indexes

- email

---

# Wallet

Purpose

Represents a financial account owned by a user.

Examples

- Cash
- SBI Account
- HDFC Savings
- Credit Card

Fields

- id
- user_id
- name
- type
- balance
- currency
- created_at
- updated_at

Relationships

Many wallets belong to one user.

Constraints

- balance >= 0

Indexes

- user_id

---

# Category

Purpose

Organizes transactions.

Examples

Income

- Salary
- Freelance
- Interest

Expense

- Food
- Shopping
- Rent

Fields

- id
- user_id
- name
- type

Relationships

One category can have many transactions.

---

# Transaction

Purpose

Stores every financial activity.

Fields

- id
- wallet_id
- category_id
- amount
- type
- description
- transaction_date
- created_at
- updated_at

Relationships

Many transactions belong to one wallet.

Many transactions belong to one category.

Constraints

- amount > 0

Indexes

- wallet_id
- category_id
- transaction_date

---

# Budget

Purpose

Stores monthly spending limits.

Fields

- id
- user_id
- category_id
- monthly_limit
- month
- year

Relationships

Many budgets belong to one user.

Constraints

One budget per category per month.

---

# Future Tables

These tables are planned but not included in MVP.

- Savings Goal
- Investment
- Loan
- Bill
- Notification
- Audit Log

---

# Future Enhancements

- Multi-currency support
- Shared wallets
- Family accounts
- Receipt storage
- AI spending insights