package main

import (
	"fmt"
	"log"
	"net/http"

	"aprendizado/api-exemplo/config"
	"aprendizado/api-exemplo/routes"
)

func main() {
	cfg := config.Load()
	mux := routes.New()

	fmt.Printf("API rodando em http://localhost:%s\n", cfg.Port)
	log.Fatal(http.ListenAndServe(":"+cfg.Port, mux))
}
