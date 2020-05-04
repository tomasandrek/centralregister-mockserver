import connexion
import json
from flask import Response


class address:
    def __init__(self, p_source, p_line1, p_line2, p_line3, p_line4, p_town, p_postcode, p_addressId, p_existingAssessments):
        self.source = p_source
        self.line1 = p_line1
        self.line2 = p_line2
        self.line3 = p_line3
        self.line4 = p_line4
        self.town = p_town
        self.postcode = p_postcode
        self.addressId = p_addressId
        self.existingAssessments = p_existingAssessments


addresses = []
addresses.append(address("GAZETTEER", "2 Marsham Street", "Line 2",
                         "Line 3", "", "London", "SW1P 4JA", "UPRN-7163757", []))
addresses.append(address("PREVIOUS_CERTIFICATE", "2 Marsham Street", "Line2",
                         "Line3", "", "London", "SW1P 4JA", "RRN-8290-6027-4450-1230-9999", []))
addresses.append(address("PREVIOUS_CERTIFICATE", "10 Marsham Street",
                         "", "", "", "London", "SW1P 4JA", "RRN-8290-6027-4450-1230-5296", []))

addresses.append(address("GAZETTEER", "Elmhurst Energy Systems Ltd", "16 St. Johns Business Park",
                         "", "", "LUTTERWORTH", "LE17 4HB", "UPRN-5498652", []))
addresses.append(address("GAZETTEER", "The Cottage", "Church Lane",
                         "Comberton", "", "CAMBRIDGE", "CB23 7ED", "UPRN-54112352", []))
addresses.append(address("GAZETTEER", "H W Coates Ltd", "Ladywood Works, Leicester Road",
                         "", "", "LUTTERWORTH", "LE17 4HD", "UPRN-12312352", []))
addresses.append(address("GAZETTEER", "Flat 5 Laughton Court", "Stoughton Road",
                         "", "", "LEICESTER", "LE2 2ED", "UPRN-9872352", []))
addresses.append(address("GAZETTEER", "56, Wendover Heights", "Old Tring Road",
                         "", "", "AYLESBURY", "HP22 6PH", "UPRN-88009872352", []))
addresses.append(address("GAZETTEER", "Flat 2", "1, Upper Cape",
                         "", "", "WARWICK", "CV34 5DS", "UPRN-14009872352", []))

addresses.append(address("GAZETTEER", "The Vestry", "Llanddewi Velfrey",
                         "", "", "NARBERTH", "SA67 7EG", "UPRN-14009871232", []))
addresses.append(address("GAZETTEER", "Bryn Mor", "Rhosgadfan",
                         "", "", "CAERNARFON", "LL54 7HR", "UPRN-98709871232", []))
addresses.append(address("GAZETTEER", "10, Lon Ty'n-y-Cae", "",
                         "", "", "CARDIFF", "CF14 6DD", "UPRN-98882871232", []))
addresses.append(address("GAZETTEER", "59, Hanbury Road", "Pontnewynydd",
                         "", "", "PONTYPOOL", "NP4 6PF", "UPRN-11882871232", []))
addresses.append(address("GAZETTEER", "Cae'r Odyn", "Rhiw",
                         "", "", "PWLLHELI", "LL53 8AS", "UPRN-11882221232", []))
addresses.append(address("GAZETTEER", "28, Penrho Estate", "Mostyn",
                         "", "", "HOLYWELL", "CH8 9QS", "UPRN-18882221232", []))

addresses.append(address("GAZETTEER", "Atos Healthcare", "Metropolitan Building 29-31, Alfred Street",
                         "", "", "BELFAST", "BT2 8ED", "UPRN-17742221232", []))
addresses.append(address("GAZETTEER", "Belfast Health Cities", "Gordon House, 22-24, Lombard Street",
                         "", "", "BELFAST", "BT1 1RD", "UPRN-47742221232", []))
addresses.append(address("PREVIOUS_CERTIFICATE", "17a, Moss Road", "Ballinaskeagh",
                         "", "", "BANBRIDGE", "BT32 5EF", "RRN-1110-6027-4450-1230-5296", []))
