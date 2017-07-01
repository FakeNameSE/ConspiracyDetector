
          Reuters- text categorization test collection
                        Distribution .
                       README file (v .)
                         September 

                         David D. Lewis
                      AT&T Labs - Research     
                     lewis@research.att.com

I. Introduction

   This README describes Distribution . of the Reuters- text
categorization test collection, a resource for research in information
retrieval, machine learning, and other corpus-based research.


II. Copyright & Notification 

   The copyright for the text of newswire articles and Reuters
annotations in the Reuters- collection resides with Reuters Ltd.
Reuters Ltd. and Carnegie Group, Inc. have agreed to allow the free
distribution of this data *for research purposes only*.  
   If you publish results based on this data set, please acknowledge
its use, refer to the data set by the name "Reuters-,
Distribution .", and inform your readers of the current location of
the data set (see "Availability & Questions").


III. Availability & Questions

   The Reuters-, Distribution . test collection is available
from David D. Lewis' professional home page, currently:
             http://www.research.att.com/~lewis

Besides this README file, the collection consists of  data files, an
SGML DTD file describing the data file format, and six files
describing the categories used to index the data.  (See Sections VI
and VII for more details.)  Some additional files, which are not part
of the collection but have been contributed by other researchers as
useful resources are also included.  All files are available
uncompressed, and in addition a single gzipped Unix tar archive of the
entire distribution is available as reuters.tar.gz.

   The text categorization mailing list, DDLBETA, is a good place to
send questions about this collection and other text categorization
issues. You may join the list by writing David Lewis at
lewis@research.att.com.


IV. History & Acknowledgements

   The documents in the Reuters- collection appeared on the
Reuters newswire in .  The documents were assembled and indexed
with categories by personnel from Reuters Ltd. (Sam Dobbins, Mike
Topliss, Steve Weinstein) and Carnegie Group, Inc. (Peggy Andersen,
Monica Cellio, Phil Hayes, Laura Knecht, Irene Nirenburg) in .  

In , the documents were made available by Reuters and CGI for
research purposes to the Information Retrieval Laboratory (W.  Bruce
Croft, Director) of the Computer and Information Science Department at
the University of Massachusetts at Amherst.  Formatting of the
documents and production of associated data files was done in  by
David D.  Lewis and Stephen Harding at the Information Retrieval
Laboratory.

Further formatting and data file production was done in  and 
by David D. Lewis and Peter Shoemaker at the Center for Information
and Language Studies, University of Chicago.  This version of the data
was made available for anonymous FTP as "Reuters-, Distribution
." in January . From  through , Distribution . was
hosted at a succession of FTP sites maintained by the Center for
Intelligent Information Retrieval (W. Bruce Croft, Director) of the
Computer Science Department at the University of Massachusetts at
Amherst.

At the ACM SIGIR ' conference in August,  a group of text
categorization researchers discussed how published results on
Reuters- could be made more comparable across studies.  It was
decided that a new version of collection should be produced with less
ambiguous formatting, and including documentation carefully spelling
out standard methods of using the collection.  The opportunity would
also be used to correct a variety of typographical and other errors in
the categorization and formatting of the collection.

Steve Finch and David D. Lewis did this cleanup of the collection
September through November of , relying heavily on Finch's
SGML-tagged version of the collection from an earlier study.  One
result of the re-examination of the collection was the removal of 
documents which were exact duplicates (based on identity of timestamps
down to the second) of other documents in the collection. The new
collection therefore has only , documents, and thus is called the
Reuters- collection.  This README describes version . of this
new collection, which we refer to as "Reuters-, Distribution
.".

In preparing the collection and documentation we have benefited from
discussions with Eric Brown, William Cohen, Fred Damerau, Yoram
Singer, Amit Singhal, and Yiming Yang, among many others.

We thank all the people and organizations listed above for their
efforts and support, without which this collection would not exist.

A variety of other changes were also made in going from Reuters-
to Reuters-:

   . Documents were marked up with SGML tags, and a corresponding
