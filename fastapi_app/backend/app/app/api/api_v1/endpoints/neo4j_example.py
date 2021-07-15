""" A Very dirty example of querying Neo, not production ready but just intended to prove basic functionality quickly."""
from fastapi import APIRouter
from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable


router = APIRouter()


class NeoData:
    def __init__(self, uri):
        # TODO WILL NEED AUTH!!!!
        self.driver = GraphDatabase.driver(uri)

    def close(self):
        self.driver.close()

    def find_all(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_all)
            return result

    def add_example_data(self):
        with self.driver.session() as session:
            result = session.write_transaction(self._add_example)
            return result

    @staticmethod
    def _add_example(tx):
        query = (
            '''MERGE p = (andy: Person {name:'Andy'})-[:WORKS_AT]->(j:JOB {name: 'Neo'})<-[:WORKS_AT]-(michael: Person {name: 'Michael'})'''
        )
        result = tx.run(query)

    @staticmethod
    def _find_all(tx):
        query = (
            '''MATCH (n:Person)-[k:WORKS_AT]->(f)
            RETURN n.name AS name, f.name as place
            ORDER BY n.name'''
        )
        result = tx.run(query)
        try:
            return [{"name": row["name"], "workplace": row["place"]} for row in result]
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise


@router.post("/add-data/")
def add_data():
    """Adds the hardcoded example data to the db"""
    neo = NeoData("neo4j://neo:7687")
    neo.add_example_data()


@router.get("/find-data/")
def add_data():
    """Gets the names of the example data 'Person' nodes in the db"""
    neo = NeoData("neo4j://neo:7687")
    data = neo.find_all()
    return data
