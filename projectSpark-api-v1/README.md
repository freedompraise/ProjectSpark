# ProjectSpark API

This is the backend API for ProjectSpark, a software tool that helps developers efficiently journal their ideas and aids in the early stages of brainstorming and project management.

## Table of Contents
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.10)
- Django (version 4.2.2)
- Django REST Framework (version 3.14.0)
- JWt for authentication (version 1.7.1)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/freedompraise/projectSpark-api-v1.git
```

2. Create a virtual environment:

```bash 
python3 -m venv venv
```

3. Activate the virtual environment:
- For Linux/macOS:
  ```
  source venv/bin/activate
  ```
- For Windows:
  ```
  venv\Scripts\activate
  ```

4. Install the required dependencies:
```bash 
pip install -r requirements.txt
```

5. Set up the database:
Change working directory to BASE_DIR
```sh 
cd projecSpark
```
Run
```sh 
python manage.py migrate
```

6. Start the development server:
```bash 
python manage.py runserver
```

## Usage
Once the development server is up and running, you can access the **projectSpark-api** endpoints to perform various operations such as user registration, authentication, idea creation, commenting, etc.

Make sure to refer to the [API Documentation](#api-documentation) section for detailed information on the available endpoints and their usage.

## API Documentation
Please refer to the [API Documentation](/docs/API_DOCUMENTATION.md) file for detailed information about the **projectSpark-api** endpoints, request/response formats, and authentication requirements.

## Contributing
Contributions are welcome! If you would like to contribute to **projectSpark-api**, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit your changes and push them to your branch.
4. Submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).