SGML DTD was produced, so that the boundaries of important sections of
documents (e.g. category fields) are unambiguous.
   . The set of categories that are legal for each of the five
controlled vocabulary fields was specified. All category names not
legal for a field were corrected to a legal category, moved to their
appropriate field, or removed, as appropriate.
   . Documents were given new ID numbers, in chronological order, and
are collected  to a file in order by ID (and therefore in order
chronologically). 


V. What is a Text Categorization Test Collection and Who Cares? 

   *Text categorization* is the task of deciding whether a piece of
text belongs to any of a set of prespecified categories.  It is a
generic text processing task useful in indexing documents for later
retrieval, as a stage in natural language processing systems, for
content analysis, and in many other roles [LEWISd].

   The use of standard, widely distributed test collections has been a
considerable aid in the development of algorithms for the related task
of *text retrieval* (finding documents that satisfy a particular
user's information need, usually expressed in an textual request).
Text retrieval test collections have allowed the comparison of
algorithms developed by a variety of researchers around the world.
(For more on text retrieval test collections see SPARCKJONES.)

   Standard test collections have been lacking, however, for text
categorization. Few data sets have been used by more than one
researcher, making results hard to compare.  The Reuters- test
collection has been used in a number of published studies since it was
made available, and we believe that the Reuters- collection will
be even more valuable.

   The collection may also be of interest to researchers in machine
learning, as it provides a classification task with challenging
properties. There are multiple categories, the categories are
overlapping and nonexhaustive, and there are relationships among the
categories.  There are interesting possibilities for the use of domain
knowledge.  There are many possible feature sets that can be extracted
from the text, and most plausible feature/example matrices are large
and sparse.  There is even some temporal structure to the data
[LEWISb], though problems with the indexing and the uneven
distribution of stories within the timespan covered may make this
collection a poor one to explore temporal issues.


VI. Formatting 

     The Reuters- collection is distributed in  files. Each of
the first  files (reut-.sgm through reut-.sgm) contain 
documents, while the last (reut-.sgm) contains  documents.  

     The files are in SGML format.  Rather than going into the details
of the SGML language, we describe here in an informal way how the SGML
tags are used to divide each file, and each document, into sections.
Readers interested in more detail on SGML are encouraged to pursue
one of the many books and web pages on the subject.

     Each of the  files begins with a document type declaration line:
               <!DOCTYPE lewis SYSTEM "lewis.dtd">

The DTD file lewis.dtd is included in the distribution.  Following the
document type declaration line are individual Reuters articles marked
up with SGML tags, as described below.


   VI.A. The REUTERS tag:

    Each article starts with an "open tag" of the form

    <REUTERS TOPICS=?? LEWISSPLIT=?? CGISPLIT=?? OLDID=?? NEWID=??>

where the ?? are filled in an appropriate fashion.  Each article ends
with a "close tag" of the form:

     </REUTERS>

In all cases the <REUTERS> and </REUTERS> tags are the only items
on their line.  

     Each REUTERS tag contains explicit specifications of the values
of five attributes, TOPICS, LEWISSPLIT, CGISPLIT, OLDID, and NEWID.
These attributes are meant to identify documents and groups of 
documents, and have the following meanings: 

     . TOPICS : The possible values are YES, NO, and BYPASS:
        a. YES indicates that *in the original data* there was at
least one entry in the TOPICS fields.
        b. NO indicates that *in the original data* the story had no
entries in the TOPICS field.
        c. BYPASS indicates that *in the original data* the story was
marked with the string "bypass" (or a typographical variant on that
string).
     This poorly-named attribute unfortunately is the subject of much
confusion. It is meant to indicate whether or not the document had
TOPICS categories *in the raw Reuters- dataset*.  The sole use of
this attribute is to defining training set splits similar to those
used in previous research. (See the section on training set splits.)
The TOPICS attribute does **NOT** indicate anything about whether or
not the Reuters- document has any TOPICS categories.  (Version
. of this document was errorful on this point.)  That can be
determined by actually looking at the TOPICS field. A story with
TOPICS="YES" can have no TOPICS categories, and a story with
TOPICS="NO" can have TOPICS categories.
     Now, a reasonable (though not certain) assumption is that for all
TOPICS="YES" stories the indexer at least thought about whether the
story belonged to a valid TOPICS category.  Thus, the TOPICS="YES"
stories with no topics can reasonably be considered negative examples
for all  valid TOPICS categories.
     TOPICS="NO" stories are more problematic in their interpretation.
Some of them presumedly result because the indexer made an explicit
decision that they did not belong to any of the  valid TOPICS
categories.  However, there are many cases where it is clear that a
story should belong to one or more TOPICS categories, but for some
reason the category was not assigned.  There appear to be certain time
intervals where large numbers of such stories are concentrated,
suggesting that some parts of the data set were simply not indexed, or
not indexed for some categories or category sets.  Also, in a few
cases, the indexer clearly meant to assign TOPICS categories, but put
them in the wrong field.  These cases have been corrected in the
Reuters- data, yielding stories that have TOPICS categories, but
where TOPICS="NO", because the the category was not assigned in the
raw version of the data.
     "BYPASS" stories clearly were not indexed, and so are useful only
for general distributional information on the language used in the
documents.

     . LEWISSPLIT : The possible values are TRAINING, TEST, and
NOT-USED.  TRAINING indicates it was used in the training set in the
experiments reported in LEWISd (Chapters  and ), LEWISb,
LEWISe, and LEWISb.  TEST indicates it was used in the test set
for those experiments, and NOT-USED means it was not used in those
experiments.

     . CGISPLIT : The possible values are TRAINING-SET and
PUBLISHED-TESTSET indicating whether the document was in the training
set or the test set for the experiments reported in HAYES and
HAYESb.

     . OLDID : The identification number (ID) the story had in the
Reuters- collection.

     . NEWID : The identification number (ID) the story has in the
Reuters-, Distribution . collection.  These IDs are assigned to
the stories in chronological order.

In addition, some REUTERS tags have a sixth attribute, CSECS, which
can be ignored.  

The use of these attributes is critical to allowing comparability
between different studies with the collection, and is discussed
further in Section VIII.


  VI.B. Document-Internal Tags 

     Just as the <REUTERS> and </REUTERS> tags serve to delimit
documents within a file, other tags are used to delimit elements
within a document.  We discuss these in the order in which they
typically appear, though the exact order should not be relied upon in
processing. In some cases, additional tags occur within an element
delimited by these top level document-internal tags.  These are
discussed in this section as well.

     We specify below whether each open/close tag pair is used exactly
once (ONCE) per a story, or a variable (VARIABLE) number of times
(possibly zero).  In many cases the start tag of a pair appears only
at the beginning of a line, with the corresponding end tag always
appearing at the end of the same line.  When this is the case, we
indicate it with the notation "SAMELINE" below, as an aid to those
processing the files without SGML tools.  

     . <DATE>, </DATE> [ONCE, SAMELINE]: Encloses the date and time
of the document, possibly followed by some non-date noise material.

     . <MKNOTE>, </MKNOTE> [VARIABLE] : Notes on certain hand
corrections that were done to the original Reuters corpus by Steve
Finch.

     . <TOPICS>, </TOPICS> [ONCE, SAMELINE]: Encloses the list of
TOPICS categories, if any, for the document. If TOPICS categories are
present, each will be delimited by the tags <D> and </D>.
     
     . <PLACES>, </PLACES> [ONCE, SAMELINE]: Same as <TOPICS>
but for PLACES categories.

     . <PEOPLE>, </PEOPLE> [ONCE, SAMELINE]: Same as <TOPICS>
but for PEOPLE categories.

     . <ORGS>, </ORGS> [ONCE, SAMELINE]: Same as <TOPICS> but
for ORGS categories.

     . <EXCHANGES>, </EXCHANGES> [ONCE, SAMELINE]: Same as
<TOPICS> but for EXCHANGES categories.

     . <COMPANIES>, </COMPANIES> [ONCE, SAMELINE]: These tags always
appear adjacent to each other, since there are no COMPANIES categories
assigned in the collection.
    
     . <UNKNOWN>, </UNKNOWN> [VARIABLE]: These tags bracket control
characters and other noisy and/or somewhat mysterious material in the
Reuters stories.

     . <TEXT>, </TEXT> [ONCE]: We have attempted to delimit all the
textual material of each story between a pair of these tags.  Some
control characters and other "junk" material may also be included.
The whitespace structure of the text has been preserved. The <TEXT>
tag has the following attribute:

        a. TYPE: This has one of three values: NORM, BRIEF, and
UNPROC.  NORM is the default value and indicates that the text of the
story had a normal structure. In this case the TEXT tag appears simply
as <TEXT>.  The tag appears as <TEXT TYPE="BRIEF"> when the story is a
short one or two line note.  The tags appears as <TEXT TYPE="UNPROC">
when the format of the story is unusual in some fashion that limited
our ability to further structure it.

The following tags optionally delimit elements inside the TEXT
element. Not all stories will have these tags:

        a. <AUTHOR>, </AUTHOR> : Author of the story. 
        b. <DATELINE>, </DATELINE> : Location the story
originated from, and day of the year. 
        c. <TITLE>, </TITLE> : Title of the story. We have attempted
to capture the text of stories with TYPE="BRIEF" within a <TITLE>
element.
        d. <BODY>, </BODY> : The main text of the story.


VII. Categories 

   A test collection for text categorization contains, at minimum, a
set of texts and, for each text, a specification of what categories
that text belongs to.  For the Reuters- collection the documents
are Reuters newswire stories, and the categories are five different
sets of content related categories.  For each document, a human
indexer decided which categories from which sets that document
belonged to.  The category sets are as follows:

              Number of    Number of Categories   Number of Categories 
Category Set  Categories     w/ + Occurrences      w/ + Occurrences  
************  **********   ********************   ******************** 
EXCHANGES                                               
ORGS                                                    
PEOPLE                                               
PLACES                                               
TOPICS                                               


The TOPICS categories are economic subject categories.  Examples
include "coconut", "gold", "inventories", and "money-supply".  This
set of categories is the one that has been used in almost all previous
research with the Reuters data. HAYESb discusses some examples of
the policies (not always obvious) used by the human indexers in
deciding whether a document belonged to a particular TOPIC category.

The EXCHANGES, ORGS, PEOPLE, and PLACES categories correspond to named
entities of the specified type.  Examples include "nasdaq"
(EXCHANGES), "gatt" (ORGS), "perez-de-cuellar" (PEOPLE), and
"australia" (PLACES). Typically a document assigned to a category from
one of these sets explicitly includes some form of the category name
in the document's text. (Something which is usually not true for
TOPICS categories.)  However, not all documents containing a named
entity corresponding to the category name are assigned to these
category, since the entity was required to be a focus of the news
story [HAYESb]. Thus these proper name categories are not as simple
to assign correctly as might be thought.

