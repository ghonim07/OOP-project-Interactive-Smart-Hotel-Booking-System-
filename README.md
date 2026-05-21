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

## 📖 Step-by-Step User Manual (How to Use)

When you run the application, follow this operational workflow to manage a customer booking:

### Step 1: Browse the Catalog
*   Type **`1`** and hit `Enter` on your keyboard.
*   The system will output the complete active hotel catalog, showing each item's unique lookup ID, classification type, structural specs, and base pricing tier.

### Step 2: Build a Reservation
*   Type **`2`** and press `Enter`.
*   The prompt will ask you to: `Enter the ID of the item to add:`.
*   Type an ID from the catalog (e.g., **`101`** for the Standard King Room, or **`S1`** for the Deep Tissue Massage) and hit `Enter`. The console will confirm the item has been saved to the active session.

### Step 3: Remove Mistaken Bookings *(Optional)*
*   If a customer changes their mind, type **`3`** and press `Enter`.
*   The system lists all current pending selections indexed numerically.
*   Type the number row you want to eliminate (e.g., **`1`**) and hit `Enter` to instantly strip it out.

### Step 4: Verify Current Session Items
*   Type **`4`** and press `Enter` at any time to double-check what items are inside the guest's pending queue along with their un-taxed base fees.

### Step 5: Process Checkout & Print Bill
*   Type **`5`** and hit `Enter`.
*   The terminal will render the finalized, professionally structured checkout folio. This displays the name of each item, the base price, the itemized polymorphic cost calculation (applying taxes or tips dynamically), and a absolute grand total.
*   *Note: This process resets the active session basket automatically so you can immediately process a new guest.*

### Step 6: Shutdown the System
*   Type **`6`** and press `Enter` to break the active infinite workflow loop and safely exit back to your desktop terminal workspace.

---
