# LegalTech Contract Parsing & Risk Extraction Engine

## Objective

Build a system that allows users to upload contracts and analyze them for risk-related clauses.

## Tech Stack

- Python
- Django
- PostgreSQL
- Git & GitHub

## Week 1 Progress

### Completed Features

- Django project setup
- PostgreSQL integration
- Documents app creation
- Document model creation
- ExtractedClause model creation
- RiskFlag model creation
- Django Admin setup
- PDF upload functionality
- Database storage using PostgreSQL

### Current Status

Week 1 completed successfully.

Users can upload PDF contracts through the Django Admin panel and data is stored in PostgreSQL.

## Project Structure

```text
documents/
├── models.py
├── admin.py
├── views.py
├── migrations/

legaltech/
├── settings.py
├── urls.py
```