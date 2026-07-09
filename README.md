# Blueheads CRM

**Simplify Sales, Amplify Relationships**

Blueheads CRM is a clean, modern, and open-source CRM application designed for sales teams to build strong customer relationships while keeping sales pipelines organized and productive. This project is a customized version of Frappe CRM, tailored as an internship project.

---

## Key Features

* **Visual Kanban Boards:** Track and move leads and deals through customized pipeline stages with intuitive drag-and-drop actions.
* **Unified Workspace:** View comments, notes, activities, tasks, calls, and email communications for any lead or deal in a single consolidated interface.
* **Custom Filtering & Views:** Create and save personalized views with advanced filtering, custom sorting, and selectable columns.
* **Built-in Integrations:** Integrates with Twilio and Exotel for telephony (calling/logging) and WhatsApp for client outreach.

---

## Tech Stack

### Frontend
- **Vue 3** (Composition API)
- **Vite** (Build Tool)
- **Tailwind CSS** (Styling)
- **Frappe UI** (Component Framework)

### Backend
- **Frappe Framework** (Python-based application framework)
- **MariaDB / PostgreSQL** (Relational database)
- **Redis** (Caching and background jobs queue)

---

## Getting Started

### Local Development
To run the frontend client locally:
```bash
cd frontend
npm install
npm run dev
```

Note: To run the full application (both frontend and backend), the project must be installed as an active app inside a configured **Frappe Bench** environment.
