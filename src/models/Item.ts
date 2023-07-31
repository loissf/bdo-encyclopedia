export interface ItemBase {
  id: number;
  name: string;
  grade: number;
  icon: string;
}

export interface ListItem extends ItemBase {
  stock: number;
  basePrice: number;
  totalTrades: number;
}

export interface SubListItem extends ItemBase {
  enhancement: number;
  stock: number;
  basePrice: number;
  totalTrades: number;
  lastPrice: number;
  lastSale: number;
  mainCategory: number;
  subCategory: number;
}

export enum PriceChange {
  Down = 1,
  Up = 2,
}

export interface HotListItem extends SubListItem {
  changeDirection: PriceChange;
  changeValue: number;
}

export interface DictionaryItem extends ItemBase {
  main_category: string;
  sub_category: string;
}

export interface SubList {
  baseItem: ListItem;
  subList: SubListItem[];
}
