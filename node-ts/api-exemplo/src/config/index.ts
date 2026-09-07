import 'dotenv/config';

// Este é o "settings.py"/"config.php" do projeto: lê o .env e expõe
// valores tipados pro resto da aplicação usar.
export const config = {
  port: Number(process.env.PORT ?? 3000),
};
