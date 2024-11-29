package main

import (
	"errors"
	"math"
	"sort"
)

var (
	ErrNoCoinInsert       = errors.New("no coin insert")
	ErrProductNotFound    = errors.New("product not found")
	ErrProductOutOfStock  = errors.New("product out of stock")
	ErrInsufficientCoin   = errors.New("insufficient coin")
	ErrInsufficientChange = errors.New("insufficient change")
	ErrNoProductSelected  = errors.New("no product selected")
	ErrProductIsDispensed = errors.New("product is dispensed")
)

type State interface {
	InsertCoin(coin Coin) error
	ChooseProduct(productId string) error
	DispenseProduct() error
}

type NoCoinInsertState struct {
	vendingMachine *VendingMachine
}

func (nci *NoCoinInsertState) InsertCoin(coin Coin) error {
	nci.vendingMachine.AddCurrentAmount(coin.denomination * coin.quantity)
	nci.vendingMachine.AddCoin(coin)
	nci.vendingMachine.UpdateState(GetCoinInsertState(GetVendingMachine()))
	return nil
}
func (nci *NoCoinInsertState) ChooseProduct(productId string) error {
	return ErrNoCoinInsert
}
func (nci *NoCoinInsertState) DispenseProduct() error {
	return ErrNoCoinInsert
}

var noCoinInsertState *NoCoinInsertState

func GetNoCoinInsertState(vendingMachine *VendingMachine) *NoCoinInsertState {
	if noCoinInsertState == nil {
		noCoinInsertState = &NoCoinInsertState{
			vendingMachine: vendingMachine,
		}
	}

	return noCoinInsertState
}

type CoinInsertState struct {
	vendingMachine *VendingMachine
}

func (nci *CoinInsertState) InsertCoin(coin Coin) error {
	nci.vendingMachine.AddCurrentAmount(coin.denomination * coin.quantity)
	nci.vendingMachine.AddCoin(coin)
	return nil
}
func (nci *CoinInsertState) ChooseProduct(productId string) error {
	product, productFound := nci.vendingMachine.products[productId]
	if !productFound {
		return ErrProductNotFound
	}

	if product.quantity <= 0 {
		return ErrProductOutOfStock
	}

	nci.vendingMachine.SetCurrentProduct(product)
	nci.vendingMachine.UpdateState(GetDispenseState(GetVendingMachine()))
	return nil
}
func (nci *CoinInsertState) DispenseProduct() error {

	return ErrNoProductSelected
}

var coinInsertState *CoinInsertState

func GetCoinInsertState(vendingMachine *VendingMachine) *CoinInsertState {
	if coinInsertState == nil {
		coinInsertState = &CoinInsertState{
			vendingMachine: vendingMachine,
		}
	}

	return coinInsertState
}

type DispenseState struct {
	vendingMachine *VendingMachine
}

func (d *DispenseState) InsertCoin(coin Coin) error {
	return ErrProductIsDispensed
}
func (d *DispenseState) ChooseProduct(productId string) error {
	return ErrProductIsDispensed
}
func (d *DispenseState) DispenseProduct() error {
	if d.vendingMachine.currentProduct.price > d.vendingMachine.currentAmount {
		return ErrInsufficientCoin
	}

	change := d.vendingMachine.currentAmount - d.vendingMachine.currentProduct.price
	if change > 0 {
		changeCoin, err := d.getChangeCoin(change)
		if err != nil {
			return err
		}

		d.vendingMachine.TakeOutCoin(changeCoin)
	}

	d.vendingMachine.Reset()
	d.vendingMachine.UpdateState(GetNoCoinInsertState(GetVendingMachine()))
	return nil
}

func (d *DispenseState) getChangeCoin(change int) (map[int]int, error) {
	result := make(map[int]int, 0)

	coins := d.vendingMachine.GetCoin()

	denominations := make([]int, 0)
	for denomination := range coins {
		denominations = append(denominations, denomination)
	}

	sort.Ints(denominations)

	for i := len(denominations) - 1; i >= 0; i-- {
		coin, found := coins[denominations[i]]
		if !found {
			continue
		}

		denomination := coin.denomination
		quantity := coin.quantity

		if change < denomination {
			continue
		}

		coinCount := math.Floor(float64(change) / float64(denomination))
		coinTake := math.Min(float64(quantity), coinCount)

		result[denomination] = int(coinTake)

		change -= int(coinTake) * denomination
		if change <= 0 {
			return result, nil
		}
	}

	return nil, ErrInsufficientChange
}

var dispenseState *DispenseState

func GetDispenseState(VendingMachine *VendingMachine) *DispenseState {
	if dispenseState == nil {
		dispenseState = &DispenseState{
			vendingMachine: vendingMachine,
		}
	}

	return dispenseState
}
