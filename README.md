Python "Either" and "Maybe"
===========================

https://github.com/kennknowles/python-either

This library provides two fundamental near-trivial data structures for Python:

 * `Either` also known as "coproduct", "sum type", "variant", "tagged union", "disjoint union", etc: A value that comes from one of two sets
 * `Maybe` also known as "option" or "Either Nothing": A value that may be missing. (Python has "None" but it does not compose)

Each is ~10 lines, mostly boilerplate, but now they are in one place in a library. 

Further Reading:
----------------

If you are unfamiliar with these concepts, here is some reading from around the web:

Either:

 * [Tagged union (Wikipedia)](http://en.wikipedia.org/wiki/Tagged_union)
 * [Either (Scala)](http://www.scala-lang.org/api/current/scala/Either.html)
 * [Boost.Variant (C++)](http://www.boost.org/doc/libs/1_50_0/doc/html/variant.html)
 * [Data.Either (Haskell)](http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-Either.html)
 * [std.variant (D)](http://dlang.org/phobos/std_variant.html)

Maybe:

 * [Option (Scala)](http://www.scala-lang.org/api/current/scala/Option.html)
 * [Maybe (Java)](https://github.com/npryce/maybe-java)
 * [Maybe pattern (Python recipe)](http://code.activestate.com/recipes/577248-maybe-pattern/)
 * [Data.Maybe (Haskell)](http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-Maybe.html)
 * [Maybe (Ruby)](https://github.com/bhb/maybe)


Contributors
------------

 * [Kenn Knowles](https://github.com/kennknowles) ([@kennknowles](https://twitter.com/KennKnowles))


Copyright and License
---------------------

Copyright 2012- Kenneth Knowles

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
