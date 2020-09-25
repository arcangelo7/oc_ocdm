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

from rdflib import URIRef, Literal

from oc_ocdm.graph_entity import GraphEntity
from oc_ocdm.graph_set import GraphSet


class TestBibliographicReference(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.graph_set = GraphSet("http://test/", "context_base", "./info_dir/info_file_", 0, "", wanted_label=False)

    def setUp(self):
        self.graph_set.g = []
        self.be = self.graph_set.add_be(self.__class__.__name__)
        self.an = self.graph_set.add_an(self.__class__.__name__)

    def test_create_content(self):
        content = "Content"
        result = self.be.create_content(content)
        self.assertTrue(result)

        triple = URIRef(str(self.be)), GraphEntity.has_content, Literal(content)
        self.assertIn(triple, self.be.g)

    def test_create_annotation(self):
        result = self.be._create_annotation(self.an)
        self.assertIsNone(result)

        triple = URIRef(str(self.be)), GraphEntity.has_annotation, URIRef(str(self.an))
        self.assertIn(triple, self.be.g)


if __name__ == '__main__':
    unittest.main()
