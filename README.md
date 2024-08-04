# KATA CACIB : RPN calculator

## Stack used

* Fastapi app
* Database (SQLite3)

### Application Structure

The API is divided in two parts `default` and `RPN calculator`.

The `RPN calculator` part is responsible for handeling all requests related to the functionalities of the RPN calculator.

The `default` contains an endpoint that allows to check if the API is in working order.

## Installation

### Template and Dependencies

* Clone this repository:

 ```zsh
 git clone https://github.com/trezakou/rpn-calculator-kata-cacib.git
 ```

### Virtual Environment Setup

An Anaconda venv was used during the development of this project, please create your own env with **python=3.11**

like so:

```bash
conda create -n ENVNAME python=3.11
```

### Dependency installations

To install the necessary packages:

```bash
conda activate ENVNAME
pip install -r requirements.txt
```

This will install the required packages within your venv.

---

### Setting up a SQLite3 Database

Database migrations are handled through Alembic. Migrations are for creating and upgrading necessary tables in your database.

First, we need to initialize the database. in order to do so, run the following command to create it:

```zsh
alembic upgrade head
```

### Running the app

Finally, run the API itself with the following command:

```zsh
uvicorn app.main:app --reload
```

### Accessing the swagger

when the app is running, the API swagger is available here:

http://localhost:8000/swagger


