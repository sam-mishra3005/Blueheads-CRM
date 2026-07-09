# How to Run Blueheads CRM

This document explains how to start your CRM locally and how to expose it to the internet for presentations. It also includes a prompt you can use to easily instruct any AI assistant to help you run the project in the future.

---

## 1. Running the Project Locally (Manual Instructions)

Your CRM backend runs inside WSL (Windows Subsystem for Linux) using the Frappe framework.

### Step 1: Start the Backend Server
1. Open **Windows PowerShell** or your terminal.
2. Run the following command to start the Frappe server inside WSL:
   ```bash
   wsl -d Ubuntu -u root -- su - frappe -c "cd frappe-bench && bench start"
   ```
3. Keep that terminal window open. The server is now running!
4. Open your browser and visit: [http://127.0.0.1:8000/blueheads_crm](http://127.0.0.1:8000/blueheads_crm)

### Step 2 (Optional): Frontend Development
If you want to edit the Vue.js frontend files and see changes instantly without rebuilding:
1. Open a **new** PowerShell window.
2. Navigate to your frontend folder:
   ```bash
   cd D:\Dev\Projects\CRM\frontend
   ```
3. Start the Vite development server:
   ```bash
   yarn dev
   ```

---

## 2. Exposing the CRM to the Internet (For Presentations)

If you need to share a public link (like you did for your presentation), you can use the high-speed Cloudflare tunnel we installed.

1. Ensure the Frappe server is running (Step 1 above).
2. Open a **new** PowerShell window.
3. Run the following command to start the tunnel:
   ```bash
   wsl -d Ubuntu -u root -- cloudflared tunnel --url http://127.0.0.1:8000
   ```
4. Look at the output in the terminal. You will see a line that looks like this:
   > `https://some-random-words.trycloudflare.com`
5. Add `/blueheads_crm` to the end of that URL and share it with your team!

---

## 3. The "AI Prompt" (Copy & Paste this to your AI)

If you ever restart your computer and want an AI assistant (like me) to just handle everything for you, simply paste the prompt below into the chat:

> **Prompt for AI:**
> "I need to start my Blueheads CRM project. The Frappe backend is installed in my WSL (Ubuntu) under the user 'frappe' in the 'frappe-bench' directory. 
> 
> Please do the following:
> 1. Use a background terminal command to run `wsl -d Ubuntu -u root -- su - frappe -c "cd frappe-bench && bench start"`.
> 2. Wait 5 seconds for the server to initialize.
> 3. I also need a public link for a presentation. Please run `wsl -d Ubuntu -u root -- cloudflared tunnel --url http://127.0.0.1:8000` in the background.
> 4. Read the logs of the cloudflared task to extract the `trycloudflare.com` URL.
> 5. Give me the final public URL appended with `/blueheads_crm` so I can share it immediately."
