"""
File: hotel_management_system.py
Author: Kritan Acharya
Description: Python-based Hotel Management System for LANGHAM Hotels
Date:06-12-2024
"""

import os
import datetime

# Global dictionary to store room details
rooms = {}


def add_room():
    try:
        # Input and validation for room number (must be integer)
        room_number_input = input("Enter room number (integer): ").strip()
        if not room_number_input.isdigit():
            raise ValueError("Room number must be a valid integer.")
        room_number = int(room_number_input)
        if room_number <= 0:
            raise ValueError("Room number must be a positive integer.")
        if room_number in rooms:
            print(f"Room {room_number} already exists.")
            return

        # Input and validation for room type
        room_type = input("Enter room type (Single/Double): ").strip().capitalize()
        if room_type not in ["Single", "Double"]:
            raise ValueError("Room type must be 'Single' or 'Double'.")

        # Input and validation for room price
        price_input = input("Enter room price per night: ").strip()
        if not price_input.replace('.', '', 1).isdigit():  # Check if input is a valid float
            raise ValueError("Price must be a valid number.")
        price = float(price_input)
        if price <= 0:
            raise ValueError("Price must be a positive number.")

        # Adding room to the dictionary
        rooms[room_number] = {'type': room_type, 'price': price, 'status': 'Available'}
        print(f"Room {room_number} added successfully.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def delete_room():
    try:
        room_number = input("Enter room number to delete: ")
        if room_number in rooms:
            del rooms[room_number]
            print(f"Room {room_number} deleted successfully.")
        else:
            raise IndexError(f"Room {room_number} does not exist.")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def display_rooms():
    try:
        if not rooms:
            raise ValueError("No rooms available.")
        for room, details in rooms.items():
            print(f"Room {room}: Type: {details['type']}, Price: {details['price']}, Status: {details['status']}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def allocate_room():
    try:
        room_number = input("Enter room number to allocate: ")
        if room_number in rooms and rooms[room_number]['status'].strip().lower() == 'available':
            customer_name = input("Enter customer name: ")
            rooms[room_number]['status'] = f"Allocated to {customer_name}"
            print(f"Room {room_number} allocated to {customer_name}.")
        else:
            raise NameError("Room is not available or does not exist.")
    except NameError as ne:
        print(f"NameError: {ne}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def display_allocations():
    try:
        for room, details in rooms.items():
            print(f"Room {room}: {details['status']}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def billing_and_deallocation():
    try:
        room_number = input("Enter room number to deallocate: ")
        if room_number in rooms and 'Allocated' in rooms[room_number]['status']:
            customer = rooms[room_number]['status'].split("to")[1].strip()
            print(f"Billing customer {customer} for Room {room_number}.")
            rooms[room_number]['status'].lower() == 'Available'
            print(f"Room {room_number} is now available.")
        else:
            raise ValueError("Room is not allocated or does not exist.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# File I/O functions
def save_to_file():
    try:
        filename = "LHMS_850001022.txt"
        with open(filename, 'w') as file:
            for room, details in rooms.items():
                file.write(f"Room {room}: {details}\n")
        print(f"Room allocation details saved to {filename}.")
    except IOError as ioe:
        print(f"IOError: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def show_from_file():
    try:
        filename = "LHMS_850001022.txt"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                print(file.read())
        else:
            raise FileNotFoundError(f"{filename} does not exist.")
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def backup_file():
    try:
        source = "LHMS_850001022.txt"
        if os.path.exists(source):
            now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            destination = f"LHMS_850001022_Backup_{now}.txt"
            with open(source, 'r') as original, open(destination, 'w') as backup:
                backup.write(original.read())
            print(f"Backup created as {destination}.")
        else:
            raise FileNotFoundError(f"{source} does not exist.")
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
    except IOError as ioe:
        print(f"IOError: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Menu system
def menu():
    while True:
        try:
            print("\nHotel Management System")
            print("1. Add Room")
            print("2. Delete Room")
            print("3. Display Rooms Details")
            print("4. Allocate Rooms")
            print("5. Display Room Allocation Details")
            print("6. Billing & De-Allocation")
            print("7. Save Room Allocation to File")
            print("8. Show Room Allocation from File")
            print("9. Backup File")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_room()
            elif choice == '2':
                delete_room()
            elif choice == '3':
                display_rooms()
            elif choice == '4':
                allocate_room()
            elif choice == '5':
                display_allocations()
            elif choice == '6':
                billing_and_deallocation()
            elif choice == '7':
                save_to_file()
            elif choice == '8':
                show_from_file()
            elif choice == '9':
                backup_file()
            elif choice == '0':
                print("Exiting application. Goodbye!")
                break
            else:
                raise ValueError("Invalid choice. Please select a valid option.")
        except EOFError:
            print("EOFError: Unexpected end of input.")
        except ImportError as ie:
            print(f"ImportError: {ie}")
        except OverflowError:
            print("OverflowError: Number too large to handle.")
        except TypeError as te:
            print(f"TypeError: {te}")
        except Exception as e:
            print(f"An unexpected error occurred in the menu: {e}")

# Run the application
if __name__ == "__main__":
    menu()
