# utils.py

from storage import StorageArea

small_area = StorageArea("Small", capacity=10)
medium_area = StorageArea("Medium", capacity=8)
large_area = StorageArea("Large", capacity=5)

customers = []


def create_customer(first_name, last_name, phone_number):
    customer = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number
    }
    customers.append(customer)
    return customer


def check_availability(size):
    if size == "Small":
        return small_area.accept_box()
    elif size == "Medium":
        return medium_area.accept_box()
    elif size == "Large":
        return large_area.accept_box()
    else:
        return False


def record_storage_retrieval(customer, box_size, action):
    if action == "store":
        storage_area = None
        if box_size == "Small":
            storage_area = small_area
        elif box_size == "Medium":
            storage_area = medium_area
        elif box_size == "Large":
            storage_area = large_area

        if storage_area and storage_area.accept_box():
            box = f"{box_size} box"
            print(f"{box} stored for {customer['first_name']} {customer['last_name']}.")
            return box
        else:
            print(f"No available space for {box_size} box.")
            return None

    elif action == "retrieve":
        box = f"{box_size} box"
        print(f"{box} retrieved for {customer['first_name']} {customer['last_name']}.")
        return box
