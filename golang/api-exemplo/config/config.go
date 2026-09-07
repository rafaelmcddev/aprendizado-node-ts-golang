package config

import "os"

// Equivalente ao settings.py / config.php: valores de configuração da
// aplicação, lidos do ambiente com um padrão caso não exista.
type Config struct {
	Port string
}

func Load() Config {
	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}
	return Config{Port: port}
}
