#-------------------------------------------------------------------------------
# Name:        test_models
# Purpose:     Unit tests for Python Schema.org models using
#              <http://schema.rdfs.org/all.rdf>
#
# Author:      Jeremy Nelson
#
# Created:     2014-02-21
# Copyright:   (c) Jeremy Nelson, Colorado College 2014
# Licence:     MIT
#-------------------------------------------------------------------------------
import json
import unittest
from models import *

class TestAPIReference(unittest.TestCase):

    def setUp(self):
        self.api_reference = APIReference()

    def test_init(self):
        self.assertEquals(type(self.api_reference), APIReference)

    def test_rdf_properties(self):
		self.assert_(hasattr(self.api_reference, "accessibilityAPI"))
		self.assert_(hasattr(self.api_reference, "accessibilityControl"))
		self.assert_(hasattr(self.api_reference, "accessibilityFeature"))
		self.assert_(hasattr(self.api_reference, "accessibilityHazard"))
		self.assert_(hasattr(self.api_reference, "accountablePerson"))
		self.assert_(hasattr(self.api_reference, "additionalType"))
		self.assert_(hasattr(self.api_reference, "alternateName"))
		self.assert_(hasattr(self.api_reference, "alternativeHeadline"))
		self.assert_(hasattr(self.api_reference, "articleBody"))
		self.assert_(hasattr(self.api_reference, "articleSection"))
		self.assert_(hasattr(self.api_reference, "assembly"))
		self.assert_(hasattr(self.api_reference, "assemblyVersion"))
		self.assert_(hasattr(self.api_reference, "associatedMedia"))
		self.assert_(hasattr(self.api_reference, "audio"))
		self.assert_(hasattr(self.api_reference, "author"))
		self.assert_(hasattr(self.api_reference, "citation"))
		self.assert_(hasattr(self.api_reference, "comment"))
		self.assert_(hasattr(self.api_reference, "contentLocation"))
		self.assert_(hasattr(self.api_reference, "contentRating"))
		self.assert_(hasattr(self.api_reference, "contributor"))
		self.assert_(hasattr(self.api_reference, "copyrightHolder"))
		self.assert_(hasattr(self.api_reference, "copyrightYear"))
		self.assert_(hasattr(self.api_reference, "dateCreated"))
		self.assert_(hasattr(self.api_reference, "dateModified"))
		self.assert_(hasattr(self.api_reference, "datePublished"))
		self.assert_(hasattr(self.api_reference, "dependencies"))
		self.assert_(hasattr(self.api_reference, "description"))
		self.assert_(hasattr(self.api_reference, "discussionUrl"))
		self.assert_(hasattr(self.api_reference, "editor"))
		self.assert_(hasattr(self.api_reference, "educationalAlignment"))
		self.assert_(hasattr(self.api_reference, "educationalUse"))
		self.assert_(hasattr(self.api_reference, "encoding"))
		self.assert_(hasattr(self.api_reference, "encodings"))
		self.assert_(hasattr(self.api_reference, "genre"))
		self.assert_(hasattr(self.api_reference, "headline"))
		self.assert_(hasattr(self.api_reference, "image"))
		self.assert_(hasattr(self.api_reference, "inLanguage"))
		self.assert_(hasattr(self.api_reference, "interactivityType"))
		self.assert_(hasattr(self.api_reference, "isBasedOnUrl"))
		self.assert_(hasattr(self.api_reference, "isFamilyFriendly"))
		self.assert_(hasattr(self.api_reference, "keywords"))
		self.assert_(hasattr(self.api_reference, "learningResourceType"))
		self.assert_(hasattr(self.api_reference, "mentions"))
		self.assert_(hasattr(self.api_reference, "name"))
		self.assert_(hasattr(self.api_reference, "proficiencyLevel"))
		self.assert_(hasattr(self.api_reference, "programmingModel"))
		self.assert_(hasattr(self.api_reference, "publisher"))
		self.assert_(hasattr(self.api_reference, "publishingPrinciples"))
		self.assert_(hasattr(self.api_reference, "sameAs"))
		self.assert_(hasattr(self.api_reference, "sourceOrganization"))
		self.assert_(hasattr(self.api_reference, "targetPlatform"))
		self.assert_(hasattr(self.api_reference, "text"))
		self.assert_(hasattr(self.api_reference, "thumbnailUrl"))
		self.assert_(hasattr(self.api_reference, "timeRequired"))
		self.assert_(hasattr(self.api_reference, "url"))
		self.assert_(hasattr(self.api_reference, "version"))
		self.assert_(hasattr(self.api_reference, "video"))
		self.assert_(hasattr(self.api_reference, "wordCount"))

    def tearDown(self):
        pass

class TestAboutPage(unittest.TestCase):

    def setUp(self):
        self.about_page = AboutPage()

    def test_init(self):
        self.assertEquals(type(self.about_page), AboutPage)

    def test_rdf_properties(self):
		self.assert_(hasattr(self.about_page, "accessibilityAPI"))
		self.assert_(hasattr(self.about_page, "accessibilityControl"))
		self.assert_(hasattr(self.about_page, "accessibilityFeature"))
		self.assert_(hasattr(self.about_page, "accessibilityHazard"))
		self.assert_(hasattr(self.about_page, "accountablePerson"))
		self.assert_(hasattr(self.about_page, "additionalType"))
		self.assert_(hasattr(self.about_page, "alternateName"))
		self.assert_(hasattr(self.about_page, "alternativeHeadline"))
		self.assert_(hasattr(self.about_page, "associatedMedia"))
		self.assert_(hasattr(self.about_page, "audio"))
		self.assert_(hasattr(self.about_page, "author"))
		self.assert_(hasattr(self.about_page, "breadcrumb"))
		self.assert_(hasattr(self.about_page, "citation"))
		self.assert_(hasattr(self.about_page, "comment"))
		self.assert_(hasattr(self.about_page, "contentLocation"))
		self.assert_(hasattr(self.about_page, "contentRating"))
		self.assert_(hasattr(self.about_page, "contributor"))
		self.assert_(hasattr(self.about_page, "copyrightHolder"))
		self.assert_(hasattr(self.about_page, "copyrightYear"))
		self.assert_(hasattr(self.about_page, "dateCreated"))
		self.assert_(hasattr(self.about_page, "dateModified"))
		self.assert_(hasattr(self.about_page, "datePublished"))
		self.assert_(hasattr(self.about_page, "description"))
		self.assert_(hasattr(self.about_page, "discussionUrl"))
		self.assert_(hasattr(self.about_page, "editor"))
		self.assert_(hasattr(self.about_page, "educationalAlignment"))
		self.assert_(hasattr(self.about_page, "educationalUse"))
		self.assert_(hasattr(self.about_page, "encoding"))
		self.assert_(hasattr(self.about_page, "encodings"))
		self.assert_(hasattr(self.about_page, "genre"))
		self.assert_(hasattr(self.about_page, "headline"))
		self.assert_(hasattr(self.about_page, "image"))
		self.assert_(hasattr(self.about_page, "inLanguage"))
		self.assert_(hasattr(self.about_page, "interactivityType"))
		self.assert_(hasattr(self.about_page, "isBasedOnUrl"))
		self.assert_(hasattr(self.about_page, "isFamilyFriendly"))
		self.assert_(hasattr(self.about_page, "isPartOf"))
		self.assert_(hasattr(self.about_page, "keywords"))
		self.assert_(hasattr(self.about_page, "lastReviewed"))
		self.assert_(hasattr(self.about_page, "learningResourceType"))
		self.assert_(hasattr(self.about_page, "mainContentOfPage"))
		self.assert_(hasattr(self.about_page, "mentions"))
		self.assert_(hasattr(self.about_page, "name"))
		self.assert_(hasattr(self.about_page, "primaryImageOfPage"))
		self.assert_(hasattr(self.about_page, "publisher"))
		self.assert_(hasattr(self.about_page, "publishingPrinciples"))
		self.assert_(hasattr(self.about_page, "relatedLink"))
		self.assert_(hasattr(self.about_page, "reviewedBy"))
		self.assert_(hasattr(self.about_page, "sameAs"))
		self.assert_(hasattr(self.about_page, "significantLink"))
		self.assert_(hasattr(self.about_page, "significantLinks"))
		self.assert_(hasattr(self.about_page, "sourceOrganization"))
		self.assert_(hasattr(self.about_page, "specialty"))
		self.assert_(hasattr(self.about_page, "text"))
		self.assert_(hasattr(self.about_page, "thumbnailUrl"))
		self.assert_(hasattr(self.about_page, "timeRequired"))
		self.assert_(hasattr(self.about_page, "url"))
		self.assert_(hasattr(self.about_page, "version"))
		self.assert_(hasattr(self.about_page, "video"))

    def tearDown(self):
        pass

class TestAcceptAction(unittest.TestCase):

	def setUp(self):
		self.accept_action = AcceptAction()

	def test_init(self):
		self.assertEquals(type(self.accept_action), AcceptAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.accept_action, "additionalType"))
		self.assert_(hasattr(self.accept_action, "agent"))
		self.assert_(hasattr(self.accept_action, "alternateName"))
		self.assert_(hasattr(self.accept_action, "description"))
		self.assert_(hasattr(self.accept_action, "endTime"))
		self.assert_(hasattr(self.accept_action, "image"))
		self.assert_(hasattr(self.accept_action, "instrument"))
		self.assert_(hasattr(self.accept_action, "name"))
		self.assert_(hasattr(self.accept_action, "object"))
		self.assert_(hasattr(self.accept_action, "participant"))
		self.assert_(hasattr(self.accept_action, "result"))
		self.assert_(hasattr(self.accept_action, "sameAs"))
		self.assert_(hasattr(self.accept_action, "startTime"))
		self.assert_(hasattr(self.accept_action, "url"))

	def tearDown(self):
		pass

class TestAccountingService(unittest.TestCase):

	def setUp(self):
		self.accounting_service = AccountingService()

	def test_init(self):
		self.assertEquals(type(self.accounting_service), AccountingService)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.accounting_service, "additionalType"))
		self.assert_(hasattr(self.accounting_service, "alternateName"))
		self.assert_(hasattr(self.accounting_service, "branchOf"))
		self.assert_(hasattr(self.accounting_service, "containedIn"))
		self.assert_(hasattr(self.accounting_service, "currenciesAccepted"))
		self.assert_(hasattr(self.accounting_service, "description"))
		self.assert_(hasattr(self.accounting_service, "geo"))
		self.assert_(hasattr(self.accounting_service, "image"))
		self.assert_(hasattr(self.accounting_service, "map"))
		self.assert_(hasattr(self.accounting_service, "maps"))
		self.assert_(hasattr(self.accounting_service, "name"))
		self.assert_(hasattr(self.accounting_service, "openingHoursSpecification"))
		self.assert_(hasattr(self.accounting_service, "paymentAccepted"))
		self.assert_(hasattr(self.accounting_service, "photo"))
		self.assert_(hasattr(self.accounting_service, "photos"))
		self.assert_(hasattr(self.accounting_service, "priceRange"))
		self.assert_(hasattr(self.accounting_service, "sameAs"))
		self.assert_(hasattr(self.accounting_service, "url"))

	def tearDown(self):
		pass

class TestAchieveAction(unittest.TestCase):

	def setUp(self):
		self.achieve_action = AchieveAction()

	def test_init(self):
		self.assertEquals(type(self.achieve_action), AchieveAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.achieve_action, "additionalType"))
		self.assert_(hasattr(self.achieve_action, "agent"))
		self.assert_(hasattr(self.achieve_action, "alternateName"))
		self.assert_(hasattr(self.achieve_action, "description"))
		self.assert_(hasattr(self.achieve_action, "endTime"))
		self.assert_(hasattr(self.achieve_action, "image"))
		self.assert_(hasattr(self.achieve_action, "instrument"))
		self.assert_(hasattr(self.achieve_action, "name"))
		self.assert_(hasattr(self.achieve_action, "object"))
		self.assert_(hasattr(self.achieve_action, "participant"))
		self.assert_(hasattr(self.achieve_action, "result"))
		self.assert_(hasattr(self.achieve_action, "sameAs"))
		self.assert_(hasattr(self.achieve_action, "startTime"))
		self.assert_(hasattr(self.achieve_action, "url"))

	def tearDown(self):
		pass

class TestAction(unittest.TestCase):

	def setUp(self):
		self.action = Action()

	def test_init(self):
		self.assertEquals(type(self.action), Action)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.action, "additionalType"))
		self.assert_(hasattr(self.action, "agent"))
		self.assert_(hasattr(self.action, "alternateName"))
		self.assert_(hasattr(self.action, "description"))
		self.assert_(hasattr(self.action, "endTime"))
		self.assert_(hasattr(self.action, "image"))
		self.assert_(hasattr(self.action, "instrument"))
		self.assert_(hasattr(self.action, "name"))
		self.assert_(hasattr(self.action, "object"))
		self.assert_(hasattr(self.action, "participant"))
		self.assert_(hasattr(self.action, "result"))
		self.assert_(hasattr(self.action, "sameAs"))
		self.assert_(hasattr(self.action, "startTime"))
		self.assert_(hasattr(self.action, "url"))

	def tearDown(self):
		pass

class TestAddAction(unittest.TestCase):

	def setUp(self):
		self.add_action = AddAction()

	def test_init(self):
		self.assertEquals(type(self.add_action), AddAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.add_action, "additionalType"))
		self.assert_(hasattr(self.add_action, "agent"))
		self.assert_(hasattr(self.add_action, "alternateName"))
		self.assert_(hasattr(self.add_action, "collection"))
		self.assert_(hasattr(self.add_action, "description"))
		self.assert_(hasattr(self.add_action, "endTime"))
		self.assert_(hasattr(self.add_action, "image"))
		self.assert_(hasattr(self.add_action, "instrument"))
		self.assert_(hasattr(self.add_action, "name"))
		self.assert_(hasattr(self.add_action, "object"))
		self.assert_(hasattr(self.add_action, "participant"))
		self.assert_(hasattr(self.add_action, "result"))
		self.assert_(hasattr(self.add_action, "sameAs"))
		self.assert_(hasattr(self.add_action, "startTime"))
		self.assert_(hasattr(self.add_action, "url"))

	def tearDown(self):
		pass

class TestAdministrativeArea(unittest.TestCase):

	def setUp(self):
		self.administrative_area = AdministrativeArea()

	def test_init(self):
		self.assertEquals(type(self.administrative_area), AdministrativeArea)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.administrative_area, "additionalType"))
		self.assert_(hasattr(self.administrative_area, "alternateName"))
		self.assert_(hasattr(self.administrative_area, "containedIn"))
		self.assert_(hasattr(self.administrative_area, "description"))
		self.assert_(hasattr(self.administrative_area, "geo"))
		self.assert_(hasattr(self.administrative_area, "image"))
		self.assert_(hasattr(self.administrative_area, "map"))
		self.assert_(hasattr(self.administrative_area, "maps"))
		self.assert_(hasattr(self.administrative_area, "name"))
		self.assert_(hasattr(self.administrative_area, "openingHoursSpecification"))
		self.assert_(hasattr(self.administrative_area, "photo"))
		self.assert_(hasattr(self.administrative_area, "photos"))
		self.assert_(hasattr(self.administrative_area, "sameAs"))
		self.assert_(hasattr(self.administrative_area, "url"))

	def tearDown(self):
		pass

class TestAdultEntertainment(unittest.TestCase):

	def setUp(self):
		self.adult_entertainment = AdultEntertainment()

	def test_init(self):
		self.assertEquals(type(self.adult_entertainment), AdultEntertainment)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.adult_entertainment, "additionalType"))
		self.assert_(hasattr(self.adult_entertainment, "alternateName"))
		self.assert_(hasattr(self.adult_entertainment, "branchOf"))
		self.assert_(hasattr(self.adult_entertainment, "containedIn"))
		self.assert_(hasattr(self.adult_entertainment, "currenciesAccepted"))
		self.assert_(hasattr(self.adult_entertainment, "description"))
		self.assert_(hasattr(self.adult_entertainment, "geo"))
		self.assert_(hasattr(self.adult_entertainment, "image"))
		self.assert_(hasattr(self.adult_entertainment, "map"))
		self.assert_(hasattr(self.adult_entertainment, "maps"))
		self.assert_(hasattr(self.adult_entertainment, "name"))
		self.assert_(hasattr(self.adult_entertainment, "openingHoursSpecification"))
		self.assert_(hasattr(self.adult_entertainment, "paymentAccepted"))
		self.assert_(hasattr(self.adult_entertainment, "photo"))
		self.assert_(hasattr(self.adult_entertainment, "photos"))
		self.assert_(hasattr(self.adult_entertainment, "priceRange"))
		self.assert_(hasattr(self.adult_entertainment, "sameAs"))
		self.assert_(hasattr(self.adult_entertainment, "url"))

	def tearDown(self):
		pass

