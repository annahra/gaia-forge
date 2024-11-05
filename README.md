# Gaia Forge

A Flask application for environmental data visualization, providing information on native species, soil chemistry, and other environmental factors around the globe.

## Prerequisites

Make sure you have the following installed:

- **Python 3.9+**
- **Neo4j** (with the server running locally)
- **pip** (Python package manager)
- **Homebrew** (for macOS users, if Neo4j needs to be installed)

## Getting Started

Follow these steps to set up the project and get it running locally.

### 1. Clone the Repository

git clone https://github.com/your-username/gaia-forge.git  
cd gaia-forge

### 2. Set Up a Virtual Environment

It’s recommended to create a virtual environment to manage dependencies.

python3 -m venv venv  
source venv/bin/activate # macOS/Linux  
venv\Scripts\activate # Windows

### 3. Install Dependencies

Install the necessary Python packages:

pip install -r requirements.txt

If you don’t have `requirements.txt`, you can manually install the main dependencies:

pip install Flask Flask-SQLAlchemy neo4j

### 4. Set Up Neo4j

#### Installing Neo4j (if not installed)

For macOS users, you can install Neo4j using Homebrew:

brew install neo4j

#### Start the Neo4j Server

neo4j start

#### Disable Authentication (Optional, for Development Only)

If you encounter authentication issues, you can disable authentication by editing the Neo4j configuration:

Open the configuration file:

nano /opt/homebrew/Cellar/neo4j/<your-version>/libexec/conf/neo4j.conf

Uncomment and set the line:

dbms.security.auth_enabled=false

Save the file and restart Neo4j:

neo4j restart

### 5. Configure Flask

In `app/__init__.py`, ensure that your Neo4j driver setup matches your configuration:

from neo4j import GraphDatabase

# Use this for no authentication:

neo4j_driver = GraphDatabase.driver("bolt://localhost:7687")

### 6. Run the Application

Start the Flask application:

python3 run.py

The app should now be running locally at `http://127.0.0.1:5000`.

### 7. Test the Endpoints

To confirm the setup, you can test the `/test_sql` and `/test_graph` endpoints.

#### SQL Test Endpoint

curl http://127.0.0.1:5000/test_sql

Expected Output:

{"message": "SQL DB connected!"}

#### Graph Test Endpoint

curl http://127.0.0.1:5000/test_graph

Expected Output:

{"message": "Graph DB connected! Node: <Node details>"}

### 8. Export Requirements (Optional)

If you install additional packages, make sure to update `requirements.txt`:

pip freeze > requirements.txt

## Contributing

Feel free to fork this project and submit pull requests. Any feedback is welcome!

## License

MIT License

This `README.md` covers the essentials for anyone to set up the project and reach the same point you've achieved. Adjust URLs or project-specific details as needed!
