# word_segmentation

This package provides several word segmenters, each implementing a different algorithm for segmenting a sentence into individual words.  Each segmenter takes as input a string which is a sentence with the spaces removed, and returns a list of words that make up the sentence.

A list of the segmenters and their algorithms are as follows (in implementation order, as each builds on the previous):
* **Max Match Word Segmenter**:  This class uses the maxmatch algorithm described in J&M (p 70 in 2E).  It starts at the beginning of the input, and greedily attempts to find the longest word in the dictionary that matches the sentence start.  It then continues to past the end of the found word to repeat the process until the entire input string is consumed.  This algorithm has bad results for English, but surprisingly, not the worst.  This class gets configured with a dictionary.
* **Greedy Unigram Word Segmenter**:  As with maxmatch, this algorithm starts at the beginning and greedily finds the best match, until the string is consumed.  However, in this case the best match is not the longest word, but the word with the highest frequency in the configured unigram provider.  The results for this algorithm are uniformly terrible, as can be expected.  This class and all the rest until the last get configured with a unigram provider.
* **Globally Optimizing Unigram Word Segmenter**:  This class uses dynamic programming to find the segmentation that will result in the highest total unigram count for all words in the segmentation.  To avoid having small, common words (such as the) overwhelm the entire segmentation, the logs of the frequencies were used instead of the actual frequencies (before that change, the results were pretty bad).  This algorithm still has the limitation that compound words will usually be split, as their components will almost always have higher frequencies than the word itself.
* **Real Word Maximizing Word Segmenter**:  Instead of maximizing unigram frequencies, this class's algorithm merely attempts to maximize the ratio of words in the dictionary to words not in the dictionary.  The results are average, or surprisingly good for how simple the algorithm sounds, though the algorithm and weightings did require some tweaking to work (which took away from its simplicity).
* **Globally Optimizing Word Length Maximizing Unigram Word Segmenter**: This algorithm attempted to work around the compound-word-splitting limitation of the Globally Optimizing Unigram Word Segmenter by rewarding longer words to a ridiculous extent -- the frequency for each word was multiplied by a large power of the length of the word.  This was one of the best algorithms, and the only one of the unigram algorithms to not split 'homework'.  (Thanks to Gregory Olmschenk for this suggestion.)
* **Bigram Word Segmenter**: This algorithm maximizes the probability of the bigrams that make up a segmentation, multiplying the probability by the number of words in the segmentation to make up for the additional fractional multiplications.  This algorithm has the best results overall, but when it fails, it fails horribly.  This class gets configured with both a unigram and a bigram provider.

The tests for each of these algorithms show their results for three sentences, "there", "the table down there", and "THIS IS THE SECOND HOMEWORK OF THE FALL SEMESTER".  In addition, a test over all segmenters shows their overall performance against 100 sentences from Sara Cone Bryant's stories for children.


## Usage
### Prerequisites and required libraries
This package requires python3 to run, and uses numpy, nltk, and pytest. It assumes that the NLTK CMUDict, Brown, and (for testing) Gutenberg corpora have been installed. For more information, see http://www.nltk.org/data.html.

### Running from the command line
To run with the default word segmenter (bigram word segmenter), run `python3 word_segmenter.py <sentence>`.  A specific segmenter can also be specified using the argument `-s <segmenter_name>`.  To see results for all six segmenters, pass the argument `--all`.

For more details, run `python word_segmenter.py --help`.

### Using as a library
All segmentation classes implement the method `segment_words(str)`.  To use a segmenter, create it using the dictionary, unigram provider, and / or bigram provider as listed in the docstrings, and then call `segment_words`.  Default providers are available as part of the package.  For more detail, see sample code in the test and in `word_segmenter.py`. 


## Included files
* `utilities/utilities.py`: methods for binary search and bisecting strings
* `word_segmentation/*_word_segmenter.py`: implementations of the word segmentation algorithms described above
* `word_segmentation/cmu_dictionary.py`: dictionary implementation that implements is_word, used by max_match
* `word_segmentation/[brown_cmu_unigram|brown_bigram]_provider.py`: unigram and bigram providers that implement get_frequency, used by all algorithms other than max_match
* `word_segmentation/test/test_*_word_segmenter.py`: individual tests for the segmenters listed above
* `word_segmentation/test/test_all_word_segmenters.py`: comparative tests for all segmenters, using test sentences from NLTK's Gutenberg corpus.
* `word_segmenter.py`: command line interface for this package
Detailed descriptions of each (non-test) class is provided in the documentation in each file.
