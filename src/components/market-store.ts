import { ListItem, SubList } from "@/models/Item";
import { defineStore } from "pinia";
import { computed, ref } from "vue";

export enum ViewType {
  ItemList,
  ItemDetail,
  ItemSubList,
}

export const useMarketStore = defineStore("market", () => {
  const listItems = ref<ListItem[]>([]);

  const viewType = ref<ViewType>();

  const selectedItem = ref<SubList>();

  return {
    listItems,
    viewType,
    selectedItem,
  };
});
