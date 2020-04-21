# Connecting Flask-SQLAlchemy with Google Cloud SQL

Playing around with Flask and Cloud SQL. Boilerplate code for connecting `Google Cloud SQL` with `Flask-SQLAlchemy`. This contains a detailed explaination of `setting up the SQL Instance` and `configuring` it to be able to edit and access the data from our production machine.

---

## How to get started

### Setting up Cloud SQL

1. Create a project in `Google Cloud Platform` and enable the `Cloud SQL Admin API` from the `Marketplace`.

2. Now, create a `Cloud SQL` Instance.

### Setting up server:

1. First clone this repo and change the directory to `cloud-sql-flask/api`.

2. Run `pip install -r requirements.txt` to install all the necessary packages.

3. Now change directory to `flask_app` and edit the file `.env` with your `Cloud SQL` configurations. The details regarding assigning the configuration is present inside all the python files. Head over to any one of them to get set them up.

4. Now change to the parent directory and start the flask server by running the following command:

    ```
    flask run
    ```

---