package main

import "fmt"

func main() {
	parkingLot = GetParkingLot()

	for i := 0; i < 3; i++ {
		spot1 := NewSpot(VehicleTypeCar)
		spot2 := NewSpot(VehicleTypeCar)
		spot3 := NewSpot(VehicleTypeCar)

		level := NewLevel()
		level.AddSpot(spot1)
		level.AddSpot(spot2)
		level.AddSpot(spot3)

		parkingLot.AddLevel(level)
	}

	parkingLot.GetAllDetail()

	car1 := &Car{}
	parkId, err := parkingLot.Park(car1)
	fmt.Println(parkId, err)

	motorCycle1 := &MotorCycle{}
	parkId2, err := parkingLot.Park(motorCycle1)
	fmt.Println(parkId2, err)

	parkingLot.GetAllDetail()

	fmt.Println(parkingLot.Checkout(parkId, motorCycle1))

	parkingLot.GetAllDetail()

}
