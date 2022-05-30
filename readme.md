#
# **Abmod sequences**

Take the following function

f: N² -\&gt; N; f(a,b)=(a\*b) mod (a+b+1)

We can define the following family of infinite sequences:

g(a,b)(n)= a, if n=0

=b, if n=1

=f(g(a,b)(n-1),g(a,b)(n-2)), if n\&gt;1

In other words, the sequence g(a,b) will start with [a,b] and then every new term is f(x,y), where x and y are the previous 2 terms.

My first idea was (a\*b) mod (a+b), however the case both terms are 0, this will be equivalent to a division by 0, and as such is undefined. Adding the +1 fixes that. You can extend it to all real numbers, if you wish, by defining it as

f(a,b)=(a\*b) mod (|a+b|+1)

However I will focus on natural numbers in this article.

Abmod sequences behave chaotically. At every step the current number can increase up to a+b, best case scenario or down to 0, worst case scenario. All sequences I tested eventually end up in a cycle, however, while seemingly unlikely, it&#39;s theoretically possible for an Abmod sequence to increase forever. Hence I propose the following conjecture:

Abmod conjecture: all Abmod sequences end in a cycle

Why would that be the case? Well consider that we are at the point (a,a). Best case scenario, the next term will be 2\*a. But worst case scenario is not a/2. It can be a/2, a/4, a/8, it can even crash down to 0 (a/infinity). On a log2 scale, at any point it can increase by at most 1, or decrease by any number, and as such it&#39;s fundamentally asymmetrical, and tends to go down. And, assuming from one point it never reaches a value higher than k, it can only end up in a cycle (by the pigeonhole principle).

However, this is not a definitive proof of the conjecture because it assumes abmod sequences behave randomly, while in fact they&#39;re not completely random. And even if the behavior was completely random, this would only show that almost all sequences end up in a cycle (probability 1), but that doesn&#39;t exclude the possibility of such a sequence existing.

This doesn&#39;t seem easy to prove at all. Like Collatz, it&#39;s unclear how much a sequence will go up before it collapses into a cycle. Plus in general the behavior of mod functions is hard to predict, hence they are used in cryptography as an one way function. Just as examples, we can consider some sequences.

g(731,736) does the following steps:

731, 736, 728, 1083, 204, 684, 852, 245, 120, 120, 181, 278, 178, 128, 66, 63, 128

After that, it collapses into a cycle of 0. Here it is graphically (on a log scale):

![](RackMultipart20220530-1-tbwcwd_html_d37951a802833400.png)

Compare that to g(731,737). The sequence is equal to:

731, 737, 1093, 1732, 2482, 3739, 3196, 6052, 2533, 3706, 2338, 2143, 3940, 4912, 622, 5479, 3022, 4144, 2419, 1108, 2500, 1897, 1456, 1690, 2833, 1378, 3562, 2023, 5572, 7288, 6559, 12544, 14272, 24493, 11074, 29482, 40375, 25288, 59128, 34960, 73639, 56440, 129160, 125524, 196795, 213100, 144844, 301105, 234520, 355264, 535255, 534640, 440392, 210040, 557884, 279610, 639025, 322342, 927502, 1176769, 1278718, 734398, 1071136, 1036258, 1980403, 443332, 1894156, 1719520, 3135604, 954580, 3844060, 4404433, 4691110, 5456086, 2679403, 712138, 2815162, 3512695, 2342812, 1268296, 3325465, 3252580, 709486, 1594534, 2198314, 3641158, 3548119, 7098076, 6722308, 7231123, 13771708, 7542916, 8108278, 10366708, 3230275, 12834268, 12620212, 18614527, 17587864, 26083672, 30405004, 15024940, 10187440, 23871169, 31447330, 37366270, 46437379, 27343030, 72702190, 21146584, 21157585, 12048670, 18244366, 12852052, 30689410, 26632615, 6642196, 32687692, 599806, 3451750, 2321044, 5542150, 313810, 2666227, 1305838, 1689850, 891565, 1225258, 1656274, 130447, 190072, 177064, 194092, 165787, 339844, 154732, 326014, 15538, 32989, 30346, 58714, 69739, 55942, 44176, 56515, 49192, 71188, 117187, 76996, 170692, 222892, 380824, 12808, 87289, 2950, 47830, 28882, 55069, 32218, 84442, 17836, 49237, 58324, 8512, 55489, 51610, 40390, 61243, 36478, 97234, 30814, 77974, 85771, 30076, 61180, 34789, 64330, 45010, 34279, 72970, 54130, 75424, 34405, 9310, 3418, 11809, 8962, 19690, 16606, 8764, 6928, 775, 7216, 5992, 5215, 376, 3640, 2860, 2299, 1300, 700, 1546, 1393, 1498, 1582, 547, 574, 940, 220, 142, 22, 154, 25, 70, 22, 52, 19, 52

