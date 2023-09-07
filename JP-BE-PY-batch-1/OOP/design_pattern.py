"""
Are design patterns exist only in OOP?

Design patterns are primarily associated with Object-Oriented Programming (OOP), but their concepts and principles can be adapted and applied to other programming paradigms as well. While design patterns were popularized in the context of OOP, they address common software design problems and provide reusable solutions that are not limited to OOP alone.

Here's how design patterns can be used in different programming paradigms:

Procedural Programming: Even in procedural languages like C, you can apply some design patterns. For example, the "Singleton" pattern can be implemented in C to ensure that there's only one instance of a global resource.

Functional Programming: Functional programming languages like Haskell or even functional aspects in languages like JavaScript can benefit from certain design patterns. For instance, the "Decorator" pattern can be adapted to functional programming by creating higher-order functions that wrap other functions.

Event-Driven Programming: Design patterns like the "Observer" pattern are commonly used in event-driven programming, where objects (observers) subscribe to events and get notified when those events occur.

Reactive Programming: In reactive programming (e.g., with libraries like RxJava or RxJS), you can apply patterns like "Observer" and "Chain of Responsibility" to handle asynchronous event streams.

Microservices and Distributed Systems: Design patterns like the "Service Registry" and "Circuit Breaker" are used in microservices and distributed systems, which may not always be purely OOP.

Aspect-Oriented Programming (AOP): AOP itself is a design pattern, and it focuses on modularizing cross-cutting concerns (e.g., logging, security) that can span multiple parts of an application. It's not limited to OOP but can be applied in various paradigms.

In summary, while design patterns originated in the context of OOP, their underlying principles and solutions can be adapted and applied to a wide range of programming paradigms and languages. The key is to understand the problem they address and adapt them to the specific characteristics and idioms of the programming paradigm you're working with.
"""



"""
Most Common Design Patterns that student should know about.

Students studying software development and programming should be familiar with a core set of common and widely-used design patterns. These design patterns provide solutions to recurring software design problems and help students write more maintainable, flexible, and scalable code. Here are some of the most important design patterns that students should know:

Singleton Pattern: Ensures a class has only one instance and provides a global point of access to it. Useful for managing shared resources like configuration settings or database connections.

Factory Method Pattern: Defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. It's useful for creating objects with specific behavior while abstracting the object creation process.

Abstract Factory Pattern: Provides an interface for creating families of related or dependent objects without specifying their concrete classes. It's useful for creating complex object structures.

Builder Pattern: Separates the construction of a complex object from its representation. It allows you to create different representations of an object using the same construction process.

Prototype Pattern: Creates new objects by copying an existing object, known as the prototype. It's useful when the cost of creating an object is more expensive or complex than copying an existing one.

Adapter Pattern: Allows the interface of an existing class to be used as another interface. It's useful when you want to make existing classes work with others without modifying their source code.

Decorator Pattern: Attaches additional responsibilities to an object dynamically. It's a flexible alternative to subclassing for extending functionality.

Observer Pattern: Defines a one-to-many dependency between objects, where one object (the subject) maintains a list of its dependents (observers) and notifies them of state changes. It's commonly used in event handling and UI updates.

Strategy Pattern: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows the algorithm to vary independently from clients that use it.

Command Pattern: Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations. It's useful for implementing undo/redo functionality and queuing requests.

State Pattern: Allows an object to alter its behavior when its internal state changes. It encapsulates the different states and their transitions in separate classes.

Composite Pattern: Composes objects into tree structures to represent part-whole hierarchies. It's useful for creating hierarchical structures of objects.

Proxy Pattern: Provides a surrogate or placeholder for another object to control access to it. It's used for various purposes, such as lazy loading, access control, and logging.

Chain of Responsibility Pattern: Passes a request along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain. It's useful for decoupling senders and receivers of requests.

MVC (Model-View-Controller) Pattern: Separates an application into three interconnected components: the model (data and business logic), the view (presentation and UI), and the controller (user input and application flow). It's widely used in GUI-based applications.

These design patterns provide a solid foundation for students to understand and apply software design principles in various programming languages and paradigms. Learning how and when to use these patterns can significantly improve code quality, maintainability, and the ability to tackle complex software design challenges.

"""




"""
All Design Patterns that exists (60)

Singleton Pattern
Factory Method Pattern
Abstract Factory Pattern
Builder Pattern
Prototype Pattern
Adapter Pattern
Bridge Pattern
Composite Pattern
Decorator Pattern
Facade Pattern
Flyweight Pattern
Proxy Pattern
Chain of Responsibility Pattern
Command Pattern
Interpreter Pattern
Iterator Pattern
Mediator Pattern
Memento Pattern
Observer Pattern
State Pattern
Strategy Pattern
Template Method Pattern
Visitor Pattern
MVC (Model-View-Controller) Pattern
MVVM (Model-View-ViewModel) Pattern
Repository Pattern
Data Access Object (DAO) Pattern
Service Locator Pattern
Dependency Injection Pattern
Inversion of Control (IoC) Pattern
Business Delegate Pattern
Front Controller Pattern
Interceptor Pattern
Null Object Pattern
Object Pool Pattern
Prototype Registry Pattern
Twin Pattern
Extension Object Pattern
Chain of Command Pattern
Specification Pattern
Dirty Flag Pattern
Double Checked Locking Pattern
Immutable Object Pattern
Metadata Mapping Pattern
Multiton Pattern
Retry Pattern
Singleton Registry Pattern
Triple Check Locking Pattern
Type Object Pattern
Unit of Work Pattern
Value Object Pattern
Active Object Pattern
Business Process Pattern
Continuation Pattern
Half-Sync/Half-Async Pattern
Layers Pattern
Master-Slave Pattern
Pipes and Filters Pattern
Thread Pool Pattern
Worker Thread Pattern
"""


