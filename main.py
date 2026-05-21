import sys
from abc import ABC, abstractmethod


# ==========================================
# REQUIREMENT 1: The Blueprint (Abstraction)
# ==========================================
class HotelOffering(ABC):
    """
    Abstract Base Class acting as the blueprint for any bookable hotel item.
    Cannot be instantiated directly.
    """
    def __init__(self, item_id: str, name: str, base_price: float):
        self._item_id = item_id
        self._name = name
        # Using the setter to enforce data validation during initialization
        self.base_price = base_price 

    @property
    def item_id(self) -> str:
        return self._item_id

    @property
    def name(self) -> str:
        return self._name

    # REQUIREMENT 3: Data Protection (Encapsulation) via Properties
    @property
    def base_price(self) -> float:
        return self.__base_price

    @base_price.setter
    def base_price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a valid numerical value.")
        if value < 0:
            raise ValueError("Price cannot be negative. Hospitality items must have a valid base cost.")
        self.__base_price = float(value)

    @abstractmethod
    def calculate_item_cost(self) -> float:
        """Forces subclasses to implement their own taxation/gratuity logic."""
        pass

    @abstractmethod
    def display_details(self) -> str:
        """Forces subclasses to format their own specification layouts."""
        pass


# ==========================================
# REQUIREMENT 2: Specialization (Inheritance)
# ==========================================
class HotelRoom(HotelOffering):
    """Type A: Specialized representation of overnight lodging accommodations."""
    def __init__(self, item_id: str, name: str, base_price: float, bed_size: str, smoking_allowed: bool):
        super().__init__(item_id, name, base_price)
        self.bed_size = bed_size
        self.smoking_allowed = smoking_allowed

    # REQUIREMENT 4: Smart Behavior (Polymorphism - 15% City Tax)
    def calculate_item_cost(self) -> float:
        return self.base_price * 1.15

    def display_details(self) -> str:
        smoke_status = "Smoking Allowed" if self.smoking_allowed else "Non-Smoking"
        return f"[{self.item_id}] {self.name:<25} | Type: Room    | Specs: {self.bed_size}, {smoke_status:<15} | Base: ${self.base_price:.2f}"


class SpaDiningService(HotelOffering):
    """Type B: Specialized representation of timed secondary hotel amenities."""
    def __init__(self, item_id: str, name: str, base_price: float, duration_mins: int, time_slot: str):
        super().__init__(item_id, name, base_price)
        self.duration_mins = duration_mins
        self.time_slot = time_slot

    # REQUIREMENT 4: Smart Behavior (Polymorphism - 20% Staff Gratuity)
    def calculate_item_cost(self) -> float:
        return self.base_price * 1.20

    def display_details(self) -> str:
        time_info = f"{self.duration_mins} mins @ {self.time_slot}"
        return f"[{self.item_id}] {self.name:<25} | Type: Service | Specs: {time_info:<23} | Base: ${self.base_price:.2f}"


# ==========================================
# REQUIREMENT 4: Customer Reservation Tracker
# ==========================================
class CustomerReservation:
    """Manages the current customer session items and polymorphism calculations."""
    def __init__(self):
        self.__items = []  # Strictly encapsulated list pointer

    def add_item(self, item: HotelOffering):
        self.__items.append(item)

    # NEWLY ADDED: Secure removal handling based on positional checkout index
    def remove_item(self, index: int) -> HotelOffering:
        """Removes an item by its 0-based index and returns it if successful."""
        if 0 <= index < len(self.__items):
            return self.__items.pop(index)
        raise IndexError("The requested reservation item index is completely out of valid bounds.")

    def get_items(self) -> list:
        return self.__items

    def calculate_total(self) -> float:
        # Polymorphic execution occurs right here when calling calculate_item_cost()
        return sum(item.calculate_item_cost() for item in self.__items)

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def clear(self):
        self.__items.clear()


