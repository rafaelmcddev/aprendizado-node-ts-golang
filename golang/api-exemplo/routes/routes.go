package routes

import (
	"net/http"

	"aprendizado/api-exemplo/controllers"
)

// Aqui a URL vira uma chamada de função — o "urls.py"/"routes/web.php".
// Desde o Go 1.22 dá pra declarar método + parâmetro direto no padrão.
func New() *http.ServeMux {
	mux := http.NewServeMux()

	mux.HandleFunc("GET /users", controllers.Index)     // GET  /users
	mux.HandleFunc("GET /users/{id}", controllers.Show)  // GET  /users/1
	mux.HandleFunc("POST /users", controllers.Store)     // POST /users

	// serve o front estático (views/index.html) em "/"
	mux.Handle("/", http.FileServer(http.Dir("./views")))

	return mux
}
