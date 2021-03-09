# CountingBalls

_What if you had a very, very large set of an unkonwn number n of elements, and you wanted to get an approximation of n using only log(log(n)) space in memory? Seems impossible, right?_



## Here's the idea
Imagine you push a ball from the top of the stairs.  
Imagine it has a 1/2 chance to stop falling at every step it encounters.  
<pre>
_O_  
   |__  
      |__  
         |__  
</pre>
If you throw n balls, you can expect half of them to stop at the first step. At the second step, you expect one fourth of the balls, then one eighth, ...  
So if `n = 2^i`, you can expect the ith step to have one ball.  
Therefore, if we look at the last step which has a ball, we can deduce a pretty terrible approximation of n.

Since we only need to store the step number i in memory (instead of n), we'll use up only `log(i) = log(log(n))` bits.
   

Credits : Seth Gilbert, National University of Singapore, for CS5234 Algorithms at Scale.
