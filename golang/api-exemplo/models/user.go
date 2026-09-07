package models

import (
	"errors"
	"strconv"
)

// "Model" = dados + regra de negócio. Sem banco de propósito.
type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

var users = []User{
	{ID: 1, Name: "Ada Lovelace", Email: "ada@example.com"},
	{ID: 2, Name: "Alan Turing", Email: "alan@example.com"},
}

func FindAll() []User {
	return users
}

// Retorna (dado, ok) — é o padrão Go pra "achei ou não achei",
// equivalente a um Optional/None em Python.
func FindByID(idParam string) (User, bool) {
	id, err := strconv.Atoi(idParam)
	if err != nil {
		return User{}, false
	}
	for _, u := range users {
		if u.ID == id {
			return u, true
		}
	}
	return User{}, false
}

func Create(name, email string) (User, error) {
	if name == "" || email == "" {
		return User{}, errors.New("name e email são obrigatórios")
	}
	user := User{ID: len(users) + 1, Name: name, Email: email}
	users = append(users, user)
	return user, nil
}