class TestAggregateOffer(unittest.TestCase):

	def setUp(self):
		self.aggregate_offer = AggregateOffer()

	def test_init(self):
		self.assertEquals(type(self.aggregate_offer), AggregateOffer)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.aggregate_offer, "addOn"))
		self.assert_(hasattr(self.aggregate_offer, "additionalType"))
		self.assert_(hasattr(self.aggregate_offer, "alternateName"))
		self.assert_(hasattr(self.aggregate_offer, "description"))
		self.assert_(hasattr(self.aggregate_offer, "highPrice"))
		self.assert_(hasattr(self.aggregate_offer, "image"))
		self.assert_(hasattr(self.aggregate_offer, "lowPrice"))
		self.assert_(hasattr(self.aggregate_offer, "name"))
		self.assert_(hasattr(self.aggregate_offer, "offerCount"))
		self.assert_(hasattr(self.aggregate_offer, "priceValidUntil"))
		self.assert_(hasattr(self.aggregate_offer, "sameAs"))
		self.assert_(hasattr(self.aggregate_offer, "url"))

	def tearDown(self):
		pass

class TestAggregateRating(unittest.TestCase):

	def setUp(self):
		self.aggregate_rating = AggregateRating()

	def test_init(self):
		self.assertEquals(type(self.aggregate_rating), AggregateRating)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.aggregate_rating, "additionalType"))
		self.assert_(hasattr(self.aggregate_rating, "alternateName"))
		self.assert_(hasattr(self.aggregate_rating, "bestRating"))
		self.assert_(hasattr(self.aggregate_rating, "description"))
		self.assert_(hasattr(self.aggregate_rating, "image"))
		self.assert_(hasattr(self.aggregate_rating, "name"))
		self.assert_(hasattr(self.aggregate_rating, "ratingCount"))
		self.assert_(hasattr(self.aggregate_rating, "ratingValue"))
		self.assert_(hasattr(self.aggregate_rating, "reviewCount"))
		self.assert_(hasattr(self.aggregate_rating, "sameAs"))
		self.assert_(hasattr(self.aggregate_rating, "url"))
		self.assert_(hasattr(self.aggregate_rating, "worstRating"))

	def tearDown(self):
		pass

class TestAgreeAction(unittest.TestCase):

	def setUp(self):
		self.agree_action = AgreeAction()

	def test_init(self):
		self.assertEquals(type(self.agree_action), AgreeAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.agree_action, "additionalType"))
		self.assert_(hasattr(self.agree_action, "agent"))
		self.assert_(hasattr(self.agree_action, "alternateName"))
		self.assert_(hasattr(self.agree_action, "description"))
		self.assert_(hasattr(self.agree_action, "endTime"))
		self.assert_(hasattr(self.agree_action, "image"))
		self.assert_(hasattr(self.agree_action, "instrument"))
		self.assert_(hasattr(self.agree_action, "name"))
		self.assert_(hasattr(self.agree_action, "object"))
		self.assert_(hasattr(self.agree_action, "participant"))
		self.assert_(hasattr(self.agree_action, "result"))
		self.assert_(hasattr(self.agree_action, "sameAs"))
		self.assert_(hasattr(self.agree_action, "startTime"))
		self.assert_(hasattr(self.agree_action, "url"))

	def tearDown(self):
		pass

class TestAirport(unittest.TestCase):

	def setUp(self):
		self.airport = Airport()

	def test_init(self):
		self.assertEquals(type(self.airport), Airport)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.airport, "additionalType"))
		self.assert_(hasattr(self.airport, "alternateName"))
		self.assert_(hasattr(self.airport, "containedIn"))
		self.assert_(hasattr(self.airport, "description"))
		self.assert_(hasattr(self.airport, "geo"))
		self.assert_(hasattr(self.airport, "image"))
		self.assert_(hasattr(self.airport, "map"))
		self.assert_(hasattr(self.airport, "maps"))
		self.assert_(hasattr(self.airport, "name"))
		self.assert_(hasattr(self.airport, "openingHoursSpecification"))
		self.assert_(hasattr(self.airport, "photo"))
		self.assert_(hasattr(self.airport, "photos"))
		self.assert_(hasattr(self.airport, "sameAs"))
		self.assert_(hasattr(self.airport, "url"))

	def tearDown(self):
		pass

class TestAlignmentObject(unittest.TestCase):

	def setUp(self):
		self.alignment_object = AlignmentObject()

	def test_init(self):
		self.assertEquals(type(self.alignment_object), AlignmentObject)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.alignment_object, "additionalType"))
		self.assert_(hasattr(self.alignment_object, "alignmentType"))
		self.assert_(hasattr(self.alignment_object, "alternateName"))
		self.assert_(hasattr(self.alignment_object, "description"))
		self.assert_(hasattr(self.alignment_object, "educationalFramework"))
		self.assert_(hasattr(self.alignment_object, "image"))
		self.assert_(hasattr(self.alignment_object, "name"))
		self.assert_(hasattr(self.alignment_object, "sameAs"))
		self.assert_(hasattr(self.alignment_object, "targetDescription"))
		self.assert_(hasattr(self.alignment_object, "targetName"))
		self.assert_(hasattr(self.alignment_object, "targetUrl"))
		self.assert_(hasattr(self.alignment_object, "url"))

	def tearDown(self):
		pass

class TestAllocateAction(unittest.TestCase):

	def setUp(self):
		self.allocate_action = AllocateAction()

	def test_init(self):
		self.assertEquals(type(self.allocate_action), AllocateAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.allocate_action, "additionalType"))
		self.assert_(hasattr(self.allocate_action, "agent"))
		self.assert_(hasattr(self.allocate_action, "alternateName"))
		self.assert_(hasattr(self.allocate_action, "description"))
		self.assert_(hasattr(self.allocate_action, "endTime"))
		self.assert_(hasattr(self.allocate_action, "image"))
		self.assert_(hasattr(self.allocate_action, "instrument"))
		self.assert_(hasattr(self.allocate_action, "name"))
		self.assert_(hasattr(self.allocate_action, "object"))
		self.assert_(hasattr(self.allocate_action, "participant"))
		self.assert_(hasattr(self.allocate_action, "result"))
		self.assert_(hasattr(self.allocate_action, "sameAs"))
		self.assert_(hasattr(self.allocate_action, "startTime"))
		self.assert_(hasattr(self.allocate_action, "url"))

	def tearDown(self):
		pass

class TestAmusementPark(unittest.TestCase):

	def setUp(self):
		self.amusement_park = AmusementPark()

	def test_init(self):
		self.assertEquals(type(self.amusement_park), AmusementPark)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.amusement_park, "additionalType"))
		self.assert_(hasattr(self.amusement_park, "alternateName"))
		self.assert_(hasattr(self.amusement_park, "branchOf"))
		self.assert_(hasattr(self.amusement_park, "containedIn"))
		self.assert_(hasattr(self.amusement_park, "currenciesAccepted"))
		self.assert_(hasattr(self.amusement_park, "description"))
		self.assert_(hasattr(self.amusement_park, "geo"))
		self.assert_(hasattr(self.amusement_park, "image"))
		self.assert_(hasattr(self.amusement_park, "map"))
		self.assert_(hasattr(self.amusement_park, "maps"))
		self.assert_(hasattr(self.amusement_park, "name"))
		self.assert_(hasattr(self.amusement_park, "openingHoursSpecification"))
		self.assert_(hasattr(self.amusement_park, "paymentAccepted"))
		self.assert_(hasattr(self.amusement_park, "photo"))
		self.assert_(hasattr(self.amusement_park, "photos"))
		self.assert_(hasattr(self.amusement_park, "priceRange"))
		self.assert_(hasattr(self.amusement_park, "sameAs"))
		self.assert_(hasattr(self.amusement_park, "url"))

	def tearDown(self):
		pass

class TestAnatomicalStructure(unittest.TestCase):

	def setUp(self):
		self.anatomical_structure = AnatomicalStructure()

	def test_init(self):
		self.assertEquals(type(self.anatomical_structure), AnatomicalStructure)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.anatomical_structure, "additionalType"))
		self.assert_(hasattr(self.anatomical_structure, "alternateName"))
		self.assert_(hasattr(self.anatomical_structure, "bodyLocation"))
		self.assert_(hasattr(self.anatomical_structure, "code"))
		self.assert_(hasattr(self.anatomical_structure, "connectedTo"))
		self.assert_(hasattr(self.anatomical_structure, "description"))
		self.assert_(hasattr(self.anatomical_structure, "diagram"))
		self.assert_(hasattr(self.anatomical_structure, "function"))
		self.assert_(hasattr(self.anatomical_structure, "guideline"))
		self.assert_(hasattr(self.anatomical_structure, "image"))
		self.assert_(hasattr(self.anatomical_structure, "medicineSystem"))
		self.assert_(hasattr(self.anatomical_structure, "name"))
		self.assert_(hasattr(self.anatomical_structure, "partOfSystem"))
		self.assert_(hasattr(self.anatomical_structure, "recognizingAuthority"))
		self.assert_(hasattr(self.anatomical_structure, "relevantSpecialty"))
		self.assert_(hasattr(self.anatomical_structure, "sameAs"))
		self.assert_(hasattr(self.anatomical_structure, "study"))
		self.assert_(hasattr(self.anatomical_structure, "subStructure"))
		self.assert_(hasattr(self.anatomical_structure, "url"))

	def tearDown(self):
		pass

class TestAnatomicalSystem(unittest.TestCase):

	def setUp(self):
		self.anatomical_system = AnatomicalSystem()

	def test_init(self):
		self.assertEquals(type(self.anatomical_system), AnatomicalSystem)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.anatomical_system, "additionalType"))
		self.assert_(hasattr(self.anatomical_system, "alternateName"))
		self.assert_(hasattr(self.anatomical_system, "code"))
		self.assert_(hasattr(self.anatomical_system, "comprisedOf"))
		self.assert_(hasattr(self.anatomical_system, "description"))
		self.assert_(hasattr(self.anatomical_system, "guideline"))
		self.assert_(hasattr(self.anatomical_system, "image"))
		self.assert_(hasattr(self.anatomical_system, "medicineSystem"))
		self.assert_(hasattr(self.anatomical_system, "name"))
		self.assert_(hasattr(self.anatomical_system, "recognizingAuthority"))
		self.assert_(hasattr(self.anatomical_system, "relatedStructure"))
		self.assert_(hasattr(self.anatomical_system, "relevantSpecialty"))
		self.assert_(hasattr(self.anatomical_system, "sameAs"))
		self.assert_(hasattr(self.anatomical_system, "study"))
		self.assert_(hasattr(self.anatomical_system, "url"))

	def tearDown(self):
		pass

class TestAnimalShelter(unittest.TestCase):

	def setUp(self):
		self.animal_shelter = AnimalShelter()

	def test_init(self):
		self.assertEquals(type(self.animal_shelter), AnimalShelter)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.animal_shelter, "additionalType"))
		self.assert_(hasattr(self.animal_shelter, "alternateName"))
		self.assert_(hasattr(self.animal_shelter, "branchOf"))
		self.assert_(hasattr(self.animal_shelter, "containedIn"))
		self.assert_(hasattr(self.animal_shelter, "currenciesAccepted"))
		self.assert_(hasattr(self.animal_shelter, "description"))
		self.assert_(hasattr(self.animal_shelter, "geo"))
		self.assert_(hasattr(self.animal_shelter, "image"))
		self.assert_(hasattr(self.animal_shelter, "map"))
		self.assert_(hasattr(self.animal_shelter, "maps"))
		self.assert_(hasattr(self.animal_shelter, "name"))
		self.assert_(hasattr(self.animal_shelter, "openingHoursSpecification"))
		self.assert_(hasattr(self.animal_shelter, "paymentAccepted"))
		self.assert_(hasattr(self.animal_shelter, "photo"))
		self.assert_(hasattr(self.animal_shelter, "photos"))
		self.assert_(hasattr(self.animal_shelter, "priceRange"))
		self.assert_(hasattr(self.animal_shelter, "sameAs"))
		self.assert_(hasattr(self.animal_shelter, "url"))

	def tearDown(self):
		pass

class TestApartmentComplex(unittest.TestCase):

	def setUp(self):
		self.apartment_complex = ApartmentComplex()

	def test_init(self):
		self.assertEquals(type(self.apartment_complex), ApartmentComplex)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.apartment_complex, "additionalType"))
		self.assert_(hasattr(self.apartment_complex, "alternateName"))
		self.assert_(hasattr(self.apartment_complex, "containedIn"))
		self.assert_(hasattr(self.apartment_complex, "description"))
		self.assert_(hasattr(self.apartment_complex, "geo"))
		self.assert_(hasattr(self.apartment_complex, "image"))
		self.assert_(hasattr(self.apartment_complex, "map"))
		self.assert_(hasattr(self.apartment_complex, "maps"))
		self.assert_(hasattr(self.apartment_complex, "name"))
		self.assert_(hasattr(self.apartment_complex, "openingHoursSpecification"))
		self.assert_(hasattr(self.apartment_complex, "photo"))
		self.assert_(hasattr(self.apartment_complex, "photos"))
		self.assert_(hasattr(self.apartment_complex, "sameAs"))
		self.assert_(hasattr(self.apartment_complex, "url"))

	def tearDown(self):
		pass

class TestAppendAction(unittest.TestCase):

	def setUp(self):
		self.append_action = AppendAction()

	def test_init(self):
		self.assertEquals(type(self.append_action), AppendAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.append_action, "additionalType"))
		self.assert_(hasattr(self.append_action, "agent"))
		self.assert_(hasattr(self.append_action, "alternateName"))
		self.assert_(hasattr(self.append_action, "collection"))
		self.assert_(hasattr(self.append_action, "description"))
		self.assert_(hasattr(self.append_action, "endTime"))
		self.assert_(hasattr(self.append_action, "image"))
		self.assert_(hasattr(self.append_action, "instrument"))
		self.assert_(hasattr(self.append_action, "name"))
		self.assert_(hasattr(self.append_action, "object"))
		self.assert_(hasattr(self.append_action, "participant"))
		self.assert_(hasattr(self.append_action, "result"))
		self.assert_(hasattr(self.append_action, "sameAs"))
		self.assert_(hasattr(self.append_action, "startTime"))
		self.assert_(hasattr(self.append_action, "url"))

	def tearDown(self):
		pass

class TestApplyAction(unittest.TestCase):

	def setUp(self):
		self.apply_action = ApplyAction()

	def test_init(self):
		self.assertEquals(type(self.apply_action), ApplyAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.apply_action, "additionalType"))
		self.assert_(hasattr(self.apply_action, "agent"))
		self.assert_(hasattr(self.apply_action, "alternateName"))
		self.assert_(hasattr(self.apply_action, "description"))
		self.assert_(hasattr(self.apply_action, "endTime"))
		self.assert_(hasattr(self.apply_action, "image"))
		self.assert_(hasattr(self.apply_action, "instrument"))
		self.assert_(hasattr(self.apply_action, "name"))
		self.assert_(hasattr(self.apply_action, "object"))
		self.assert_(hasattr(self.apply_action, "participant"))
		self.assert_(hasattr(self.apply_action, "result"))
		self.assert_(hasattr(self.apply_action, "sameAs"))
		self.assert_(hasattr(self.apply_action, "startTime"))
		self.assert_(hasattr(self.apply_action, "url"))

	def tearDown(self):
		pass

class TestApprovedIndication(unittest.TestCase):

	def setUp(self):
		self.approved_indication = ApprovedIndication()

	def test_init(self):
		self.assertEquals(type(self.approved_indication), ApprovedIndication)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.approved_indication, "additionalType"))
		self.assert_(hasattr(self.approved_indication, "alternateName"))
		self.assert_(hasattr(self.approved_indication, "code"))
		self.assert_(hasattr(self.approved_indication, "description"))
		self.assert_(hasattr(self.approved_indication, "guideline"))
		self.assert_(hasattr(self.approved_indication, "image"))
		self.assert_(hasattr(self.approved_indication, "medicineSystem"))
		self.assert_(hasattr(self.approved_indication, "name"))
		self.assert_(hasattr(self.approved_indication, "recognizingAuthority"))
		self.assert_(hasattr(self.approved_indication, "relevantSpecialty"))
		self.assert_(hasattr(self.approved_indication, "sameAs"))
		self.assert_(hasattr(self.approved_indication, "study"))
		self.assert_(hasattr(self.approved_indication, "url"))

	def tearDown(self):
		pass

class TestAquarium(unittest.TestCase):

	def setUp(self):
		self.aquarium = Aquarium()

	def test_init(self):
		self.assertEquals(type(self.aquarium), Aquarium)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.aquarium, "additionalType"))
		self.assert_(hasattr(self.aquarium, "alternateName"))
		self.assert_(hasattr(self.aquarium, "containedIn"))
		self.assert_(hasattr(self.aquarium, "description"))
		self.assert_(hasattr(self.aquarium, "geo"))
		self.assert_(hasattr(self.aquarium, "image"))
		self.assert_(hasattr(self.aquarium, "map"))
		self.assert_(hasattr(self.aquarium, "maps"))
		self.assert_(hasattr(self.aquarium, "name"))
		self.assert_(hasattr(self.aquarium, "openingHoursSpecification"))
		self.assert_(hasattr(self.aquarium, "photo"))
		self.assert_(hasattr(self.aquarium, "photos"))
		self.assert_(hasattr(self.aquarium, "sameAs"))
		self.assert_(hasattr(self.aquarium, "url"))

	def tearDown(self):
		pass

