# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

`GET '/api/v1.0/categories'`

- Fetches a list of category objects with the id and the type of a category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains alist of objects of `id: category_id, type: category_string`.

```json
{
  "categories": [
    {
      "id": 1,
      "type": "Art"
    },
    {
      "id": 2,
      "type": "Geography"
    }
  ]
}
```

`GET '/api/v1.0/questions'`

- Fetches a list of question objects with the id, question, answer, category and difficulty of a question
- Request Arguments: None
- Returns: An object with keys,`total_questions`, `categories` and `questions`, that contains a list of objects of `id: question_id, question: question_string, answer: answer_string, category: category_string, difficulty: difficulty_int`.

```json
{
  "questions":[
    {"id": 1,
     "question": "How does this work?",
     "answer": "No idea.",
     "category": "Art",
     "difficulty":2
    }],
  "total_questions": 10,
  "categories": [{"id": 1, "type": "Art"}]
}
```

`DELETE '/api/v1.0/questions/<question_id>'`

- Deletes a question objects with the specified id
- Request Arguments: question_id
- Returns: An object with keys, `deleted` which contains the id of the deleted question, `total_questions`, `categories` and `questions`, that contains a list of objects of `id: question_id, question: question_string, answer: answer_string, category: category_string, difficulty: difficulty_int`.

```json
{
  "deleted": 2,
  "questions":[
    {"id": 1,
     "question": "How does this work?",
     "answer": "No idea.",
     "category": "Art",
     "difficulty":2
    }],
  "total_questions": 10,
  "categories": [{"id": 1, "type": "Art"}]
}
```


`POST '/api/v1.0/questions/create'`

- Creates a new question object
- Request Arguments: None
- Returns: An object with keys, `created` which is the id of the newly created question, `total_questions` and `questions`, that contains a list of objects of `id: question_id, question: question_string, answer: answer_string, category: category_string, difficulty: difficulty_int`.

```json
{
  "created": 222,
  "questions":[
    {"id": 1,
     "question": "How does this work?",
     "answer": "No idea.",
     "category": "Art",
     "difficulty":2
    }],
  "total_questions": 10
}
```

`POST '/api/v1.0/questions/search'`

- Searches for a question and returns the search restuls
- Request Arguments: None
- Returns: An object with keys, `total_questions` and `questions`, that contains a list of objects of `id: question_id, question: question_string, answer: answer_string, category: category_string, difficulty: difficulty_int`.

```json
{
  "questions":[
    {"id": 1,
     "question": "How does this work?",
     "answer": "No idea.",
     "category": "Art",
     "difficulty":2
    }],
  "total_questions": 10
}
```

`GET '/api/v1.0/categories/<category_id>/questions'`

- Fetches all questions for a given category
- Request Arguments: category_id
- Returns: An object with keys, `current_category`, `total_questions` and `questions`, that contains a list of objects of `id: question_id, question: question_string, answer: answer_string, category: category_string, difficulty: difficulty_int`.

```json
{
  "questions":[
    {"id": 1,
     "question": "How does this work?",
     "answer": "No idea.",
     "category": "Art",
     "difficulty":2
    }],
  "total_questions": 10,
  "current_category": "Art"
}
```

`POST '/api/v1.0/quizzes'`

- Fetches questions for a quizz
- Request Arguments: category_id
- Returns: An object with key, `question`, that contains the next question to be answered `id: question_id, question: question_string, answer: answer_string, category: category_string, difficulty: difficulty_int`.

```json
{
  "questions":
    {"id": 1,
     "question": "How does this work?",
     "answer": "No idea.",
     "category": "Art",
     "difficulty":2
    }
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
