<h2><a href="https://leetcode.com/problems/construct-binary-tree-from-string/">536. Construct Binary Tree from String</a></h2><h3>Medium</h3><hr><div><p>You need to construct a binary tree from a string consisting of parenthesis and integers.</p>

<p>The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.</p>

<p>You always start to construct the <b>left</b> child node of the parent first if it exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/butree.jpg" style="width: 382px; height: 322px;">
<pre style="position: relative;"><strong>Input:</strong> s = "4(2(3)(1))(6(5))"
<strong>Output:</strong> [4,2,6,3,1,5]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> s = "4(2(3)(1))(6(5)(7))"
<strong>Output:</strong> [4,2,6,3,1,5,7]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 3:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> s = "-4(2(3)(1))(6(5)(7))"
<strong>Output:</strong> [-4,2,6,3,1,5,7]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of digits, <code>'('</code>, <code>')'</code>, and <code>'-'</code> only.</li>
</ul>
</div>