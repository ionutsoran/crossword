"""
Copyright Ionut Soran 2021. ALL RIGHTS RESERVED.
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
"""
from src.components.crossword import Crossword
import pytest


class TestCrossword:

    @classmethod
    def get_offset_dictionary(cls, candidate, adjectives):
        return [{"letter": x.upper(), "word": adjectives[idx].upper(), "offset": 0} for idx, x in enumerate(candidate)]

    @pytest.mark.parametrize("candidate", ["Narcis"])
    @pytest.mark.parametrize("adjectives", [["Ingenios", "Amuzant", "Creativ", "Corect", "Prietenos", "Sincer"]])
    @pytest.mark.parametrize("crossword_args", [{"cw_image": None, "cell_x": 90, "cell_y": 90}])
    def test_case_narcis(self, mocker, candidate, adjectives, crossword_args):
        mocker.patch('src.components.crossword.Crossword._get_input_from_user', return_value=None)

        crossword = Crossword(**crossword_args)
        mocker.patch.object(crossword, '_main_candidate', new=candidate)
        mocker.patch.object(crossword, '_offset_dictionary', new=self.get_offset_dictionary(candidate, adjectives))

        crossword.run()

    @pytest.mark.parametrize("candidate", ["Alexia"])
    @pytest.mark.parametrize("adjectives",
                             [["Affable", "Sociable", "Sensitive", "Extraordinaire", "Optimistic", "Ambitious"]])
    @pytest.mark.parametrize("crossword_args", [{"cw_image": None, "cell_x": 90, "cell_y": 90}])
    def test_case_alexia(self, mocker, candidate, adjectives, crossword_args):
        mocker.patch('src.components.crossword.Crossword._get_input_from_user', return_value=None)

        crossword = Crossword(**crossword_args)
        mocker.patch.object(crossword, '_main_candidate', new=candidate)
        mocker.patch.object(crossword, '_offset_dictionary', new=self.get_offset_dictionary(candidate, adjectives))

        crossword.run()

    @pytest.mark.parametrize("candidate", ["Haeun"])
    @pytest.mark.parametrize("adjectives", [["Straightforward", "Neat", "Wise", "Mature", "Unique"]])
    @pytest.mark.parametrize("crossword_args", [{"cw_image": None, "cell_x": 90, "cell_y": 90}])
    def test_case_haeun(self, mocker, candidate, adjectives, crossword_args):
        mocker.patch('src.components.crossword.Crossword._get_input_from_user', return_value=None)

        crossword = Crossword(**crossword_args)
        mocker.patch.object(crossword, '_main_candidate', new=candidate)
        mocker.patch.object(crossword, '_offset_dictionary', new=self.get_offset_dictionary(candidate, adjectives))

        crossword.run()

    @pytest.mark.parametrize("candidate", ["Paul"])
    @pytest.mark.parametrize("adjectives", [["Polite", "Versatile", "Prudent", "Tactful"]])
    @pytest.mark.parametrize("crossword_args", [{"cw_image": None, "cell_x": 90, "cell_y": 90}])
    def test_case_paul(self, mocker, candidate, adjectives, crossword_args):
        mocker.patch('src.components.crossword.Crossword._get_input_from_user', return_value=None)

        crossword = Crossword(**crossword_args)
        mocker.patch.object(crossword, '_main_candidate', new=candidate)
        mocker.patch.object(crossword, '_offset_dictionary', new=self.get_offset_dictionary(candidate, adjectives))

        crossword.run()

    @pytest.mark.parametrize("candidate", ["Angelo"])
    @pytest.mark.parametrize("adjectives", [["Cautious", "Frank", "Intelligent", "Relaxed", "Loyal", "Cool"]])
    @pytest.mark.parametrize("crossword_args", [{"cw_image": None, "cell_x": 90, "cell_y": 90}])
    def test_case_angelo(self, mocker, candidate, adjectives, crossword_args):
        mocker.patch('src.components.crossword.Crossword._get_input_from_user', return_value=None)

        crossword = Crossword(**crossword_args)
        mocker.patch.object(crossword, '_main_candidate', new=candidate)
        mocker.patch.object(crossword, '_offset_dictionary', new=self.get_offset_dictionary(candidate, adjectives))

        crossword.run()

    @pytest.mark.parametrize("candidate", ["Sonia"])
    @pytest.mark.parametrize("adjectives", [["Smart", "Ambitious", "Friendly", "Beautiful", "Empath"]])
    @pytest.mark.parametrize("crossword_args", [{"cw_image": None, "cell_x": 90, "cell_y": 90}])
    def test_case_sonia(self, mocker, candidate, adjectives, crossword_args):
        mocker.patch('src.components.crossword.Crossword._get_input_from_user', return_value=None)

        crossword = Crossword(**crossword_args)
        mocker.patch.object(crossword, '_main_candidate', new=candidate)
        mocker.patch.object(crossword, '_offset_dictionary', new=self.get_offset_dictionary(candidate, adjectives))

        crossword.run()

    @pytest.mark.parametrize("candidate", ["Riul"])
    @pytest.mark.parametrize("adjectives", [["Friendly", "Intelligent", "Beautiful", "Loyal"]])
    @pytest.mark.parametrize("crossword_args", [{"cw_image": None, "cell_x": 90, "cell_y": 90}])
    def test_case_riul(self, mocker, candidate, adjectives, crossword_args):
        mocker.patch('src.components.crossword.Crossword._get_input_from_user', return_value=None)

        crossword = Crossword(**crossword_args)
        mocker.patch.object(crossword, '_main_candidate', new=candidate)
        mocker.patch.object(crossword, '_offset_dictionary', new=self.get_offset_dictionary(candidate, adjectives))

        crossword.run()