class TestArriveAction(unittest.TestCase):

	def setUp(self):
		self.arrive_action = ArriveAction()

	def test_init(self):
		self.assertEquals(type(self.arrive_action), ArriveAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.arrive_action, "additionalType"))
		self.assert_(hasattr(self.arrive_action, "agent"))
		self.assert_(hasattr(self.arrive_action, "alternateName"))
		self.assert_(hasattr(self.arrive_action, "description"))
		self.assert_(hasattr(self.arrive_action, "endTime"))
		self.assert_(hasattr(self.arrive_action, "image"))
		self.assert_(hasattr(self.arrive_action, "instrument"))
		self.assert_(hasattr(self.arrive_action, "name"))
		self.assert_(hasattr(self.arrive_action, "object"))
		self.assert_(hasattr(self.arrive_action, "participant"))
		self.assert_(hasattr(self.arrive_action, "result"))
		self.assert_(hasattr(self.arrive_action, "sameAs"))
		self.assert_(hasattr(self.arrive_action, "startTime"))
		self.assert_(hasattr(self.arrive_action, "url"))

	def tearDown(self):
		pass

class TestArtGallery(unittest.TestCase):

	def setUp(self):
		self.art_gallery = ArtGallery()

	def test_init(self):
		self.assertEquals(type(self.art_gallery), ArtGallery)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.art_gallery, "additionalType"))
		self.assert_(hasattr(self.art_gallery, "alternateName"))
		self.assert_(hasattr(self.art_gallery, "branchOf"))
		self.assert_(hasattr(self.art_gallery, "containedIn"))
		self.assert_(hasattr(self.art_gallery, "currenciesAccepted"))
		self.assert_(hasattr(self.art_gallery, "description"))
		self.assert_(hasattr(self.art_gallery, "geo"))
		self.assert_(hasattr(self.art_gallery, "image"))
		self.assert_(hasattr(self.art_gallery, "map"))
		self.assert_(hasattr(self.art_gallery, "maps"))
		self.assert_(hasattr(self.art_gallery, "name"))
		self.assert_(hasattr(self.art_gallery, "openingHoursSpecification"))
		self.assert_(hasattr(self.art_gallery, "paymentAccepted"))
		self.assert_(hasattr(self.art_gallery, "photo"))
		self.assert_(hasattr(self.art_gallery, "photos"))
		self.assert_(hasattr(self.art_gallery, "priceRange"))
		self.assert_(hasattr(self.art_gallery, "sameAs"))
		self.assert_(hasattr(self.art_gallery, "url"))

	def tearDown(self):
		pass

class TestArtery(unittest.TestCase):

	def setUp(self):
		self.artery = Artery()

	def test_init(self):
		self.assertEquals(type(self.artery), Artery)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.artery, "additionalType"))
		self.assert_(hasattr(self.artery, "alternateName"))
		self.assert_(hasattr(self.artery, "arterialBranch"))
		self.assert_(hasattr(self.artery, "bodyLocation"))
		self.assert_(hasattr(self.artery, "code"))
		self.assert_(hasattr(self.artery, "connectedTo"))
		self.assert_(hasattr(self.artery, "description"))
		self.assert_(hasattr(self.artery, "diagram"))
		self.assert_(hasattr(self.artery, "function"))
		self.assert_(hasattr(self.artery, "guideline"))
		self.assert_(hasattr(self.artery, "image"))
		self.assert_(hasattr(self.artery, "medicineSystem"))
		self.assert_(hasattr(self.artery, "name"))
		self.assert_(hasattr(self.artery, "partOfSystem"))
		self.assert_(hasattr(self.artery, "recognizingAuthority"))
		self.assert_(hasattr(self.artery, "relevantSpecialty"))
		self.assert_(hasattr(self.artery, "sameAs"))
		self.assert_(hasattr(self.artery, "source"))
		self.assert_(hasattr(self.artery, "study"))
		self.assert_(hasattr(self.artery, "subStructure"))
		self.assert_(hasattr(self.artery, "supplyTo"))
		self.assert_(hasattr(self.artery, "url"))

	def tearDown(self):
		pass

class TestArticle(unittest.TestCase):

	def setUp(self):
		self.article = Article()

	def test_init(self):
		self.assertEquals(type(self.article), Article)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.article, "accessibilityAPI"))
		self.assert_(hasattr(self.article, "accessibilityControl"))
		self.assert_(hasattr(self.article, "accessibilityFeature"))
		self.assert_(hasattr(self.article, "accessibilityHazard"))
		self.assert_(hasattr(self.article, "accountablePerson"))
		self.assert_(hasattr(self.article, "additionalType"))
		self.assert_(hasattr(self.article, "alternateName"))
		self.assert_(hasattr(self.article, "alternativeHeadline"))
		self.assert_(hasattr(self.article, "articleBody"))
		self.assert_(hasattr(self.article, "articleSection"))
		self.assert_(hasattr(self.article, "associatedMedia"))
		self.assert_(hasattr(self.article, "audio"))
		self.assert_(hasattr(self.article, "author"))
		self.assert_(hasattr(self.article, "citation"))
		self.assert_(hasattr(self.article, "comment"))
		self.assert_(hasattr(self.article, "contentLocation"))
		self.assert_(hasattr(self.article, "contentRating"))
		self.assert_(hasattr(self.article, "contributor"))
		self.assert_(hasattr(self.article, "copyrightHolder"))
		self.assert_(hasattr(self.article, "copyrightYear"))
		self.assert_(hasattr(self.article, "dateCreated"))
		self.assert_(hasattr(self.article, "dateModified"))
		self.assert_(hasattr(self.article, "datePublished"))
		self.assert_(hasattr(self.article, "description"))
		self.assert_(hasattr(self.article, "discussionUrl"))
		self.assert_(hasattr(self.article, "editor"))
		self.assert_(hasattr(self.article, "educationalAlignment"))
		self.assert_(hasattr(self.article, "educationalUse"))
		self.assert_(hasattr(self.article, "encoding"))
		self.assert_(hasattr(self.article, "encodings"))
		self.assert_(hasattr(self.article, "genre"))
		self.assert_(hasattr(self.article, "headline"))
		self.assert_(hasattr(self.article, "image"))
		self.assert_(hasattr(self.article, "inLanguage"))
		self.assert_(hasattr(self.article, "interactivityType"))
		self.assert_(hasattr(self.article, "isBasedOnUrl"))
		self.assert_(hasattr(self.article, "isFamilyFriendly"))
		self.assert_(hasattr(self.article, "keywords"))
		self.assert_(hasattr(self.article, "learningResourceType"))
		self.assert_(hasattr(self.article, "mentions"))
		self.assert_(hasattr(self.article, "name"))
		self.assert_(hasattr(self.article, "publisher"))
		self.assert_(hasattr(self.article, "publishingPrinciples"))
		self.assert_(hasattr(self.article, "sameAs"))
		self.assert_(hasattr(self.article, "sourceOrganization"))
		self.assert_(hasattr(self.article, "text"))
		self.assert_(hasattr(self.article, "thumbnailUrl"))
		self.assert_(hasattr(self.article, "timeRequired"))
		self.assert_(hasattr(self.article, "url"))
		self.assert_(hasattr(self.article, "version"))
		self.assert_(hasattr(self.article, "video"))
		self.assert_(hasattr(self.article, "wordCount"))

	def tearDown(self):
		pass

class TestAskAction(unittest.TestCase):

	def setUp(self):
		self.ask_action = AskAction()

	def test_init(self):
		self.assertEquals(type(self.ask_action), AskAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.ask_action, "additionalType"))
		self.assert_(hasattr(self.ask_action, "agent"))
		self.assert_(hasattr(self.ask_action, "alternateName"))
		self.assert_(hasattr(self.ask_action, "description"))
		self.assert_(hasattr(self.ask_action, "endTime"))
		self.assert_(hasattr(self.ask_action, "image"))
		self.assert_(hasattr(self.ask_action, "instrument"))
		self.assert_(hasattr(self.ask_action, "name"))
		self.assert_(hasattr(self.ask_action, "object"))
		self.assert_(hasattr(self.ask_action, "participant"))
		self.assert_(hasattr(self.ask_action, "question"))
		self.assert_(hasattr(self.ask_action, "result"))
		self.assert_(hasattr(self.ask_action, "sameAs"))
		self.assert_(hasattr(self.ask_action, "startTime"))
		self.assert_(hasattr(self.ask_action, "url"))

	def tearDown(self):
		pass

class TestAssessAction(unittest.TestCase):

	def setUp(self):
		self.assess_action = AssessAction()

	def test_init(self):
		self.assertEquals(type(self.assess_action), AssessAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.assess_action, "additionalType"))
		self.assert_(hasattr(self.assess_action, "agent"))
		self.assert_(hasattr(self.assess_action, "alternateName"))
		self.assert_(hasattr(self.assess_action, "description"))
		self.assert_(hasattr(self.assess_action, "endTime"))
		self.assert_(hasattr(self.assess_action, "image"))
		self.assert_(hasattr(self.assess_action, "instrument"))
		self.assert_(hasattr(self.assess_action, "name"))
		self.assert_(hasattr(self.assess_action, "object"))
		self.assert_(hasattr(self.assess_action, "participant"))
		self.assert_(hasattr(self.assess_action, "result"))
		self.assert_(hasattr(self.assess_action, "sameAs"))
		self.assert_(hasattr(self.assess_action, "startTime"))
		self.assert_(hasattr(self.assess_action, "url"))

	def tearDown(self):
		pass

class TestAssignAction(unittest.TestCase):

	def setUp(self):
		self.assign_action = AssignAction()

	def test_init(self):
		self.assertEquals(type(self.assign_action), AssignAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.assign_action, "additionalType"))
		self.assert_(hasattr(self.assign_action, "agent"))
		self.assert_(hasattr(self.assign_action, "alternateName"))
		self.assert_(hasattr(self.assign_action, "description"))
		self.assert_(hasattr(self.assign_action, "endTime"))
		self.assert_(hasattr(self.assign_action, "image"))
		self.assert_(hasattr(self.assign_action, "instrument"))
		self.assert_(hasattr(self.assign_action, "name"))
		self.assert_(hasattr(self.assign_action, "object"))
		self.assert_(hasattr(self.assign_action, "participant"))
		self.assert_(hasattr(self.assign_action, "result"))
		self.assert_(hasattr(self.assign_action, "sameAs"))
		self.assert_(hasattr(self.assign_action, "startTime"))
		self.assert_(hasattr(self.assign_action, "url"))

	def tearDown(self):
		pass

class TestAttorney(unittest.TestCase):

	def setUp(self):
		self.attorney = Attorney()

	def test_init(self):
		self.assertEquals(type(self.attorney), Attorney)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.attorney, "additionalType"))
		self.assert_(hasattr(self.attorney, "alternateName"))
		self.assert_(hasattr(self.attorney, "branchOf"))
		self.assert_(hasattr(self.attorney, "containedIn"))
		self.assert_(hasattr(self.attorney, "currenciesAccepted"))
		self.assert_(hasattr(self.attorney, "description"))
		self.assert_(hasattr(self.attorney, "geo"))
		self.assert_(hasattr(self.attorney, "image"))
		self.assert_(hasattr(self.attorney, "map"))
		self.assert_(hasattr(self.attorney, "maps"))
		self.assert_(hasattr(self.attorney, "name"))
		self.assert_(hasattr(self.attorney, "openingHoursSpecification"))
		self.assert_(hasattr(self.attorney, "paymentAccepted"))
		self.assert_(hasattr(self.attorney, "photo"))
		self.assert_(hasattr(self.attorney, "photos"))
		self.assert_(hasattr(self.attorney, "priceRange"))
		self.assert_(hasattr(self.attorney, "sameAs"))
		self.assert_(hasattr(self.attorney, "url"))

	def tearDown(self):
		pass

class TestAudience(unittest.TestCase):

	def setUp(self):
		self.audience = Audience()

	def test_init(self):
		self.assertEquals(type(self.audience), Audience)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.audience, "additionalType"))
		self.assert_(hasattr(self.audience, "alternateName"))
		self.assert_(hasattr(self.audience, "audienceType"))
		self.assert_(hasattr(self.audience, "description"))
		self.assert_(hasattr(self.audience, "geographicArea"))
		self.assert_(hasattr(self.audience, "image"))
		self.assert_(hasattr(self.audience, "name"))
		self.assert_(hasattr(self.audience, "sameAs"))
		self.assert_(hasattr(self.audience, "url"))

	def tearDown(self):
		pass

class TestAudioObject(unittest.TestCase):

	def setUp(self):
		self.audio_object = AudioObject()

	def test_init(self):
		self.assertEquals(type(self.audio_object), AudioObject)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.audio_object, "accessibilityAPI"))
		self.assert_(hasattr(self.audio_object, "accessibilityControl"))
		self.assert_(hasattr(self.audio_object, "accessibilityFeature"))
		self.assert_(hasattr(self.audio_object, "accessibilityHazard"))
		self.assert_(hasattr(self.audio_object, "accountablePerson"))
		self.assert_(hasattr(self.audio_object, "additionalType"))
		self.assert_(hasattr(self.audio_object, "alternateName"))
		self.assert_(hasattr(self.audio_object, "alternativeHeadline"))
		self.assert_(hasattr(self.audio_object, "associatedArticle"))
		self.assert_(hasattr(self.audio_object, "associatedMedia"))
		self.assert_(hasattr(self.audio_object, "audio"))
		self.assert_(hasattr(self.audio_object, "author"))
		self.assert_(hasattr(self.audio_object, "bitrate"))
		self.assert_(hasattr(self.audio_object, "citation"))
		self.assert_(hasattr(self.audio_object, "comment"))
		self.assert_(hasattr(self.audio_object, "contentLocation"))
		self.assert_(hasattr(self.audio_object, "contentRating"))
		self.assert_(hasattr(self.audio_object, "contentSize"))
		self.assert_(hasattr(self.audio_object, "contentUrl"))
		self.assert_(hasattr(self.audio_object, "contributor"))
		self.assert_(hasattr(self.audio_object, "copyrightHolder"))
		self.assert_(hasattr(self.audio_object, "copyrightYear"))
		self.assert_(hasattr(self.audio_object, "dateCreated"))
		self.assert_(hasattr(self.audio_object, "dateModified"))
		self.assert_(hasattr(self.audio_object, "datePublished"))
		self.assert_(hasattr(self.audio_object, "description"))
		self.assert_(hasattr(self.audio_object, "discussionUrl"))
		self.assert_(hasattr(self.audio_object, "editor"))
		self.assert_(hasattr(self.audio_object, "educationalAlignment"))
		self.assert_(hasattr(self.audio_object, "educationalUse"))
		self.assert_(hasattr(self.audio_object, "embedUrl"))
		self.assert_(hasattr(self.audio_object, "encodesCreativeWork"))
		self.assert_(hasattr(self.audio_object, "encoding"))
		self.assert_(hasattr(self.audio_object, "encodingFormat"))
		self.assert_(hasattr(self.audio_object, "encodings"))
		self.assert_(hasattr(self.audio_object, "expires"))
		self.assert_(hasattr(self.audio_object, "genre"))
		self.assert_(hasattr(self.audio_object, "headline"))
		self.assert_(hasattr(self.audio_object, "image"))
		self.assert_(hasattr(self.audio_object, "inLanguage"))
		self.assert_(hasattr(self.audio_object, "interactivityType"))
		self.assert_(hasattr(self.audio_object, "isBasedOnUrl"))
		self.assert_(hasattr(self.audio_object, "isFamilyFriendly"))
		self.assert_(hasattr(self.audio_object, "keywords"))
		self.assert_(hasattr(self.audio_object, "learningResourceType"))
		self.assert_(hasattr(self.audio_object, "mentions"))
		self.assert_(hasattr(self.audio_object, "name"))
		self.assert_(hasattr(self.audio_object, "playerType"))
		self.assert_(hasattr(self.audio_object, "publisher"))
		self.assert_(hasattr(self.audio_object, "publishingPrinciples"))
		self.assert_(hasattr(self.audio_object, "regionsAllowed"))
		self.assert_(hasattr(self.audio_object, "requiresSubscription"))
		self.assert_(hasattr(self.audio_object, "sameAs"))
		self.assert_(hasattr(self.audio_object, "sourceOrganization"))
		self.assert_(hasattr(self.audio_object, "text"))
		self.assert_(hasattr(self.audio_object, "thumbnailUrl"))
		self.assert_(hasattr(self.audio_object, "timeRequired"))
		self.assert_(hasattr(self.audio_object, "uploadDate"))
		self.assert_(hasattr(self.audio_object, "url"))
		self.assert_(hasattr(self.audio_object, "version"))
		self.assert_(hasattr(self.audio_object, "video"))

	def tearDown(self):
		pass

