#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2016, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.
import unittest

from rdflib import Literal, URIRef

from oc_ocdm import GraphEntity
from oc_ocdm import GraphSet
from oc_ocdm.counter_handler import FilesystemCounterHandler


class TestResponsibleAgent(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.counter_handler = FilesystemCounterHandler("./info_dir/")
        cls.graph_set = GraphSet("http://test/", "context_base", cls.counter_handler, "", wanted_label=False)

    def setUp(self):
        self.graph_set.g = []
        self.ra = self.graph_set.add_ra(self.__class__.__name__)
        self.ar = self.graph_set.add_ar(self.__class__.__name__)

    def test_create_name(self):
        name = "Name"
        result = self.ra.create_name(name)
        self.assertIsNone(result)

        triple = self.ra.res, GraphEntity.name, Literal(name)
        self.assertIn(triple, self.ra.g)

    def test_create_given_name(self):
        given_name = "GivenName"
        result = self.ra.create_given_name(given_name)
        self.assertIsNone(result)

        triple = self.ra.res, GraphEntity.given_name, Literal(given_name)
        self.assertIn(triple, self.ra.g)

    def test_create_family_name(self):
        family_name = "GivenName"
        result = self.ra.create_family_name(family_name)
        self.assertIsNone(result)

        triple = self.ra.res, GraphEntity.family_name, Literal(family_name)
        self.assertIn(triple, self.ra.g)

    def test_has_role(self):
        result = self.ra.has_role(self.ar)
        self.assertIsNone(result)

        triple = self.ar.res, GraphEntity.is_held_by, self.ra.res
        self.assertIn(triple, self.ar.g)

    def test_has_related_agent(self):
        related_agent = URIRef("http://test/RelatedAgent")
        result = self.ra.has_related_agent(related_agent)
        self.assertIsNone(result)

        triple = self.ra.res, GraphEntity.relation, related_agent
        self.assertIn(triple, self.ra.g)


if __name__ == '__main__':
    unittest.main()
