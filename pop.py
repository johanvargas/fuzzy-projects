ó
dGð^c           @   s¥   d  d l  Z  d  d l Z d d d d g Z d d d d	 g Z d d d g Z g  Z g  Z d
   Z d   Z	 d   Z
 d   Z d   Z e d d d	 d g  Z e GHd S(   iÿÿÿÿNt   Mt   Ct   Xt   Is   (VM)t   Dt   Lt   Vc         C   s    t  t |    } | j   | S(   N(   t   listt   strt   reverse(   t   numt   x(    (    s)   /Users/johanvargas/Documents/pylab/pop.pyt   get_num   s    
c         C   s	   | |  S(   N(    (   t   base_positiont   NUMERALS(    (    s)   /Users/johanvargas/Documents/pylab/pop.pyt   get_key   s    c         C   s}   d d d g } d   } x^ t D]V } |  | k r t j |  } t | | d <t | | d <t | |  | d <q q W| S(   sô   
	original on single.py

	Basic version to get fucntionality but not extensible beyond 10,000??
	missing function of using 'key' over later iterations on higher numbers
	plus adding high number(vinculus etc...) symbols to appropriate entries

	c         S   s   |  d k r d S|  d S(   Ni   iþÿÿÿi   (    (   R   (    (    s)   /Users/johanvargas/Documents/pylab/pop.pyt   <lambda>)   t    i    i   i   N(   t   NoneR   t   indext   PENTAS(   t   numeralt   base_post   keyt   lt   nR   (    (    s)   /Users/johanvargas/Documents/pylab/pop.pyt   set_key_test   s    
	c         C   sÆ   |  d k r d S| d | d | d | d | d | d | d | d | d | d | d | d | d | d | d | d | d | d | d | d | d g
 } | t  |   d S(   Ni    t   nullai   i   (   t   int(   t   digitR   t   table(    (    s)   /Users/johanvargas/Documents/pylab/pop.pyR   8   s    c         C   s   t  t d |   } t t  t d |   t  } t j |  t | |  } t j |  | t  |   d k rx d  St |  | d  S(   Ni
   i   (   t   lenR   R   R   t	   containert   appendR   t   convert(   t   lstt   countt   bpt   at   b(    (    s)   /Users/johanvargas/Documents/pylab/pop.pyR"   P   s    
i   (   t   timeitt   randomR   R   R   R   R    t
   container2R   R   R   R   R"   t   t(    (    (    s)   /Users/johanvargas/Documents/pylab/pop.pyt   <module>   s   					