from abc import ABC, abstractmethod
class BaseVehicle(ABC):
    def __init__(self):
        self.__odometer = 0
    @property
    def odometer(self):
        return self.__odometer

    def drive(self, distance):
        if distance <= 0:
            raise ValueError("Quãng đường phải lớn hơn 0.")

        self.__odometer += distance

    @abstractmethod
    def calculate_efficiency(self):
        pass    
    
    def __lt__(self, other):
        return self.odometer < other.odometer

    @staticmethod
    def validate_license_plate(plate):
        return len(plate) == 9 and plate.startswith("29")


class ElectricBus(BaseVehicle):
    def calculate_efficiency(self):
        efficiency = 100 - (self.odometer * 0.005)

        if efficiency < 50:
            return 50.0

        return efficiency


class AutonomousFeature:
    def calculate_efficiency(self):
        return 95.0

class RoboBus(ElectricBus, AutonomousFeature):
    def __init__(self, plate):
        super().__init__()
        self.plate = plate

    def calculate_efficiency(self):
        electric_efficiency = ElectricBus.calculate_efficiency(self)
        autonomous_efficiency = AutonomousFeature.calculate_efficiency(self)

        return (electric_efficiency + autonomous_efficiency) / 2
    
def show_menu():
    print("\n===== SMART TRANSIT MENU =====")
    print("1. Khởi tạo & Đăng ký xe lai RoboBus mới")
    print("2. Giả lập vận hành & Kiểm tra hiệu suất")
    print("3. Thoát")


def create_vehicle():
    while True:
        plate = input("Nhập biển số xe (9 ký tự, bắt đầu bằng 29): ").strip()

        if BaseVehicle.validate_license_plate(plate):
            vehicle = RoboBus(plate)

            print("\n[Thành công]: Khởi tạo phương tiện RoboBus thành công!")

            print("[MRO Architecture]:"," -> ".join(cls.__name__ for cls in RoboBus.__mro__))

            return vehicle

        print("Biển số không hợp lệ. Vui lòng nhập lại!")


def simulate_drive(vehicle):
    if vehicle is None:
        print("Chưa có phương tiện nào được khởi tạo!")
        return

    try:
        distance = float(
            input("Nhập số km di chuyển mới phát sinh: ")
        )

        vehicle.drive(distance)

        efficiency = vehicle.calculate_efficiency()

        print("\n[Thành công]: Cập nhật lộ trình xe chạy thành công.")
        print(f"Tổng quãng đường tích lũy (Odometer): {vehicle.odometer} km")

        print(f"Hiệu suất tiêu thụ năng lượng tích hợp: {efficiency:.1f}%")

    except ValueError as error:
        print(f"Lỗi: {error}")


current_vehicle = None

while True:
    show_menu()

    choice = input("Chọn chức năng (1-3): ").strip()

    if choice == "1":
        current_vehicle = create_vehicle()

    elif choice == "2":
        simulate_drive(current_vehicle)

    elif choice == "3":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
