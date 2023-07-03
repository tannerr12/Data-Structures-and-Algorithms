<h2><a href="https://leetcode.com/problems/number-of-squareful-arrays/">996. Number of Squareful Arrays</a></h2><h3>Hard</h3><hr><div><p>An array is <strong>squareful</strong> if the sum of every pair of adjacent elements is a <strong>perfect square</strong>.</p>

<p>Given an integer array nums, return <em>the number of permutations of </em><code>nums</code><em> that are <strong>squareful</strong></em>.</p>

<p>Two permutations <code>perm1</code> and <code>perm2</code> are different if there is some index <code>i</code> such that <code>perm1[i] != perm2[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> nums = [1,17,8]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [1,8,17] and [17,8,1] are the valid permutations.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> nums = [2,2,2]
<strong>Output:</strong> 1
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 12</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>