"""
Is OOP fundamental pillars are enough to teach or should we also teach the design patterns

Teaching inheritance, encapsulation, polymorphism, and abstraction (often referred to as the four fundamental pillars of Object-Oriented Programming, or OOP) is essential for students to understand the basics of OOP and foundational programming concepts. These concepts are fundamental and provide a solid basis for writing object-oriented code.

However, teaching design patterns alongside these fundamental concepts is highly beneficial for several reasons:

Practical Application: Design patterns provide practical solutions to common software design problems. They bridge the gap between theory and real-world software development, helping students see how to apply OOP principles effectively.

Best Practices: Design patterns embody best practices in software design. Students learn how experienced developers have solved problems, leading to more maintainable, scalable, and robust code.

Problem-Solving Skills: Studying design patterns encourages students to think critically and analytically about software design challenges. It promotes problem-solving skills and teaches them how to make informed design decisions.

Communication: Design patterns offer a common vocabulary for developers to discuss and communicate design decisions. When students understand design patterns, they can better collaborate with other developers.

Readability and Reusability: Patterns can make code more readable and maintainable by providing a structured way to organize and extend it. This is valuable in large-scale projects and collaborative environments.

Career Preparation: Knowledge of design patterns is often expected in job interviews for software development positions. Employers value developers who can design and implement solutions using established patterns.

Software Quality: Understanding design patterns can lead to higher-quality software that is easier to test and maintain.

Therefore, while teaching the fundamental OOP concepts is crucial, introducing students to design patterns complements their education by preparing them for real-world software development challenges and industry expectations. However, it's essential to strike a balance and ensure that students have a strong understanding of the basics before diving into more advanced topics like design patterns. The order and depth of teaching these topics may vary depending on the curriculum and the students' skill levels.
"""


"Design Patterns provide solution to the commonly occuring problems in efficient and scalable manner"
"""
Pattern Name
Purpose
Implementation
Example
"""

"""
3 Basic Type of Design Patterns
- Creational
- Structural
- Behavioral
"""

"""
Creational
- SignleTone
- Factory
- Builder
- Prototype
"""

"""
Structural
- Adaptor
- Decorator
- Facade
- Proxy
"""

"""
Behavioral
- Strategy
- Observer
- State
- Chain of responisbility
- Template
- Flyweight
"""

"""
Concurrency Design Pattern
- read/write lock patterns
- thread pool pattern
- etc
"""


"""
Characteristics
- language independent
- created by experts
"""

"""
Design Pattern: Singleton and Factory (Creational Deisng Pattern)

Singleton Pattern 
use to have only one instance of the class. It will not allow creating multiple instances of same class

There is simple way and there are still 3 more ways to achieve the same purpose. For now, we will go with simple one
"""

