import connexion


def schemes__get():
    response = [{
        "schemeId": 60,
        "name": "Test Schema 01"
    }, {
        "schemeId": 60,
        "name": "Test Schema 02"
    }]

    return response, 200


def schemes__post() -> str:
    return 'schemes__post'


def schemes_x_assessors__get(schemeId) -> str:
    return 'schemes_x_assessors__get schemeId={schemeId}'.format(schemeId=schemeId)


def schemes_x_assessors_x__get(schemeId, schemeAssessorId) -> str:
    return 'schemes_x_assessors_x__get schemeId={schemeId} schemeAssessorId={schemeAssessorId}'.format(schemeId=schemeId, schemeAssessorId=schemeAssessorId)


def schemes_x_assessors_x__put(schemeId, schemeAssessorId):
    if schemeId != 60:
        return 'Scheme not found', 404

    if schemeAssessorId == 'EES/090001':
        return connexion.request.json, 200
    else:
        return connexion.request.json, 201


def search_assessors__get() -> str:
    return 'search_assessors__get'


def search_addresses__get() -> str:
    return 'search_addresses__get'


def assessments_x__get() -> str:
    return 'assessments_x__get'


def assessments_x_x__post(assessmentType, assessmentId) -> str:
    return 'assessments_x_x__post assessmentType={assessmentType} assessmentId={assessmentId}'.format(assessmentType=assessmentType, assessmentId=assessmentId)


def reports_assessors_status__get() -> str:
    return 'reports_assessors_status__get'


def migrations_assessors_x__put(schemeAssessorId) -> str:
    return 'schemes_x_assessors_x__put  schemeAssessorId={schemeAssessorId}'.format(schemeAssessorId=schemeAssessorId)


def migrations_assessments_x__put(assessmentId) -> str:
    return 'migrations_assessments_x__put  assessmentId={assessmentId}'.format(assessmentId=assessmentId)


def migrations_addresses_x__put(addressId) -> str:
    return 'migrations_addresses_x__put  addressId={addressId}'.format(addressId=addressId)