Reuters-, Distribution . includes five files
(all-exchanges-strings.lc.txt, all-orgs-strings.lc.txt,
all-people-strings.lc.txt, all-places-strings.lc.txt, and
all-topics-strings.lc.txt) which list the names of *all* legal
categories in each set.  A sixth file, cat-descriptions_.txt
gives some additional information on the category sets.

Note that a sixth category field, COMPANIES, was present in the
original Reuters materials distributed by Carnegie Group, but no
company information was actually included in these fields. In the
Reuters- collection this field is always empty.

In the table above we note how many categories appear in at least  of
the , documents in the collection, and how many appear at least
 of the documents.  Many categories appear in no documents, but we
encourage researchers to include these categories when evaluating the
effectiveness of their categorization system. 

Additional details of the documents, categories, and corpus
preparation process appear in LEWISb, and at greater length in
Section . of LEWISd.

VIII. Using Reuters- for Text Categorization Research

     In testing a method for text categorization it is important that
knowledge of the nature of the test data not unduly influence the
development of the system, or the performance obtained will be
unrealistically high.  One way of dealing with this is to divide a set
of data into two subsets: a training set and a test set.  An
experimenter then develops a categorization system by automated
training on the training set only, and/or by human knowledge
engineering based on examination of the training set only.  The
categorization system is then tested on the previously unexamined test
set.  A number of variations on this basic theme are possible---see
WEISS for a good discussion.

     Effectiveness results can only be compared between studies that
