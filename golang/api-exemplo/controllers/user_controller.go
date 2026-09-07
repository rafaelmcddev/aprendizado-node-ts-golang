package controllers

import (
	"encoding/json"
	"net/http"

	"aprendizado/api-exemplo/models"
)

// "Controller" = recebe a requisição, chama o Model, escreve a resposta.

func Index(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(models.FindAll())
}

func Show(w http.ResponseWriter, r *http.Request) {
	id := r.PathValue("id")
	user, ok := models.FindByID(id)

	if !ok {
		// debug tip: um fmt.Println(id) aqui mostra o valor cru vindo da URL
		http.Error(w, `{"error":"usuário não encontrado"}`, http.StatusNotFound)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(user)
}

type storeInput struct {
	Name  string `json:"name"`
	Email string `json:"email"`
}

func Store(w http.ResponseWriter, r *http.Request) {
	var input storeInput
	if err := json.NewDecoder(r.Body).Decode(&input); err != nil {
		http.Error(w, `{"error":"body inválido"}`, http.StatusBadRequest)
		return
	}

	user, err := models.Create(input.Name, input.Email)
	if err != nil {
		http.Error(w, `{"error":"`+err.Error()+`"}`, http.StatusBadRequest)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(user)
}
