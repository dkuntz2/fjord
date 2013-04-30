# fjord

fjord is a static site generator based on 
[mynt](https://github.com/Anomareh/mynt) (at least for now).

Basically, there are a few features I think mynt is missing, and I would like to
attempt to implement some of the features I want. That's about all this is...

## What makes fjord different?

fjord is slightly different from mynt in the following aspects:

-   All tags are converted to titlecase.

While that's not a huge number of changes (it's only one...), it's enough for
now. Plus, I'm just sorta hacking this together to give me the features I want.

## Installing

fjord is not yet available from PyPI, but you can install the latest trunk using

    # pip install git+https://github.com/dkuntz2/fjord.git

Alternatively, you can download fjord's repository and run

    $ python2 setup.py build

    # python2 setup.py install



----

# mynt

_Another static site generator?_

With the ever growing population of static site generators, all filling a certain need, I've yet to find one that allows the generation of anything but the simplest of blogs.

That's where mynt comes in, being designed to give you all the features of a CMS with none of the often rigid implementations of those features.


### Install

From PyPI:

    $ pip install mynt

Latest trunk:

    $ pip install git+https://github.com/Anomareh/mynt.git


### Getting started

After installing mynt head on over and give the [quickstart][quickstart] page and [docs][docs] a read.


### Dependencies

+ [houdini.py][houdini]
+ [Jinja2][jinja]
+ [misaka][misaka]
+ [Pygments][pygments]
+ [PyYAML][pyyaml]
+ [watchdog][watchdog]


### Support

If you run into any issues or have any questions, either open an [issue][issues] or hop in #mynt on irc.freenode.net.


[docs]: http://mynt.mirroredwhite.com/
[houdini]: http://python-houdini.61924.nl/
[issues]: https://github.com/Anomareh/mynt/issues
[jinja]: http://jinja.pocoo.org/
[misaka]: http://misaka.61924.nl/
[pygments]: http://pygments.org/
[pyyaml]: http://pyyaml.org/
[quickstart]: http://mynt.mirroredwhite.com/docs/quickstart/
[watchdog]: http://packages.python.org/watchdog/
