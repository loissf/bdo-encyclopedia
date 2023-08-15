import { getFile } from "@/queries";
import jsonItems from "../resources/items.json";
import { DictionaryItem } from "@/models/Item";

interface JsonDictionaryItem {
  id: string;
  name: string;
  grade: string;
  main_category: string;
  sub_category: string;
}

const items = jsonItems as { [key: string]: JsonDictionaryItem };

const enhancementNames: { [key: number]: string } = {
  16: "PRI",
  17: "DUO",
  18: "TRI",
  19: "TET",
  20: "PEN",
};

export function getIconUrl(itemId: number): string {
  return `https:\\cdn.arsha.io/icons/${itemId}.png`;
}

export function getEnhancementName(itemId: number, level: number) {
  const item = items[`${itemId}`];

  if (item.main_category === "20") {
    return `${enhancementNames[level + 15]}`;
  } else if (level > 0 && level <= 15) {
    return `+${level}`;
  } else if (level > 15 && level <= 20) {
    return `${enhancementNames[level]}`;
  }

  return "";
}

export function getEnhancementSymbolIcon(itemId: number, level: number) {
  const item = items[itemId];

  const path = "static/gear_lvl";

  if (item.main_category === "20") {
    return getFile(`${path}/${enhancementNames[level + 15]}.png`);
  } else if (level > 0 && level <= 15) {
    return getFile(`${path}/${level}.png`);
  } else if (level > 15 && level <= 20) {
    return getFile(`${path}/${enhancementNames[level]}.png`);
  }

  return "";
}

function decodeHtmlCharCodes(str: string) {
  return str.replace(/(&#(\d+);)/g, function (match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}

export function searchItem(term: string) {
  return Object.values(items)
    .filter((x) =>
      decodeHtmlCharCodes(x.name).toLowerCase().includes(term.toLowerCase())
    )
    .slice(0, 100)
    .map(
      (x) =>
        ({
          id: parseInt(x.id),
          name: x.name,
          grade: parseInt(x.grade),
          icon: `https:\\cdn.arsha.io/icons/${x.id}.png`,
          mainCategory: x.main_category,
          subCategory: x.sub_category,
        } as DictionaryItem)
    );
}
