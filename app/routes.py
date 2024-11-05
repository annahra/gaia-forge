from flask import Blueprint, jsonify
from app import db, neo4j_driver

main = Blueprint('main', __name__)

@main.route('/test_sql')
def test_sql():
  return jsonify({"message": "SQL DB connected!"})

@main.route('/test_graph')
def test_graph():
  with neo4j_driver.session() as session:
    result = session.run("MATCH (n) RETURN n LIMIT 1")
    node = result.single()
    return jsonify({"message": f"Graph DB connected! Node: {node}"})