class TestAuthorizeAction(unittest.TestCase):

	def setUp(self):
		self.authorize_action = AuthorizeAction()

	def test_init(self):
		self.assertEquals(type(self.authorize_action), AuthorizeAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.authorize_action, "additionalType"))
		self.assert_(hasattr(self.authorize_action, "agent"))
		self.assert_(hasattr(self.authorize_action, "alternateName"))
		self.assert_(hasattr(self.authorize_action, "description"))
		self.assert_(hasattr(self.authorize_action, "endTime"))
		self.assert_(hasattr(self.authorize_action, "image"))
		self.assert_(hasattr(self.authorize_action, "instrument"))
		self.assert_(hasattr(self.authorize_action, "name"))
		self.assert_(hasattr(self.authorize_action, "object"))
		self.assert_(hasattr(self.authorize_action, "participant"))
		self.assert_(hasattr(self.authorize_action, "result"))
		self.assert_(hasattr(self.authorize_action, "sameAs"))
		self.assert_(hasattr(self.authorize_action, "startTime"))
		self.assert_(hasattr(self.authorize_action, "url"))

	def tearDown(self):
		pass

class TestAutoBodyShop(unittest.TestCase):

	def setUp(self):
		self.auto_body_shop = AutoBodyShop()

	def test_init(self):
		self.assertEquals(type(self.auto_body_shop), AutoBodyShop)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.auto_body_shop, "additionalType"))
		self.assert_(hasattr(self.auto_body_shop, "alternateName"))
		self.assert_(hasattr(self.auto_body_shop, "branchOf"))
		self.assert_(hasattr(self.auto_body_shop, "containedIn"))
		self.assert_(hasattr(self.auto_body_shop, "currenciesAccepted"))
		self.assert_(hasattr(self.auto_body_shop, "description"))
		self.assert_(hasattr(self.auto_body_shop, "geo"))
		self.assert_(hasattr(self.auto_body_shop, "image"))
		self.assert_(hasattr(self.auto_body_shop, "map"))
		self.assert_(hasattr(self.auto_body_shop, "maps"))
		self.assert_(hasattr(self.auto_body_shop, "name"))
		self.assert_(hasattr(self.auto_body_shop, "openingHoursSpecification"))
		self.assert_(hasattr(self.auto_body_shop, "paymentAccepted"))
		self.assert_(hasattr(self.auto_body_shop, "photo"))
		self.assert_(hasattr(self.auto_body_shop, "photos"))
		self.assert_(hasattr(self.auto_body_shop, "priceRange"))
		self.assert_(hasattr(self.auto_body_shop, "sameAs"))
		self.assert_(hasattr(self.auto_body_shop, "url"))

	def tearDown(self):
		pass

class TestAutoDealer(unittest.TestCase):

	def setUp(self):
		self.auto_dealer = AutoDealer()

	def test_init(self):
		self.assertEquals(type(self.auto_dealer), AutoDealer)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.auto_dealer, "additionalType"))
		self.assert_(hasattr(self.auto_dealer, "alternateName"))
		self.assert_(hasattr(self.auto_dealer, "branchOf"))
		self.assert_(hasattr(self.auto_dealer, "containedIn"))
		self.assert_(hasattr(self.auto_dealer, "currenciesAccepted"))
		self.assert_(hasattr(self.auto_dealer, "description"))
		self.assert_(hasattr(self.auto_dealer, "geo"))
		self.assert_(hasattr(self.auto_dealer, "image"))
		self.assert_(hasattr(self.auto_dealer, "map"))
		self.assert_(hasattr(self.auto_dealer, "maps"))
		self.assert_(hasattr(self.auto_dealer, "name"))
		self.assert_(hasattr(self.auto_dealer, "openingHoursSpecification"))
		self.assert_(hasattr(self.auto_dealer, "paymentAccepted"))
		self.assert_(hasattr(self.auto_dealer, "photo"))
		self.assert_(hasattr(self.auto_dealer, "photos"))
		self.assert_(hasattr(self.auto_dealer, "priceRange"))
		self.assert_(hasattr(self.auto_dealer, "sameAs"))
		self.assert_(hasattr(self.auto_dealer, "url"))

	def tearDown(self):
		pass

class TestAutoPartsStore(unittest.TestCase):

	def setUp(self):
		self.auto_parts_store = AutoPartsStore()

	def test_init(self):
		self.assertEquals(type(self.auto_parts_store), AutoPartsStore)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.auto_parts_store, "additionalType"))
		self.assert_(hasattr(self.auto_parts_store, "alternateName"))
		self.assert_(hasattr(self.auto_parts_store, "branchOf"))
		self.assert_(hasattr(self.auto_parts_store, "containedIn"))
		self.assert_(hasattr(self.auto_parts_store, "currenciesAccepted"))
		self.assert_(hasattr(self.auto_parts_store, "description"))
		self.assert_(hasattr(self.auto_parts_store, "geo"))
		self.assert_(hasattr(self.auto_parts_store, "image"))
		self.assert_(hasattr(self.auto_parts_store, "map"))
		self.assert_(hasattr(self.auto_parts_store, "maps"))
		self.assert_(hasattr(self.auto_parts_store, "name"))
		self.assert_(hasattr(self.auto_parts_store, "openingHoursSpecification"))
		self.assert_(hasattr(self.auto_parts_store, "paymentAccepted"))
		self.assert_(hasattr(self.auto_parts_store, "photo"))
		self.assert_(hasattr(self.auto_parts_store, "photos"))
		self.assert_(hasattr(self.auto_parts_store, "priceRange"))
		self.assert_(hasattr(self.auto_parts_store, "sameAs"))
		self.assert_(hasattr(self.auto_parts_store, "url"))

	def tearDown(self):
		pass

class TestAutoRental(unittest.TestCase):

	def setUp(self):
		self.auto_rental = AutoRental()

	def test_init(self):
		self.assertEquals(type(self.auto_rental), AutoRental)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.auto_rental, "additionalType"))
		self.assert_(hasattr(self.auto_rental, "alternateName"))
		self.assert_(hasattr(self.auto_rental, "branchOf"))
		self.assert_(hasattr(self.auto_rental, "containedIn"))
		self.assert_(hasattr(self.auto_rental, "currenciesAccepted"))
		self.assert_(hasattr(self.auto_rental, "description"))
		self.assert_(hasattr(self.auto_rental, "geo"))
		self.assert_(hasattr(self.auto_rental, "image"))
		self.assert_(hasattr(self.auto_rental, "map"))
		self.assert_(hasattr(self.auto_rental, "maps"))
		self.assert_(hasattr(self.auto_rental, "name"))
		self.assert_(hasattr(self.auto_rental, "openingHoursSpecification"))
		self.assert_(hasattr(self.auto_rental, "paymentAccepted"))
		self.assert_(hasattr(self.auto_rental, "photo"))
		self.assert_(hasattr(self.auto_rental, "photos"))
		self.assert_(hasattr(self.auto_rental, "priceRange"))
		self.assert_(hasattr(self.auto_rental, "sameAs"))
		self.assert_(hasattr(self.auto_rental, "url"))

	def tearDown(self):
		pass

class TestAutoRepair(unittest.TestCase):

	def setUp(self):
		self.auto_repair = AutoRepair()

	def test_init(self):
		self.assertEquals(type(self.auto_repair), AutoRepair)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.auto_repair, "additionalType"))
		self.assert_(hasattr(self.auto_repair, "alternateName"))
		self.assert_(hasattr(self.auto_repair, "branchOf"))
		self.assert_(hasattr(self.auto_repair, "containedIn"))
		self.assert_(hasattr(self.auto_repair, "currenciesAccepted"))
		self.assert_(hasattr(self.auto_repair, "description"))
		self.assert_(hasattr(self.auto_repair, "geo"))
		self.assert_(hasattr(self.auto_repair, "image"))
		self.assert_(hasattr(self.auto_repair, "map"))
		self.assert_(hasattr(self.auto_repair, "maps"))
		self.assert_(hasattr(self.auto_repair, "name"))
		self.assert_(hasattr(self.auto_repair, "openingHoursSpecification"))
		self.assert_(hasattr(self.auto_repair, "paymentAccepted"))
		self.assert_(hasattr(self.auto_repair, "photo"))
		self.assert_(hasattr(self.auto_repair, "photos"))
		self.assert_(hasattr(self.auto_repair, "priceRange"))
		self.assert_(hasattr(self.auto_repair, "sameAs"))
		self.assert_(hasattr(self.auto_repair, "url"))

	def tearDown(self):
		pass

class TestAutoWash(unittest.TestCase):

	def setUp(self):
		self.auto_wash = AutoWash()

	def test_init(self):
		self.assertEquals(type(self.auto_wash), AutoWash)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.auto_wash, "additionalType"))
		self.assert_(hasattr(self.auto_wash, "alternateName"))
		self.assert_(hasattr(self.auto_wash, "branchOf"))
		self.assert_(hasattr(self.auto_wash, "containedIn"))
		self.assert_(hasattr(self.auto_wash, "currenciesAccepted"))
		self.assert_(hasattr(self.auto_wash, "description"))
		self.assert_(hasattr(self.auto_wash, "geo"))
		self.assert_(hasattr(self.auto_wash, "image"))
		self.assert_(hasattr(self.auto_wash, "map"))
		self.assert_(hasattr(self.auto_wash, "maps"))
		self.assert_(hasattr(self.auto_wash, "name"))
		self.assert_(hasattr(self.auto_wash, "openingHoursSpecification"))
		self.assert_(hasattr(self.auto_wash, "paymentAccepted"))
		self.assert_(hasattr(self.auto_wash, "photo"))
		self.assert_(hasattr(self.auto_wash, "photos"))
		self.assert_(hasattr(self.auto_wash, "priceRange"))
		self.assert_(hasattr(self.auto_wash, "sameAs"))
		self.assert_(hasattr(self.auto_wash, "url"))

	def tearDown(self):
		pass

class TestAutomatedTeller(unittest.TestCase):

	def setUp(self):
		self.automated_teller = AutomatedTeller()

	def test_init(self):
		self.assertEquals(type(self.automated_teller), AutomatedTeller)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.automated_teller, "additionalType"))
		self.assert_(hasattr(self.automated_teller, "alternateName"))
		self.assert_(hasattr(self.automated_teller, "branchOf"))
		self.assert_(hasattr(self.automated_teller, "containedIn"))
		self.assert_(hasattr(self.automated_teller, "currenciesAccepted"))
		self.assert_(hasattr(self.automated_teller, "description"))
		self.assert_(hasattr(self.automated_teller, "geo"))
		self.assert_(hasattr(self.automated_teller, "image"))
		self.assert_(hasattr(self.automated_teller, "map"))
		self.assert_(hasattr(self.automated_teller, "maps"))
		self.assert_(hasattr(self.automated_teller, "name"))
		self.assert_(hasattr(self.automated_teller, "openingHoursSpecification"))
		self.assert_(hasattr(self.automated_teller, "paymentAccepted"))
		self.assert_(hasattr(self.automated_teller, "photo"))
		self.assert_(hasattr(self.automated_teller, "photos"))
		self.assert_(hasattr(self.automated_teller, "priceRange"))
		self.assert_(hasattr(self.automated_teller, "sameAs"))
		self.assert_(hasattr(self.automated_teller, "url"))

	def tearDown(self):
		pass

class TestAutomotiveBusiness(unittest.TestCase):

	def setUp(self):
		self.automotive_business = AutomotiveBusiness()

	def test_init(self):
		self.assertEquals(type(self.automotive_business), AutomotiveBusiness)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.automotive_business, "additionalType"))
		self.assert_(hasattr(self.automotive_business, "alternateName"))
		self.assert_(hasattr(self.automotive_business, "branchOf"))
		self.assert_(hasattr(self.automotive_business, "containedIn"))
		self.assert_(hasattr(self.automotive_business, "currenciesAccepted"))
		self.assert_(hasattr(self.automotive_business, "description"))
		self.assert_(hasattr(self.automotive_business, "geo"))
		self.assert_(hasattr(self.automotive_business, "image"))
		self.assert_(hasattr(self.automotive_business, "map"))
		self.assert_(hasattr(self.automotive_business, "maps"))
		self.assert_(hasattr(self.automotive_business, "name"))
		self.assert_(hasattr(self.automotive_business, "openingHoursSpecification"))
		self.assert_(hasattr(self.automotive_business, "paymentAccepted"))
		self.assert_(hasattr(self.automotive_business, "photo"))
		self.assert_(hasattr(self.automotive_business, "photos"))
		self.assert_(hasattr(self.automotive_business, "priceRange"))
		self.assert_(hasattr(self.automotive_business, "sameAs"))
		self.assert_(hasattr(self.automotive_business, "url"))

	def tearDown(self):
		pass

class TestBakery(unittest.TestCase):

	def setUp(self):
		self.bakery = Bakery()

	def test_init(self):
		self.assertEquals(type(self.bakery), Bakery)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bakery, "acceptsReservations"))
		self.assert_(hasattr(self.bakery, "additionalType"))
		self.assert_(hasattr(self.bakery, "alternateName"))
		self.assert_(hasattr(self.bakery, "branchOf"))
		self.assert_(hasattr(self.bakery, "containedIn"))
		self.assert_(hasattr(self.bakery, "currenciesAccepted"))
		self.assert_(hasattr(self.bakery, "description"))
		self.assert_(hasattr(self.bakery, "geo"))
		self.assert_(hasattr(self.bakery, "image"))
		self.assert_(hasattr(self.bakery, "map"))
		self.assert_(hasattr(self.bakery, "maps"))
		self.assert_(hasattr(self.bakery, "menu"))
		self.assert_(hasattr(self.bakery, "name"))
		self.assert_(hasattr(self.bakery, "openingHoursSpecification"))
		self.assert_(hasattr(self.bakery, "paymentAccepted"))
		self.assert_(hasattr(self.bakery, "photo"))
		self.assert_(hasattr(self.bakery, "photos"))
		self.assert_(hasattr(self.bakery, "priceRange"))
		self.assert_(hasattr(self.bakery, "sameAs"))
		self.assert_(hasattr(self.bakery, "servesCuisine"))
		self.assert_(hasattr(self.bakery, "url"))

	def tearDown(self):
		pass

class TestBankOrCreditUnion(unittest.TestCase):

	def setUp(self):
		self.bank_or_credit_union = BankOrCreditUnion()

	def test_init(self):
		self.assertEquals(type(self.bank_or_credit_union), BankOrCreditUnion)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bank_or_credit_union, "additionalType"))
		self.assert_(hasattr(self.bank_or_credit_union, "alternateName"))
		self.assert_(hasattr(self.bank_or_credit_union, "branchOf"))
		self.assert_(hasattr(self.bank_or_credit_union, "containedIn"))
		self.assert_(hasattr(self.bank_or_credit_union, "currenciesAccepted"))
		self.assert_(hasattr(self.bank_or_credit_union, "description"))
		self.assert_(hasattr(self.bank_or_credit_union, "geo"))
		self.assert_(hasattr(self.bank_or_credit_union, "image"))
		self.assert_(hasattr(self.bank_or_credit_union, "map"))
		self.assert_(hasattr(self.bank_or_credit_union, "maps"))
		self.assert_(hasattr(self.bank_or_credit_union, "name"))
		self.assert_(hasattr(self.bank_or_credit_union, "openingHoursSpecification"))
		self.assert_(hasattr(self.bank_or_credit_union, "paymentAccepted"))
		self.assert_(hasattr(self.bank_or_credit_union, "photo"))
		self.assert_(hasattr(self.bank_or_credit_union, "photos"))
		self.assert_(hasattr(self.bank_or_credit_union, "priceRange"))
		self.assert_(hasattr(self.bank_or_credit_union, "sameAs"))
		self.assert_(hasattr(self.bank_or_credit_union, "url"))

	def tearDown(self):
		pass

class TestBarOrPub(unittest.TestCase):

	def setUp(self):
		self.bar_or_pub = BarOrPub()

	def test_init(self):
		self.assertEquals(type(self.bar_or_pub), BarOrPub)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bar_or_pub, "acceptsReservations"))
		self.assert_(hasattr(self.bar_or_pub, "additionalType"))
		self.assert_(hasattr(self.bar_or_pub, "alternateName"))
		self.assert_(hasattr(self.bar_or_pub, "branchOf"))
		self.assert_(hasattr(self.bar_or_pub, "containedIn"))
		self.assert_(hasattr(self.bar_or_pub, "currenciesAccepted"))
		self.assert_(hasattr(self.bar_or_pub, "description"))
		self.assert_(hasattr(self.bar_or_pub, "geo"))
		self.assert_(hasattr(self.bar_or_pub, "image"))
		self.assert_(hasattr(self.bar_or_pub, "map"))
		self.assert_(hasattr(self.bar_or_pub, "maps"))
		self.assert_(hasattr(self.bar_or_pub, "menu"))
		self.assert_(hasattr(self.bar_or_pub, "name"))
		self.assert_(hasattr(self.bar_or_pub, "openingHoursSpecification"))
		self.assert_(hasattr(self.bar_or_pub, "paymentAccepted"))
		self.assert_(hasattr(self.bar_or_pub, "photo"))
		self.assert_(hasattr(self.bar_or_pub, "photos"))
		self.assert_(hasattr(self.bar_or_pub, "priceRange"))
		self.assert_(hasattr(self.bar_or_pub, "sameAs"))
		self.assert_(hasattr(self.bar_or_pub, "servesCuisine"))
		self.assert_(hasattr(self.bar_or_pub, "url"))

	def tearDown(self):
		pass

