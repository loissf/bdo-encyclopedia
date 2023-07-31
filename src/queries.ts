import axios from "axios";
import qs from "qs";
import { ListItem, SubListItem, SubList } from "./models/Item";

const url = "http://127.0.0.1:5000";

function mapSubList(data: SubListItem[]): SubList {
  if (data.length > 1 && data.some((x) => x.id !== data[0].id)) {
    throw Error("Invalid item details");
  }

  const { totalStock, totalTrades } = data.reduce(
    (previous, next) => {
      previous.totalStock += parseInt(next.stock.toString());
      previous.totalTrades += parseInt(next.totalTrades.toString());
      return previous;
    },
    { totalStock: 0, totalTrades: 0 }
  );

  const baseItem: ListItem = {
    id: data[0].id,
    name: data[0].name,
    grade: data[0].grade,
    icon: data[0].icon,
    stock: totalStock,
    basePrice: data[0].basePrice,
    totalTrades: totalTrades,
  };

  return {
    baseItem,
    subList: data,
  };
}

export async function getItem(id: number): Promise<SubList | undefined> {
  try {
    const { data } = await axios.get<SubListItem[]>(`${url}/items/${id}`);
    return data.length !== 0 ? mapSubList(data) : undefined;
  } catch (e) {
    console.log(e);
    return undefined;
  }
}

export async function getItemSearch(ids: number[]): Promise<ListItem[]> {
  try {
    const { data } = await axios.get<ListItem[]>(`${url}/items`, {
      params: {
        id: ids,
      },
      paramsSerializer: {
        encode: (params: number[]) =>
          qs.stringify(params, { indices: false, encode: false }),
      },
    });

    return data;
  } catch (e) {
    console.log(e);
    return [];
  }
}

export async function getCategory(
  categoryId: number,
  subcategoryId: number
): Promise<ListItem[]> {
  try {
    const { data } = await axios.get<ListItem[]>(
      `${url}/category/${categoryId}/${subcategoryId}`
    );

    return data;
  } catch (e) {
    console.log(e);
    return [];
  }
}
