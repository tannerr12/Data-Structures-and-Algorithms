<h2><a href="https://leetcode.com/problems/minimum-number-of-frogs-croaking/">1419. Minimum Number of Frogs Croaking</a></h2><h3>Medium</h3><hr><div><p>You are given the string <code>croakOfFrogs</code>, which represents a combination of the string <code>"croak"</code> from different frogs, that is, multiple frogs can croak at the same time, so multiple <code>"croak"</code> are mixed.</p>

<p><em>Return the minimum number of </em>different<em> frogs to finish all the croaks in the given string.</em></p>

<p>A valid <code>"croak"</code> means a frog is printing five letters <code>'c'</code>, <code>'r'</code>, <code>'o'</code>, <code>'a'</code>, and <code>'k'</code> <strong>sequentially</strong>. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid <code>"croak"</code> return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> croakOfFrogs = "croakcroak"
<strong>Output:</strong> 1 
<strong>Explanation:</strong> One frog yelling "croak<strong>"</strong> twice.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> croakOfFrogs = "crcoakroak"
<strong>Output:</strong> 2 
<strong>Explanation:</strong> The minimum number of frogs is two. 
The first frog could yell "<strong>cr</strong>c<strong>oak</strong>roak".
The second frog could yell later "cr<strong>c</strong>oak<strong>roak</strong>".
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 3:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> croakOfFrogs = "croakcrook"
<strong>Output:</strong> -1
<strong>Explanation:</strong> The given string is an invalid combination of "croak<strong>"</strong> from different frogs.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= croakOfFrogs.length &lt;= 10<sup>5</sup></code></li>
	<li><code>croakOfFrogs</code> is either <code>'c'</code>, <code>'r'</code>, <code>'o'</code>, <code>'a'</code>, or <code>'k'</code>.</li>
</ul>
</div>