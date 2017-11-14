# Python Design Patterns Video

UML Diagrams Explained: https://en.wikipedia.org/wiki/Class_diagram

## Classification of Patterns

Creational Patterns
Structural Patterns
Behavioral Patterns

## Inheritance

Override vs Overload

A parent method is overriden if the subclass re-defines
it in it's own class definition.

A parent method is `overloaded` if the subclass
overrides it and changes the calling signiture.

## Factory Pattern

- Defines an interface for creating an object, but defers
object instantiation to run time.

**NOTE**: A class that just defines empty methods can be considered an interface (by convention) An actual abstract
base class can also be used to explicitly define attributes.

## Abstract Factory

- Provide an interface for creating families of related objects without specifying their concrete classes.
- An extension of the factory pattern.
- Adds another level of abstraction.

Factories should return objects that follow the same interface (a factory shouldn't be responsible for generating objects for multiple interfaces). This is because the caller
can't expect the methods to be the same.

Q: Still need to understand difference between `Abstract Factor` and `Factory` besides the additional layer of abstraction.

## Builder Pattern

Separate the Construction of a complex object from its prepresentation so that the same construction process can create different representations.

FROM: https://sourcemaking.com/design_patterns/builder

> Affords finer control over the construction process. 
> Unlike creational patterns that construct products 
> in one shot, the Builder pattern constructs the 
> product step by step under the control of the "director".

Another good example: https://davidcorne.com/2013/01/21/builder-pattern/#more-680