# ==========================================
# REQUIREMENT 5: Terminal Interaction Loop
# ==========================================
def seed_hotel_catalog() -> dict:
    """Helper catalog dictionary using IDs as primary key maps for swift parsing."""
    catalog = [
        HotelRoom("101", "Standard King Room", 150.00, "King", False),
        HotelRoom("102", "Deluxe Twin Suite", 220.00, "Twin", False),
        HotelRoom("204", "Penthouse Oasis", 550.00, "Queen", True),
        SpaDiningService("S1", "Deep Tissue Swedish Massage", 120.00, 60, "14:00"),
        SpaDiningService("D1", "3-Course Chef Tasting", 85.00, 90, "19:30")
    ]
    return {item.item_id.upper(): item for item in catalog}

def main():
    catalog = seed_hotel_catalog()
    reservation = CustomerReservation()

    print("==================================================")
    print("  WELCOME TO THE SMART HOTEL MANAGEMENT SYSTEM   ")
    print("==================================================")

    while True:
        print("\n--- MAIN WORKFLOW MENU ---")
        print("[1] View All Available Hotel Offerings")
        print("[2] Add Offering to Customer Reservation")
        print("[3] Remove Offering from Reservation")  # Added choice
        print("[4] View Current Pending Items")
        print("[5] Print Final Folio & Generate Bill")
        print("[6] Close System (Exit)")
        
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            print("\n========================= AVAILABLE HOTEL OFFERINGS =========================")
            for item in catalog.values():
                print(item.display_details())
            print("=============================================================================")

        elif choice == "2":
            item_id = input("Enter the ID of the item to add: ").strip().upper()
            if item_id in catalog:
                selected_item = catalog[item_id]
                reservation.add_item(selected_item)
                print(f"✓ Success: '{selected_item.name}' added to current booking record.")
            else:
                print("❌ Error: Valid selection not found. Please review the catalogue IDs and try again.")

        elif choice == "3":
            # NEW OPERATION: Safe interactive deletion sequence
            if reservation.is_empty():
                print("\n[!] The customer's reservation is empty. Nothing to remove.")
                continue
            
            print("\n--- SELECT AN ITEM TO REMOVE ---")
            for index, item in enumerate(reservation.get_items(), 1):
                print(f" [{index}] {item.name:<30} (${item.base_price:.2f})")
            
            try:
                removal_input = input("Enter the list number you wish to delete: ").strip()
                selected_index = int(removal_input) - 1  # Standardize back to 0-based index
                
                removed_item = reservation.remove_item(selected_index)
                print(f"✓ Success: '{removed_item.name}' has been removed from the reservation.")
            except (ValueError, IndexError):
                print("❌ Error: Invalid selection. Please enter a valid item number from the list above.")

        elif choice == "4":
            if reservation.is_empty():
                print("\n[!] The customer's reservation is currently empty.")
            else:
                print("\n--- CURRENT PENDING RESERVATION ITEMS ---")
                for index, item in enumerate(reservation.get_items(), 1):
                    print(f" {index}. {item.name:<30} (Base Nightly Rate/Fee: ${item.base_price:.2f})")

        elif choice == "5":
            if reservation.is_empty():
                print("\n❌ Checkout Aborted: Cannot generate a blank billing folio.")
                continue

            print("\n" + "="*55)
            print("             FINAL HOSPITALITY BILLING FOLIO             ")
            print("="*55)
            print(f"{'Item Name':<30} | {'Base':<8} | {'Final (Inc. Tax/Tip)':<12}")
            print("-"*55)
            
            for item in reservation.get_items():
                base = f"${item.base_price:.2f}"
                final = f"${item.calculate_item_cost():.2f}"
                print(f"{item.name:<30} | {base:<8} | {final:<12}")
                
            print("-"*55)
            grand_total = reservation.calculate_total()
            print(f"{'GRAND TOTAL DUE:':<41} ${grand_total:.2f}")
            print("="*55)
            print("    Thank you for choosing our establishment. Safe travels!   ")
            print("="*55)
            
            # Reset session post-checkout
            reservation.clear()

        elif choice == "6":
            print("\nThank you.")
            sys.exit(0)

        else:
            print("❌ Invalid Input: Please enter a single digit from 1 to 6 corresponding to the options above.")

if __name__ == "__main__":
    main()