the same training and test set (or that use cross-validation
procedures).  One problem with the Reuters- collection was that
the ambiguity of formatting and annotation led different researchers
to use different training/test divisions. This was particularly
problematic when researchers attempted to remove documents that "had
no TOPICS", as there were several definitions of what this meant.

     To eliminate these ambiguities from the Reuters- collection
we specify exactly which articles are in each of the recommended
training sets and test sets by specifying the values those articles
will have on the TOPICS, LEWISSPLIT, and CGISPLIT attributes of the
REUTERS tags.  We strongly encourage that all studies on Reuters-
use one of the following training test divisions (or use multiple
random splits, e.g. cross-validation):

VIII.A. The Modified Lewis ("ModLewis") Split:

 Training Set (, docs): LEWISSPLIT="TRAIN";  TOPICS="YES" or "NO"
 Test Set (, docs):  LEWISSPLIT="TEST"; TOPICS="YES" or "NO"
 Unused (,): LEWISSPLIT="NOT-USED" or TOPICS="BYPASS"

This replaces the / split ( unused) of the Reuters-
collection, which was used in LEWISd (Chapters  and ), LEWISb,
LEWISc, LEWISe, and LEWISb. Note the following:

      . The duplicate documents removed in forming Reuters- are
of course not present. 
      . The documents with TOPICS="BYPASS" are not used, since