addresses.append(address("GAZETTEER", "78, St. James's Road", "",
                         "", "", "BELFAST", "BT12 6ED", "UPRN-88742110232", []))
addresses.append(address("GAZETTEER", "39, Lord Warden's Glade", "",
                         "", "", "BANGOR", "BT19 1GW", "UPRN-98742110232", []))
addresses.append(address("GAZETTEER", "Apartment 219", "10, Edward Street",
                         "", "", "BELFAST", "BT1 2LP", "UPRN-14742110232", []))


def schemes__get():
    response = {
        "data": {
            "schemes": [
                {
                    "name": "Elmhurst",
                    "schemeId": 3
                }
            ]
        }
    }

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
            'schemeId': 3,
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
            'schemeId': 3,
            'name': 'Test Schema 01'
        },
        'schemeAssessorId': 'X999-0002',
        'searchResultsComparisonPostcode': 'SW1P 4JA'
    }]

    if schemeId == 3:
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
            'schemeId': 3,
            'name': 'Test Schema 01'
        },
        'schemeAssessorId': 'X999-0001',
        'searchResultsComparisonPostcode': 'SW1P 4JA'
    }

    if schemeId != 3:
        return 'Scheme not found', 404

    if schemeAssessorId == 'X999-0001':
        return response, 200
    else:
        return 'Assessor not found', 404


def schemes_x_assessors_x__put(schemeId, schemeAssessorId):
    if schemeId != 3:
        return 'Scheme not found', 404

    if schemeAssessorId == 'EES/090001':
        return connexion.request.json, 200
    else:
        return connexion.request.json, 201


def assessors__get() -> str:
    return 'assessors__get'


def search_addresses__get(**query):
    if 'postcode' not in query and 'street' not in query and 'buildingReferenceNumber' not in query:
        return [], 500

    items = [x for x in addresses]

    if 'postcode' in query:
        postcode = query['postcode']
        if (postcode != ''):
            items = [x for x in items if x.postcode == postcode]

    if 'street' in query:
        street = query['street']
        items = [x for x in items if x.line1 == street]

    if 'town' in query:
        town = query['town']
        items = [x for x in items if x.town == town]

    if 'buildingReferenceNumber' in query:
        buildingReferenceNumber = query['buildingReferenceNumber']
        items = [x for x in addresses if x.addressId ==
                 buildingReferenceNumber]

    json_dump = json.dumps([ob.__dict__ for ob in items])
    return Response(json_dump, status=200, mimetype='application/json')


def assessments_x__get() -> str:
    return 'assessments_x__get'


def assessments_x__post(assessmentId) -> str:
    return 'assessments_x__post assessmentId={assessmentId}'.format(assessmentId=assessmentId)


def reports_assessors_status__get() -> str:
    return 'reports_assessors_status__get'


def migrations_assessors_x__put(schemeAssessorId) -> str:
    return 'schemes_x_assessors_x__put  schemeAssessorId={schemeAssessorId}'.format(schemeAssessorId=schemeAssessorId)


def assessments_domesticepc_x__put(assessmentId) -> str:
    return 'assessments_domesticepc_x__put  assessmentId={assessmentId}'.format(assessmentId=assessmentId)


def migrations_addresses_x__put(addressId):
    return connexion.request.json, 201


def greendeal_assessments_x__get() -> str:
    return 'greendeal_assessments_x__get'


def greendeal_rhi_assessments_x_latest__get() -> str:
    return 'greendeal_rhi_assessments_x_latest__get'


def greendeal_disclosure_assessments_x_plans__put(assessmentId) -> str:
    return 'greendeal_disclosure_assessments_x_plans__put  assessmentId={assessmentId}'.format(assessmentId=assessmentId)


def greendeal_disclosure_plans_x__put(planId) -> str:
    return 'greendeal_disclosure_plans_x__put  planId={planId}'.format(planId=planId)


def greendeal_disclosure_plans_x__delete(planId) -> str:
    return 'greendeal_disclosure_plans_x__delete  planId={planId}'.format(planId=planId)
