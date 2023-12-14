=================================
good software architect practices
=================================

:date: 2023-10-09 11:49
:tags: software
:slug: software-architect
:summary: notes on software architecture, based on roadmap.sh 
:lang: en
:status: published

.. |ex| replace:: example:

.. contents:: Table of Contents
   :depth: 2
   :backlinks: entry

``Software architects`` design software solutions with high-level decisions from ground up, concerning the tools, platforms, etc that are used, leading engineers in creating the final product (like with full-stack development).          

``Software architecture`` is concerned with context:
1. functional requirements (what should the system do?)
2. non-functional requirements (functionality, reliability, usability, efficiency, maintainability, scalability)
3. restrictions (legal requirements, standards, cost, time-to-market, talent hiring)

Mapping software architecture out allows you to identify potential problem areas ahead of time, but also means that it's vital and a risk to the trajectory of a project.

software architecture practices
-------------------------------
1. keeping documentation of all aspects of architectural design and their interrelationships with other aspects of the projects (including their expected goals/functions)
2. regular checkup system to re-evaluate architecture, whether they achieve purpose, and whether the system itself conforms to the intended architecture type
3. extra systems at every stage of the architecture to maintain quality assurance of the system's tasks, goals, and outputs

levels of architecture
----------------------
* application level = detailed and lowest level design, focused on one single application, communication within one dev team
* solution level = some high but mainly low-level design. Focus on one/more application(s) that fulfill business needs, with communication between multiple dev teams
* enterprise level = highest level of architecture, focused on multiple solutions. High level design requiring application architects, with communication across organisation

Krucheten's 4+1 Model
'''''''''''''''''''''
describes architecture of software-based systems, allows us to describe system from perspective of different stakeholders. The development (programmer's perspective, focused on software management and domain UML diagrams), logical (functionality provided to end users and system behaviours), physical (topology/distribution of software effects on physical layer and their interconnectivity), and process (communication/control flow concurrency/data flow across system processes) views, with the plus one scenarios (use cases to start off system testing, verify that system meets stakeholder requirements). 

Unified Modeling Language
-------------------------
``UML`` is commonly used standardised modeling language used to provide visually representation notation of software system design and structure. It describes the static system structure through object attributes and relationships as well as diagrams that show object collaboration and state changes which illustrate the dynamic behaviour of the system. A subset of behaviour diagrams are interaction diagrams which focuses on the flow of control and data as sequence or communication diagrams. (to create UMLs, ``Lucidchart`` recommended)

Component Diagrams
''''''''''''''''''
component = module of classes that serve a common purpose, giving bird's eye view of system components and how they relate/what purpose they serve. Circle components provide the interface for 2 components to interact, with arrows (with/without arrowheads) specify relationships.

Class Diagrams
''''''''''''''
structural diagram modelling classes in a system showing relationships between each class object which is filled with data, split into 3 sections: their name, attributes, and operations. Bidirectional relationships are indicated by arrowhead-less lines. Levels of multiplicity between classes are indicated by numbers (|ex| one/multiple bookings vs max one customer). Class inheritance is shown by a special arrowhead (empty arrowheads).
- plus signs indicate public attribute operations
- minuses indicate private (access modifier)
- hash symbols indicates that the attribute/operation is protected
- underline shows that it is static

Activity Diagrams
'''''''''''''''''
describes dynamic behaviour modelling control flow between activities:
1. start node = starting point of activity
2. state object in which behaviour of object represented described
3. certain condition satisfaction decides decision node with multiple possible control laws
4. end node
Horizontal fork/join represents concurrent control laws (one in, many out). Synchronisation object would have multiple slows coming in and one/more control systems going out.

Deployment Diagrams
'''''''''''''''''''
models physical deployment of software artifacts, showing hardware components, what software runs on each node, and how they are interconnected. Each node can represent a hardware/software object (connected by lines without arrowheads), act as containers to hold other node objects. Component objects represent element of software on client machine. Interfaces shown for communication between application and business layers. Dependencies between components and software artifacts (ex application layer linked to data access layer) shown using dashed line and arrowhead for direction.

Use Case Diagram
''''''''''''''''
models users of system (actors), and their interaction with the system, helping to define functional requirements. Use cases are defined by oval object, described inside. 

Software Architecture Patterns
------------------------------

There are a variety of software architecture structures |ex| 
Layered pattern architecture
''''''''''''''''''''''''''''
Or ``Multi-Tiered Architecture`` is a database-driven architecture where data begins at the top layer and works its way down until it reaches the infrastructure layer, typically a database.

Event-driven architecture
'''''''''''''''''''''''''
sometimes programs wait till event occurs; sometimes data will need to be processed and sometimes not. Central unit (event service bus) processes data before delegating to relevant modules) — super useful in complex environments but can be difficult when error handling if modules handling same events.

Apart from knowing patterns, knowing quality measures, understanding and using different tech stacks.

Programming
-----------
Recommended books for programming knowledge: 
- Experience & Knowledge Management in Software Engineering by Kurt Schneider. 
- Clean Code by Robert C. Martin
Also, Technology Radar from thoughtworks provides categorised insight on tools, techniques, platforms, languages, frameworks.

Skills
''''''
- understanding of web applications, cybersecurity, open source technologies
- experience with database platforms, analysing code for issues/errors, operations & DevOps skills

Documentation
'''''''''''''
Generate documentation where possible, but as much as necessary, as little as possible. 
