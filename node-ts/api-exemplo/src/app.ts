import express from 'express';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import userRoutes from './routes/user.routes.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export const app = express();

app.use(express.json());              // middleware: transforma body JSON em req.body
app.use(express.static(path.join(__dirname, 'views'))); // serve o front (index.html)

app.use('/users', userRoutes);        // toda rota que começa com /users vai pra cá

// middleware de erro global: qualquer throw não tratado cai aqui
app.use((err: Error, req: express.Request, res: express.Response, next: express.NextFunction) => {
  console.error(err);
  res.status(500).json({ error: 'erro interno' });
});