class TestBeach(unittest.TestCase):

	def setUp(self):
		self.beach = Beach()

	def test_init(self):
		self.assertEquals(type(self.beach), Beach)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.beach, "additionalType"))
		self.assert_(hasattr(self.beach, "alternateName"))
		self.assert_(hasattr(self.beach, "containedIn"))
		self.assert_(hasattr(self.beach, "description"))
		self.assert_(hasattr(self.beach, "geo"))
		self.assert_(hasattr(self.beach, "image"))
		self.assert_(hasattr(self.beach, "map"))
		self.assert_(hasattr(self.beach, "maps"))
		self.assert_(hasattr(self.beach, "name"))
		self.assert_(hasattr(self.beach, "openingHoursSpecification"))
		self.assert_(hasattr(self.beach, "photo"))
		self.assert_(hasattr(self.beach, "photos"))
		self.assert_(hasattr(self.beach, "sameAs"))
		self.assert_(hasattr(self.beach, "url"))

	def tearDown(self):
		pass

class TestBeautySalon(unittest.TestCase):

	def setUp(self):
		self.beauty_salon = BeautySalon()

	def test_init(self):
		self.assertEquals(type(self.beauty_salon), BeautySalon)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.beauty_salon, "additionalType"))
		self.assert_(hasattr(self.beauty_salon, "alternateName"))
		self.assert_(hasattr(self.beauty_salon, "branchOf"))
		self.assert_(hasattr(self.beauty_salon, "containedIn"))
		self.assert_(hasattr(self.beauty_salon, "currenciesAccepted"))
		self.assert_(hasattr(self.beauty_salon, "description"))
		self.assert_(hasattr(self.beauty_salon, "geo"))
		self.assert_(hasattr(self.beauty_salon, "image"))
		self.assert_(hasattr(self.beauty_salon, "map"))
		self.assert_(hasattr(self.beauty_salon, "maps"))
		self.assert_(hasattr(self.beauty_salon, "name"))
		self.assert_(hasattr(self.beauty_salon, "openingHoursSpecification"))
		self.assert_(hasattr(self.beauty_salon, "paymentAccepted"))
		self.assert_(hasattr(self.beauty_salon, "photo"))
		self.assert_(hasattr(self.beauty_salon, "photos"))
		self.assert_(hasattr(self.beauty_salon, "priceRange"))
		self.assert_(hasattr(self.beauty_salon, "sameAs"))
		self.assert_(hasattr(self.beauty_salon, "url"))

	def tearDown(self):
		pass

class TestBedAndBreakfast(unittest.TestCase):

	def setUp(self):
		self.bed_and_breakfast = BedAndBreakfast()

	def test_init(self):
		self.assertEquals(type(self.bed_and_breakfast), BedAndBreakfast)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bed_and_breakfast, "additionalType"))
		self.assert_(hasattr(self.bed_and_breakfast, "alternateName"))
		self.assert_(hasattr(self.bed_and_breakfast, "branchOf"))
		self.assert_(hasattr(self.bed_and_breakfast, "containedIn"))
		self.assert_(hasattr(self.bed_and_breakfast, "currenciesAccepted"))
		self.assert_(hasattr(self.bed_and_breakfast, "description"))
		self.assert_(hasattr(self.bed_and_breakfast, "geo"))
		self.assert_(hasattr(self.bed_and_breakfast, "image"))
		self.assert_(hasattr(self.bed_and_breakfast, "map"))
		self.assert_(hasattr(self.bed_and_breakfast, "maps"))
		self.assert_(hasattr(self.bed_and_breakfast, "name"))
		self.assert_(hasattr(self.bed_and_breakfast, "openingHoursSpecification"))
		self.assert_(hasattr(self.bed_and_breakfast, "paymentAccepted"))
		self.assert_(hasattr(self.bed_and_breakfast, "photo"))
		self.assert_(hasattr(self.bed_and_breakfast, "photos"))
		self.assert_(hasattr(self.bed_and_breakfast, "priceRange"))
		self.assert_(hasattr(self.bed_and_breakfast, "sameAs"))
		self.assert_(hasattr(self.bed_and_breakfast, "url"))

	def tearDown(self):
		pass


class TestBefriendAction(unittest.TestCase):

	def setUp(self):
		self.befriend_action = BefriendAction()

	def test_init(self):
		self.assertEquals(type(self.befriend_action), BefriendAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.befriend_action, "additionalType"))
		self.assert_(hasattr(self.befriend_action, "agent"))
		self.assert_(hasattr(self.befriend_action, "alternateName"))
		self.assert_(hasattr(self.befriend_action, "description"))
		self.assert_(hasattr(self.befriend_action, "endTime"))
		self.assert_(hasattr(self.befriend_action, "image"))
		self.assert_(hasattr(self.befriend_action, "instrument"))
		self.assert_(hasattr(self.befriend_action, "name"))
		self.assert_(hasattr(self.befriend_action, "object"))
		self.assert_(hasattr(self.befriend_action, "participant"))
		self.assert_(hasattr(self.befriend_action, "result"))
		self.assert_(hasattr(self.befriend_action, "sameAs"))
		self.assert_(hasattr(self.befriend_action, "startTime"))
		self.assert_(hasattr(self.befriend_action, "url"))

	def tearDown(self):
		pass

class TestBikeStore(unittest.TestCase):

	def setUp(self):
		self.bike_store = BikeStore()

	def test_init(self):
		self.assertEquals(type(self.bike_store), BikeStore)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bike_store, "additionalType"))
		self.assert_(hasattr(self.bike_store, "alternateName"))
		self.assert_(hasattr(self.bike_store, "branchOf"))
		self.assert_(hasattr(self.bike_store, "containedIn"))
		self.assert_(hasattr(self.bike_store, "currenciesAccepted"))
		self.assert_(hasattr(self.bike_store, "description"))
		self.assert_(hasattr(self.bike_store, "geo"))
		self.assert_(hasattr(self.bike_store, "image"))
		self.assert_(hasattr(self.bike_store, "map"))
		self.assert_(hasattr(self.bike_store, "maps"))
		self.assert_(hasattr(self.bike_store, "name"))
		self.assert_(hasattr(self.bike_store, "openingHoursSpecification"))
		self.assert_(hasattr(self.bike_store, "paymentAccepted"))
		self.assert_(hasattr(self.bike_store, "photo"))
		self.assert_(hasattr(self.bike_store, "photos"))
		self.assert_(hasattr(self.bike_store, "priceRange"))
		self.assert_(hasattr(self.bike_store, "sameAs"))
		self.assert_(hasattr(self.bike_store, "url"))

	def tearDown(self):
		pass

class TestBlog(unittest.TestCase):

	def setUp(self):
		self.blog = Blog()

	def test_init(self):
		self.assertEquals(type(self.blog), Blog)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.blog, "accessibilityAPI"))
		self.assert_(hasattr(self.blog, "accessibilityControl"))
		self.assert_(hasattr(self.blog, "accessibilityFeature"))
		self.assert_(hasattr(self.blog, "accessibilityHazard"))
		self.assert_(hasattr(self.blog, "accountablePerson"))
		self.assert_(hasattr(self.blog, "additionalType"))
		self.assert_(hasattr(self.blog, "alternateName"))
		self.assert_(hasattr(self.blog, "alternativeHeadline"))
		self.assert_(hasattr(self.blog, "associatedMedia"))
		self.assert_(hasattr(self.blog, "audio"))
		self.assert_(hasattr(self.blog, "author"))
		self.assert_(hasattr(self.blog, "blogPost"))
		self.assert_(hasattr(self.blog, "blogPosts"))
		self.assert_(hasattr(self.blog, "citation"))
		self.assert_(hasattr(self.blog, "comment"))
		self.assert_(hasattr(self.blog, "contentLocation"))
		self.assert_(hasattr(self.blog, "contentRating"))
		self.assert_(hasattr(self.blog, "contributor"))
		self.assert_(hasattr(self.blog, "copyrightHolder"))
		self.assert_(hasattr(self.blog, "copyrightYear"))
		self.assert_(hasattr(self.blog, "dateCreated"))
		self.assert_(hasattr(self.blog, "dateModified"))
		self.assert_(hasattr(self.blog, "datePublished"))
		self.assert_(hasattr(self.blog, "description"))
		self.assert_(hasattr(self.blog, "discussionUrl"))
		self.assert_(hasattr(self.blog, "editor"))
		self.assert_(hasattr(self.blog, "educationalAlignment"))
		self.assert_(hasattr(self.blog, "educationalUse"))
		self.assert_(hasattr(self.blog, "encoding"))
		self.assert_(hasattr(self.blog, "encodings"))
		self.assert_(hasattr(self.blog, "genre"))
		self.assert_(hasattr(self.blog, "headline"))
		self.assert_(hasattr(self.blog, "image"))
		self.assert_(hasattr(self.blog, "inLanguage"))
		self.assert_(hasattr(self.blog, "interactivityType"))
		self.assert_(hasattr(self.blog, "isBasedOnUrl"))
		self.assert_(hasattr(self.blog, "isFamilyFriendly"))
		self.assert_(hasattr(self.blog, "keywords"))
		self.assert_(hasattr(self.blog, "learningResourceType"))
		self.assert_(hasattr(self.blog, "mentions"))
		self.assert_(hasattr(self.blog, "name"))
		self.assert_(hasattr(self.blog, "publisher"))
		self.assert_(hasattr(self.blog, "publishingPrinciples"))
		self.assert_(hasattr(self.blog, "sameAs"))
		self.assert_(hasattr(self.blog, "sourceOrganization"))
		self.assert_(hasattr(self.blog, "text"))
		self.assert_(hasattr(self.blog, "thumbnailUrl"))
		self.assert_(hasattr(self.blog, "timeRequired"))
		self.assert_(hasattr(self.blog, "url"))
		self.assert_(hasattr(self.blog, "version"))
		self.assert_(hasattr(self.blog, "video"))

	def tearDown(self):
		pass


class TestBlogPosting(unittest.TestCase):

	def setUp(self):
		self.blog_posting = BlogPosting()

	def test_init(self):
		self.assertEquals(type(self.blog_posting), BlogPosting)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.blog_posting, "accessibilityAPI"))
		self.assert_(hasattr(self.blog_posting, "accessibilityControl"))
		self.assert_(hasattr(self.blog_posting, "accessibilityFeature"))
		self.assert_(hasattr(self.blog_posting, "accessibilityHazard"))
		self.assert_(hasattr(self.blog_posting, "accountablePerson"))
		self.assert_(hasattr(self.blog_posting, "additionalType"))
		self.assert_(hasattr(self.blog_posting, "alternateName"))
		self.assert_(hasattr(self.blog_posting, "alternativeHeadline"))
		self.assert_(hasattr(self.blog_posting, "articleBody"))
		self.assert_(hasattr(self.blog_posting, "articleSection"))
		self.assert_(hasattr(self.blog_posting, "associatedMedia"))
		self.assert_(hasattr(self.blog_posting, "audio"))
		self.assert_(hasattr(self.blog_posting, "author"))
		self.assert_(hasattr(self.blog_posting, "citation"))
		self.assert_(hasattr(self.blog_posting, "comment"))
		self.assert_(hasattr(self.blog_posting, "contentLocation"))
		self.assert_(hasattr(self.blog_posting, "contentRating"))
		self.assert_(hasattr(self.blog_posting, "contributor"))
		self.assert_(hasattr(self.blog_posting, "copyrightHolder"))
		self.assert_(hasattr(self.blog_posting, "copyrightYear"))
		self.assert_(hasattr(self.blog_posting, "dateCreated"))
		self.assert_(hasattr(self.blog_posting, "dateModified"))
		self.assert_(hasattr(self.blog_posting, "datePublished"))
		self.assert_(hasattr(self.blog_posting, "description"))
		self.assert_(hasattr(self.blog_posting, "discussionUrl"))
		self.assert_(hasattr(self.blog_posting, "editor"))
		self.assert_(hasattr(self.blog_posting, "educationalAlignment"))
		self.assert_(hasattr(self.blog_posting, "educationalUse"))
		self.assert_(hasattr(self.blog_posting, "encoding"))
		self.assert_(hasattr(self.blog_posting, "encodings"))
		self.assert_(hasattr(self.blog_posting, "genre"))
		self.assert_(hasattr(self.blog_posting, "headline"))
		self.assert_(hasattr(self.blog_posting, "image"))
		self.assert_(hasattr(self.blog_posting, "inLanguage"))
		self.assert_(hasattr(self.blog_posting, "interactivityType"))
		self.assert_(hasattr(self.blog_posting, "isBasedOnUrl"))
		self.assert_(hasattr(self.blog_posting, "isFamilyFriendly"))
		self.assert_(hasattr(self.blog_posting, "keywords"))
		self.assert_(hasattr(self.blog_posting, "learningResourceType"))
		self.assert_(hasattr(self.blog_posting, "mentions"))
		self.assert_(hasattr(self.blog_posting, "name"))
		self.assert_(hasattr(self.blog_posting, "publisher"))
		self.assert_(hasattr(self.blog_posting, "publishingPrinciples"))
		self.assert_(hasattr(self.blog_posting, "sameAs"))
		self.assert_(hasattr(self.blog_posting, "sourceOrganization"))
		self.assert_(hasattr(self.blog_posting, "text"))
		self.assert_(hasattr(self.blog_posting, "thumbnailUrl"))
		self.assert_(hasattr(self.blog_posting, "timeRequired"))
		self.assert_(hasattr(self.blog_posting, "url"))
		self.assert_(hasattr(self.blog_posting, "version"))
		self.assert_(hasattr(self.blog_posting, "video"))
		self.assert_(hasattr(self.blog_posting, "wordCount"))

	def tearDown(self):
		pass


class TestBloodTest(unittest.TestCase):

	def setUp(self):
		self.blood_test = BloodTest()

	def test_init(self):
		self.assertEquals(type(self.blood_test), BloodTest)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.blood_test, "additionalType"))
		self.assert_(hasattr(self.blood_test, "affectedBy"))
		self.assert_(hasattr(self.blood_test, "alternateName"))
		self.assert_(hasattr(self.blood_test, "code"))
		self.assert_(hasattr(self.blood_test, "description"))
		self.assert_(hasattr(self.blood_test, "guideline"))
		self.assert_(hasattr(self.blood_test, "image"))
		self.assert_(hasattr(self.blood_test, "medicineSystem"))
		self.assert_(hasattr(self.blood_test, "name"))
		self.assert_(hasattr(self.blood_test, "normalRange"))
		self.assert_(hasattr(self.blood_test, "recognizingAuthority"))
		self.assert_(hasattr(self.blood_test, "relevantSpecialty"))
		self.assert_(hasattr(self.blood_test, "sameAs"))
		self.assert_(hasattr(self.blood_test, "signDetected"))
		self.assert_(hasattr(self.blood_test, "study"))
		self.assert_(hasattr(self.blood_test, "url"))
		self.assert_(hasattr(self.blood_test, "usedToDiagnose"))
		self.assert_(hasattr(self.blood_test, "usesDevice"))

	def tearDown(self):
		pass


class TestBodyOfWater(unittest.TestCase):

	def setUp(self):
		self.body_of_water = BodyOfWater()

	def test_init(self):
		self.assertEquals(type(self.body_of_water), BodyOfWater)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.body_of_water, "additionalType"))
		self.assert_(hasattr(self.body_of_water, "alternateName"))
		self.assert_(hasattr(self.body_of_water, "containedIn"))
		self.assert_(hasattr(self.body_of_water, "description"))
		self.assert_(hasattr(self.body_of_water, "geo"))
		self.assert_(hasattr(self.body_of_water, "image"))
		self.assert_(hasattr(self.body_of_water, "map"))
		self.assert_(hasattr(self.body_of_water, "maps"))
		self.assert_(hasattr(self.body_of_water, "name"))
		self.assert_(hasattr(self.body_of_water, "openingHoursSpecification"))
		self.assert_(hasattr(self.body_of_water, "photo"))
		self.assert_(hasattr(self.body_of_water, "photos"))
		self.assert_(hasattr(self.body_of_water, "sameAs"))
		self.assert_(hasattr(self.body_of_water, "url"))

	def tearDown(self):
		pass

