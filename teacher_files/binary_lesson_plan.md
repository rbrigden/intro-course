# Binary and Digital Communication #

## Analog Signals ##

Binary is the language of our digital age and few of us, even those with computer science experience, rarely see it in our daily interaction with technology. Before the age of the computer in the early 20th century, radio and other analog forms of communication were developing at a rapid pace. Telephones and radios transmit audio by correlating the intensity of a sound wave to a voltage. Simply put, these changes in voltage formed an ``analog signal``, which could be picked up by a receiver and replicated as audio. An analog signal is any continuous signal with a time varying quantity (frequency, amplitude, etc). Analog signals have many advantages and are still core to many technologies that involve wireless communication, but they also have some serious downsides. If you have ever heard the crackling sound of your car radio or the fuzziness of your television, you will have already seen the issues that arise with analog signal interference, electric noise, and distortion. These signal errors are acceptable when you are trying to listen to a talk show, but become problematic if you are trying to calculate the telemetry of the rocket midflight and the numbers become garbled. 

## Binary ##

``Digital signals`` answer this problem quite elegantly. A digital signal is a series of quantized or discrete values. In more human language, digital signals can only have two states, on or off. These states are represented by the numbers 1 (on) and 0 (off). ``Binary`` is a way in which these digital signals can be transformed into intelligible data. Binary is a base-2 numerical system, meaning that each digit represents a multiple of two. The numbers that we are used to have a one's place, a ten's place and so on. Now imagine if each of those placeholders could only take a 1 or a 0, and each digit represent an ascending multiple of two. 

Take the number 27, for example. In our traditional number system, we think of 27 as having three "ones" and two "tens": 

> 2 * 10 + 7 * 1 = 20 + 7 = 27

 Now, let us try concocting this number in binary. In binary, we think of 27 being composed of one "sixteen", one "eight", one "two", and one "one". Written out, that is: 

> 00011011 = 1 * 16 + 1 * 8 + 1 * 2 + 1 * 1 = 16 + 8 + 2 + 1 = 27

Now hopefully most of that makes sense, but what the heck are those zeroes doing there? Well, those zeroes are placeholders. Just like in our base-10 number system, binary uses zeroes to hold the place of multiples of its base (in the case of binary, this is 2). The digit values of binary start from 1 and progress onwards by multiples of 2.

```
128 64 32 16 8 4 2 1  # first eight digit values of binary
 0  0  0  1  1 0 1 1  # the binary representation of 27, multiply the binary value (1 or 0) by the digit value of each and add to yield the number representation.
```




## Resources ##

[fun binary game](http://britton.disted.camosun.bc.ca/binary.swf)