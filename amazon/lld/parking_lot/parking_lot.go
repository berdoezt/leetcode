package main

import (
	"errors"
	"fmt"
	"strings"

	"github.com/google/uuid"
)

var (
	ErrSpotNotAvailable   error = errors.New("no spot available")
	ErrParkingLotFull     error = errors.New("parking lot full for this vehicle type")
	ErrInvalidIdFormat    error = errors.New("invalid id format")
	ErrLevelNotFound      error = errors.New("level not found")
	ErrSpotNotFound       error = errors.New("spot not found")
	ErrVehicleIsDifferent error = errors.New("vehicle is different")
)

type spot struct {
	id           string
	vehicle      Vehicle
	available    bool
	vehicle_type VehicleType
}

func NewSpot(vehicleType VehicleType) *spot {
	return &spot{
		id:           uuid.New().String(),
		available:    true,
		vehicle_type: vehicleType,
	}
}

func (s *spot) Available(vehicleType VehicleType) bool {
	return s.vehicle_type == vehicleType && s.available
}

func (s *spot) Park(vehicle Vehicle) string {
	s.available = false
	s.vehicle = vehicle

	return s.id
}

func (s *spot) Checkout(vehicle Vehicle) (string, error) {
	if vehicle != s.vehicle {
		return "", ErrVehicleIsDifferent
	}

	s.available = true
	s.vehicle = nil

	return s.id, nil
}

type level struct {
	id    string
	spots map[string]*spot
}

func NewLevel() *level {
	return &level{
		id:    uuid.New().String(),
		spots: make(map[string]*spot),
	}
}

func (l *level) Park(vehicle Vehicle) (string, error) {
	for _, spot := range l.spots {
		if spot.Available(vehicle.GetType()) {
			spotId := spot.Park(vehicle)
			levelId := l.id
			return fmt.Sprintf("%s:%s", levelId, spotId), nil
		}
	}

	return "", ErrSpotNotAvailable
}

func (l *level) AddSpot(spot *spot) {
	l.spots[spot.id] = spot
}

func (l *level) GetSpot(spotId string) (*spot, error) {
	spot, spotFound := l.spots[spotId]
	if !spotFound {
		return nil, ErrSpotNotFound
	}

	return spot, nil
}

var parkingLot *ParkingLot

func GetParkingLot() *ParkingLot {
	if parkingLot == nil {
		parkingLot = &ParkingLot{
			levels: make(map[string]*level),
		}
	}

	return parkingLot
}

type ParkingLot struct {
	levels map[string]*level
}

func (pk *ParkingLot) Park(vehicle Vehicle) (string, error) {
	for index, level := range pk.levels {
		parkId, err := level.Park(vehicle)
		if err != nil {
			fmt.Printf("Level %s : %s\n", index, err.Error())
			continue
		}

		return parkId, nil
	}

	return "", ErrParkingLotFull
}

func (pk *ParkingLot) Checkout(id string, vehicle Vehicle) error {
	if !strings.Contains(id, ":") {
		return ErrInvalidIdFormat
	}

	ids := strings.Split(id, ":")
	levelId := ids[0]
	spotId := ids[1]

	level, err := pk.GetLevel(levelId)
	if err != nil {
		return err
	}

	spot, err := level.GetSpot(spotId)
	if err != nil {
		return err
	}

	_, err = spot.Checkout(vehicle)
	if err != nil {
		return err
	}

	return nil
}

func (pk *ParkingLot) GetAllDetail() {
	for levelId, level := range pk.levels {
		fmt.Printf("Level : %s\n", levelId)
		for _, spot := range level.spots {
			fmt.Printf("Spot %+v\n", spot)
		}
		fmt.Println()
	}
}

func (pk *ParkingLot) GetLevel(levelId string) (*level, error) {
	level, levelFound := pk.levels[levelId]
	if !levelFound {
		return nil, ErrLevelNotFound
	}

	return level, nil
}

func (pk *ParkingLot) AddLevel(level *level) {
	pk.levels[level.id] = level
}