class TestBone(unittest.TestCase):

	def setUp(self):
		self.bone = Bone()

	def test_init(self):
		self.assertEquals(type(self.bone), Bone)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bone, "additionalType"))
		self.assert_(hasattr(self.bone, "alternateName"))
		self.assert_(hasattr(self.bone, "bodyLocation"))
		self.assert_(hasattr(self.bone, "code"))
		self.assert_(hasattr(self.bone, "connectedTo"))
		self.assert_(hasattr(self.bone, "description"))
		self.assert_(hasattr(self.bone, "diagram"))
		self.assert_(hasattr(self.bone, "function"))
		self.assert_(hasattr(self.bone, "guideline"))
		self.assert_(hasattr(self.bone, "image"))
		self.assert_(hasattr(self.bone, "medicineSystem"))
		self.assert_(hasattr(self.bone, "name"))
		self.assert_(hasattr(self.bone, "partOfSystem"))
		self.assert_(hasattr(self.bone, "recognizingAuthority"))
		self.assert_(hasattr(self.bone, "relevantSpecialty"))
		self.assert_(hasattr(self.bone, "sameAs"))
		self.assert_(hasattr(self.bone, "study"))
		self.assert_(hasattr(self.bone, "subStructure"))
		self.assert_(hasattr(self.bone, "url"))

	def tearDown(self):
		pass

class TestBook(unittest.TestCase):

	def setUp(self):
		self.book = Book()

	def test_init(self):
		self.assertEquals(type(self.book), Book)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.book, "accessibilityAPI"))
		self.assert_(hasattr(self.book, "accessibilityControl"))
		self.assert_(hasattr(self.book, "accessibilityFeature"))
		self.assert_(hasattr(self.book, "accessibilityHazard"))
		self.assert_(hasattr(self.book, "accountablePerson"))
		self.assert_(hasattr(self.book, "additionalType"))
		self.assert_(hasattr(self.book, "alternateName"))
		self.assert_(hasattr(self.book, "alternativeHeadline"))
		self.assert_(hasattr(self.book, "associatedMedia"))
		self.assert_(hasattr(self.book, "audio"))
		self.assert_(hasattr(self.book, "author"))
		self.assert_(hasattr(self.book, "bookEdition"))
		self.assert_(hasattr(self.book, "bookFormat"))
		self.assert_(hasattr(self.book, "citation"))
		self.assert_(hasattr(self.book, "comment"))
		self.assert_(hasattr(self.book, "contentLocation"))
		self.assert_(hasattr(self.book, "contentRating"))
		self.assert_(hasattr(self.book, "contributor"))
		self.assert_(hasattr(self.book, "copyrightHolder"))
		self.assert_(hasattr(self.book, "copyrightYear"))
		self.assert_(hasattr(self.book, "dateCreated"))
		self.assert_(hasattr(self.book, "dateModified"))
		self.assert_(hasattr(self.book, "datePublished"))
		self.assert_(hasattr(self.book, "description"))
		self.assert_(hasattr(self.book, "discussionUrl"))
		self.assert_(hasattr(self.book, "editor"))
		self.assert_(hasattr(self.book, "educationalAlignment"))
		self.assert_(hasattr(self.book, "educationalUse"))
		self.assert_(hasattr(self.book, "encoding"))
		self.assert_(hasattr(self.book, "encodings"))
		self.assert_(hasattr(self.book, "genre"))
		self.assert_(hasattr(self.book, "headline"))
		self.assert_(hasattr(self.book, "illustrator"))
		self.assert_(hasattr(self.book, "image"))
		self.assert_(hasattr(self.book, "inLanguage"))
		self.assert_(hasattr(self.book, "interactivityType"))
		self.assert_(hasattr(self.book, "isBasedOnUrl"))
		self.assert_(hasattr(self.book, "isFamilyFriendly"))
		self.assert_(hasattr(self.book, "isbn"))
		self.assert_(hasattr(self.book, "keywords"))
		self.assert_(hasattr(self.book, "learningResourceType"))
		self.assert_(hasattr(self.book, "mentions"))
		self.assert_(hasattr(self.book, "name"))
		self.assert_(hasattr(self.book, "numberOfPages"))
		self.assert_(hasattr(self.book, "publisher"))
		self.assert_(hasattr(self.book, "publishingPrinciples"))
		self.assert_(hasattr(self.book, "sameAs"))
		self.assert_(hasattr(self.book, "sourceOrganization"))
		self.assert_(hasattr(self.book, "text"))
		self.assert_(hasattr(self.book, "thumbnailUrl"))
		self.assert_(hasattr(self.book, "timeRequired"))
		self.assert_(hasattr(self.book, "url"))
		self.assert_(hasattr(self.book, "version"))
		self.assert_(hasattr(self.book, "video"))

	def tearDown(self):
		pass

class TestBookFormatType(unittest.TestCase):

	def setUp(self):
		self.book_format_type = BookFormatType()

	def test_init(self):
		self.assertEquals(type(self.book_format_type), BookFormatType)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.book_format_type, "additionalType"))
		self.assert_(hasattr(self.book_format_type, "alternateName"))
		self.assert_(hasattr(self.book_format_type, "description"))
		self.assert_(hasattr(self.book_format_type, "image"))
		self.assert_(hasattr(self.book_format_type, "name"))
		self.assert_(hasattr(self.book_format_type, "sameAs"))
		self.assert_(hasattr(self.book_format_type, "url"))

	def tearDown(self):
		pass


class TestBookStore(unittest.TestCase):

	def setUp(self):
		self.book_store = BookStore()

	def test_init(self):
		self.assertEquals(type(self.book_store), BookStore)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.book_store, "additionalType"))
		self.assert_(hasattr(self.book_store, "alternateName"))
		self.assert_(hasattr(self.book_store, "branchOf"))
		self.assert_(hasattr(self.book_store, "containedIn"))
		self.assert_(hasattr(self.book_store, "currenciesAccepted"))
		self.assert_(hasattr(self.book_store, "description"))
		self.assert_(hasattr(self.book_store, "geo"))
		self.assert_(hasattr(self.book_store, "image"))
		self.assert_(hasattr(self.book_store, "map"))
		self.assert_(hasattr(self.book_store, "maps"))
		self.assert_(hasattr(self.book_store, "name"))
		self.assert_(hasattr(self.book_store, "openingHoursSpecification"))
		self.assert_(hasattr(self.book_store, "paymentAccepted"))
		self.assert_(hasattr(self.book_store, "photo"))
		self.assert_(hasattr(self.book_store, "photos"))
		self.assert_(hasattr(self.book_store, "priceRange"))
		self.assert_(hasattr(self.book_store, "sameAs"))
		self.assert_(hasattr(self.book_store, "url"))

	def tearDown(self):
		pass



class TestBookmarkAction(unittest.TestCase):

	def setUp(self):
		self.bookmark_action = BookmarkAction()

	def test_init(self):
		self.assertEquals(type(self.bookmark_action), BookmarkAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bookmark_action, "additionalType"))
		self.assert_(hasattr(self.bookmark_action, "agent"))
		self.assert_(hasattr(self.bookmark_action, "alternateName"))
		self.assert_(hasattr(self.bookmark_action, "description"))
		self.assert_(hasattr(self.bookmark_action, "endTime"))
		self.assert_(hasattr(self.bookmark_action, "image"))
		self.assert_(hasattr(self.bookmark_action, "instrument"))
		self.assert_(hasattr(self.bookmark_action, "name"))
		self.assert_(hasattr(self.bookmark_action, "object"))
		self.assert_(hasattr(self.bookmark_action, "participant"))
		self.assert_(hasattr(self.bookmark_action, "result"))
		self.assert_(hasattr(self.bookmark_action, "sameAs"))
		self.assert_(hasattr(self.bookmark_action, "startTime"))
		self.assert_(hasattr(self.bookmark_action, "url"))

	def tearDown(self):
		pass


class TestBorrowAction(unittest.TestCase):

	def setUp(self):
		self.borrow_action = BorrowAction()

	def test_init(self):
		self.assertEquals(type(self.borrow_action), BorrowAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.borrow_action, "additionalType"))
		self.assert_(hasattr(self.borrow_action, "agent"))
		self.assert_(hasattr(self.borrow_action, "alternateName"))
		self.assert_(hasattr(self.borrow_action, "description"))
		self.assert_(hasattr(self.borrow_action, "endTime"))
		self.assert_(hasattr(self.borrow_action, "image"))
		self.assert_(hasattr(self.borrow_action, "instrument"))
		self.assert_(hasattr(self.borrow_action, "lender"))
		self.assert_(hasattr(self.borrow_action, "name"))
		self.assert_(hasattr(self.borrow_action, "object"))
		self.assert_(hasattr(self.borrow_action, "participant"))
		self.assert_(hasattr(self.borrow_action, "result"))
		self.assert_(hasattr(self.borrow_action, "sameAs"))
		self.assert_(hasattr(self.borrow_action, "startTime"))
		self.assert_(hasattr(self.borrow_action, "url"))

	def tearDown(self):
		pass

class TestBowlingAlley(unittest.TestCase):

	def setUp(self):
		self.bowling_alley = BowlingAlley()

	def test_init(self):
		self.assertEquals(type(self.bowling_alley), BowlingAlley)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bowling_alley, "additionalType"))
		self.assert_(hasattr(self.bowling_alley, "alternateName"))
		self.assert_(hasattr(self.bowling_alley, "branchOf"))
		self.assert_(hasattr(self.bowling_alley, "containedIn"))
		self.assert_(hasattr(self.bowling_alley, "currenciesAccepted"))
		self.assert_(hasattr(self.bowling_alley, "description"))
		self.assert_(hasattr(self.bowling_alley, "geo"))
		self.assert_(hasattr(self.bowling_alley, "image"))
		self.assert_(hasattr(self.bowling_alley, "map"))
		self.assert_(hasattr(self.bowling_alley, "maps"))
		self.assert_(hasattr(self.bowling_alley, "name"))
		self.assert_(hasattr(self.bowling_alley, "openingHoursSpecification"))
		self.assert_(hasattr(self.bowling_alley, "paymentAccepted"))
		self.assert_(hasattr(self.bowling_alley, "photo"))
		self.assert_(hasattr(self.bowling_alley, "photos"))
		self.assert_(hasattr(self.bowling_alley, "priceRange"))
		self.assert_(hasattr(self.bowling_alley, "sameAs"))
		self.assert_(hasattr(self.bowling_alley, "url"))

	def tearDown(self):
		pass


class TestBrainStructure(unittest.TestCase):

	def setUp(self):
		self.brain_structure = BrainStructure()

	def test_init(self):
		self.assertEquals(type(self.brain_structure), BrainStructure)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.brain_structure, "additionalType"))
		self.assert_(hasattr(self.brain_structure, "alternateName"))
		self.assert_(hasattr(self.brain_structure, "bodyLocation"))
		self.assert_(hasattr(self.brain_structure, "code"))
		self.assert_(hasattr(self.brain_structure, "connectedTo"))
		self.assert_(hasattr(self.brain_structure, "description"))
		self.assert_(hasattr(self.brain_structure, "diagram"))
		self.assert_(hasattr(self.brain_structure, "function"))
		self.assert_(hasattr(self.brain_structure, "guideline"))
		self.assert_(hasattr(self.brain_structure, "image"))
		self.assert_(hasattr(self.brain_structure, "medicineSystem"))
		self.assert_(hasattr(self.brain_structure, "name"))
		self.assert_(hasattr(self.brain_structure, "partOfSystem"))
		self.assert_(hasattr(self.brain_structure, "recognizingAuthority"))
		self.assert_(hasattr(self.brain_structure, "relevantSpecialty"))
		self.assert_(hasattr(self.brain_structure, "sameAs"))
		self.assert_(hasattr(self.brain_structure, "study"))
		self.assert_(hasattr(self.brain_structure, "subStructure"))
		self.assert_(hasattr(self.brain_structure, "url"))

	def tearDown(self):
		pass

class TestBrand(unittest.TestCase):

	def setUp(self):
		self.brand = Brand()

	def test_init(self):
		self.assertEquals(type(self.brand), Brand)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.brand, "additionalType"))
		self.assert_(hasattr(self.brand, "alternateName"))
		self.assert_(hasattr(self.brand, "description"))
		self.assert_(hasattr(self.brand, "image"))
		self.assert_(hasattr(self.brand, "name"))
		self.assert_(hasattr(self.brand, "sameAs"))
		self.assert_(hasattr(self.brand, "url"))

	def tearDown(self):
		pass



class TestBrewery(unittest.TestCase):

	def setUp(self):
		self.brewery = Brewery()

	def test_init(self):
		self.assertEquals(type(self.brewery), Brewery)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.brewery, "acceptsReservations"))
		self.assert_(hasattr(self.brewery, "additionalType"))
		self.assert_(hasattr(self.brewery, "alternateName"))
		self.assert_(hasattr(self.brewery, "branchOf"))
		self.assert_(hasattr(self.brewery, "containedIn"))
		self.assert_(hasattr(self.brewery, "currenciesAccepted"))
		self.assert_(hasattr(self.brewery, "description"))
		self.assert_(hasattr(self.brewery, "geo"))
		self.assert_(hasattr(self.brewery, "image"))
		self.assert_(hasattr(self.brewery, "map"))
		self.assert_(hasattr(self.brewery, "maps"))
		self.assert_(hasattr(self.brewery, "menu"))
		self.assert_(hasattr(self.brewery, "name"))
		self.assert_(hasattr(self.brewery, "openingHoursSpecification"))
		self.assert_(hasattr(self.brewery, "paymentAccepted"))
		self.assert_(hasattr(self.brewery, "photo"))
		self.assert_(hasattr(self.brewery, "photos"))
		self.assert_(hasattr(self.brewery, "priceRange"))
		self.assert_(hasattr(self.brewery, "sameAs"))
		self.assert_(hasattr(self.brewery, "servesCuisine"))
		self.assert_(hasattr(self.brewery, "url"))

	def tearDown(self):
		pass



class TestBroadcastEvent(unittest.TestCase):

	def setUp(self):
		self.broadcast_event = BroadcastEvent()

	def test_init(self):
		self.assertEquals(type(self.broadcast_event), BroadcastEvent)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.broadcast_event, "additionalType"))
		self.assert_(hasattr(self.broadcast_event, "alternateName"))
		self.assert_(hasattr(self.broadcast_event, "attendee"))
		self.assert_(hasattr(self.broadcast_event, "attendees"))
		self.assert_(hasattr(self.broadcast_event, "description"))
		self.assert_(hasattr(self.broadcast_event, "doorTime"))
		self.assert_(hasattr(self.broadcast_event, "eventStatus"))
		self.assert_(hasattr(self.broadcast_event, "free"))
		self.assert_(hasattr(self.broadcast_event, "image"))
		self.assert_(hasattr(self.broadcast_event, "name"))
		self.assert_(hasattr(self.broadcast_event, "performer"))
		self.assert_(hasattr(self.broadcast_event, "performers"))
		self.assert_(hasattr(self.broadcast_event, "previousStartDate"))
		self.assert_(hasattr(self.broadcast_event, "publishedOn"))
		self.assert_(hasattr(self.broadcast_event, "sameAs"))
		self.assert_(hasattr(self.broadcast_event, "subEvent"))
		self.assert_(hasattr(self.broadcast_event, "subEvents"))
		self.assert_(hasattr(self.broadcast_event, "superEvent"))
		self.assert_(hasattr(self.broadcast_event, "url"))

	def tearDown(self):
		pass


class TestBroadcastService(unittest.TestCase):

	def setUp(self):
		self.broadcast_service = BroadcastService()

	def test_init(self):
		self.assertEquals(type(self.broadcast_service), BroadcastService)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.broadcast_service, "additionalType"))
		self.assert_(hasattr(self.broadcast_service, "alternateName"))
		self.assert_(hasattr(self.broadcast_service, "area"))
		self.assert_(hasattr(self.broadcast_service, "broadcaster"))
		self.assert_(hasattr(self.broadcast_service, "description"))
		self.assert_(hasattr(self.broadcast_service, "image"))
		self.assert_(hasattr(self.broadcast_service, "name"))
		self.assert_(hasattr(self.broadcast_service, "parentService"))
		self.assert_(hasattr(self.broadcast_service, "sameAs"))
		self.assert_(hasattr(self.broadcast_service, "url"))

	def tearDown(self):
		pass

class TestBuddhistTemple(unittest.TestCase):

	def setUp(self):
		self.buddhist_temple = BuddhistTemple()

	def test_init(self):
		self.assertEquals(type(self.buddhist_temple), BuddhistTemple)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.buddhist_temple, "additionalType"))
		self.assert_(hasattr(self.buddhist_temple, "alternateName"))
		self.assert_(hasattr(self.buddhist_temple, "containedIn"))
		self.assert_(hasattr(self.buddhist_temple, "description"))
		self.assert_(hasattr(self.buddhist_temple, "geo"))
		self.assert_(hasattr(self.buddhist_temple, "image"))
		self.assert_(hasattr(self.buddhist_temple, "map"))
		self.assert_(hasattr(self.buddhist_temple, "maps"))
		self.assert_(hasattr(self.buddhist_temple, "name"))
		self.assert_(hasattr(self.buddhist_temple, "openingHoursSpecification"))
		self.assert_(hasattr(self.buddhist_temple, "photo"))
		self.assert_(hasattr(self.buddhist_temple, "photos"))
		self.assert_(hasattr(self.buddhist_temple, "sameAs"))
		self.assert_(hasattr(self.buddhist_temple, "url"))

	def tearDown(self):
		pass


