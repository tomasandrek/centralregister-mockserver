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


def schemes_x_assessors__get(schemeId):
    response = [{
        'firstName': 'Jo',
        'lastName': 'Blogs',
        'middleNames': 'T',
        'contactDetails': {
            'telephoneNumber': '123456',
            'email': 'j.t.bloggs@example.com'
        },
        'qualifications': {
            'domesticRdSap': 'ACTIVE',
            'domesticSap': 'ACTIVE',
            'nonDomesticDec': 'ACTIVE',
            'nonDomesticNos3': 'ACTIVE',
            'nonDomesticNos4': 'ACTIVE',
            'nonDomesticNos5': 'ACTIVE',
            'nonDomesticSp3': 'ACTIVE',
            'nonDomesticCc4': 'ACTIVE'
        },
        'dateOfBirth': '1990-01-10',
        'registeredBy': {
            'schemeId': 60,
            'name': 'Test Schema 01'
        },
        'schemeAssessorId': 'X999-0001',
        'searchResultsComparisonPostcode': 'SW1P 4JA'
    }, {
        'firstName': 'Vlado',
        'lastName': 'Polacok',
        'middleNames': 'J',
        'contactDetails': {
            'telephoneNumber': '123456',
            'email': 'v.j.polacok@example.com'
        },
        'qualifications': {
            'domesticRdSap': 'ACTIVE',
            'domesticSap': 'ACTIVE',
            'nonDomesticDec': 'ACTIVE',
            'nonDomesticNos3': 'ACTIVE',
            'nonDomesticNos4': 'ACTIVE',
            'nonDomesticNos5': 'ACTIVE',
            'nonDomesticSp3': 'ACTIVE',
            'nonDomesticCc4': 'ACTIVE'
        },
        'dateOfBirth': '1972-01-10',
        'registeredBy': {
            'schemeId': 60,
            'name': 'Test Schema 01'
        },
        'schemeAssessorId': 'X999-0002',
        'searchResultsComparisonPostcode': 'SW1P 4JA'
    }]

    if schemeId == 60:
        return response, 200
    else:
        return 'Scheme not found', 404


def schemes_x_assessors_x__get(schemeId, schemeAssessorId):
    response = {
        'firstName': 'Jo',
        'lastName': 'Blogs',
        'middleNames': 'T',
        'contactDetails': {
            'telephoneNumber': '123456',
            'email': 'j.t.bloggs@example.com'
        },
        'qualifications': {
            'domesticRdSap': 'ACTIVE',
            'domesticSap': 'ACTIVE',
            'nonDomesticDec': 'ACTIVE',
            'nonDomesticNos3': 'ACTIVE',
            'nonDomesticNos4': 'ACTIVE',
            'nonDomesticNos5': 'ACTIVE',
            'nonDomesticSp3': 'ACTIVE',
            'nonDomesticCc4': 'ACTIVE'
        },
        'dateOfBirth': '1990-01-10',
        'registeredBy': {
            'schemeId': 60,
            'name': 'Test Schema 01'
        },
        'schemeAssessorId': 'X999-0001',
        'searchResultsComparisonPostcode': 'SW1P 4JA'
    }

    if schemeId != 60:
        return 'Scheme not found', 404

    if schemeAssessorId == 'X999-0001':
        return response, 200
    else:
        return 'Assessor not found', 404


def schemes_x_assessors_x__put(schemeId, schemeAssessorId):
    if schemeId != 60:
        return 'Scheme not found', 404

    if schemeAssessorId == 'EES/090001':
        return connexion.request.json, 200
    else:
        return connexion.request.json, 201


def search_assessors__get() -> str:
    return 'search_assessors__get'


def search_addresses__get(**query):
    if 'postcode' not in query and 'street' not in query and 'addressId' not in query:
        return [], 500

    if 'street' in query:
        street = query['street']

    if 'postcode' in query:

        postcode = query['postcode']

        if postcode == 'SW1P 4JX':
            return [], 403

        if postcode != 'SW1P 4JA':
            return [], 200

        if 'street' in query and street == '2 Marsham Street':
            response = [{
                'source': 'GAZETTEER',
                'line1': '2 Marsham Street',
                'line2': 'Line 2',
                'line3': 'Line 3',
                'line4': '',
                'town': 'London',
                'postcode': 'SW1P 4JA',
                'addressId': 'UPRN-7163757',
                'existingAssessments': []
            }]
            return response, 200

        if 'street' in query and street != '2 Marsham Street':
            response = []
            return response, 200

        response = [{
            'source': 'GAZETTEER',
            'line1': '2 Marsham Street',
            'line2': 'Line 2',
            'line3': 'Line 3',
            'line4': '',
            'town': 'London',
            'postcode': 'SW1P 4JA',
            'addressId': 'UPRN-7163757',
            'existingAssessments': []
        }, {
            'source': 'PREVIOUS_CERTIFICATE',
            'line1': '2 Marsham Street',
            'line2': 'Line2',
            'line3': 'Line3',
            'line4': '',
            'town': 'London',
            'postcode': 'SW1P 4JA',
            'addressId': 'RRN-8290-6027-4450-1230-9999',
            'existingAssessments': []
        }, {
            'source': 'PREVIOUS_CERTIFICATE',
            'line1': '10 Marsham Street',
            'line2': '',
            'line3': '',
            'line4': '',
            'town': 'London',
            'postcode': 'SW1P 4JA',
            'addressId': 'RRN-8290-6027-4450-1230-5296',
            'existingAssessments': []
        }]

        return response, 200

    if 'addressId' in query:

        addressId = query['addressId']

        if addressId == 'UPRN-7163757':
            response = [{
                'source': 'GAZETTEER',
                'line1': '2 Marsham Street',
                'line2': 'Line 2',
                'line3': 'Line 3',
                'line4': '',
                'town': 'London',
                'postcode': 'SW1P 4JA',
                'addressId': 'UPRN-7163757',
                'existingAssessments': []
            }]
            return response, 200

        if addressId == 'RRN-8290-6027-4450-1230-5296':
            response = [{
                'source': 'PREVIOUS_CERTIFICATE',
                'line1': '10 Marsham Street',
                'line2': '',
                'line3': '',
                'line4': '',
                'town': 'London',
                'postcode': 'SW1P 4JA',
                'addressId': 'RRN-8290-6027-4450-1230-5296',
                'existingAssessments': []
            }]
            return response, 200

        if addressId == 'RRN-8290-6027-4450-1230-9999':
            response = [{
                'source': 'PREVIOUS_CERTIFICATE',
                'line1': '2 Marsham Street',
                'line2': 'Line2',
                'line3': 'Line3',
                'line4': '',
                'town': 'London',
                'postcode': 'SW1P 4JA',
                'addressId': 'RRN-8290-6027-4450-1230-9999',
                'existingAssessments': []
            }]
            return response, 200

        return [], 403


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


def migrations_addresses_x__put(addressId):
    return connexion.request.json, 201
