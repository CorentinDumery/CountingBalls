# CountingBalls
## Here's the idea
Imagine you push a ball from the top of the stairs.  
Imagine it has a 1/2 chance to stop falling at every step it encounters.  
<pre>
 O  
   |_  
      |_  
         |_  
</pre>
If you throw n balls, you can expect half of them to stop at the first step. At the second step, you expect one fourth of the balls, then one eighth, ...  
So if n = 2^i, you can expect the ith step to have one ball.  
Therefore, if we look at the last step which has a ball, we can deduce a pretty terrible approximation of n.
