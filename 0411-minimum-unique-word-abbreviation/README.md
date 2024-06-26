<h2><a href="https://leetcode.com/problems/minimum-unique-word-abbreviation/">411. Minimum Unique Word Abbreviation</a></h2><h3>Hard</h3><hr><div><p>A string can be <strong>abbreviated</strong> by replacing any number of <strong>non-adjacent</strong> substrings with their lengths. For example, a string such as <code>"substitution"</code> could be abbreviated as (but not limited to):</p>

<ul>
	<li><code>"s10n"</code> (<code>"s <u>ubstitutio</u> n"</code>)</li>
	<li><code>"sub4u4"</code> (<code>"sub <u>stit</u> u <u>tion</u>"</code>)</li>
	<li><code>"12"</code> (<code>"<u>substitution</u>"</code>)</li>
	<li><code>"su3i1u2on"</code> (<code>"su <u>bst</u> i <u>t</u> u <u>ti</u> on"</code>)</li>
	<li><code>"substitution"</code> (no substrings replaced)</li>
</ul>

<p>Note that <code>"s55n"</code> (<code>"s <u>ubsti</u> <u>tutio</u> n"</code>) is not a valid abbreviation of <code>"substitution"</code> because the replaced substrings are adjacent.</p>

<p>The <strong>length</strong> of an abbreviation is the number of letters that were not replaced plus the number of substrings that were replaced. For example, the abbreviation <code>"s10n"</code> has a length of <code>3</code> (<code>2</code> letters + <code>1</code> substring) and <code>"su3i1u2on"</code> has a length of <code>9</code> (<code>6</code> letters + <code>3</code> substrings).</p>

<p>Given a target string <code>target</code> and an array of strings <code>dictionary</code>, return <em>an <strong>abbreviation</strong> of </em><code>target</code><em> with the <strong>shortest possible length</strong> such that it is <strong>not an abbreviation</strong> of <strong>any</strong> string in </em><code>dictionary</code><em>. If there are multiple shortest abbreviations, return any of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> target = "apple", dictionary = ["blade"]
<strong>Output:</strong> "a4"
<strong>Explanation:</strong> The shortest abbreviation of "apple" is "5", but this is also an abbreviation of "blade".
The next shortest abbreviations are "a4" and "4e". "4e" is an abbreviation of blade while "a4" is not.
Hence, return "a4".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> target = "apple", dictionary = ["blade","plain","amber"]
<strong>Output:</strong> "1p3"
<strong>Explanation:</strong> "5" is an abbreviation of both "apple" but also every word in the dictionary.
"a4" is an abbreviation of "apple" but also "amber".
"4e" is an abbreviation of "apple" but also "blade".
"1p3", "2p2", and "3l1" are the next shortest abbreviations of "apple".
Since none of them are abbreviations of words in the dictionary, returning any of them is correct.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == target.length</code></li>
	<li><code>n == dictionary.length</code></li>
	<li><code>1 &lt;= m &lt;= 21</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li><code>log<sub>2</sub>(n) + m &lt;= 21</code> if <code>n &gt; 0</code></li>
	<li><code>target</code> and <code>dictionary[i]</code> consist of lowercase English letters.</li>
	<li><code>dictionary</code> does not contain <code>target</code>.</li>
</ul>
</div>