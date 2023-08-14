export interface Item {
  id: number;
  name: string;
  grade: number;
  enhancement: number;
  quantity: number;
}

export class Process {
  materials: Item[];

  results: Item[];

  constructor(materials: Item[], results: Item[]) {
    this.materials = materials;
    this.results = results;
  }
}

export class Enhancement extends Process {
  base: Item;
  failstack: number;

  constructor(
    materials: Item[],
    results: Item[],
    base: Item,
    failstack: number
  ) {
    super(materials, results);
    this.base = base;
    this.failstack = failstack;
  }
}
