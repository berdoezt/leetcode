package main

type VehicleType int

const (
	VehicleTypeCar        VehicleType = 1
	VehicleTypeMotorCycle VehicleType = 2
)

type Vehicle interface {
	GetType() VehicleType
}

type Car struct {
}

func (c *Car) GetType() VehicleType {
	return VehicleTypeCar
}

type MotorCycle struct {
}

func (mc *MotorCycle) GetType() VehicleType {
	return VehicleTypeMotorCycle
}