"""
Factory Pattern
use to create instances of class
FactoryClass will get exposed to dev and dev will use this class to create instance of someother class i.e
DatabaseFactory() can give use the conn instance of mysql, postgress, mongodb etc
by using factoryClass we will not need to import mysql, postgress or mongodb in every modules. We will only import factoryClass module

Factory Class Patterns vs Factory Method Patter


When to use Factory Patterns: Scenarios

Certainly! Here are ten examples where the Factory Design Pattern can be applied:

UI Element Creation: Creating different types of user interface elements, such as buttons, text fields, and checkboxes.

Logging: Generating different types of loggers, like file loggers, database loggers, and console loggers.

Payment Methods: Implementing various payment methods, including credit card, PayPal, and Bitcoin.

Notification Services: Creating notifications for different channels like email, SMS, and push notifications.

Authentication Providers: Handling authentication with different providers like OAuth, LDAP, and custom authentication systems.

Document Generation: Generating documents in various formats, such as PDFs, Word documents, and HTML reports.

Connection Pools: Managing database connection pools for different database systems like MySQL, PostgreSQL, and MongoDB.

Image Processing Filters: Applying different image filters or transformations, like grayscale, sepia, and blur.

Vehicle Manufacturing: Building different types of vehicles like cars, motorcycles, and trucks in an automotive production system.

Notification Subscribers: Creating subscribers for various notification channels, such as email subscribers, SMS subscribers, and webhook subscribers.




Difference between Factory Class Pattern (simple) and Factory Method Pattern (complex)

class Animal:
    def speak(self):
        pass
class Dog(Vehicle):
    def speak(self):
        return "mewo"
class Cat(Vehicle):
    def speak(self):
        return "woof"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "cat":
            return Cat()
        elif animal_type == "dog":
            return Dog()
        else:
            raise ValueError("Invalid Animal type")

# Client code
factory = AnimalFactory()
cat = factory.create_animal("cat")
dog = factory.create_animal("dog")

print(cat.speak())  # Output: Car is moving
print(dog.speak())  # Output: Motorcycle is moving



class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalCreator:
    def create_animal(self):
        pass
class DogCreator(AnimalCreator):
    def create_animal(self):
        return Dog()
class CatCreator(AnimalCreator):
    def create_animal(self):
        return Cat()

# Client code
dog_creator = DogCreator()
cat_creator = CatCreator()

dog = dog_creator.create_animal()
cat = cat_creator.create_animal()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!




Now try to extend both of the above examples by adding a new Animal type "Lion".
in Factory Method Pattern this will go smoothly, without needed to modify any existing code
class Lion(Animal):
    def speak(self):
        return "Roar!"

class LionCreator(AnimalCreator):
    def create_animal(self):
        return Lion()

# Client code
lion_creator = LionCreator()
lion = lion_creator.create_animal()

print(lion.speak())  # Output: Roar!


Benefit of Factory Method Pattern
Open-Closed Principle:
Single Responsibility Principle:


Factory Class Method can also be extending but an if condition also needed to be added in AnimalFactory core logic.
The complexity will grow if we have 100 types then 100 if condition needed to be added.
But
In Factory Method Pattern each type will have their own sub_class as well as sub_creator_class. And for this to work we just need to inherit both class with appropriate class


"""

"""
Design Pattern Proxy and Facade (Structual Deisng Pattern)
Proxy Pattern: It is used when you need to control access to an object, delay its creation, or add additional functionality before or after the underlying object's operations. Common use cases include lazy loading, access control, logging, and caching.
11:23
Facade Pattern: In the Facade Pattern, you have a facade class that provides a higher-level interface to a set of subsystems or interfaces. Clients interact with the facade, which internally communicates with the subsystems.
11:24
Connect TV, Audio and DVD player together is an example of facade
11:28
Yes, you can think of the Facade Pattern as a way to connect and simplify the interactions between multiple components or subsystems using a wrapper class. The main goal of the Facade Pattern is to provide a unified and simplified interface to a complex system or a set of related classes or components.
In essence, the Facade acts as a "facade" or entry point to the subsystems, allowing clients to interact with the system without needing to know the intricate details of how those subsystems work or are connected. It abstracts the complexities and provides a higher-level interface.
So, when you create a wrapper class that connects several components together and presents a simplified interface to clients, you are indeed employing the Facade Pattern to improve the usability and maintainability of your code. This pattern is especially useful when dealing with complex systems or when you want to shield clients from unnecessary intricacies.

"""



"""
Design Pattern: Strategy and Observer (Behavoural Deisng Pattern)








Diff between Factory and Strategy Design Pattern 

Factory Class/Method Design Patterns deals with creational of object
Strategy Design Patterns deals with behaviour

Factory Class/Method Design Patterns deal with how difference classes (that are similar in terms of inheritance) objects are created
Strategy Desgin Patterns deals with how different methods of the class can be added in the class in a way that class is scalable



Question:
lets say we have an example and call it example 1.
We have 2 class, DocumentText and DocumentPDF. When we want to create a pdf we will create an instance from DocumentPDF and for textfile we will create instance from DocumentText.
Here we cannot use strategy pattern since they both class exists separately and therefore we will have to use Factory Method Design Pattern.

now take another example and call it example 2.
We are designing a class where we need to add both behaviour that we can create pdf by calling the method create_pdf and we can create text file by calling the method create_text_file.
In this scenario we shouldn't add 2 methods in this class instead we should use strategy pattern here.

Am I correct in my assumption?

Answer:
Yes, your assumption is correct. The choice between using the Factory Method Design Pattern and the Strategy Design Pattern depends on the specific requirements and context of your design.

In **Example 1**:

- If you have two separate classes, `DocumentText` and `DocumentPDF`, each responsible for creating different types of documents, it makes sense to use the Factory Method Design Pattern. Each class acts as a factory for creating a specific type of object (text or PDF document). You would create instances of `DocumentText` or `DocumentPDF` based on the type of document you need.

In **Example 2**:

- If you have a single class responsible for creating both PDF and text documents and you want to make the choice of which document type to create dynamically, then using the Strategy Design Pattern is a better approach. You can define different strategies (PDF creation strategy and text file creation strategy) and encapsulate them as interchangeable behaviors. The `create_pdf` and `create_text_file` methods can delegate the actual creation logic to the selected strategy.

So, your choice of design pattern should align with the specific requirements and the level of flexibility and extensibility you need in your system. Example 1 represents a case where different classes handle the creation of different types, while Example 2 represents a case where a single class should be flexible in its behavior, making it suitable for the Strategy pattern.


"""
