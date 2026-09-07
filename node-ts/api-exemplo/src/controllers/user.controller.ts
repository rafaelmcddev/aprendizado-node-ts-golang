import type { Request, Response } from 'express';
import * as userModel from '../models/user.model.js';

// "Controller" = recebe a requisição, chama o Model, devolve a resposta.
// Equivalente à view do Django ou ao Controller do Laravel.

export function index(req: Request, res: Response) {
  res.json(userModel.findAll());
}

export function show(req: Request, res: Response) {
  const id = Number(req.params.id);
  const user = userModel.findById(id);

  if (!user) {
    // debug tip: coloque um console.log(id) aqui se quiser ver o
    // valor chegando do request.params
    return res.status(404).json({ error: 'usuário não encontrado' });
  }

  res.json(user);
}

export function store(req: Request, res: Response) {
  const { name, email } = req.body;

  if (!name || !email) {
    return res.status(400).json({ error: 'name e email são obrigatórios' });
  }

  const user = userModel.create({ name, email });
  res.status(201).json(user);
}