And then it goes into the following cycle:

52, 79, 16, 16, 25, 22, 22, 34, 7, 28, 16, 43, 28

It can also be pictured graphically

![](RackMultipart20220530-1-tbwcwd_html_949363de2da22ce0.png)

I&#39;ve kinda cheated here a bit, because I searched for the sequence with a,b\&lt;1000 which reaches the biggest number and (731,737) turned out to be the winning one. It reaches a peak of over 72 million, almost 100 thousand times 737.

The cycles &quot;0&quot; and &quot;52, 79, 16, 16, 25, 22, 22, 34, 7, 28, 16, 43, 28&quot;, along with &quot;7,4,4&quot;, seem to be the most common ones. The cycle &quot;1&quot; can be reached by g(1,1), however it cannot be reached in any other way.

Another way to think about it is as a directed graph, in which every pair of 2 numbers has a directed edge to another pair

(a,b) -\&gt; (b,f(a,b))

This is how the directed graph looks like for a and b between 0 and 5

(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0) -\&gt; (0, 0)

NONE -\&gt; (0, 1)

(0, 1) -\&gt; (1, 0)

NONE -\&gt; (0, 2)

(0, 2), (3, 2) -\&gt; (2, 0)

(1, 1) -\&gt; (1, 1)

NONE -\&gt; (0, 3)

(0, 3), (2, 3), (8, 3) -\&gt; (3, 0)

(2, 1) -\&gt; (1, 2)

(1, 2), (5, 2) -\&gt; (2, 2)

(2, 2) -\&gt; (2, 4)

(2, 4) -\&gt; (4, 1)

(4, 1) -\&gt; (1, 4)

(1, 4), (7, 4), (3, 4) -\&gt; (4, 4)

(4, 4) -\&gt; (4, 7)

(4, 7) -\&gt; (7, 4)

(4, 2) -\&gt; (2, 1)

NONE -\&gt; (0, 4)

(0, 4), (5, 4) -\&gt; (4, 0)

(3, 1) -\&gt; (1, 3)

(1, 3) -\&gt; (3, 3)

(3, 3) -\&gt; (3, 2)

NONE -\&gt; (3, 1)

NONE -\&gt; (0, 5)

(0, 5), (4, 5) -\&gt; (5, 0)

NONE -\&gt; (2, 3)

(5, 1) -\&gt; (1, 5)

(1, 5) -\&gt; (5, 5)

(5, 5) -\&gt; (5, 3)

(5, 3) -\&gt; (3, 6)

(3, 6) -\&gt; (6, 8)

(6, 8) -\&gt; (8, 3)

NONE -\&gt; (4, 2)

NONE -\&gt; (5, 1)

NONE -\&gt; (2, 5)

(2, 5) -\&gt; (5, 2)

(4, 3) -\&gt; (3, 4)

NONE -\&gt; (4, 3)

NONE -\&gt; (3, 5)

(3, 5) -\&gt; (5, 6)

(5, 6) -\&gt; (6, 6)

(6, 6) -\&gt; (6, 10)

(6, 10) -\&gt; (10, 9)

(10, 9) -\&gt; (9, 10)

(9, 10) -\&gt; (10, 10)

(10, 10) -\&gt; (10, 16)

(10, 16), (16, 16) -\&gt; (16, 25)

(16, 25) -\&gt; (25, 22)

(25, 22) -\&gt; (22, 22)

(22, 22) -\&gt; (22, 34)

(22, 34) -\&gt; (34, 7)

(34, 7) -\&gt; (7, 28)

(7, 28) -\&gt; (28, 16)

(28, 16) -\&gt; (16, 43)

(16, 43) -\&gt; (43, 28)

(43, 28) -\&gt; (28, 52)

(28, 52) -\&gt; (52, 79)

(52, 79) -\&gt; (79, 16)

(79, 16) -\&gt; (16, 16)

NONE -\&gt; (4, 5)

NONE -\&gt; (5, 4)

The advantages of seeing it this way is that cycles in a sequence are cycles in a graph, and calculations don&#39;t have to be repeated (thus it&#39;s a form of memoization).

It could be that there&#39;s a pattern I&#39;m missing here, but as far as I know it seems that, outside of a few basic rules (f(x,0)=0, f(x,1)=x), it is completely chaotic. I&#39;m curious if anyone could figure other patterns going on.