class TestBusStation(unittest.TestCase):

	def setUp(self):
		self.bus_station = BusStation()

	def test_init(self):
		self.assertEquals(type(self.bus_station), BusStation)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bus_station, "additionalType"))
		self.assert_(hasattr(self.bus_station, "alternateName"))
		self.assert_(hasattr(self.bus_station, "containedIn"))
		self.assert_(hasattr(self.bus_station, "description"))
		self.assert_(hasattr(self.bus_station, "geo"))
		self.assert_(hasattr(self.bus_station, "image"))
		self.assert_(hasattr(self.bus_station, "map"))
		self.assert_(hasattr(self.bus_station, "maps"))
		self.assert_(hasattr(self.bus_station, "name"))
		self.assert_(hasattr(self.bus_station, "openingHoursSpecification"))
		self.assert_(hasattr(self.bus_station, "photo"))
		self.assert_(hasattr(self.bus_station, "photos"))
		self.assert_(hasattr(self.bus_station, "sameAs"))
		self.assert_(hasattr(self.bus_station, "url"))

	def tearDown(self):
		pass


class TestBusStop(unittest.TestCase):

	def setUp(self):
		self.bus_stop = BusStop()

	def test_init(self):
		self.assertEquals(type(self.bus_stop), BusStop)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.bus_stop, "additionalType"))
		self.assert_(hasattr(self.bus_stop, "alternateName"))
		self.assert_(hasattr(self.bus_stop, "containedIn"))
		self.assert_(hasattr(self.bus_stop, "description"))
		self.assert_(hasattr(self.bus_stop, "geo"))
		self.assert_(hasattr(self.bus_stop, "image"))
		self.assert_(hasattr(self.bus_stop, "map"))
		self.assert_(hasattr(self.bus_stop, "maps"))
		self.assert_(hasattr(self.bus_stop, "name"))
		self.assert_(hasattr(self.bus_stop, "openingHoursSpecification"))
		self.assert_(hasattr(self.bus_stop, "photo"))
		self.assert_(hasattr(self.bus_stop, "photos"))
		self.assert_(hasattr(self.bus_stop, "sameAs"))
		self.assert_(hasattr(self.bus_stop, "url"))

	def tearDown(self):
		pass


class TestBusinessAudience(unittest.TestCase):

	def setUp(self):
		self.business_audience = BusinessAudience()

	def test_init(self):
		self.assertEquals(type(self.business_audience), BusinessAudience)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.business_audience, "additionalType"))
		self.assert_(hasattr(self.business_audience, "alternateName"))
		self.assert_(hasattr(self.business_audience, "audienceType"))
		self.assert_(hasattr(self.business_audience, "description"))
		self.assert_(hasattr(self.business_audience, "geographicArea"))
		self.assert_(hasattr(self.business_audience, "image"))
		self.assert_(hasattr(self.business_audience, "name"))
		self.assert_(hasattr(self.business_audience, "numberofEmployees"))
		self.assert_(hasattr(self.business_audience, "sameAs"))
		self.assert_(hasattr(self.business_audience, "url"))
		self.assert_(hasattr(self.business_audience, "yearlyRevenue"))
		self.assert_(hasattr(self.business_audience, "yearsInOperation"))

	def tearDown(self):
		pass

class TestBusinessEntityType(unittest.TestCase):

	def setUp(self):
		self.business_entity_type = BusinessEntityType()

	def test_init(self):
		self.assertEquals(type(self.business_entity_type), BusinessEntityType)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.business_entity_type, "additionalType"))
		self.assert_(hasattr(self.business_entity_type, "alternateName"))
		self.assert_(hasattr(self.business_entity_type, "description"))
		self.assert_(hasattr(self.business_entity_type, "image"))
		self.assert_(hasattr(self.business_entity_type, "name"))
		self.assert_(hasattr(self.business_entity_type, "sameAs"))
		self.assert_(hasattr(self.business_entity_type, "url"))

	def tearDown(self):
		pass


class TestBusinessEvent(unittest.TestCase):

	def setUp(self):
		self.business_event = BusinessEvent()

	def test_init(self):
		self.assertEquals(type(self.business_event), BusinessEvent)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.business_event, "additionalType"))
		self.assert_(hasattr(self.business_event, "alternateName"))
		self.assert_(hasattr(self.business_event, "attendee"))
		self.assert_(hasattr(self.business_event, "attendees"))
		self.assert_(hasattr(self.business_event, "description"))
		self.assert_(hasattr(self.business_event, "doorTime"))
		self.assert_(hasattr(self.business_event, "eventStatus"))
		self.assert_(hasattr(self.business_event, "image"))
		self.assert_(hasattr(self.business_event, "name"))
		self.assert_(hasattr(self.business_event, "performer"))
		self.assert_(hasattr(self.business_event, "performers"))
		self.assert_(hasattr(self.business_event, "previousStartDate"))
		self.assert_(hasattr(self.business_event, "sameAs"))
		self.assert_(hasattr(self.business_event, "subEvent"))
		self.assert_(hasattr(self.business_event, "subEvents"))
		self.assert_(hasattr(self.business_event, "superEvent"))
		self.assert_(hasattr(self.business_event, "url"))

	def tearDown(self):
		pass



class TestBusinessFunction(unittest.TestCase):

	def setUp(self):
		self.business_function = BusinessFunction()

	def test_init(self):
		self.assertEquals(type(self.business_function), BusinessFunction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.business_function, "additionalType"))
		self.assert_(hasattr(self.business_function, "alternateName"))
		self.assert_(hasattr(self.business_function, "description"))
		self.assert_(hasattr(self.business_function, "image"))
		self.assert_(hasattr(self.business_function, "name"))
		self.assert_(hasattr(self.business_function, "sameAs"))
		self.assert_(hasattr(self.business_function, "url"))

	def tearDown(self):
		pass


class TestBuyAction(unittest.TestCase):

	def setUp(self):
		self.buy_action = BuyAction()

	def test_init(self):
		self.assertEquals(type(self.buy_action), BuyAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.buy_action, "additionalType"))
		self.assert_(hasattr(self.buy_action, "agent"))
		self.assert_(hasattr(self.buy_action, "alternateName"))
		self.assert_(hasattr(self.buy_action, "description"))
		self.assert_(hasattr(self.buy_action, "endTime"))
		self.assert_(hasattr(self.buy_action, "image"))
		self.assert_(hasattr(self.buy_action, "instrument"))
		self.assert_(hasattr(self.buy_action, "name"))
		self.assert_(hasattr(self.buy_action, "object"))
		self.assert_(hasattr(self.buy_action, "participant"))
		self.assert_(hasattr(self.buy_action, "result"))
		self.assert_(hasattr(self.buy_action, "sameAs"))
		self.assert_(hasattr(self.buy_action, "startTime"))
		self.assert_(hasattr(self.buy_action, "url"))
		self.assert_(hasattr(self.buy_action, "vendor"))

	def tearDown(self):
		pass



class TestCafeOrCoffeeShop(unittest.TestCase):

	def setUp(self):
		self.cafe_or_coffee_shop = CafeOrCoffeeShop()

	def test_init(self):
		self.assertEquals(type(self.cafe_or_coffee_shop), CafeOrCoffeeShop)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.cafe_or_coffee_shop, "acceptsReservations"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "additionalType"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "alternateName"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "branchOf"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "containedIn"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "currenciesAccepted"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "description"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "geo"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "image"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "map"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "maps"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "menu"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "name"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "openingHoursSpecification"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "paymentAccepted"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "photo"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "photos"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "priceRange"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "sameAs"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "servesCuisine"))
		self.assert_(hasattr(self.cafe_or_coffee_shop, "url"))

	def tearDown(self):
		pass


class TestCampground(unittest.TestCase):

	def setUp(self):
		self.campground = Campground()

	def test_init(self):
		self.assertEquals(type(self.campground), Campground)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.campground, "additionalType"))
		self.assert_(hasattr(self.campground, "alternateName"))
		self.assert_(hasattr(self.campground, "containedIn"))
		self.assert_(hasattr(self.campground, "description"))
		self.assert_(hasattr(self.campground, "geo"))
		self.assert_(hasattr(self.campground, "image"))
		self.assert_(hasattr(self.campground, "map"))
		self.assert_(hasattr(self.campground, "maps"))
		self.assert_(hasattr(self.campground, "name"))
		self.assert_(hasattr(self.campground, "openingHoursSpecification"))
		self.assert_(hasattr(self.campground, "photo"))
		self.assert_(hasattr(self.campground, "photos"))
		self.assert_(hasattr(self.campground, "sameAs"))
		self.assert_(hasattr(self.campground, "url"))

	def tearDown(self):
		pass


class TestCanal(unittest.TestCase):

	def setUp(self):
		self.canal = Canal()

	def test_init(self):
		self.assertEquals(type(self.canal), Canal)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.canal, "additionalType"))
		self.assert_(hasattr(self.canal, "alternateName"))
		self.assert_(hasattr(self.canal, "containedIn"))
		self.assert_(hasattr(self.canal, "description"))
		self.assert_(hasattr(self.canal, "geo"))
		self.assert_(hasattr(self.canal, "image"))
		self.assert_(hasattr(self.canal, "map"))
		self.assert_(hasattr(self.canal, "maps"))
		self.assert_(hasattr(self.canal, "name"))
		self.assert_(hasattr(self.canal, "openingHoursSpecification"))
		self.assert_(hasattr(self.canal, "photo"))
		self.assert_(hasattr(self.canal, "photos"))
		self.assert_(hasattr(self.canal, "sameAs"))
		self.assert_(hasattr(self.canal, "url"))

	def tearDown(self):
		pass


class TestCancelAction(unittest.TestCase):

	def setUp(self):
		self.cancel_action = CancelAction()

	def test_init(self):
		self.assertEquals(type(self.cancel_action), CancelAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.cancel_action, "additionalType"))
		self.assert_(hasattr(self.cancel_action, "agent"))
		self.assert_(hasattr(self.cancel_action, "alternateName"))
		self.assert_(hasattr(self.cancel_action, "description"))
		self.assert_(hasattr(self.cancel_action, "endTime"))
		self.assert_(hasattr(self.cancel_action, "image"))
		self.assert_(hasattr(self.cancel_action, "instrument"))
		self.assert_(hasattr(self.cancel_action, "name"))
		self.assert_(hasattr(self.cancel_action, "object"))
		self.assert_(hasattr(self.cancel_action, "participant"))
		self.assert_(hasattr(self.cancel_action, "result"))
		self.assert_(hasattr(self.cancel_action, "sameAs"))
		self.assert_(hasattr(self.cancel_action, "scheduledTime"))
		self.assert_(hasattr(self.cancel_action, "startTime"))
		self.assert_(hasattr(self.cancel_action, "url"))

	def tearDown(self):
		pass


class TestCasino(unittest.TestCase):

	def setUp(self):
		self.casino = Casino()

	def test_init(self):
		self.assertEquals(type(self.casino), Casino)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.casino, "additionalType"))
		self.assert_(hasattr(self.casino, "alternateName"))
		self.assert_(hasattr(self.casino, "branchOf"))
		self.assert_(hasattr(self.casino, "containedIn"))
		self.assert_(hasattr(self.casino, "currenciesAccepted"))
		self.assert_(hasattr(self.casino, "description"))
		self.assert_(hasattr(self.casino, "geo"))
		self.assert_(hasattr(self.casino, "image"))
		self.assert_(hasattr(self.casino, "map"))
		self.assert_(hasattr(self.casino, "maps"))
		self.assert_(hasattr(self.casino, "name"))
		self.assert_(hasattr(self.casino, "openingHoursSpecification"))
		self.assert_(hasattr(self.casino, "paymentAccepted"))
		self.assert_(hasattr(self.casino, "photo"))
		self.assert_(hasattr(self.casino, "photos"))
		self.assert_(hasattr(self.casino, "priceRange"))
		self.assert_(hasattr(self.casino, "sameAs"))
		self.assert_(hasattr(self.casino, "url"))

	def tearDown(self):
		pass


class TestCatholicChurch(unittest.TestCase):

	def setUp(self):
		self.catholic_church = CatholicChurch()

	def test_init(self):
		self.assertEquals(type(self.catholic_church), CatholicChurch)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.catholic_church, "additionalType"))
		self.assert_(hasattr(self.catholic_church, "alternateName"))
		self.assert_(hasattr(self.catholic_church, "containedIn"))
		self.assert_(hasattr(self.catholic_church, "description"))
		self.assert_(hasattr(self.catholic_church, "geo"))
		self.assert_(hasattr(self.catholic_church, "image"))
		self.assert_(hasattr(self.catholic_church, "map"))
		self.assert_(hasattr(self.catholic_church, "maps"))
		self.assert_(hasattr(self.catholic_church, "name"))
		self.assert_(hasattr(self.catholic_church, "openingHoursSpecification"))
		self.assert_(hasattr(self.catholic_church, "photo"))
		self.assert_(hasattr(self.catholic_church, "photos"))
		self.assert_(hasattr(self.catholic_church, "sameAs"))
		self.assert_(hasattr(self.catholic_church, "url"))

	def tearDown(self):
		pass


class TestCemetery(unittest.TestCase):

	def setUp(self):
		self.cemetery = Cemetery()

	def test_init(self):
		self.assertEquals(type(self.cemetery), Cemetery)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.cemetery, "additionalType"))
		self.assert_(hasattr(self.cemetery, "alternateName"))
		self.assert_(hasattr(self.cemetery, "containedIn"))
		self.assert_(hasattr(self.cemetery, "description"))
		self.assert_(hasattr(self.cemetery, "geo"))
		self.assert_(hasattr(self.cemetery, "image"))
		self.assert_(hasattr(self.cemetery, "map"))
		self.assert_(hasattr(self.cemetery, "maps"))
		self.assert_(hasattr(self.cemetery, "name"))
		self.assert_(hasattr(self.cemetery, "openingHoursSpecification"))
		self.assert_(hasattr(self.cemetery, "photo"))
		self.assert_(hasattr(self.cemetery, "photos"))
		self.assert_(hasattr(self.cemetery, "sameAs"))
		self.assert_(hasattr(self.cemetery, "url"))

	def tearDown(self):
		pass


class TestCheckAction(unittest.TestCase):

	def setUp(self):
		self.check_action = CheckAction()

	def test_init(self):
		self.assertEquals(type(self.check_action), CheckAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.check_action, "additionalType"))
		self.assert_(hasattr(self.check_action, "agent"))
		self.assert_(hasattr(self.check_action, "alternateName"))
		self.assert_(hasattr(self.check_action, "description"))
		self.assert_(hasattr(self.check_action, "endTime"))
		self.assert_(hasattr(self.check_action, "image"))
		self.assert_(hasattr(self.check_action, "instrument"))
		self.assert_(hasattr(self.check_action, "name"))
		self.assert_(hasattr(self.check_action, "object"))
		self.assert_(hasattr(self.check_action, "participant"))
		self.assert_(hasattr(self.check_action, "result"))
		self.assert_(hasattr(self.check_action, "sameAs"))
		self.assert_(hasattr(self.check_action, "startTime"))
		self.assert_(hasattr(self.check_action, "url"))

	def tearDown(self):
		pass


class TestCheckInAction(unittest.TestCase):

	def setUp(self):
		self.check_in_action = CheckInAction()

	def test_init(self):
		self.assertEquals(type(self.check_in_action), CheckInAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.check_in_action, "additionalType"))
		self.assert_(hasattr(self.check_in_action, "agent"))
		self.assert_(hasattr(self.check_in_action, "alternateName"))
		self.assert_(hasattr(self.check_in_action, "description"))
		self.assert_(hasattr(self.check_in_action, "endTime"))
		self.assert_(hasattr(self.check_in_action, "image"))
		self.assert_(hasattr(self.check_in_action, "instrument"))
		self.assert_(hasattr(self.check_in_action, "name"))
		self.assert_(hasattr(self.check_in_action, "object"))
		self.assert_(hasattr(self.check_in_action, "participant"))
		self.assert_(hasattr(self.check_in_action, "result"))
		self.assert_(hasattr(self.check_in_action, "sameAs"))
		self.assert_(hasattr(self.check_in_action, "startTime"))
		self.assert_(hasattr(self.check_in_action, "url"))

	def tearDown(self):
		pass


