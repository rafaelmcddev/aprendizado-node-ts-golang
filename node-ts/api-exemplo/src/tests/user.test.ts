import { describe, it, expect } from 'vitest';
import { findById, findAll, create } from '../models/user.model.js';

describe('user model', () => {
  it('lista usuários iniciais', () => {
    expect(findAll().length).toBe(2);
  });

  it('acha usuário existente por id', () => {
    expect(findById(1)?.name).toBe('Ada Lovelace');
  });

  it('retorna undefined pra id inexistente', () => {
    expect(findById(999)).toBeUndefined();
  });

  it('cria um novo usuário', () => {
    const user = create({ name: 'Grace Hopper', email: 'grace@example.com' });
    expect(user.id).toBeGreaterThan(0);
    expect(findById(user.id)?.name).toBe('Grace Hopper');
  });
});
