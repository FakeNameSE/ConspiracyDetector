# ConspiracyDetector
Crackpot conspiracy theory detection through machine learning
## Requirements:
- Python3
- Sklearn
- tabulate
- nltk (you might need to download some of its data files too)

All of these libraries should be installable through `pip` and if nltk gives you any errors when running this, run `import nltk` and then `nltk.download()` in an interactive python interpreter. Select the most popular packages to download.
## Usage:
Note, if python2 is your default, replace python with python3 for all of these commands:

To train run `python train.py filename.pkl.z training_data/` in the projects root directory with filename being the desired name of your saved model.

To run a prediction: `python predict.py filename.pkl.z test/marx.txt` with filename being the name of your savefile and marx.txt the name of the file you want a prediction on.
### Why no pretrained models?
I did not include a pretrained model for several reasons:
1) Do you really want to load and exeecute a binary file you got from some random person on the internet
2) Because of the nature of pickle and joblib, a saved model would only work on a computer running the same version of sklearn and python
3) It should'nt be to much of a problem seeing as training a new model only takes me a little over two mintues on a laptop from 2007.

## So what is this?
Just as my title says, this weekend project (actually developed over summer break over the course of two weekdays) is a system that uses machine learning to detect conspiracy theories. In other words, I applied the miracles of modern mathematics and computer science to the prickly problem of detecting people who are totally off their rocker, or in the words of the verdict that my machine gives, "bonkers!". If you would like, you can read more about my motivations and the actual development of the project [here](https://ggarrettgrossman.ddns.net/machine%20learning/coding/conspiracy-detector/).
## And what does it actually do?
### What it does...
This state of the art system, trained upon the craziness of the ilk of Alex Jones and David Duke (alongside many others, as well as more rational literature to prevent the machine from gaining too dim a view of humanity if it ever becomes sentient), delivers a verdict of "Bonkers!" or "Not too nuts!" when given a text file as an input.
### What it does not do...
An important caveat is that this system does not detect bias or even fake news (a much tougher problem because it can look pretty similar to reputable news sources). Instead it focuses on the previously (at least to the best of my knowledge) untackled problem of statistically determining if a given piece of text is absolutely nuts (shape-shifting, Jewish, alien lizard nuts).
### Can it do that?
Yes!
This system can scientifically determine based only upon its training and the input text file whether or not that text is a  conspiracy theory. In fact, if you stick around a little longer, I will show you some results, as well as just what exactly a conspiracy theory really is.
## And how does it do any of this?
### Magic!
No, not quite.
### Dark Magic!
Closer, but still not quite accurate.
### Support Vector Machines!
Yep, almost indistinguishable from dark magic, this system is actually powered by math! It uses a support vector machine (SVM), a machine learning model that can be used as a binary classifier, meaning a much fancier spam filter which is capable of assigning new inputs (after training) to one of two categories (so bonkers and not bonkers in this case). My blog post on this project  [here](https://ggarrettgrossman.ddns.net/machine%20learning/coding/conspiracy-detector/) delves a little deeper into the actual mechanics of this process (hint: Thanks to David Duke and his love for Jews and communists, I had to add word stemming among other things to the tokenizaton process to keep this system from jumping every time it heard one of those two words).
## So what constitutes a crazy text?
After each training session, the system extracts the top ten features that you can see here:

`Top 10 most important features:`
<table>
<thead>
<tr><th style="text-align: right;">  Rank</th><th style="text-align: right;">   Weight</th><th>Bonkers   </th><th style="text-align: right;">  Weight</th><th>Fine     </th></tr>
</thead>
<tbody>
<tr><td style="text-align: right;">     1</td><td style="text-align: right;">-1.91936 </td><td>o         </td><td style="text-align: right;">0.964309</td><td>change   </td></tr>
<tr><td style="text-align: right;">     2</td><td style="text-align: right;">-1.21264 </td><td>jew       </td><td style="text-align: right;">0.87151 </td><td>wildlife </td></tr>
<tr><td style="text-align: right;">     3</td><td style="text-align: right;">-1.09732 </td><td>government</td><td style="text-align: right;">0.82531 </td><td>reynard  </td></tr>
<tr><td style="text-align: right;">     4</td><td style="text-align: right;">-1.09311 </td><td>ei        </td><td style="text-align: right;">0.805876</td><td>trump    </td></tr>
<tr><td style="text-align: right;">     5</td><td style="text-align: right;">-1.08023 </td><td>louse     </td><td style="text-align: right;">0.805513</td><td>senator  </td></tr>
<tr><td style="text-align: right;">     6</td><td style="text-align: right;">-1.06831 </td><td>n         </td><td style="text-align: right;">0.773819</td><td>specie   </td></tr>
<tr><td style="text-align: right;">     7</td><td style="text-align: right;">-1.062   </td><td>txt       </td><td style="text-align: right;">0.753482</td><td>â        </td></tr>
<tr><td style="text-align: right;">     8</td><td style="text-align: right;">-1.01539 </td><td>ee        </td><td style="text-align: right;">0.749294</td><td>prince   </td></tr>
<tr><td style="text-align: right;">     9</td><td style="text-align: right;">-0.999346</td><td>obama     </td><td style="text-align: right;">0.719461</td><td>sea      </td></tr>
<tr><td style="text-align: right;">    10</td><td style="text-align: right;">-0.930854</td><td>written   </td><td style="text-align: right;">0.703385</td><td>energy   </td></tr>
<tr><td style="text-align: right;">    11</td><td style="text-align: right;">-0.91092 </td><td>jewish    </td><td style="text-align: right;">0.678142</td><td>place    </td></tr>
<tr><td style="text-align: right;">    12</td><td style="text-align: right;">-0.901538</td><td>magazine  </td><td style="text-align: right;">0.672481</td><td>climate  </td></tr>
<tr><td style="text-align: right;">    13</td><td style="text-align: right;">-0.886269</td><td>medium    </td><td style="text-align: right;">0.670092</td><td>important</td></tr>
<tr><td style="text-align: right;">    14</td><td style="text-align: right;">-0.885437</td><td>american  </td><td style="text-align: right;">0.655379</td><td>point    </td></tr>
<tr><td style="text-align: right;">    15</td><td style="text-align: right;">-0.829171</td><td>right     </td><td style="text-align: right;">0.651944</td><td>section  </td></tr>
<tr><td style="text-align: right;">    16</td><td style="text-align: right;">-0.807909</td><td>st        </td><td style="text-align: right;">0.648213</td><td>photon   </td></tr>
<tr><td style="text-align: right;">    17</td><td style="text-align: right;">-0.7689  </td><td>d         </td><td style="text-align: right;">0.641958</td><td>orofino  </td></tr>
<tr><td style="text-align: right;">    18</td><td style="text-align: right;">-0.761795</td><td>litical   </td><td style="text-align: right;">0.641508</td><td>king     </td></tr>
<tr><td style="text-align: right;">    19</td><td style="text-align: right;">-0.744603</td><td>generator </td><td style="text-align: right;">0.619919</td><td>conflict </td></tr>
<tr><td style="text-align: right;">    20</td><td style="text-align: right;">-0.742536</td><td>freedom   </td><td style="text-align: right;">0.60663 </td><td>himself  </td></tr>
</tbody>
</table>

Now, some weird things come up, mainly on the crazy side, because the input text is still a little dirty despite several attempts to clean it up. However, the system actually works quite well as you can see from its confusion matrix and classification report (from the test set):

	Classification Report:
	             precision    recall  f1-score   support
	
	    bonkers       0.99      0.99      0.99       298
	       fine       0.99      0.99      0.99       303
	
	avg / total       0.99      0.99      0.99       601
	
	
	Confusion Matrix:
	[[294   4]
	 [  4 299]] 

Overall, the top 10 features seem to indicate that a lot of conspiracy theories tend to focus on Jews, Obama, and the Government, as well as on our freedom being taken away, as the words "American" and "freedom" seem to indicate.

## So, can I see it in action?
Of course! I have open sourced the code (duh) and here is a sample result:
`Input classified as:`
<table>
<tbody>
<tr><td>Verdict  </td><td>Not too nuts!      </td></tr>
<tr><td>Certainty</td><td>0.23487657038082999</td></tr>
</tbody>
</table>

This sample corresponds to the *Communist Manifesto*, a text which originally gave me some trouble because while it is not an insane conspiracy theory, the repeated use of the word "communist" was not doing it any favors (the same tokenization modifications I made to deal with David Duke's obsession with Jews also fixed this). 
Also, the certainty does not correspond to a probability, but is actually according to sklearn's documentation the "The confidence score for a sample is the signed distance of that sample to the hyperplane", or in other words a completely useless number that will be the first thing that I will change when I revisit the code.
## How does it perform in the real world?
In addition to the 99% accuracy that you saw above, my ultimate test was seeing if the system could differentiate between a Washington Post article and a [Conservapedia](http://www.conservapedia.com/Main_Page) Article (a Christian fundamentalist version of Wikipedia that among other things believes that Obama is an Islamist Terrorist and that trickle down economics work).
