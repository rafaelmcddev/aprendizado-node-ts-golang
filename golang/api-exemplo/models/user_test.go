package models

import "testing"

func TestFindAll(t *testing.T) {
	if len(FindAll()) != 2 {
		t.Errorf("esperava 2 usuários iniciais, veio %d", len(FindAll()))
	}
}

func TestFindByIDExistente(t *testing.T) {
	user, ok := FindByID("1")
	if !ok || user.Name != "Ada Lovelace" {
		t.Errorf("esperava Ada Lovelace, veio %+v (ok=%v)", user, ok)
	}
}

func TestFindByIDInexistente(t *testing.T) {
	_, ok := FindByID("999")
	if ok {
		t.Error("esperava não encontrar o usuário 999")
	}
}

func TestCreate(t *testing.T) {
	user, err := Create("Grace Hopper", "grace@example.com")
	if err != nil {
		t.Fatalf("não esperava erro, veio: %v", err)
	}
	if user.ID == 0 {
		t.Error("esperava um ID gerado")
	}
}

func TestCreateSemNome(t *testing.T) {
	_, err := Create("", "grace@example.com")
	if err == nil {
		t.Error("esperava erro por falta de name")
	}
}
