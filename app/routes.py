from fastapi import APIRouter, HTTPException
import dal

router = APIRouter()

@router.get('/employees/engineering/high-salary')
def get_engineering_high_salary_employees():
    try: 
        data = dal.get_engineering_high_salary_employees()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/employees/by-age-and-role')
def get_employees_by_age_and_role():
    try: 
        data = dal.get_employees_by_age_and_role()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/employees/top-seniority')
def get_top_seniority_employees_excluding_hr():
    try: 
        data = dal.get_top_seniority_employees_excluding_hr()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/employees/age-or-seniority')
def get_employees_by_age_or_seniority():
    try: 
        data = dal.get_employees_by_age_or_seniority()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/employees/managers/excluding-departments')
def get_managers_excluding_departments():
    try: 
        data = dal.get_managers_excluding_departments()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/employees/by-lastname-and-age')
def get_employees_by_lastname_and_age():
    try: 
        data = dal.get_employees_by_lastname_and_age()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
