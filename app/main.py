from fastapi import FastAPI

app = FastAPI()

"""
Only uncomment below to create new tables,
otherwise the tests will fail if not connected
"""
# Base.metadata.create_all(bind=engin