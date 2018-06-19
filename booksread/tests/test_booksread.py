import os
from unittest import TestCase


class TestLoadWordsModel(TestCase):
    def test_load_model(self):
        import booksread
        is_loaded = booksread.load()
        self.assertTrue(is_loaded)
    
    def test_WORDS_MODEL_not_loaded(self):
        from collections import Counter
        from booksread import models

        self.assertFalse(len(models.WORDS_MODEL.keys())> 0)

    def test_WORD_PAIRS_MODEL_not_loaded(self):
        from booksread import models
        self.assertFalse(len(models.WORD_TUPLES_MODEL.keys()) > 0)
    