subsequent analysis strongly indicates that they were not categorized
by the indexers.  
      . The , unused documents should not be tested on and should
not be used for supervised learning.  However, they may useful as
additional information on the statistical distribution of words,
phrases, and other features that might used to predict categories.

This split assigns documents from April ,  and before to the
training set, and documents from April ,  and after to the test
set.

WARNING: Given the many changes in going from Reuters- to
Reuters-, including correction of many typographical errors in
category labels, results on the ModLewis split cannot be compared
with any published results on the Reuters- collection!


VIII.B. The Modified Apte ("ModApte") Split :

 Training Set (, docs): LEWISSPLIT="TRAIN";  TOPICS="YES"
 Test Set (, docs): LEWISSPLIT="TEST"; TOPICS="YES"
 Unused (, docs):   LEWISSPLIT="NOT-USED"; TOPICS="YES"
                     or TOPICS="NO" 
                     or TOPICS="BYPASS"

This replaces the / split (, not used) of the
Reuters- collection.  These are our best approximation to the
training and test splits used in APTE and APTEb. Note the
following:

      . As with the ModLewis, those documents removed in forming
Reuters- are not present, and BYPASS documents are not used.  
      . The intent in APTE and APTEb was to use the Lewis split,
but restrict it to documents with at least one TOPICS categories.
However, but it was not clear exactly what Apte, et al meant by having
at least one TOPICS category (e.g. how was "bypass" treated, whether
this was before or after any fixing of typographical errors, etc.). We
have encoded our interpretation in the TOPICS attribute.  ***Note
that, as discussed above, some TOPICS="YES" stories have no TOPICS
categories, and a few TOPICS="NO" stories have TOPICS
categories. These facts are irrelevant to the definition of the
split.*** If you are using a learning algorithm that requires each
training document to have at least TOPICS category, you can screen out
the training documents with no TOPICS categories. Please do NOT screen
out any of the , documents - that will make your results
incomparable with other studies.

      . As with ModLewis, it may be desirable to use the , Unused
