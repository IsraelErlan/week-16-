from connection import get_collection, init_db
from pymongo import MongoClient
from pprint import pprint

# init_db()

def run_query(query, projection):
    col = get_collection()
    res = col.find(query, projection)
    return res.to_list()


def convert_objects_to_srting(data: list):
    for obj in data: 
        if '_id' in obj: 
            obj['_id'] = str(obj['_id'])
    return data


def run_query_and_convert_to_string(query, projection):
    data = run_query(query, projection)
    data = convert_objects_to_srting(data)
    return data

def get_engineering_high_salary_employees():
    query = {'job_role.department' :'Engineering', 
             'salary': {'$gt': 65000}}
    projection = {'_id': 0,
                  'employee_id': 1, 
                  'name': 1, 
                  'salary': 1}
    
    data = run_query(query, projection)
    return data


def get_employees_by_age_and_role():
    query = {'$and': [{'age': {'$gte': 30}}, {'age': {'$lte': 45}}],
            '$or': [{'job_role.title': 'Engineer'}, {'job_role.title': 'Specialist'}]
    }
    projection = {}
    data = run_query_and_convert_to_string(query, projection)
    return data


def get_top_seniority_employees_excluding_hr():
    query = {'job_role.department' :{'$ne': 'HR'}}
    col = get_collection()
    res = col.find(query).sort({'years_at_company': -1})
    data = res.to_list(7)
    data = convert_objects_to_srting(data)
    return data
    

def get_employees_by_age_or_seniority():
    query = {
            '$or': [{'age': {'$gt': 50}}, {'years_at_company': {'$lt': 3}}]
    }
    projection = {'_id': 0,
                  'employee_id': 1, 
                  'name': 1, 
                  'age': 1,
                  'years_at_company': 1}
    data = run_query_and_convert_to_string(query, projection)
    return data


def get_managers_excluding_departments():
    query = {
            '$and': [
                {'job_role.title':'Manager'}, 
                {'job_role.department': {'$ne': 'Sales'}} , 
                {'job_role.department': {'$ne': 'Marketing'}} 
                     ]
    }
    projection = {}
    data = run_query_and_convert_to_string(query, projection)
    return data



def get_employees_by_lastname_and_age(): 
    query = { '$or': [
                {'name': {'$regex': ' Wright$'}},
                {'name': {'$regex': ' Nelson$'}}
                    ],
            'age': {'$lt': 35}
    }
    projection = {'_id': 0,
                  'name': 1, 
                  'age': 1,
                  'job_role.department': 1}
    data = run_query(query, projection)
    return data

d = get_employees_by_lastname_and_age()
pprint(d)
print(len(d))
