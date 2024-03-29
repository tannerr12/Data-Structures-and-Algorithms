<h2><a href="https://leetcode.com/problems/swap-adjacent-in-lr-string/">777. Swap Adjacent in LR String</a></h2><h3>Medium</h3><hr><div><p>In a string composed of <code>'L'</code>, <code>'R'</code>, and <code>'X'</code> characters, like <code>"RXXLRXRXL"</code>, a move consists of either replacing one occurrence of <code>"XL"</code> with <code>"LX"</code>, or replacing one occurrence of <code>"RX"</code> with <code>"XR"</code>. Given the starting string <code>start</code> and the ending string <code>end</code>, return <code>True</code> if and only if there exists a sequence of moves to transform one string to the other.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> start = "RXXLRXRXL", end = "XRLXXRRLX"
<strong>Output:</strong> true
<strong>Explanation:</strong> We can transform start to end following these steps:
RXXLRXRXL -&gt;
XRXLRXRXL -&gt;
XRLXRXRXL -&gt;
XRLXXRRXL -&gt;
XRLXXRRLX
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> start = "X", end = "L"
<strong>Output:</strong> false
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= start.length&nbsp;&lt;= 10<sup>4</sup></code></li>
	<li><code>start.length == end.length</code></li>
	<li>Both <code>start</code> and <code>end</code> will only consist of characters in <code>'L'</code>, <code>'R'</code>, and&nbsp;<code>'X'</code>.</li>
</ul>
</div>