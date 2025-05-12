# Telegram Inventory Bot

A lightweight Telegram bot for managing store inventory using Firebase as a backend. Easily add, list, and delete products directly through Telegram commands.

## 🚀 Motivation

This project was created to simplify inventory management for small shops and individuals through a user-friendly Telegram interface. The goal is to provide a minimal, accessible tool that does not require any specialized hardware or software beyond a smartphone.

## 🧠 Features

- 📦 Add new products with name, quantity, and price.
- 📄 List all products in the inventory.
- 🗑️ Delete products (admin-only).
- 🔒 Admin access control (by Telegram user ID).
- ☁️ Persistent storage using Firebase Realtime Database.

## 🔧 Tech Stack

- **Python 3**
- **Python Telegram Bot** (telegram.ext)
- **Firebase Realtime Database**
- **Google Cloud SDK**
- **Docker (optional for deployment)**

## 🖥️ Demo

In this type of application, creating an online demo is practically impossible, so to demonstrate how it works, I'll attach screenshots of how it works later.


## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jesusgallardooo/proyecto_dig.git
cd proyecto_dig
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Set up firebase

- Create a Firebase project at https://console.firebase.google.com/

- Download the serviceAccountKey.json from your Firebase settings.

- Place it in the project root folder.

### 4. Set environment variables

Create a .env file and add your bot token and admin Telegram user ID:

```
TELEGRAM_TOKEN = your_bot_token_here
ADMIN_ID = your_telegram_id
```

### 5. Run the bot

```
python bot.py
```

## ☁️ Deployment

Although the bot runs on Telegram, you need to host the backend (this Python bot) on a server so it can stay online and listen for incoming messages. Here are a few options:

### Option 1: Run Locally (Development Mode)

```bash
python bot.py
```
***⚠️ The bot will stop working when you shut down your computer. Use this only for testing.***

### Option 2: Deploy on Heroku (Recommended for Beginners)

1. Create a Heroku account and a new app.

2. Add your environment variables (TELEGRAM_TOKEN, ADMIN_ID) in the dashboard.

3. Push your code using Git or use the Heroku CLI.

4. Add a Procfile and enable worker dynos if needed.

### Option 3: Use Docker + VPS

Run your bot in a Docker container and deploy it on a VPS like DigitalOcean or AWS EC2.

```
docker build -t telegram-bot .
docker run -d telegram-bot
```

### Option 4: Serverless (Advanced)

You can also use Google Cloud Functions or AWS Lambda + API Gateway with webhooks, but this requires modifying the bot to use webhook mode instead of polling.

## 🧪 Usage


### /start

Shows a welcome message.

![](/assets/start.png)

### /add <product> <quantity> <price>

Adds a new product to the inventory.

```
/add AppMacBook  1 1500.99
```

![](/assets/addProducto.png)

You can also update the products that have been added before. but using the correct prompt.

![](/assets/addActualizacion.png)

If you try to use an incorrect prompt with the /add, the result is going to be:

![](/assets/addError.png)

### /list

Returns a formatted list of all products.

if there's some articles added, the result of this prompt is going to be: 
![](/assets/listProducto.png)

but, if the inventory is empty, the result is going to be :
![](/assets/listVacio.png)

### /delete <product> (Admin only)

Deletes a product from the database.

```
/delete MacBook
```

![](/assets/delete.png)

## 📂 Folder Structure

```
├── bot.py                  # Main bot logic
├── firebase_config.py      # Firebase configuration
├── requirements.txt
├── .env.example
└── README.md
```

## 🤝 Contributing

We welcome contributions! Please check the [CONTRIBUTING.md](/CONTRIBUTING.md) file for guidelines and future ideas.

## 🌐 Author

Developed by Jesús Gallardo