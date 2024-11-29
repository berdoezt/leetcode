package main

import (
	"fmt"
	"sync"
)

type Product struct {
	id       string
	name     string
	price    int
	quantity int
}

type Coin struct {
	denomination int // 1, 5, 10, 20, 50, 100
	quantity     int
}

type VendingMachine struct {
	currentState   State
	currentAmount  int
	currentProduct *Product
	products       map[string]*Product
	coins          map[int]*Coin
	mutex          sync.Mutex
}

func (vm *VendingMachine) GetStatus() {
	fmt.Println("======Products========")
	for _, product := range vm.products {
		fmt.Printf("%+v\n", product)
	}

	fmt.Println("======Coins========")
	for _, coin := range vm.coins {
		fmt.Printf("%+v\n", coin)
	}
}

func (vm *VendingMachine) AddCurrentAmount(amount int) {
	vm.currentAmount += amount
}

func (vm *VendingMachine) TakeOutCoin(coinQuantity map[int]int) {
	for denomination, quantity := range coinQuantity {
		coin := vm.coins[denomination]
		coin.quantity -= quantity
	}

	fmt.Println("here is your change", coinQuantity)
}

func (vm *VendingMachine) InsertCoin(coin Coin) error {
	return vm.currentState.InsertCoin(coin)
}

func (vm *VendingMachine) GetCoin() map[int]*Coin {
	return vm.coins
}

func (vm *VendingMachine) ChooseProduct(productId string) error {
	return vm.currentState.ChooseProduct(productId)
}

func (vm *VendingMachine) SetCurrentProduct(product *Product) {
	vm.currentProduct = product
	product.quantity -= 1
}

func (vm *VendingMachine) DispenseProduct() error {
	err := vm.currentState.DispenseProduct()
	if err != nil {
		vm.currentProduct.quantity += 1
		return err
	}
	return nil
}

func (vm *VendingMachine) UpdateState(newState State) {
	vm.currentState = newState
}

func (vm *VendingMachine) AddProduct(newProduct Product) {
	vm.products[newProduct.id] = &newProduct
}

func (vm *VendingMachine) AddCoin(newCoin Coin) {
	_, found := vm.coins[newCoin.denomination]
	if !found {
		vm.coins[newCoin.denomination] = &newCoin
	} else {
		vm.coins[newCoin.denomination].quantity += newCoin.quantity
	}

}

func (vm *VendingMachine) Reset() {
	vm.currentAmount = 0
	vm.currentProduct = nil
}

var vendingMachine *VendingMachine

func GetVendingMachine() *VendingMachine {
	if vendingMachine == nil {
		vendingMachine = &VendingMachine{
			products: make(map[string]*Product),
			coins:    make(map[int]*Coin),
		}
	}

	vendingMachine.currentState = GetNoCoinInsertState(vendingMachine)
	return vendingMachine
}