documents for gathering statistical information about feature
distribution.

As with ModLewis, this split assigns documents from April ,  and
before to the training set, and documents from April ,  and after
to the test set.  The difference is that only documents with at least
one TOPICS category are used.  The rationale for this restriction is
that while some documents lack TOPICS categories because no TOPICS
apply (i.e. the document is a true negative example for all TOPICS
categories), it appears that others simply were never assigned TOPICS
categories by the indexers. (Unfortunately, the amount of time that
has passed since the collection was created has made it difficult to
establish exactly what went on during the indexing.)

WARNING: Given the many changes in going from Reuters- to
Reuters-, including correction of many typographical errors in
category labels, results on the ModApte split cannot be compared
with any published results on the Reuters- collection!


VIII.C. The Modified Hayes ("ModHayes") Split: 
 Training Set ( docs): CGISPLIT="TRAINING-SET"
 Test Set ( docs): CGISPLIT="PUBLISHED-TESTSET"
 Unused ( docs)

This is the best approximation we have to the training and test splits
used in HAYES, HAYESb, and Chapter  of LEWISd.  It replaces the
/ split of the Reuters- collection.  Note the following:

      . As with the other splits, the duplicate documents removed in
forming Reuters- are not present. 

      . "Training" in HAYES and HAYESb was actually done by human
beings looking at the documents and writing categorization rules. 
We can not be sure which of the document files were actually looked
at.  

      . We specify that the BYPASS stories and the TOPICS=NO stories
are part of the training set, since they were used during manual
knowledge engineering in the original Hayes experiments. That does not
mean researchers are obliged to give these stories to, for instance, a
supervised learning algorithm.  As mentioned in the other splits, they
may be more useful for getting distributional information about
features.
 
There are a number of problems with the ModHayes split that make it
less than desirable for text categorization research, including
unusual distribution of categories, pairs of near-duplicate documents,
and chronological burstiness.  (See [LEWISb, Ch. ] for more
details.)

Despite these problems, this split is of interest because it provides
the ability to compare results with those of the CONSTRUE system
[HAYES, HAYESb].  Comparison of results on the ModHayes split with
previously published results on the original Hayes split in HAYES
and HAYESb (and LEWISb, Ch. ) is possible, though the following
points should be taken into account:

   . The testset we provide in the ModHayes split has one fewer
document than the one Hayes used. The document that was removed
(OLDID="") was a timestamp duplicate of the document with
OLDID="" and NEWID="". So in computing effectiveness
measures for comparison with HAYES/b, the document with
NEWID="" should be counted twice.

   . The documents in the Hayes testset had relatively few errors and
anomalies in their categorization. And the errors which we did find
and correct appear unlikely to have affected the original Hayes
results. In particular, it appears that the only errors in the TOPICS
field were the addition of a few invalid categories that were not
evaluated on.  However, for completeness we list the changes in the
Hayes testset documents made going from Reuters- to Reuters-
(all documents are referred to by their NEWID):

   Removal of invalid TOPIC "loan" : , , , , ,
, , , , 

   Removal of invalid TOPIC "gbond" : , 

   Removal of invalid TOPIC "tbill" : 

   Removal of invalid TOPIC "cbond" : 

   Removal of invalid TOPIC "fbond" : 

   Correction of invalid PEOPLE mancera to mancera-aguayo: ,
, , , 

   Correction of invalid PEOPLE andriesssen to andriessen : 

   Correction of invalid PLACES "ivory" and "coast" to single correct
PLACE "ivory-coast": 

    . The effectiveness measures used in HAYES and HAYESb were
somewhat nonstandard. See Ch.  of LEWISd for a discussion.


VIII.D. Other Splits
  
     We strongly encourage researchers to use one (or more) of the
