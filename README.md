# Phase 3 Code Challenge: Articles - without SQLAlchemy

Welcome to the Phase 3 Code Challenge for the Articles project! In this challenge, you will be working on building a simple articles management system without using SQLAlchemy, a popular Object-Relational Mapping (ORM) library. Instead, you will directly interact with the database using raw SQL queries and Python.

## Project Overview

In this challenge, you'll be tasked with creating a basic system for managing articles. Users should be able to perform the following actions:

1. **Create an Article**: Users can create new articles by providing a title, content, and author information.

2. **Retrieve Articles**: Users can retrieve a list of all articles or view a specific article by its ID.

3. **Update an Article**: Users can update the content of an existing article by providing a new content.

4. **Delete an Article**: Users can delete an article by its ID.

## Project Structure

The project has the following files and directories:

- `main.py`: This is the main entry point of the application. It contains the logic for handling user interactions and processing their commands.

- `database.py`: This file contains the functions to interact with the database using raw SQL queries. You will implement functions for creating, retrieving, updating, and deleting articles.

- `models.py`: In this file, you will define a simple `Article` class that represents the structure of an article. This class will help you manage the data before interacting with the database.

## Getting Started

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/articles-challenge-without-sqlalchemy.git
```

2. Navigate to the project directory:

```
cd articles-challenge-without-sqlalchemy
```

3. Open the `database.py` file and implement the required functions for interacting with the database. You'll be using raw SQL queries to perform CRUD operations.

4. In the `models.py` file, define the `Article` class with attributes such as `id`, `title`, `content`, and `author`.

5. Open the `main.py` file and implement the user interaction logic. Prompt the user with options to create, retrieve, update, or delete articles based on their input.

6. Test your application by running the `main.py` script:

```
python main.py
```

## Project Requirements

- You should use raw SQL queries to interact with the database.

- All user interactions should be handled in the `main.py` file.

- Implement functions in `database.py` to perform CRUD operations on articles.

- Create a `models.py` file with the `Article` class to manage article data.

- Ensure error handling and validation for user inputs.




