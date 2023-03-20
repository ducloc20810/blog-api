from flask import Blueprint, jsonify
from ..db import db
from ..models.test import Test
from ..schemas.test import TestSchema

test = Blueprint("test", __name__)
TestsSchema = TestSchema(many=True)


@test.get("/test")
def get_test():
    new_test = Test(name="test")
    db.session.add(new_test)
    db.session.commit()
    tests = Test.query.all()
    return TestsSchema.jsonify(tests)
