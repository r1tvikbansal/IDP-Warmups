import unittest

import pickling


class Test(unittest.TestCase):

    def test_pickle_matches(self):
        """
        #name(Test that the pickle matches the expected output)
        """
        save_list = ["kiwis", "bananas", "carrots", "capsicum"]
        pickling.save_shopping_list(save_list, "shopping_list.pkl")
        loaded_list = pickling.load_shopping_list("shopping_list.pkl")
        self.assertEqual(save_list, loaded_list,
                         "Loaded list should match the saved")
