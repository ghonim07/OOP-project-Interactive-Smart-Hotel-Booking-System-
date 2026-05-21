# VIDEO LINK: <https://youtu.be/tWeZmovj-I0>

# Interactive Smart Hotel Booking System

A robust terminal-based command-line interface (CLI) application built using Python to streamline front-desk management operations. This project serves as a practical assessment demonstrating the rigorous application of advanced Object-Oriented Programming (OOP) architectures in a production hospitality domain.

## 🚀 Key Features

- **Interactive Front-Desk Console**: A resilient command loop structured to avoid abrupt software crashes by managing inputs gracefully.
- **Dynamic Catalogue Processing**: Real-time evaluation and loading of varied luxury rooms and localized amenities.
- **Granular Folio Engine**: Displays clean checkout invoices detailing baseline pricing alongside dynamic itemized calculations.

## 🏗️ Architecture Design Patterns

The backend infrastructure maps specifically out across the four fundamental pillars of object-oriented program structural execution:

1. **Abstraction (The Blueprint)**: Built using an abstract framework class (`HotelOffering`) via Python's native `abc` module. This enforces strict contracts for all downstream functional additions.
2. **Inheritance (Specialization)**: Derivatives explicitly expand upon the baseline layout to build tailored models for structural types like `HotelRoom` and `SpaDiningService`.
3. **Encapsulation (Data Protection)**: Prevents structural exploitation or faulty parameter modification using private state bindings combined with clean conditional `@property` getters and setters.
4. **Polymorphic Execution (Smart Behavior)**: Avoids complex cascading conditions by overriding standard computational interfaces. Hotel rooms programmatically evaluate a localized `15% City Hospitality Tax`, whereas service dependencies switch to calculate a mandatory `20% Staff Gratuity Fee`.