class TestCheckOutAction(unittest.TestCase):

	def setUp(self):
		self.check_out_action = CheckOutAction()

	def test_init(self):
		self.assertEquals(type(self.check_out_action), CheckOutAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.check_out_action, "additionalType"))
		self.assert_(hasattr(self.check_out_action, "agent"))
		self.assert_(hasattr(self.check_out_action, "alternateName"))
		self.assert_(hasattr(self.check_out_action, "description"))
		self.assert_(hasattr(self.check_out_action, "endTime"))
		self.assert_(hasattr(self.check_out_action, "image"))
		self.assert_(hasattr(self.check_out_action, "instrument"))
		self.assert_(hasattr(self.check_out_action, "name"))
		self.assert_(hasattr(self.check_out_action, "object"))
		self.assert_(hasattr(self.check_out_action, "participant"))
		self.assert_(hasattr(self.check_out_action, "result"))
		self.assert_(hasattr(self.check_out_action, "sameAs"))
		self.assert_(hasattr(self.check_out_action, "startTime"))
		self.assert_(hasattr(self.check_out_action, "url"))

	def tearDown(self):
		pass


class TestCheckoutPage(unittest.TestCase):

	def setUp(self):
		self.checkout_page = CheckoutPage()

	def test_init(self):
		self.assertEquals(type(self.checkout_page), CheckoutPage)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.checkout_page, "accessibilityAPI"))
		self.assert_(hasattr(self.checkout_page, "accessibilityControl"))
		self.assert_(hasattr(self.checkout_page, "accessibilityFeature"))
		self.assert_(hasattr(self.checkout_page, "accessibilityHazard"))
		self.assert_(hasattr(self.checkout_page, "accountablePerson"))
		self.assert_(hasattr(self.checkout_page, "additionalType"))
		self.assert_(hasattr(self.checkout_page, "alternateName"))
		self.assert_(hasattr(self.checkout_page, "alternativeHeadline"))
		self.assert_(hasattr(self.checkout_page, "associatedMedia"))
		self.assert_(hasattr(self.checkout_page, "audio"))
		self.assert_(hasattr(self.checkout_page, "author"))
		self.assert_(hasattr(self.checkout_page, "breadcrumb"))
		self.assert_(hasattr(self.checkout_page, "citation"))
		self.assert_(hasattr(self.checkout_page, "comment"))
		self.assert_(hasattr(self.checkout_page, "contentLocation"))
		self.assert_(hasattr(self.checkout_page, "contentRating"))
		self.assert_(hasattr(self.checkout_page, "contributor"))
		self.assert_(hasattr(self.checkout_page, "copyrightHolder"))
		self.assert_(hasattr(self.checkout_page, "copyrightYear"))
		self.assert_(hasattr(self.checkout_page, "dateCreated"))
		self.assert_(hasattr(self.checkout_page, "dateModified"))
		self.assert_(hasattr(self.checkout_page, "datePublished"))
		self.assert_(hasattr(self.checkout_page, "description"))
		self.assert_(hasattr(self.checkout_page, "discussionUrl"))
		self.assert_(hasattr(self.checkout_page, "editor"))
		self.assert_(hasattr(self.checkout_page, "educationalAlignment"))
		self.assert_(hasattr(self.checkout_page, "educationalUse"))
		self.assert_(hasattr(self.checkout_page, "encoding"))
		self.assert_(hasattr(self.checkout_page, "encodings"))
		self.assert_(hasattr(self.checkout_page, "genre"))
		self.assert_(hasattr(self.checkout_page, "headline"))
		self.assert_(hasattr(self.checkout_page, "image"))
		self.assert_(hasattr(self.checkout_page, "inLanguage"))
		self.assert_(hasattr(self.checkout_page, "interactivityType"))
		self.assert_(hasattr(self.checkout_page, "isBasedOnUrl"))
		self.assert_(hasattr(self.checkout_page, "isFamilyFriendly"))
		self.assert_(hasattr(self.checkout_page, "isPartOf"))
		self.assert_(hasattr(self.checkout_page, "keywords"))
		self.assert_(hasattr(self.checkout_page, "lastReviewed"))
		self.assert_(hasattr(self.checkout_page, "learningResourceType"))
		self.assert_(hasattr(self.checkout_page, "mainContentOfPage"))
		self.assert_(hasattr(self.checkout_page, "mentions"))
		self.assert_(hasattr(self.checkout_page, "name"))
		self.assert_(hasattr(self.checkout_page, "primaryImageOfPage"))
		self.assert_(hasattr(self.checkout_page, "publisher"))
		self.assert_(hasattr(self.checkout_page, "publishingPrinciples"))
		self.assert_(hasattr(self.checkout_page, "relatedLink"))
		self.assert_(hasattr(self.checkout_page, "reviewedBy"))
		self.assert_(hasattr(self.checkout_page, "sameAs"))
		self.assert_(hasattr(self.checkout_page, "significantLink"))
		self.assert_(hasattr(self.checkout_page, "significantLinks"))
		self.assert_(hasattr(self.checkout_page, "sourceOrganization"))
		self.assert_(hasattr(self.checkout_page, "specialty"))
		self.assert_(hasattr(self.checkout_page, "text"))
		self.assert_(hasattr(self.checkout_page, "thumbnailUrl"))
		self.assert_(hasattr(self.checkout_page, "timeRequired"))
		self.assert_(hasattr(self.checkout_page, "url"))
		self.assert_(hasattr(self.checkout_page, "version"))
		self.assert_(hasattr(self.checkout_page, "video"))

	def tearDown(self):
		pass


class TestChildCare(unittest.TestCase):

	def setUp(self):
		self.child_care = ChildCare()

	def test_init(self):
		self.assertEquals(type(self.child_care), ChildCare)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.child_care, "additionalType"))
		self.assert_(hasattr(self.child_care, "alternateName"))
		self.assert_(hasattr(self.child_care, "branchOf"))
		self.assert_(hasattr(self.child_care, "containedIn"))
		self.assert_(hasattr(self.child_care, "currenciesAccepted"))
		self.assert_(hasattr(self.child_care, "description"))
		self.assert_(hasattr(self.child_care, "geo"))
		self.assert_(hasattr(self.child_care, "image"))
		self.assert_(hasattr(self.child_care, "map"))
		self.assert_(hasattr(self.child_care, "maps"))
		self.assert_(hasattr(self.child_care, "name"))
		self.assert_(hasattr(self.child_care, "openingHoursSpecification"))
		self.assert_(hasattr(self.child_care, "paymentAccepted"))
		self.assert_(hasattr(self.child_care, "photo"))
		self.assert_(hasattr(self.child_care, "photos"))
		self.assert_(hasattr(self.child_care, "priceRange"))
		self.assert_(hasattr(self.child_care, "sameAs"))
		self.assert_(hasattr(self.child_care, "url"))

	def tearDown(self):
		pass


class TestChildrensEvent(unittest.TestCase):

	def setUp(self):
		self.childrens_event = ChildrensEvent()

	def test_init(self):
		self.assertEquals(type(self.childrens_event), ChildrensEvent)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.childrens_event, "additionalType"))
		self.assert_(hasattr(self.childrens_event, "alternateName"))
		self.assert_(hasattr(self.childrens_event, "attendee"))
		self.assert_(hasattr(self.childrens_event, "attendees"))
		self.assert_(hasattr(self.childrens_event, "description"))
		self.assert_(hasattr(self.childrens_event, "doorTime"))
		self.assert_(hasattr(self.childrens_event, "eventStatus"))
		self.assert_(hasattr(self.childrens_event, "image"))
		self.assert_(hasattr(self.childrens_event, "name"))
		self.assert_(hasattr(self.childrens_event, "performer"))
		self.assert_(hasattr(self.childrens_event, "performers"))
		self.assert_(hasattr(self.childrens_event, "previousStartDate"))
		self.assert_(hasattr(self.childrens_event, "sameAs"))
		self.assert_(hasattr(self.childrens_event, "subEvent"))
		self.assert_(hasattr(self.childrens_event, "subEvents"))
		self.assert_(hasattr(self.childrens_event, "superEvent"))
		self.assert_(hasattr(self.childrens_event, "url"))

	def tearDown(self):
		pass


class TestChooseAction(unittest.TestCase):

	def setUp(self):
		self.choose_action = ChooseAction()

	def test_init(self):
		self.assertEquals(type(self.choose_action), ChooseAction)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.choose_action, "additionalType"))
		self.assert_(hasattr(self.choose_action, "agent"))
		self.assert_(hasattr(self.choose_action, "alternateName"))
		self.assert_(hasattr(self.choose_action, "description"))
		self.assert_(hasattr(self.choose_action, "endTime"))
		self.assert_(hasattr(self.choose_action, "image"))
		self.assert_(hasattr(self.choose_action, "instrument"))
		self.assert_(hasattr(self.choose_action, "name"))
		self.assert_(hasattr(self.choose_action, "object"))
		self.assert_(hasattr(self.choose_action, "option"))
		self.assert_(hasattr(self.choose_action, "participant"))
		self.assert_(hasattr(self.choose_action, "result"))
		self.assert_(hasattr(self.choose_action, "sameAs"))
		self.assert_(hasattr(self.choose_action, "startTime"))
		self.assert_(hasattr(self.choose_action, "url"))

	def tearDown(self):
		pass


class TestChurch(unittest.TestCase):

	def setUp(self):
		self.church = Church()

	def test_init(self):
		self.assertEquals(type(self.church), Church)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.church, "additionalType"))
		self.assert_(hasattr(self.church, "alternateName"))
		self.assert_(hasattr(self.church, "containedIn"))
		self.assert_(hasattr(self.church, "description"))
		self.assert_(hasattr(self.church, "geo"))
		self.assert_(hasattr(self.church, "image"))
		self.assert_(hasattr(self.church, "map"))
		self.assert_(hasattr(self.church, "maps"))
		self.assert_(hasattr(self.church, "name"))
		self.assert_(hasattr(self.church, "openingHoursSpecification"))
		self.assert_(hasattr(self.church, "photo"))
		self.assert_(hasattr(self.church, "photos"))
		self.assert_(hasattr(self.church, "sameAs"))
		self.assert_(hasattr(self.church, "url"))

	def tearDown(self):
		pass


class TestCity(unittest.TestCase):

	def setUp(self):
		self.city = City()

	def test_init(self):
		self.assertEquals(type(self.city), City)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.city, "additionalType"))
		self.assert_(hasattr(self.city, "alternateName"))
		self.assert_(hasattr(self.city, "containedIn"))
		self.assert_(hasattr(self.city, "description"))
		self.assert_(hasattr(self.city, "geo"))
		self.assert_(hasattr(self.city, "image"))
		self.assert_(hasattr(self.city, "map"))
		self.assert_(hasattr(self.city, "maps"))
		self.assert_(hasattr(self.city, "name"))
		self.assert_(hasattr(self.city, "openingHoursSpecification"))
		self.assert_(hasattr(self.city, "photo"))
		self.assert_(hasattr(self.city, "photos"))
		self.assert_(hasattr(self.city, "sameAs"))
		self.assert_(hasattr(self.city, "url"))

	def tearDown(self):
		pass


class TestCityHall(unittest.TestCase):

	def setUp(self):
		self.city_hall = CityHall()

	def test_init(self):
		self.assertEquals(type(self.city_hall), CityHall)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.city_hall, "additionalType"))
		self.assert_(hasattr(self.city_hall, "alternateName"))
		self.assert_(hasattr(self.city_hall, "containedIn"))
		self.assert_(hasattr(self.city_hall, "description"))
		self.assert_(hasattr(self.city_hall, "geo"))
		self.assert_(hasattr(self.city_hall, "image"))
		self.assert_(hasattr(self.city_hall, "map"))
		self.assert_(hasattr(self.city_hall, "maps"))
		self.assert_(hasattr(self.city_hall, "name"))
		self.assert_(hasattr(self.city_hall, "openingHoursSpecification"))
		self.assert_(hasattr(self.city_hall, "photo"))
		self.assert_(hasattr(self.city_hall, "photos"))
		self.assert_(hasattr(self.city_hall, "sameAs"))
		self.assert_(hasattr(self.city_hall, "url"))

	def tearDown(self):
		pass


class TestCivicStructure(unittest.TestCase):

	def setUp(self):
		self.civic_structure = CivicStructure()

	def test_init(self):
		self.assertEquals(type(self.civic_structure), CivicStructure)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.civic_structure, "additionalType"))
		self.assert_(hasattr(self.civic_structure, "alternateName"))
		self.assert_(hasattr(self.civic_structure, "containedIn"))
		self.assert_(hasattr(self.civic_structure, "description"))
		self.assert_(hasattr(self.civic_structure, "geo"))
		self.assert_(hasattr(self.civic_structure, "image"))
		self.assert_(hasattr(self.civic_structure, "map"))
		self.assert_(hasattr(self.civic_structure, "maps"))
		self.assert_(hasattr(self.civic_structure, "name"))
		self.assert_(hasattr(self.civic_structure, "openingHoursSpecification"))
		self.assert_(hasattr(self.civic_structure, "photo"))
		self.assert_(hasattr(self.civic_structure, "photos"))
		self.assert_(hasattr(self.civic_structure, "sameAs"))
		self.assert_(hasattr(self.civic_structure, "url"))

	def tearDown(self):
		pass



class TestClass(unittest.TestCase):

	def setUp(self):
		self.class_ = Class()

	def test_init(self):
		self.assertEquals(type(self.class_), Class)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.class_, "additionalType"))
		self.assert_(hasattr(self.class_, "alternateName"))
		self.assert_(hasattr(self.class_, "description"))
		self.assert_(hasattr(self.class_, "image"))
		self.assert_(hasattr(self.class_, "name"))
		self.assert_(hasattr(self.class_, "sameAs"))
		self.assert_(hasattr(self.class_, "url"))

	def tearDown(self):
		pass



class TestClip(unittest.TestCase):

	def setUp(self):
		self.clip = Clip()

	def test_init(self):
		self.assertEquals(type(self.clip), Clip)

	def test_rdf_properties(self):
		self.assert_(hasattr(self.clip, "accessibilityAPI"))
		self.assert_(hasattr(self.clip, "accessibilityControl"))
		self.assert_(hasattr(self.clip, "accessibilityFeature"))
		self.assert_(hasattr(self.clip, "accessibilityHazard"))
		self.assert_(hasattr(self.clip, "accountablePerson"))
		self.assert_(hasattr(self.clip, "additionalType"))
		self.assert_(hasattr(self.clip, "alternateName"))
		self.assert_(hasattr(self.clip, "alternativeHeadline"))
		self.assert_(hasattr(self.clip, "associatedMedia"))
		self.assert_(hasattr(self.clip, "audio"))
		self.assert_(hasattr(self.clip, "author"))
		self.assert_(hasattr(self.clip, "citation"))
		self.assert_(hasattr(self.clip, "clipNumber"))
		self.assert_(hasattr(self.clip, "comment"))
		self.assert_(hasattr(self.clip, "contentLocation"))
		self.assert_(hasattr(self.clip, "contentRating"))
		self.assert_(hasattr(self.clip, "contributor"))
		self.assert_(hasattr(self.clip, "copyrightHolder"))
		self.assert_(hasattr(self.clip, "copyrightYear"))
		self.assert_(hasattr(self.clip, "dateCreated"))
		self.assert_(hasattr(self.clip, "dateModified"))
		self.assert_(hasattr(self.clip, "datePublished"))
		self.assert_(hasattr(self.clip, "description"))
		self.assert_(hasattr(self.clip, "discussionUrl"))
		self.assert_(hasattr(self.clip, "editor"))
		self.assert_(hasattr(self.clip, "educationalAlignment"))
		self.assert_(hasattr(self.clip, "educationalUse"))
		self.assert_(hasattr(self.clip, "encoding"))
		self.assert_(hasattr(self.clip, "encodings"))
		self.assert_(hasattr(self.clip, "genre"))
		self.assert_(hasattr(self.clip, "headline"))
		self.assert_(hasattr(self.clip, "image"))
		self.assert_(hasattr(self.clip, "inLanguage"))
		self.assert_(hasattr(self.clip, "interactivityType"))
		self.assert_(hasattr(self.clip, "isBasedOnUrl"))
		self.assert_(hasattr(self.clip, "isFamilyFriendly"))
		self.assert_(hasattr(self.clip, "keywords"))
		self.assert_(hasattr(self.clip, "learningResourceType"))
		self.assert_(hasattr(self.clip, "mentions"))
		self.assert_(hasattr(self.clip, "name"))
		self.assert_(hasattr(self.clip, "partOfEpisode"))
		self.assert_(hasattr(self.clip, "publisher"))
		self.assert_(hasattr(self.clip, "publishingPrinciples"))
		self.assert_(hasattr(self.clip, "sameAs"))
		self.assert_(hasattr(self.clip, "sourceOrganization"))
		self.assert_(hasattr(self.clip, "text"))
		self.assert_(hasattr(self.clip, "thumbnailUrl"))
		self.assert_(hasattr(self.clip, "timeRequired"))
		self.assert_(hasattr(self.clip, "url"))
		self.assert_(hasattr(self.clip, "version"))
		self.assert_(hasattr(self.clip, "video"))

	def tearDown(self):
		pass




if __name__ == '__main__':
    unittest.main()