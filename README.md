# BuzzBoard - Updates Platform

BuzzBoard is a web-based platform where users can post, view, and search for "updates." It's a social-style application where users can interact with updates posted by others. This project was built using Django and Bootstrap, with features like search functionality and the ability to post text and images in each update.

## Features

- **User Authentication**: Users can register, login, and logout.
- **Post Updates**: Users can post updates, including text and images.
- **Search Updates**: The search functionality allows users to search for specific updates by content.
- **Responsive Design**: Built with Bootstrap, the platform is responsive and works across different screen sizes.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (default, can be replaced with PostgreSQL or MySQL)
- **Authentication**: Django's built-in authentication system
- **Version Control**: Git
- **Deployment**: Can be deployed on platforms like Heroku, AWS, or DigitalOcean

## Installation Instructions

Follow the steps below to run the project locally.

### Prerequisites

Ensure that you have the following installed on your system:

- **Python**: 3.x or later
- **Django**: 5.x or later
- **pip**: Python package installer

### Setup

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/buzzboard.git
    ```

2. Navigate to the project directory:
    ```bash
    cd buzzboard
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - For **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - For **Mac/Linux**:
        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

7. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:
    ```bash
    python manage.py runserver
    ```

9. Access the application by navigating to `http://127.0.0.1:8000/` in your browser.

### Project Structure

- `buzzMessage/` - Main app handling the updates.
- `templates/` - HTML templates for rendering pages.
- `static/` - Static files (CSS, JavaScript, images).
- `requirements.txt` - Python dependencies.
- `urls.py` - URL routing for the application.

## Usage

- Register a new account or log in to an existing one.
- After logging in, you'll be redirected to the homepage where you can post updates.
- Use the search bar to search for specific updates.
- View updates with or without images.

## Screenshots

### Home Page:
![home](https://github.com/user-attachments/assets/899d6b9c-d922-41fa-8127-0f177a89e530)


### User Home:![user home](https://github.com/user-attachments/assets/602814bd-2169-47da-834f-e36d5134473d)



### Update Post:
![update](https://github.com/user-attachments/assets/e6f46179-9054-4c5e-be24-0279e495d5a4)


### Delete Post:![delete](https://github.com/user-attachments/assets/a4e3c348-34cf-4be7-a860-402889c6b7f3)



### Search Results:
![Screenshot (124)](https://github.com/user-attachments/assets/2cd4bf92-e213-48db-8364-e268f49ed806)![Screenshot (123)](https://github.com/user-attachments/assets/883d3608-0e04-48e9-8a20-aa60e23722dd)


### Log in Page:![login](https://github.com/user-attachments/assets/a6d26ddd-7e65-4f3b-a796-311ec29b288e)


### Registration Pgae:![registration](https://github.com/user-attachments/assets/c33c857a-bdee-4ca3-abe8-03527fdfe010)


### Search Results:

## Contributing

Feel free to fork this repository and submit pull requests if you wish to contribute. Please make sure your code adheres to the PEP 8 style guide and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
