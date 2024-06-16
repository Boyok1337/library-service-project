
# Library Service Project

This project was created specifically for a library management system. It facilitates the operation of library services, including book borrowings, user management, and payment handling via this API.

## 👩‍💻 _Installation & Run_

### 🧠 Set up the environment

### 📝 Set environment variable

- Copy and rename the **.env.sample** file to **.env**
- Open the .env file and edit the environment variables
- Save the .env file securely
- Add the .env file to .gitignore

On Windows:
```python
python -m venv venv 
venv\Scripts\activate
```

On UNIX or macOS:
```python
python3 -m venv venv 
source venv/bin/activate
```

### 🗃️ Install requirements

```python
docker-compose up --build
```

### 👥 Create a superuser (optional)

If you want to perform all available features, create a superuser account in a new terminal:
```python
docker exec -it library-service-project-db-1 /bin/sh
python manage.py createsuperuser
```

### 😄 Go to site [http://localhost:8000/](http://localhost:8000/)


## 📰 Features

- **1** JWT Authentication
- **2** Fake data for testing API
- **3** Swagger documentation
- **4** Docker
- **5** Telegram Bot
- **6** Redis as cache handler
- **7** Stripe Payment Integration


## 🚀 Services Overview

### Book Service

Manage books in the library.

### User Service

Manage user authentication and registration.

### Borrowing Service

Manage borrowings of books by users.

### Payment Service (Stripe)

Handle payments for book borrowings.

### Notification Service (Telegram)

Send notifications about borrowings and payments.

## 📲 Telegram Bot Functionality

The Telegram bot is set up to interact with users and administrators, providing timely notifications and allowing users to manage their borrowings.

### Key Features:

- **User Registration**: The bot registers users by linking their Telegram chat IDs to their user profiles.
- **Notifications**: Users receive notifications for:
  - New borrowings created.
  - Borrowing due dates.
  - Overdue borrowings.
  - Successful payments.
  - Notifications for new borrowings and overdue books.
- **Commands**:
  - `/start`: Initiates the registration process.
  - `/all_borrow`: Admin command to list all borrowings.
  - `/upcoming_borrow`: Lists upcoming borrowings for the user.

### Setting Up the Telegram Bot

1. **Create a Telegram Bot**: Use BotFather to create a new bot and get the API token.
2. **Configure Environment Variables**: Add the API token to your `.env` file.
3. **Run the Bot**: Ensure the bot is running and integrated with your Django project.

## 💳 Payment Handling

Payments for book borrowings are processed through Stripe. The integration ensures secure and efficient handling of transactions.

### Key Features:

- **Payment Creation**: Automatically create a Stripe payment session when a new borrowing is created.
- **Payment Status**: Track and update payment statuses (Pending, Paid).
- **Fines**: Calculate and process fines for overdue borrowings.

### Setting Up Stripe Payments

1. **Create a Stripe Account**: Set up a Stripe account and get the API keys.
2. **Configure Environment Variables**: Add the Stripe API keys to your `.env` file.
3. **Payment Workflow**: Implement the workflow to create, handle, and track payments using Stripe's API.

### Stripe Payment Workflow

- **Creating Payment Session**: A payment session is created when a user borrows a book. This session calculates the total price based on the borrowing duration and the book's daily fee.
- **Successful Payment**: Upon successful payment, the status is updated, and a notification is sent to the user.
- **Cancellation and Expiration**: Handle payment session cancellations and check for expired sessions regularly.

## 📝 Contributing

If you want to contribute to the project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Submit a pull request.

## 😋 _Enjoy it!_

---
