// "Model" = dados + regra de negócio. Sem banco aqui de propósito:
// o foco deste projeto é o fluxo, não SQL.

export type User = { id: number; name: string; email: string };

const users: User[] = [
  { id: 1, name: 'Ada Lovelace', email: 'ada@example.com' },
  { id: 2, name: 'Alan Turing', email: 'alan@example.com' },
];

export function findAll(): User[] {
  return users;
}

export function findById(id: number): User | undefined {
  return users.find((u) => u.id === id);
}

export function create(data: Omit<User, 'id'>): User {
  const user: User = { id: users.length + 1, ...data };
  users.push(user);
  return user;
}
