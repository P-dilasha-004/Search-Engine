from search_one import search_one, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_two import search_two, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_three import keyword_to_titles, title_to_info, search_three, article_length,key_by_author, filter_to_author, filter_out, articles_from_year, display_result
from search_engine_repo.tests.search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles, BASIC, ADVANCED, ADVANCED_TO_QUESTION, article_metadata
from unittest.mock import patch
from unittest import TestCase, main


class TestSearch(TestCase):
    titles = article_titles()
    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):

        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search_one('dog'), expected_dog_search_results)

    def test_search_one(self):

        expected = []
        self.assertEqual(search_one(""), expected)
        self.assertEqual(search_one("  "), expected)
        self.assertEqual(search_one("z"), expected)


        expected = ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)']
        self.assertEqual(search_one("computer"), expected)
        self.assertEqual(search_one("Computer"), expected)
        self.assertEqual(search_one("coMpUter"), expected)
        self.assertEqual(search_one("COMPUTER"), expected)


        expected = ['Edogawa, Tokyo', 'Ken Kennedy (computer scientist)', 'Kevin Cadogan', 'Rock music', 'Black dog (ghost)', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Fiskerton, Lincolnshire', 'Fisk University', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'Tony Kaye (musician)', "Wake Forest Demon Deacons men's soccer"]
        self.assertEqual(search_one("k"), expected)

        expected = ['English folk music (1500–1899)']
        self.assertEqual(search_one("1500"), expected)
        self.assertEqual(search_one(1500), expected)

        expected = ['Mexican dog-faced bat', 'Old-time music', 'Reflection-oriented programming', 'Voice classification in non-classical music', 'Single-board computer', 'List of computer role-playing games']
        self.assertEqual(search_one("-"), expected)


    def test_title_length(self):
        expected = []
        self.assertEqual(title_length(12, []), expected)
        self.assertEqual(title_length(0, self.titles), expected)
        self.assertEqual(title_length(-12, self.titles), expected)

        expected = self.titles
        self.assertEqual(title_length(1000, self.titles), expected)
        
        expected = "Not a valid length"
        self.assertEqual(title_length('1000', self.titles), expected)

        expected = ['Rock music', 'Guide dog', 'Endoglin', 'Sun dog']
        self.assertEqual(title_length(10, self.titles), expected)


        
    def test_article_count(self):
        expected = self.titles
        self.assertEqual(article_count(1000, self.titles), expected)
        self.assertEqual(article_count(len(self.titles), self.titles), expected)
        self.assertEqual(article_count(5, self.titles), expected[:5])


        expected = []
        self.assertEqual(article_count(0, self.titles), expected)
        self.assertEqual(article_count(-9, self.titles), expected)

    def test_random_article(self):
        expected = ''
        self.assertEqual(random_article(1000, self.titles), expected)
        self.assertEqual(random_article(len(self.titles), self.titles), expected)
        self.assertEqual(random_article(3, []), expected)
        self.assertEqual(random_article(-9, self.titles), expected)

        expected = 'Not a valid index'
        self.assertEqual(random_article('sijan', self.titles), expected)

        # get_print
        expected = self.titles[4]
        self.assertEqual(random_article(4, self.titles), expected)
        self.assertEqual(random_article(4.0, self.titles), expected)

    def test_favorite_article(self):
        expected = False
        self.assertEqual(favorite_article('', self.titles), expected)
        self.assertEqual(favorite_article('this is not in the list', self.titles), expected)

        expected = True
        self.assertEqual(favorite_article('Human computer', self.titles), expected)
        self.assertEqual(favorite_article('humaN comPuter', self.titles), expected)
        self.assertEqual(favorite_article('HUMAN COMPUTER', self.titles), expected)
        self.assertEqual(favorite_article('  HUMAN COMPUTER', self.titles), expected)
        self.assertEqual(favorite_article('HUMAN COMPUTER', self.titles), expected)
        self.assertEqual(favorite_article('  HUMAN COMPUTER  ', self.titles), expected)

    def test_multiple_keywords(self):
        expected = self.titles
        self.assertEqual(set(multiple_keywords('', self.titles)), set(expected))

        expected = set(search_two('computer')).union(set(search_two('science')))
        self.assertEqual(set(multiple_keywords('science', search_two('computer'))), expected)
        
        #same keyword
        expected = set(search_two('computer'))
        self.assertEqual(set(multiple_keywords('computer', search_two('computer'))), expected)

        expected = set(search_two('computer'))
        self.assertEqual(set(multiple_keywords('computer', [])), expected)
        
    def test_search_two(self):
        expected_search_music_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['1936 in music', 'RussBot', 1243745950, 23417], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        self.assertEqual(search_two('music'), expected_search_music_results)
        self.assertEqual(search_two('MuSiC'), expected_search_music_results)
        expected_search_music_results = []
        self.assertEqual(search_two(''), expected_search_music_results)
        self.assertEqual(search_two('dilasha'), expected_search_music_results)


    def test_article_length(self):
        expected_results = [['Endogenous cannabinoid', 'Pegship', 1168971903, 26], ['Reflection-oriented programming', 'Nihonjoe', 1143366937, 38], ['Craig Martin (soccer)', 'Mr Jake', 1174203493, 709], ['Lua (programming language)', 'Burna Boy', 1113957128, 0], ['The Hunchback of Notre Dame (musical)', 'Nihonjoe', 1192176615, 42], ['China national soccer team', 'RussBot', 1199103839, 45], ['Register (music)', 'Pegship', 1082665179, 598]]
        self.assertEqual(article_length(1000, article_metadata()), expected_results)
        expected_results = []
        self.assertEqual(article_length(1000, search_two('music')), expected_results)
        self.assertEqual(article_length(-10, article_metadata()), expected_results)
        expected_results = [['Lua (programming language)', 'Burna Boy', 1113957128, 0]]
        self.assertEqual(article_length(0, article_metadata()), expected_results)


    def test_unique_authors(self):
        expected_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['Endogenous cannabinoid', 'Pegship', 1168971903, 26]]
        self.assertEqual(unique_authors(5, article_metadata()), expected_results)
        
        expected_results = []
        self.assertEqual(unique_authors(-10, article_metadata()), expected_results)
        self.assertEqual(unique_authors(5, []), expected_results)
        self.assertEqual(unique_authors(0, article_metadata()), expected_results)
        
        expected_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['Endogenous cannabinoid', 'Pegship', 1168971903, 26], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Human computer', 'Bearcat', 1248275178, 4750], ['Old-time music', 'Nihonjoe', 1124771619, 12755]]
        self.assertEqual(unique_authors(100000, article_metadata()), expected_results)

    def test_most_recent_article(self):
        expected_results = ['Fisk University', 'RussBot', 1263393671, 16246]
        self.assertEqual(most_recent_article(article_metadata()), expected_results)
        
        expected_results = []
        self.assertEqual(most_recent_article([[]]), expected_results)
        self.assertEqual(most_recent_article([]), expected_results)

    def test_favorite_author(self):
        expected_results = True
        self.assertEqual(favorite_author('rUssbOt', search_two('music')), expected_results)
        
        expected_results = False
        self.assertEqual(favorite_author('sijan', search_two('music')), expected_results)

    def test_title_and_author(self):
        expected_results = [('Spain national beach soccer team', 'jack johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')]
        self.assertEqual(title_and_author(search_two('soccer')), expected_results)
        
        expected_results = []
        self.assertEqual(title_and_author(search_two('sijan')), expected_results)

    def test_refine_search(self):
        expected_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Arabic music', 'RussBot', 1209417864, 25114]]
        self.assertEqual(refine_search('pop', search_two('music')), expected_results)
        
        expected_results = []
        self.assertEqual(refine_search('pop', search_two('soccer')), expected_results)

        expected_results = []
        self.assertEqual(refine_search('music', search_two('sijan')), expected_results)
        
    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search_two('dog', dummy_keyword_dict), expected_search_results)


    def test_title_to_info(self):

        metadata = [[]]
        expected_results = {}
        self.assertEqual(title_to_info(metadata), expected_results)

        metadata = [["Group Project", "Harry", 11908347357, 5000], ["", "Madison", 1190834, 3200]]
        expected_results = {"Group Project": {"author": "Harry", "length": 5000, "timestamp": 11908347357}}
        self.assertEqual(title_to_info(metadata), expected_results)

        metadata = [["", "Harry", 11908347357, 5000], ["", "Madison", 1190834, 3200]]
        expected_results = {}
        self.assertEqual(title_to_info(metadata), expected_results)

        metadata = [["Harry Potter", "J.K. Rowling", 11908347357, 5000]]
        expected_results = {"Harry Potter": {"author": "J.K. Rowling", "length": 5000, "timestamp": 11908347357}}
        self.assertEqual(title_to_info(metadata), expected_results)

        metadata = [["Harry Potter", "J.K. Rowling", 11908347357, 5000], ["Blues", "Madison", 1190834, 3200], ["Group Project", "MSD", 567893434, 12000]]
        expected_results = {"Harry Potter": {"author": "J.K. Rowling", "length": 5000, "timestamp": 11908347357}, "Blues": {"author": "Madison", "length": 3200, "timestamp": 1190834}, "Group Project": {"author": "MSD", "length": 12000, "timestamp": 567893434}}
        self.assertEqual(title_to_info(metadata), expected_results)

        metadata = [[12345, "J.K. Rowling", 11908347357, 5000]]
        expected_results = {12345: {"author": "J.K. Rowling", "length": 5000, "timestamp": 11908347357}}
        self.assertEqual(title_to_info(metadata), expected_results)

        metadata = [["Harry Potter", "", 11908347357, 5000]]
        expected_results = {"Harry Potter": {"author": "", "length": 5000, "timestamp": 11908347357}}
        self.assertEqual(title_to_info(metadata), expected_results)

    def test_search_three(self): 

        expected_results = []

        keyword = "Dilasha"
        keyword_to_titles = {}
        self.assertEqual(search_three(keyword, keyword_to_titles), expected_results)

        keyword = ""
        keyword_to_titles = {'Hermione': ["Harry Potter"]} 
        self.assertEqual(search_three(keyword, keyword_to_titles), expected_results)

        keyword = ""
        keyword_to_titles = {}
        self.assertEqual(search_three(keyword, keyword_to_titles), expected_results)

        keyword = "Hermione"
        keyword_to_titles = {'Hermione': []}
        self.assertEqual(search_three(keyword, keyword_to_titles), expected_results)

        keyword = "hermione"
        keyword_to_titles = {'Hermione': []}
        self.assertEqual(search_three(keyword, keyword_to_titles), expected_results)

        expected_results = ["Harry Potter"]
        keyword = "Hermione"
        keyword_to_titles = {'Hermione': ["Harry Potter"]}
        self.assertEqual(search_three(keyword, keyword_to_titles), expected_results)

        expected_results = ["chemistry", "math", "biology"]
        keyword = "Stem"
        keyword_to_titles = {"humanities": ["history", "philosophy", "literature"], "Stem": ["chemistry", "math", "biology"]}
        self.assertEqual(search_three(keyword, keyword_to_titles), expected_results)


    def test_key_by_author(self): 

        expected_results = {}
        article_titles = []
        title_to_info = {'The Kite Runner': {'author': 'Khaled Hosseini', 'timestamp': 12323454545, 'length': 700000}}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_results)
        
        expected_results = {}
        article_titles = ["Harry Potter", "The Book Thief", "Rock Paper Scissors"]
        title_to_info = {}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_results)

        expected_results = {}
        article_titles = []
        title_to_info = {}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_results)

        expected_results = {'Khaled Hosseini': ['The Kite Runner']}
        article_titles = ["The Kite Runner", "Blues"]
        title_to_info = {'The Kite Runner': {'author': 'Khaled Hosseini', 'timestamp': 12323454545, 'length': 700000}}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_results)

        expected_results = {'Khaled Hosseini': ['The Kite Runner'], 'J.K. Rowling': ['Harry Potter']}
        article_titles = ["The Kite Runner", "Harry Potter"]
        title_to_info = {'The Kite Runner': {'author': 'Khaled Hosseini', 'timestamp': 12323454545, 'length': 700000}, "Harry Potter": {"author": "J.K. Rowling", "timestamp": 11908347357, "length": 5000}}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_results)

        expected_results = {'Khaled Hosseini': ['The Kite Runner', 'Thousand Splendid Suns'], 'J.K. Rowling': ['Harry Potter']}
        article_titles = ["The Kite Runner", "Harry Potter", "Thousand Splendid Suns"]
        title_to_info = {'The Kite Runner': {'author': 'Khaled Hosseini', 'timestamp': 12323454545, 'length': 700000}, "Harry Potter": {"author": "J.K. Rowling", "timestamp": 11908347357, "length": 5000}, "Thousand Splendid Suns": {'author': 'Khaled Hosseini', 'timestamp': 12323454545, 'length': 700000}}
        self.assertEqual(key_by_author(article_titles, title_to_info), expected_results)


    def test_filter_out(self): 

        keyword = "Kathmandu"
        keyword_to_titles = {'Nepal': ['History of Nepal', 'Prithvi Narayan Shah'], 'India': ['Kedarnath', 'Badrinath']}
        article_title = []
        expected_results = []
        self.assertEqual(filter_out(keyword, article_title, keyword_to_titles), expected_results)

        keyword = "Nepal"
        keyword_to_titles = {'Nepal': ['History of Nepal']}
        article_title = ['History of Nepal']
        expected_results = [] 
        self.assertEqual(filter_out(keyword, article_title, keyword_to_titles), expected_results)

        keyword = "Kathmandu"
        keyword_to_titles = {}
        article_title = ['History of Nepal', 'Prithvi Narayan Shah', 'Kedarnath']
        expected_results = ['History of Nepal', 'Prithvi Narayan Shah', 'Kedarnath'] 
        self.assertEqual(filter_out(keyword, article_title, keyword_to_titles), expected_results)

        keyword = "Kathmandu"
        keyword_to_titles = {'Nepal': ['History of Nepal', 'Prithvi Narayan Shah'], 'India': ['Kedarnath', 'Badrinath']}
        article_title = ['Hello', 'World']
        expected_results = ['Hello', 'World']
        self.assertEqual(filter_out(keyword, article_title, keyword_to_titles), expected_results)
    
        keyword = "Nepal"
        keyword_to_titles = {'Nepal': ['History of Nepal', 'Prithvi Narayan Shah'], 'India': ['Kedarnath', 'Badrinath']}
        article_title = ['History of Nepal', 'Prithvi Narayan Shah', 'Kedarnath', 'Badrinath']
        expected_results = ['Kedarnath', 'Badrinath']
        self.assertEqual(filter_out(keyword, article_title, keyword_to_titles), expected_results)

        keyword = "Nepal"
        keyword_to_titles = {'Nepal': ['History of Nepal', 'Prithvi Narayan Shah'], 'India': ['Kedarnath', 'Badrinath']}
        article_title = ['History of Nepal', 'Prithvi Narayan Shah', 'Kedarnath']
        expected_results = ['Kedarnath']
        self.assertEqual(filter_out(keyword, article_title, keyword_to_titles), expected_results)

        keyword = "nepal"
        keyword_to_titles = {'Nepal': ['History of Nepal', 'Prithvi Narayan Shah'], 'India': ['Kedarnath', 'Badrinath']}
        article_title = ['History of Nepal', 'Prithvi Narayan Shah', 'Kedarnath', 'Badrinath']
        expected_results = ['History of Nepal', 'Prithvi Narayan Shah', 'Kedarnath', 'Badrinath']
        self.assertEqual(filter_out(keyword, article_title, keyword_to_titles), expected_results)
          
    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_title_length(self, input_mock):
        keyword = 'computer'
        advanced_option = 1
        max_length = 30
    
        output = get_print(input_mock, [keyword, advanced_option, max_length])
        expected_list = set()
      
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(max_length) + '\n'+ "\nHere are your articles: ['Human computer', 'Single-board computer', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'Mode (computer interface)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_number_of_articles(self, input_mock):
        keyword = 'computer'
        advanced_option = 2
        num_articles = 5
  
        output = get_print(input_mock, [keyword, advanced_option, num_articles])
        
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(num_articles) + '\n'+ "\nHere are your articles: ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_random_article(self, input_mock):
        keyword = 'computer'
        advanced_option = 3
        random_index = 4
        
        output = get_print(input_mock, [keyword, advanced_option, random_index])
        
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(random_index) + '\n'+ "\nHere are your articles: Personal computer\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_favorite_article(self, input_mock):
        keyword = 'computer'
        advanced_option = 4
        favorite_article = 'Human Computer'
       
        output = get_print(input_mock, [keyword, advanced_option, favorite_article])
        
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(favorite_article) + '\n'+ "\nHere are your articles: ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)']\nYour favorite article is in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_multiple_keywords(self, input_mock):
        keyword = 'computer'
        advanced_option = 5
        additional_keyword = 'science'
       
        output = get_print(input_mock, [keyword, advanced_option, additional_keyword])
        expected_list = list(set(search_three('computer')).union(set(search_three('science'))))

        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(additional_keyword) + '\n'+ f"\nHere are your articles: {expected_list}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'computer'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
       
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)']\n"

        self.assertEqual(output, expected)
        
    @patch('builtins.input')
    def test_basic_search_int(self, input_mock):
        keyword = 'sijan'
        advanced_option = 7

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"

        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_article_length_int(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_article_length_int(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 0

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_unique_authors_int(self, input_mock):
        keyword = 'soccer'
        advanced_option = 2
        advanced_response = 5

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_most_recent_article_int(self, input_mock):
        keyword = 'soccer'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_favorite_author_int(self, input_mock):
        keyword = 'soccer'
        advanced_option = 4
        advanced_response = 'Mack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\nYour favorite author is in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_title_and_author_int(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option)+ "\nHere are your articles: [('Spain national beach soccer team', 'jack johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_refine_search_int(self, input_mock):
        keyword = 'music'
        advanced_option = 6
        advanced_response = 'pop'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Arabic music', 'RussBot', 1209417864, 25114]]\n"

        self.assertEqual(output, expected)
        
    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_option_one(self,input_mock): 
        keyword = "canada"
        advanced_option = 1
        advanced_response = 500000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'Lights (musician)', 'Old-time music', 'Will Johnson (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_option_two(self, input_mock): 
        keyword = "april"
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Gary King': ['1922 in music'], 'jack johnson': ['1986 in music', 'Alex Turner (musician)'], 'RussBot': ['2009 in music', '1936 in music'], 'Burna Boy': ['Lights (musician)', '2008 in music'], 'Nihonjoe': ['1996 in music'], 'Jack Johnson': ['2006 in music'], 'Bearcat': ['2007 in music']}\n"
       
        self.assertEqual(output, expected)
        
    @patch('builtins.input')
    def test_option_three(self, input_mock): 
        keyword = "may"
        advanced_option = 3
        advanced_response = "Gary King"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['1922 in music']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_option_four(self, input_mock):
        keyword = "blues"
        advanced_option = 4
        advanced_response = "use"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', '2008 in music']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_option_five(self, input_mock):
        keyword = "the"
        advanced_option = 5
        advanced_response = 2007

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', 'List of soul musicians', 'List of overtone musicians', 'Tim Arnold (musician)', '2007 Bulldogs RLFC season', 'Geoff Smith (British musician)', 'B (programming language)', 'Richard Wright (musician)', 'Voice classification in non-classical music', 'Craig Martin (soccer)', 'Alex Turner (musician)', 'List of gospel musicians', 'The Hunchback of Notre Dame (musical)', 'Traditional Thai musical instruments', 'Les Cousins (music club)', '2006 in music', 'Spawning (computer gaming)', 'Ruby (programming language)', 'Mode (computer interface)', '2007 in music']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_option_six(self, input_mock):
        keyword = "cage"
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Noise (music)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_option_seven(self, input_mock):
        keyword = "Pashupatinath"
        advanced_option = 1 
        advanced_response = 300000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected) 

if __name__ == "__main__":
    main()