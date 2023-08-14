import { getFile } from "@/queries";
import jsonItems from "../resources/items.json";

interface DictionaryItem {
  id: string;
  name: string;
  grade: string;
  main_category: string;
  sub_category: string;
}

const items = jsonItems as { [key: string]: DictionaryItem };

const enhancementNames: { [key: number]: string } = {
  16: "PRI",
  17: "DUO",
  18: "TRI",
  19: "TET",
  20: "PEN",
};

const enhancementSymbols: { [key: number]: string } = {
  16: "I",
  17: "II",
  18: "III",
  19: "IV",
  20: "V",
};

export function getEnhancementName(itemId: number, level: number) {
  const item = items[`${itemId}`];

  if (level === 0) {
    return "";
  } else if (item.main_category === "20") {
    return `${enhancementNames[level + 15]}`;
  }
  if (level > 0 && level <= 15) {
    return `+${level}`;
  } else if (level > 15 && level <= 20) {
    return `${enhancementNames[level]}`;
  }

  return "";
}

export function getEnhancementSymbol(itemId: number, level: number) {
  const item = items[itemId];

  if (level === 0) {
    return "";
  } else if (level === 0) {
    return "";
  } else if (item.main_category === "20") {
    return `${enhancementSymbols[level + 15]}`;
  }
  if (level > 0 && level <= 15) {
    return `+${level}`;
  } else if (level > 15 && level <= 20) {
    return `${enhancementSymbols[level]}`;
  }

  return "";
}

export function getEnhancementSymbolIcon(itemId: number, level: number) {
  const item = items[itemId];

  const path = "static/gear_lvl";

  if (level === 0) {
    return "";
  } else if (level === 0) {
    return "";
  } else if (item.main_category === "20") {
    return getFile(`${path}/${enhancementNames[level + 15]}.png`);
  }
  if (level > 0 && level <= 15) {
    return getFile(`${path}/${level}.png`);
  } else if (level > 15 && level <= 20) {
    return getFile(`${path}/${enhancementNames[level]}.png`);
  }

  return "";
}