above splits for their experiments (or use cross-validation on one of
the sets of documents defined in the above splits).  We recommend the
Modified Apte ("ModApte") Split for research on predicting the TOPICS
field, since the evidence is that a significant number of documents
that should have TOPICS do not.  The ModLewis split can be used if the
researcher has a strong need to test the ability of a system to deal
with examples belonging to no category. While it is likely that some
of these examples should indeed belong to a category, the ModLewis
split is at least better than the corresponding split from
Reuters-, in that it eliminates the "bypass" stories.

     We in particular encourage you to resist the following
temptations:
     . Defining new splits based on whether or not the documents
actually have any TOPICS categories.  (See the discussion of the
ModApte split.) 
     . Testing your system only on the "easy" categories.  This is a
temptation we have succumbed to in the past, but will resist in the
future.  Yes, we know that some of the  TOPICS categories have few
or no positive training examples or few or no positive test examples
or both.  Yes, purely supervised learning systems will do very badly
on these categories.  Knowledge-based systems, on the other hand,
might do well on them, while doing poorly in comparison with
supervised learning on categories with lots of positive
examples. These comparisons are of great interest.  Of course, it's of
great interest to *in addition* analyze subsets of categories
(e.g. lots of positive examples vs. few positive examples, etc.). 
 
     Note that one strategy we considered and rejected is to assume
that documents which have no TOPICS but do have categories in other
fields (PLACES, etc.) could be assumed to belong to no TOPICS
categories. This does not appear to be a safe assumption - we have
found a number of examples of documents with PLACES but no TOPICS when
there are TOPICS that clearly apply.

IX. Feature Sets in Text Categorization 

   For many text categorization methods, particularly those using
statistical classification techniques, it is convenient to represent
documents not as a sequence of characters, but rather as a tuple of
numeric or binary feature values.  For instance, the value of feature
Fi for a document Dj might be  if the string of characters
"financial" occurred in the document with whitespace on either side,
and  otherwise.  Or the value of Fi for Dj might be the number of
occurrences of "financial" in document Dj.  In information retrieval
such features are often called "indexing terms" and one often speaks
of a term being "present" in a document, to mean that the feature
takes on a non-default value. (Usually, but not always, any value but
 is non-default.)

  Comparisons between text categorization methods that represent
documents as feature tuples are aided by ensuring that the same tuple
representation is used with all methods, thus avoiding conflating
differences in feature extraction with differences in, say, machine
learning methods.  For that reason, the Reuters- distribution
included not only the formatted text of the Reuters stories, but also
feature tuple representations of the stories in each of two feature
sets, one based on words and one based on noun phrases.  Surprisingly,
almost no use was made of these files by other researchers, so we have
not included files of this sort in the Reuters- distribution.

    However, we are willing to make available as part of the
distribution any tuple representations of this sort that researchers
want to contribute. (Contact lewis@research.att.com if you would like
to do this.) Perhaps the ideal situation would be if someone with a
strong interest in feature set formation produced tuples based on a
high quality set of features which other researchers interested only
in learning algorithms could make use of.


X. Bibliography

[This needs to be updated.]

@article{APTE
 ,author = "Chidanand Apt{\'{e}} and Fred Damerau and Sholom M. Weiss"
 ,title = "Automated Learning of Decision Rules for Text Categorization"
 ,journal = "ACM Transactions on Information Systems"
 ,year = 
 , note = "To appear."
 }

@inproceedings{APTEb
 ,author = "Chidanand Apt{\'{e}} and Fred Damerau and Sholom M. Weiss"
 ,title = "Toward Language Independent Automated Learning of Text Categorization Models"
 ,booktitle = sigir
 ,year = 
 ,note = "To appear."
 }

@inproceedings{HAYES
,author = "Philip J. Hayes and Peggy M. Anderson and Irene B. Nirenburg and 
Linda M. Schmandt"
,title = "{TCS}: A Shell for Content-Based Text Categorization"
,booktitle = "IEEE Conference on Artificial Intelligence Applications"
,year = 
}

