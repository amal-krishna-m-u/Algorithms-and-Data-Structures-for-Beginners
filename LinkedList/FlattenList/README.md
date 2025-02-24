given a linkedlist with next and child pointer, it is not necesseary that a child pointer exists.
flatten the linkedlist .


Node{
	int val
	Node next
	Node child
}



input:
1-2-3-4-5-6-Null
		|
		7-8-9-10-Null
			|
			11-12-13-Null
					|
					14-15-Null


ouput:
1-2-3-7-8-11-14-15-13-9-10-4-5-6


and the implementation I have done is of timecomplexity and spacecomplexity are of O(n) and O(n).
this is a corrected version of the question encountered in a amazon SDE1 interview 


main copy.py is the correct one 



