package main

import (
	"fmt"

	"github.com/google/uuid"
)

func main() {

	vendingMachine := GetVendingMachine()

	product1 := Product{
		id:       uuid.New().String(),
		name:     "taro",
		price:    2000,
		quantity: 10,
	}
	vendingMachine.AddProduct(product1)

	coin1 := Coin{
		denomination: 1,
		quantity:     1000000,
	}
	vendingMachine.AddCoin(coin1)

	// ==============

	result := vendingMachine.InsertCoin(Coin{
		denomination: 5000,
		quantity:     1,
	})
	fmt.Println(result)

	// result = vendingMachine.InsertCoin(Coin{
	// 	denomination: 1000,
	// 	quantity:     1,
	// })
	// fmt.Println(result)

	result = vendingMachine.ChooseProduct(product1.id)
	fmt.Println(result)

	result = vendingMachine.DispenseProduct()
	fmt.Println(result)

	vendingMachine.GetStatus()

}