@inproceedings{HAYESb
,author = "Philip J. Hayes and Steven P. Weinstein"
,title = "{CONSTRUE/TIS:} A System for Content-Based Indexing of a 
Database of News Stories"
,booktitle = "Second Annual Conference on Innovative Applications of
Artificial Intelligence"
,year = 
}

@incollection{HAYES 
 ,author = "Philip J. Hayes"
 ,title = "Intelligent High-Volume Text Processing using Shallow,
Domain-Specific Techniques" 
 ,booktitle = "Text-Based Intelligent Systems"
 ,publisher = "Lawrence Erlbaum"
 ,address =  "Hillsdale, NJ"
 ,year = 
 ,editor = "Paul S. Jacobs"
}

@inproceedings{LEWISc 
  ,author = "David D. Lewis" 
  ,title = "Evaluating Text Categorization" 
  ,booktitle = "Proceedings of Speech and Natural Language Workshop" 
  ,year =  
  ,month = feb 
  ,organization = "Defense Advanced Research Projects Agency" 
  ,publisher = "Morgan Kaufmann" 
  ,pages = "--" 

}

@phdthesis{LEWISd
,author = "David Dolan Lewis"
,title = "Representation and Learning in Information Retrieval"
,school = "Computer Science Dept.; Univ. of Massachusetts; Amherst, MA "
,year = 
,note = "Technical Report --."
}

@inproceedings{LEWISe
,author = "David D. Lewis"
,title = "Data Extraction as Text Categorization: An Experiment with
the {MUC-} Corpus"
,booktitle = "Proceedings of the Third Message Understanding Evaluation
and Conference"
,year = 
,month = may
,organization = "Defense Advanced Research Projects Agency"
,publisher = "Morgan Kaufmann"
,address = "Los Altos, CA"

}

@inproceedings{LEWISb
 ,author = "David D. Lewis"
 ,title = "An Evaluation of Phrasal and Clustered Representations on a Text
Categorization Task"
 ,booktitle = "Fifteenth Annual International ACM SIGIR Conference on
Research and Development in Information Retrieval"
 ,year = 
 ,pages = "--"
}

@inproceedings{LEWISd 
,author = "David D. Lewis and Richard M. Tong"
,title = "Text Filtering in {MUC-} and {MUC-}"
,booktitle = "Proceedings of the Fourth Message Understanding Conference ({MUC-})"
,year = 
,month = jun
,organization = "Defense Advanced Research Projects Agency"
,publisher = "Morgan Kaufmann"
,address = "Los Altos, CA"
}

@inproceedings{LEWISe
,author = "David D. Lewis" 
,title = "Feature Selection and Feature Extraction for Text Categorization"
,booktitle = "Proceedings of Speech and Natural Language Workshop"
,year = 
,month = feb 
,organization = "Defense Advanced Research Projects Agency"
,publisher = "Morgan Kaufmann"
,pages = "--"
}

@inproceedings{LEWISb
 ,author = "David D. Lewis and Marc Ringuette"
 ,title = "A Comparison of Two Learning Algorithms for Text Categorization"
 ,booktitle = "Symposium on Document Analysis and Information Retrieval"
 ,year = 
 ,organization = "ISRI; Univ. of Nevada, Las Vegas"
 ,address = "Las Vegas, NV"
 ,month = apr
 ,pages = "--"
}

@article{LEWISd
, author       = "David D. Lewis and Philip J. Hayes"
, title        = "Guest Editorial"
, journal      = "ACM Transactions on Information Systems"
, year         =  
, volume       = 
, number       = 
, pages        = ""
, month        = jul
}

@article{SPARCKJONES
,author = "K. {Sparck Jones} and  C. J. {van Rijsbergen}"
,title =  "Information Retrieval Test Collections"
,journal = "Journal of Documentation"
,year = 
,volume = 
,number = 
,pages = "--"
  }

@book{WEISS
 ,author = "Sholom M. Weiss and Casimir A. Kulikowski"
 ,title = "Computer Systems That Learn" 
 ,publisher = "Morgan Kaufmann"
 ,year = 
 ,address = "San Mateo, CA"
 }




